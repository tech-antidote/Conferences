#!/usr/bin/env python3
"""Audit the trustworthiness of OCR text in the Markdown corpus.

The converter (tools/pdf2md.py) gap-fills image-only slides by rendering the
page and running Tesseract over it, fencing the result in a labelled block:

    > Text below was recovered by OCR (confidence 86/100) from an image-only
    > slide. Wording is approximate; verify exact values against the source PDF.

    ```text
    ...
    ```

That label is the converter's *own* claim about quality. This script tests the
claim two ways:

  PASS 1 -- corpus statistics.  Every OCR block is parsed out, measured, and
  the stated confidences are summarised (deciles + the <60 / 60-75 / 75-85 />85
  bands).  Because pdf2md drops individual lines scoring under 60, the stated
  number is a *survivor* mean: it says nothing about what was thrown away, and
  this pass is deliberately not the last word.

  PASS 2 -- ground truth.  A stratified sample of blocks is re-derived from
  source: the slide's page is re-rendered with pymupdf at 200 DPI and re-OCR'd
  independently, unfiltered.  Comparing the corpus text against that raw
  re-OCR, plus a corpus-derived vocabulary check, gives an accuracy verdict
  that does not depend on Tesseract grading its own homework.

The vocabulary is built from the corpus's *structural* text -- the PDF text
layer, which is exact -- so a token that appears in no text layer anywhere in
730 security talks is a strong garble signal, without needing a dictionary that
would reject "vmcs", "kallsyms" or "0xffffffff" anyway.

Usage:
    /opt/mdvenv/bin/python tools/audit_ocr.py --out markdown --sample 16
"""

from __future__ import annotations

import argparse
import collections
import csv
import io
import json
import os
import random
import re
import statistics
import subprocess
import sys
from difflib import SequenceMatcher

# --- knobs mirrored from tools/pdf2md.py so re-OCR matches the converter -----
OCR_DPI = 200
OCR_MAX_EDGE_PX = 3000
OCR_TIMEOUT = 120
OCR_MIN_LINE_CONFIDENCE = 60.0  # pdf2md drops lines below this

CONF_BANDS = ((0, 60, "<60"), (60, 75, "60-75"), (75, 85, "75-85"), (85, 101, ">85"))

# Matches both the current label and the older one that predates confidence.
OCR_MARKER_RE = re.compile(
    r"^>\s*Text below was recovered by OCR(?:\s*\(confidence\s*(\d+)\s*/\s*100\))?",
    re.IGNORECASE,
)
SLIDE_RE = re.compile(r"^##\s+Slide\s+(\d+)\s*$")
FENCE_OPEN = "```text"
FENCE_CLOSE = "```"

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")
HEX_RE = re.compile(r"\b(?:0x[0-9A-Fa-f]{3,}|[0-9A-Fa-f]{6,})\b")
PATHY_RE = re.compile(r"[/\\][A-Za-z0-9_.-]+|\w+\(\)|::|->|\$\s*\w+|#include|\bdef\b|\breturn\b")


# ---------------------------------------------------------------------------
# Corpus parsing
# ---------------------------------------------------------------------------

class OcrBlock:
    __slots__ = ("path", "rel", "deck", "talk", "slide", "conf", "text",
                 "source_pdf", "pages", "line_no")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))

    @property
    def chars(self) -> int:
        return len(self.text)

    def tech_score(self) -> float:
        """How code/terminal/hex-like this block looks (0..1-ish, unbounded top)."""
        t = self.text
        if not t:
            return 0.0
        n = max(len(t), 1)
        hexish = sum(len(m.group(0)) for m in HEX_RE.finditer(t)) / n
        pathy = len(PATHY_RE.findall(t)) / max(len(t.split()), 1)
        punct = sum(1 for c in t if c in "{}[]()<>;=|&*/\\#$%_") / n
        digits = sum(1 for c in t if c.isdigit()) / n
        return 3.0 * hexish + 1.5 * pathy + 2.0 * punct + 1.0 * digits


def parse_frontmatter(lines: list[str]) -> dict:
    if not lines or lines[0].strip() != "---":
        return {}
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            v = v[1:-1]
        fm[k.strip()] = v
    return fm


def parse_file(path: str, md_root: str) -> tuple[list[OcrBlock], str, dict]:
    """Return (ocr blocks, structural text with OCR blocks removed, frontmatter)."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            lines = fh.read().split("\n")
    except OSError:
        return [], "", {}

    fm = parse_frontmatter(lines)
    rel = os.path.relpath(path, md_root)
    deck = rel.split(os.sep)[0] if os.sep in rel else ""
    talk = os.path.basename(path)

    blocks: list[OcrBlock] = []
    struct: list[str] = []
    slide = 0
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = SLIDE_RE.match(line)
        if m:
            slide = int(m.group(1))
            i += 1
            continue
        m = OCR_MARKER_RE.match(line)
        if m:
            conf = int(m.group(1)) if m.group(1) else None
            marker_line = i + 1
            j = i + 1
            # Skip blank lines to the opening fence.
            while j < n and not lines[j].strip():
                j += 1
            if j < n and lines[j].strip() == FENCE_OPEN:
                j += 1
                body = []
                while j < n and lines[j].strip() != FENCE_CLOSE:
                    body.append(lines[j])
                    j += 1
                blocks.append(OcrBlock(
                    path=path, rel=rel, deck=deck, talk=talk, slide=slide,
                    conf=conf, text="\n".join(body).strip(),
                    source_pdf=fm.get("source_pdf", ""),
                    pages=fm.get("pages", ""), line_no=marker_line,
                ))
                i = j + 1
                continue
            i = j
            continue
        struct.append(line)
        i += 1
    return blocks, "\n".join(struct), fm


def walk_corpus(md_root: str):
    for dirpath, _dirs, files in os.walk(md_root):
        for name in sorted(files):
            if name.endswith(".md") and name not in ("README.md", "INDEX.md"):
                yield os.path.join(dirpath, name)


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def summarise(values: list[float]) -> dict:
    if not values:
        return {}
    vs = sorted(values)
    out = {
        "n": len(vs),
        "min": vs[0],
        "max": vs[-1],
        "mean": round(statistics.fmean(vs), 2),
        "median": statistics.median(vs),
        "stdev": round(statistics.pstdev(vs), 2) if len(vs) > 1 else 0.0,
    }
    out["deciles"] = [round(vs[min(len(vs) - 1, int(len(vs) * d / 10))], 1)
                      for d in range(0, 11)]
    return out


def band_of(conf: float) -> str:
    for lo, hi, name in CONF_BANDS:
        if lo <= conf < hi:
            return name
    return ">85"


# ---------------------------------------------------------------------------
# Vocabulary from the exact (text-layer) half of the corpus
# ---------------------------------------------------------------------------

def build_vocab(struct_texts: list[str], min_count: int = 2) -> set[str]:
    counter: collections.Counter[str] = collections.Counter()
    for txt in struct_texts:
        for w in WORD_RE.findall(txt):
            if len(w) >= 3:
                counter[w.lower()] += 1
    return {w for w, c in counter.items() if c >= min_count}


def vocab_hit_rate(text: str, vocab: set[str]) -> tuple[float, list[str]]:
    """Fraction of >=3-letter alphabetic tokens known to the corpus vocabulary."""
    words = [w.lower() for w in WORD_RE.findall(text) if len(w) >= 3]
    if not words:
        return 1.0, []
    misses = [w for w in words if w not in vocab]
    return 1.0 - len(misses) / len(words), misses


# ---------------------------------------------------------------------------
# Ground truth: re-render + re-OCR from the source PDF
# ---------------------------------------------------------------------------

def render_page(pdf_path: str, page_index: int, png_out: str | None):
    import pymupdf
    doc = pymupdf.open(pdf_path)
    try:
        if page_index < 0 or page_index >= doc.page_count:
            return None, None
        page = doc[page_index]
        dpi = OCR_DPI
        long_in = max(page.rect.width, page.rect.height) / 72.0
        if long_in > 0 and long_in * dpi > OCR_MAX_EDGE_PX:
            dpi = max(120, int(OCR_MAX_EDGE_PX / long_in))
        gray = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
        png_gray = gray.tobytes("png")
        if png_out:
            page.get_pixmap(dpi=min(dpi, 150)).save(png_out)
        return png_gray, dpi
    finally:
        doc.close()


def reocr(png: bytes, tesseract: str = "/usr/bin/tesseract"):
    """Independent, UNFILTERED re-OCR. Returns (raw_text, filtered_text, words)."""
    proc = subprocess.run(
        [tesseract, "stdin", "stdout", "--psm", "3", "--oem", "1", "-l", "eng", "tsv"],
        input=png, capture_output=True, timeout=OCR_TIMEOUT,
    )
    tsv = proc.stdout.decode("utf-8", "replace")
    grouped: collections.OrderedDict = collections.OrderedDict()
    words: list[tuple[str, float]] = []
    for row in csv.DictReader(io.StringIO(tsv), delimiter="\t"):
        w = (row.get("text") or "").strip()
        if not w:
            continue
        try:
            conf = float(row.get("conf", -1))
        except ValueError:
            continue
        if conf < 0:
            continue
        words.append((w, conf))
        grouped.setdefault(
            (row.get("block_num"), row.get("par_num"), row.get("line_num")), []
        ).append((w, conf))
    raw_lines, kept_lines = [], []
    for ws in grouped.values():
        line = " ".join(w for w, _ in ws)
        raw_lines.append(line)
        if sum(c for _, c in ws) / len(ws) >= OCR_MIN_LINE_CONFIDENCE:
            kept_lines.append(line)
    return "\n".join(raw_lines), "\n".join(kept_lines), words


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def compare(stored: str, raw: str) -> dict:
    a, b = norm(stored), norm(raw)
    ratio = SequenceMatcher(None, a, b).ratio() if a and b else 0.0
    st = set(stored.split())
    rt = set(raw.split())
    recall = len(st & rt) / len(st) if st else 0.0
    return {"similarity": round(ratio, 3), "token_recall": round(recall, 3)}


def classify(sim: float, recall: float, vocab_rate: float) -> str:
    """Verdict heuristic; the human read of the page image is the final word."""
    if recall >= 0.9 and vocab_rate >= 0.75:
        return "accurate"
    if recall >= 0.75 and vocab_rate >= 0.55:
        return "mostly accurate"
    if recall >= 0.5 or vocab_rate >= 0.4:
        return "partly mangled"
    return "garbage"


# ---------------------------------------------------------------------------
# Sampling
# ---------------------------------------------------------------------------

def pick_sample(blocks: list[OcrBlock], n: int, src_root: str, rng: random.Random,
                tech_bias: bool = True) -> list[OcrBlock]:
    """Stratify across the confidence range, preferring technical-looking blocks.

    Blocks whose source PDF is missing (e.g. DEF CON, fetched separately) cannot
    be ground-truthed and are excluded.
    """
    usable = [b for b in blocks
              if b.source_pdf and os.path.exists(os.path.join(src_root, b.source_pdf))
              and b.chars >= 60]
    if not usable:
        return []

    def take(cand: list[OcrBlock], k: int, used: set[int]) -> list[OcrBlock]:
        cand = [b for b in cand if id(b) not in used]
        if tech_bias:
            cand = sorted(cand, key=lambda b: -b.tech_score())[: max(k * 5, 15)]
        rng.shuffle(cand)
        out = cand[:k]
        used.update(id(b) for b in out)
        return out

    used: set[int] = set()
    picked: list[OcrBlock] = []

    # (a) span the stated-confidence range using labelled blocks.
    buckets: dict[str, list[OcrBlock]] = collections.defaultdict(list)
    for b in usable:
        if b.conf is not None:
            buckets[band_of(float(b.conf))].append(b)
    live = [name for *_r, name in CONF_BANDS if buckets.get(name)]
    if live:
        per = max(1, int(round(n * 0.6)) // len(live))
        for name in live:
            picked.extend(take(buckets[name], per, used))

    # (b) spread the rest over decks that the reconversion has not relabelled
    #     yet, so the audit is not confined to one conference.
    by_deck: dict[str, list[OcrBlock]] = collections.defaultdict(list)
    for b in usable:
        by_deck[b.deck].append(b)
    decks = sorted(by_deck, key=lambda d: -len(by_deck[d]))
    di = 0
    while len(picked) < n and decks:
        deck = decks[di % len(decks)]
        got = take(by_deck[deck], 1, used)
        if not got:
            decks.remove(deck)
            if not decks:
                break
            continue
        picked.extend(got)
        di += 1
    return picked[:n]


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Audit OCR quality in the Markdown corpus.")
    ap.add_argument("--out", default="markdown",
                    help="Markdown corpus root (default: markdown)")
    ap.add_argument("--src", default=None,
                    help="repo root holding the source PDFs (default: parent of --out)")
    ap.add_argument("--sample", type=int, default=0,
                    help="ground-truth spot-check this many blocks (0 = stats only)")
    ap.add_argument("--seed", type=int, default=1729, help="sampling seed")
    ap.add_argument("--images", default=None,
                    help="directory to write rendered sample page PNGs into")
    ap.add_argument("--json", default=None, help="write full results as JSON here")
    ap.add_argument("--tesseract", default="/usr/bin/tesseract")
    ap.add_argument("--no-tech-bias", action="store_true",
                    help="sample uniformly instead of favouring code/terminal slides")
    ap.add_argument("--quote-chars", type=int, default=220,
                    help="characters of evidence to quote per sample")
    args = ap.parse_args(argv)

    md_root = os.path.abspath(args.out)
    src_root = os.path.abspath(args.src) if args.src else os.path.dirname(md_root)
    if not os.path.isdir(md_root):
        print(f"error: no such corpus directory: {md_root}", file=sys.stderr)
        return 2

    blocks: list[OcrBlock] = []
    struct_texts: list[str] = []
    files = 0
    files_with_ocr = 0
    struct_chars = 0
    for path in walk_corpus(md_root):
        bs, struct, _fm = parse_file(path, md_root)
        files += 1
        struct_texts.append(struct)
        struct_chars += len(struct)
        if bs:
            files_with_ocr += 1
            blocks.extend(bs)

    # ---------------- Pass 1: corpus statistics ----------------
    total_chars = sum(b.chars for b in blocks)
    labelled = [b for b in blocks if b.conf is not None]
    unlabelled = [b for b in blocks if b.conf is None]
    confs = [float(b.conf) for b in labelled]

    print("=" * 78)
    print("PASS 1 -- CORPUS OCR STATISTICS")
    print("=" * 78)
    print(f"markdown root      : {md_root}")
    print(f"markdown files     : {files}  ({files_with_ocr} contain OCR blocks)")
    print(f"OCR blocks         : {len(blocks)}")
    print(f"OCR characters     : {total_chars:,}")
    print(f"structural chars   : {struct_chars:,}  "
          f"(OCR = {100.0 * total_chars / max(struct_chars + total_chars, 1):.1f}% of corpus text)")
    print(f"blocks w/ stated confidence : {len(labelled)}")
    print(f"blocks w/o stated confidence: {len(unlabelled)} "
          f"({sum(b.chars for b in unlabelled):,} chars)")

    if confs:
        s = summarise(confs)
        print()
        print("Stated confidence (labelled blocks):")
        print(f"  min {s['min']:.0f}  median {s['median']:.0f}  mean {s['mean']:.2f}  "
              f"max {s['max']:.0f}  sd {s['stdev']:.2f}")
        print("  deciles (p0..p100): " + " ".join(f"{d:g}" for d in s["deciles"]))
        print()
        print("  band      blocks    share      chars     char share")
        by_band = collections.Counter(band_of(c) for c in confs)
        chars_band: collections.Counter[str] = collections.Counter()
        for b in labelled:
            chars_band[band_of(float(b.conf))] += b.chars
        lab_chars = sum(chars_band.values()) or 1
        for _lo, _hi, name in CONF_BANDS:
            k = by_band.get(name, 0)
            print(f"  {name:<8} {k:>7}  {100.0 * k / len(confs):>6.2f}%  "
                  f"{chars_band.get(name, 0):>10,}  {100.0 * chars_band.get(name, 0) / lab_chars:>6.2f}%")

    print()
    print("Per-deck OCR volume (top 12 by OCR chars):")
    deck_blocks: collections.Counter[str] = collections.Counter()
    deck_chars: collections.Counter[str] = collections.Counter()
    deck_conf: dict[str, list[float]] = collections.defaultdict(list)
    for b in blocks:
        deck_blocks[b.deck] += 1
        deck_chars[b.deck] += b.chars
        if b.conf is not None:
            deck_conf[b.deck].append(float(b.conf))
    print(f"  {'deck':<34} {'blocks':>7} {'chars':>10} {'mean conf':>10}")
    for deck, ch in deck_chars.most_common(12):
        mc = statistics.fmean(deck_conf[deck]) if deck_conf.get(deck) else float("nan")
        mcs = f"{mc:.1f}" if mc == mc else "n/a"
        print(f"  {deck[:34]:<34} {deck_blocks[deck]:>7} {ch:>10,} {mcs:>10}")

    # Vocabulary coherence over the whole corpus.
    vocab = build_vocab(struct_texts)
    print()
    print(f"Corpus vocabulary from PDF text layer: {len(vocab):,} distinct words "
          f"(seen >= 2x)")
    rates = []
    for b in blocks:
        r, _ = vocab_hit_rate(b.text, vocab)
        rates.append((r, b))
    only_rates = [r for r, _ in rates]
    if only_rates:
        vs = summarise([round(r, 4) for r in only_rates])
        print(f"OCR-block vocabulary hit rate: median {vs['median']:.3f}  "
              f"mean {vs['mean']:.3f}")
        print("  deciles (p0..p100): " + " ".join(f"{d:.3f}" for d in vs["deciles"]))
        for thr in (0.3, 0.5, 0.7):
            bad = [(r, b) for r, b in rates if r < thr]
            print(f"  blocks below {thr:.0%} known-word rate: {len(bad):>5} "
                  f"({100.0 * len(bad) / len(rates):>5.2f}%), "
                  f"{sum(b.chars for _, b in bad):>9,} chars "
                  f"({100.0 * sum(b.chars for _, b in bad) / max(total_chars, 1):>5.2f}% of OCR chars)")

    results = {
        "files": files, "files_with_ocr": files_with_ocr,
        "blocks": len(blocks), "ocr_chars": total_chars,
        "struct_chars": struct_chars,
        "labelled": len(labelled), "unlabelled": len(unlabelled),
        "confidence": summarise(confs) if confs else {},
        "bands": {name: sum(1 for c in confs if band_of(c) == name)
                  for *_r, name in CONF_BANDS},
        "samples": [],
    }

    # ---------------- Pass 2: ground truth ----------------
    if args.sample > 0:
        rng = random.Random(args.seed)
        chosen = pick_sample(blocks, args.sample, src_root, rng,
                             tech_bias=not args.no_tech_bias)
        print()
        print("=" * 78)
        print(f"PASS 2 -- GROUND-TRUTH SPOT CHECKS ({len(chosen)} blocks)")
        print("=" * 78)
        if args.images:
            os.makedirs(args.images, exist_ok=True)
        for i, b in enumerate(chosen, 1):
            pdf = os.path.join(src_root, b.source_pdf)
            png_out = (os.path.join(args.images, f"s{i:02d}_slide{b.slide}.png")
                       if args.images else None)
            print()
            print(f"--- sample {i}/{len(chosen)} " + "-" * 50)
            print(f"deck   : {b.deck}")
            print(f"talk   : {b.talk}")
            print(f"slide  : {b.slide}   stated confidence: "
                  f"{b.conf if b.conf is not None else 'unlabelled'}")
            print(f"pdf    : {b.source_pdf}")
            print(f"md     : {b.rel}:{b.line_no}   ocr chars: {b.chars}   "
                  f"tech score: {b.tech_score():.2f}")
            try:
                png, dpi = render_page(pdf, b.slide - 1, png_out)
            except Exception as exc:  # noqa: BLE001
                print(f"  RENDER FAILED: {exc}")
                continue
            if png is None:
                print("  RENDER FAILED: page index out of range")
                continue
            try:
                raw, refiltered, words = reocr(png, args.tesseract)
            except Exception as exc:  # noqa: BLE001
                print(f"  RE-OCR FAILED: {exc}")
                continue
            cmp_raw = compare(b.text, raw)
            cmp_filt = compare(b.text, refiltered)
            vrate, misses = vocab_hit_rate(b.text, vocab)
            low = sum(1 for _w, c in words if c < OCR_MIN_LINE_CONFIDENCE)
            verdict = classify(cmp_raw["similarity"], cmp_raw["token_recall"], vrate)
            measured = statistics.fmean([c for _w, c in words]) if words else 0.0
            print(f"  re-render dpi {dpi}; raw re-OCR {len(raw)} chars, "
                  f"corpus block {b.chars} chars "
                  f"(kept {100.0 * b.chars / max(len(raw), 1):.0f}% of page text)")
            print(f"  raw re-OCR mean word conf {measured:.1f}; "
                  f"{low}/{len(words)} words below {OCR_MIN_LINE_CONFIDENCE:.0f} "
                  f"({100.0 * low / max(len(words), 1):.0f}% discarded by the filter)")
            print(f"  similarity vs raw re-OCR {cmp_raw['similarity']:.3f}, "
                  f"token recall {cmp_raw['token_recall']:.3f}; "
                  f"vs refiltered {cmp_filt['similarity']:.3f}")
            print(f"  corpus-vocabulary hit rate {vrate:.3f}"
                  + (f"  unknown tokens: {', '.join(misses[:8])}" if misses else ""))
            print(f"  VERDICT (heuristic): {verdict}")
            q = b.text[: args.quote_chars].replace("\n", " | ")
            print(f'  corpus text: "{q}"')
            if png_out:
                print(f"  page image : {png_out}")
            results["samples"].append({
                "deck": b.deck, "talk": b.talk, "slide": b.slide,
                "stated_conf": b.conf, "chars": b.chars,
                "measured_mean_conf": round(measured, 1),
                "pct_words_below_60": round(100.0 * low / max(len(words), 1), 1),
                "similarity_raw": cmp_raw["similarity"],
                "token_recall": cmp_raw["token_recall"],
                "vocab_hit_rate": round(vrate, 3),
                "verdict": verdict, "png": png_out,
                "text": b.text, "raw_reocr": raw,
            })

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=2)
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
