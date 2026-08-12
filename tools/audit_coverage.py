#!/usr/bin/env python3
"""
audit_coverage.py — detect CONTENT LOSS in the PDF -> Markdown corpus.

The question this answers is not "did the converter produce a file?" but "does
that file still contain the text the PDF itself carries?". A deck can convert
cleanly, carry correct frontmatter and a full run of `## Slide N` headings and
still be missing most of its words, because the structural pass silently
returned nothing for pages that do have a text layer.

So every check here is a comparison against ground truth read straight out of
the PDF with PyMuPDF's own extractor:

  1. COVERAGE RATIO — sum(page.get_text()) over the whole document vs the text
     actually present in the Markdown. Counted in alphanumeric characters so
     Markdown scaffolding (`**`, `|`, `#`, blank lines) cannot inflate the
     result, and with OCR blocks excluded so recovered-from-pixels text cannot
     paper over a structural-pass failure. A healthy deck lands near 1.0.

  2. EMPTY SLIDES — `## Slide N` headings with no body. Empty is not by itself
     a bug: a full-bleed photograph legitimately has nothing to extract. The
     audit therefore opens the source page and separates the two cases, which
     is the whole point of the exercise:
        - source page has a text layer  -> BUG, the converter dropped real text
        - source page has no text layer -> correct, and OCR is re-run to prove
          there is nothing readable in the pixels either

  3. STARVED DECKS — many pages, almost no Markdown. Same per-page diagnosis,
     because the interesting distinction is identical: sparse source vs lost
     text.

Usage:
    python3 tools/audit_coverage.py --out markdown --sample 120
    python3 tools/audit_coverage.py --out markdown --sample 0 --json report.json
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from collections import defaultdict

os.environ.setdefault("PYMUPDF_MESSAGE", "path:" + os.devnull)
os.environ.setdefault("OMP_THREAD_LIMIT", "1")

import pymupdf  # noqa: E402

pymupdf.TOOLS.mupdf_display_errors(False)

# ocr_page()/image_coverage() live in the converter; re-implementing them here
# would audit a different pipeline than the one that produced the corpus.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import pdf2md  # noqa: E402
except Exception:  # noqa: BLE001
    pdf2md = None

SLIDE_RE = re.compile(r"^## Slide (\d+)\s*$")
OCR_NOTE_RE = re.compile(r"^>\s*Text below was recovered by OCR")
FENCE_RE = re.compile(r"^```")

# A page whose text layer holds at least this many alphanumeric characters is
# unambiguously carrying text; anything the Markdown lost from it is lost text.
PAGE_TEXT_BUG_ALNUM = 20

# OCR yield above this on a supposedly empty page means readable pixels the
# converter's gate skipped.
OCR_BUG_ALNUM = 60

# Some decks embed subset fonts with no usable ToUnicode map. Their text layer
# extracts as glyph codes -- a Caesar-shifted alphabet, C0 control bytes, or
# Arabic/Greek codepoints -- that renders correctly on screen and is unreadable
# as text. Character counts alone cannot see this: the characters are all there,
# they just do not spell anything. Counting common English words does see it,
# and the distinction matters because the two failure modes need different
# fixes (recover the text layer vs fall back to OCR).
ENGLISH_PROBE = re.compile(
    r"\b(the|and|for|with|this|that|from|are|not|you|use|can|our|all|but|has)\b", re.I)
# Hits per 1000 characters, measured over a whole deck. Font mapping is a
# document-level property and the test needs a document-sized sample: bullet
# fragments and code listings can legitimately go a hundred characters without
# a stopword, so a per-page version of this test misfires. Measured across 604
# decks: median 9.8, 5th percentile 3.1, and the sparsest genuinely-English deck
# in the archive scores 0.81. Decks with unmapped fonts score exactly 0.00, so
# the threshold sits well clear of both populations.
DECODABLE_MIN_HITS = 0.3
DECODABLE_MIN_CHARS = 1500

REPLACEMENT = "�"


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

def alnum_len(s: str) -> int:
    return sum(1 for c in s if c.isalnum())


def dedup_lines(text: str) -> str:
    """Drop repeated lines within a page.

    Slide decks built as overlays draw the same line once per build step, so
    `get_text()` hands back three identical copies of a code listing that the
    slide shows once. PyMuPDF4LLM keeps one copy, which is right -- but it makes
    a raw character comparison read as 67% content loss on a deck that lost
    nothing. Comparing against deduplicated ground truth removes that illusion
    without hiding real drops.
    """
    seen, out = set(), []
    for line in text.splitlines():
        key = re.sub(r"\s+", "", line)
        if not key:
            continue
        if key in seen:
            continue
        seen.add(key)
        out.append(line)
    return "\n".join(out)


def english_rate(s: str) -> float:
    """Common-English-word hits per 1000 characters. 0 means "not text"."""
    if not s:
        return 0.0
    return 1000.0 * len(ENGLISH_PROBE.findall(s)) / len(s)


def is_decodable(s: str) -> bool | None:
    """True if a text layer reads as language, None if there is too little to tell."""
    if len(s) < DECODABLE_MIN_CHARS:
        return None
    return english_rate(s) >= DECODABLE_MIN_HITS


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter dict, body). Values are left as raw strings."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fm = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        fm[k.strip()] = v
    return fm, text[end + 5:]


def parse_markdown(path: str) -> dict:
    """Split a converted deck into per-slide bodies, separating OCR from structure.

    `struct` counts only text the structural pass produced. `ocr` counts text
    inside the OCR fences. Keeping them apart is what makes an OCR-heavy deck
    with a broken structural pass visible instead of merely "fine".
    """
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        raw = fh.read()
    fm, body = parse_frontmatter(raw)

    slides: list[dict] = []
    cur: dict | None = None
    preamble: list[str] = []
    companion: list[str] = []
    in_companion = False
    mode = "struct"          # struct | ocr-note | ocr-fence
    for line in body.splitlines():
        m = SLIDE_RE.match(line)
        if m:
            cur = {"n": int(m.group(1)), "struct": [], "ocr": []}
            slides.append(cur)
            in_companion = False
            mode = "struct"
            continue
        if line.startswith("## Companion resources"):
            in_companion = True
            cur = None
            continue
        if in_companion:
            companion.append(line)
            continue
        if cur is None:
            preamble.append(line)
            continue

        if mode == "struct":
            if OCR_NOTE_RE.match(line):
                mode = "ocr-note"
                continue
            cur["struct"].append(line)
        elif mode == "ocr-note":
            # The note is followed by a blank line then a ```text fence.
            if FENCE_RE.match(line):
                mode = "ocr-fence"
            elif line.strip():
                mode = "struct"
                cur["struct"].append(line)
        elif mode == "ocr-fence":
            if FENCE_RE.match(line):
                mode = "struct"
            else:
                cur["ocr"].append(line)

    for s in slides:
        s["struct_text"] = "\n".join(s["struct"]).strip()
        s["ocr_text"] = "\n".join(s["ocr"]).strip()
        s["struct_alnum"] = alnum_len(s["struct_text"])
        s["ocr_alnum"] = alnum_len(s["ocr_text"])
        del s["struct"], s["ocr"]

    return {
        "frontmatter": fm,
        "body_chars": len(body),
        "slides": slides,
        "companion_alnum": alnum_len("\n".join(companion)),
        "preamble_alnum": alnum_len("\n".join(preamble)),
    }


# ---------------------------------------------------------------------------
# PDF ground truth
# ---------------------------------------------------------------------------

def pdf_page_text(pdf_path: str, want_coverage: bool = False
                  ) -> tuple[list[str], list[float], str | None]:
    """Per-page text layer, and optionally per-page raster image coverage.

    Coverage matters because it is the converter's own OCR gate: a page below
    OCR_IMAGE_COVERAGE never gets rendered, so a page drawn entirely in vector
    graphics is skipped by both passes.
    """
    try:
        doc = pymupdf.open(pdf_path)
        if doc.needs_pass:
            doc.close()
            return [], [], "encrypted"
        pages, cov = [], []
        for page in doc:
            try:
                pages.append(page.get_text() or "")
            except Exception:  # noqa: BLE001
                pages.append("")
            cov.append(pdf2md.image_coverage(page) if (want_coverage and pdf2md) else 0.0)
        doc.close()
        return pages, cov, None
    except Exception as exc:  # noqa: BLE001
        return [], [], f"{type(exc).__name__}: {exc}"


def audit_deck(job: tuple) -> dict:
    md_path, pdf_path, rel_md, rel_pdf = job
    out = {"markdown": rel_md, "source_pdf": rel_pdf, "error": ""}
    try:
        parsed = parse_markdown(md_path)
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"markdown-read: {type(exc).__name__}: {exc}"
        return out

    pages, coverage, err = pdf_page_text(pdf_path, want_coverage=True)
    if err:
        out["error"] = f"pdf-read: {err}"
        return out

    slides = parsed["slides"]
    page_alnum = [alnum_len(dedup_lines(t)) for t in pages]
    page_alnum_raw = [alnum_len(t) for t in pages]
    struct_alnum = sum(s["struct_alnum"] for s in slides)
    ocr_alnum = sum(s["ocr_alnum"] for s in slides)
    pdf_alnum = sum(page_alnum)
    pdf_text = "\n".join(pages)
    decodable = is_decodable(pdf_text)

    # Slides whose only "content" is U+FFFD are empty in every sense that
    # matters, so alnum -- not raw length -- decides emptiness.
    empty = [s["n"] for s in slides if s["struct_alnum"] == 0 and s["ocr_alnum"] == 0]
    # Slides empty of structural text but carrying text in the source layer are
    # the direct evidence of a dropped page.
    dropped_pages, dropped_readable, lossy = [], [], []
    for s in slides:
        i = s["n"] - 1
        if not (0 <= i < len(pages)) or page_alnum[i] < PAGE_TEXT_BUG_ALNUM:
            continue
        # Under-covered: the page carries text, the slide kept less than half of
        # it. Only these pages are worth a page-level diagnosis -- probing a
        # page the Markdown already represents would indict a healthy deck.
        if s["struct_alnum"] < 0.5 * page_alnum[i]:
            lossy.append(s["n"])
        if s["struct_alnum"]:
            continue
        dropped_pages.append(s["n"])
        if decodable is not False:
            dropped_readable.append(s["n"])

    # Why is each empty slide empty? Answered from the source, for every empty
    # slide rather than a sample, using only cheap signals.
    census: dict[str, int] = defaultdict(int)
    never_ocred = []
    for n in empty:
        i = n - 1
        if not (0 <= i < len(pages)):
            continue
        if page_alnum[i] >= PAGE_TEXT_BUG_ALNUM:
            census["text-layer-present-but-dropped"] += 1
        elif pdf2md is not None and coverage[i] < pdf2md.OCR_IMAGE_COVERAGE:
            # No text layer and too little raster coverage: the OCR gate never
            # fired, so nothing ever looked at this page's pixels.
            census["no-text-layer-ocr-never-attempted"] += 1
            never_ocred.append(n)
        else:
            census["no-text-layer-ocr-ran-and-found-nothing"] += 1

    md_all = "\n".join(s["struct_text"] + s["ocr_text"] for s in slides)
    out.update({
        "pages": len(pages),
        "slides": len(slides),
        "pdf_alnum": pdf_alnum,
        "pdf_alnum_raw": sum(page_alnum_raw),
        "duplicate_draw_chars": sum(page_alnum_raw) - pdf_alnum,
        "pdf_decodable": decodable,
        "pdf_english_rate": round(english_rate(pdf_text), 2),
        "md_replacement_chars": md_all.count(REPLACEMENT),
        "md_english_rate": round(english_rate(md_all), 2),
        "struct_alnum": struct_alnum,
        "ocr_alnum": ocr_alnum,
        "companion_alnum": parsed["companion_alnum"],
        "md_body_chars": parsed["body_chars"],
        "ratio_struct": (struct_alnum / pdf_alnum) if pdf_alnum else None,
        "ratio_total": ((struct_alnum + ocr_alnum) / pdf_alnum) if pdf_alnum else None,
        "empty_slides": len(empty),
        "empty_slide_nums": empty[:400],
        "empty_share": (len(empty) / len(slides)) if slides else None,
        "dropped_pages": len(dropped_pages),
        "dropped_page_nums": dropped_pages[:400],
        "dropped_readable_pages": len(dropped_readable),
        "dropped_readable_page_nums": dropped_readable[:400],
        "lossy_pages": len(lossy),
        "lossy_page_nums": lossy[:400],
        "empty_census": dict(census),
        "never_ocred_page_nums": never_ocred[:400],
        "chars_per_page": (struct_alnum + ocr_alnum) / len(pages) if pages else 0.0,
        "pdf_chars_per_page": pdf_alnum / len(pages) if pages else 0.0,
        "frontmatter_pages": parsed["frontmatter"].get("pages", ""),
    })
    return out


# ---------------------------------------------------------------------------
# Per-page diagnosis: "correct - source has no text" vs "BUG - text dropped"
# ---------------------------------------------------------------------------

def diagnose_page(page: "pymupdf.Page", deck_decodable: bool | None = None,
                  do_ocr: bool = True) -> dict:
    """Open one source page and decide why the Markdown for it came out empty.

    Every branch is decided from the source, never from the Markdown: what the
    text layer holds, whether the deck's fonts map to real characters, and what
    OCR can read off the rendered pixels. `deck_decodable` comes from the whole
    document because one slide of bullet fragments is too small a sample to tell
    "terse" from "not language".
    """
    text = page.get_text() or ""
    eng = english_rate(text)
    d = {
        "text_layer_alnum": alnum_len(text),
        "text_layer_english_rate": round(eng, 2),
        "ascii_frac": round(sum(1 for c in text if 32 <= ord(c) < 127) / len(text), 2)
                      if text else 0.0,
        "text_layer_sample": " ".join(text.split())[:180],
        "image_coverage": pdf2md.image_coverage(page) if pdf2md else None,
        "n_images": len(page.get_images(full=True)),
        "n_drawings": 0,
        "ocr_alnum": 0,
        "ocr_conf": 0.0,
        "ocr_sample": "",
    }
    try:
        d["n_drawings"] = len(page.get_drawings())
    except Exception:  # noqa: BLE001
        pass

    has_text = d["text_layer_alnum"] >= PAGE_TEXT_BUG_ALNUM
    readable = has_text and deck_decodable is not False

    if readable:
        # Clean, extractable prose that never reached the Markdown.
        d["verdict"] = "BUG-readable-text-layer-dropped"
        return d

    if do_ocr and pdf2md is not None:
        # ocr_page() has grown extra return values over time; take the first two
        # positionally so this audit keeps working when it grows more.
        result = pdf2md.ocr_page(page)
        otext, oconf = result[0], result[1]
        d["ocr_alnum"] = alnum_len(otext)
        d["ocr_conf"] = round(oconf, 1)
        d["ocr_sample"] = " ".join(otext.split())[:180]

    if has_text:
        # Glyph codes with no ToUnicode map: the page shows words, the text
        # layer spells nothing, and the Markdown gets U+FFFD instead of content.
        d["verdict"] = ("BUG-unmappable-font-ocr-would-recover"
                        if d["ocr_alnum"] >= OCR_BUG_ALNUM
                        else "unmappable-font-and-ocr-also-fails")
    elif d["ocr_alnum"] >= OCR_BUG_ALNUM:
        d["verdict"] = "BUG-readable-pixels-not-captured"
    elif d["text_layer_alnum"] > 0:
        d["verdict"] = "minor-trace-text-dropped"
    elif d["n_images"] == 0 and d["n_drawings"] <= 2:
        d["verdict"] = "correct-blank-page"
    else:
        d["verdict"] = "correct-image-only-no-readable-text"
    return d


def diagnose_deck(pdf_path: str, page_nums: list[int], max_pages: int,
                  do_ocr: bool = True) -> list[dict]:
    """Diagnose a spread of pages (first/middle/last, not just the first few)."""
    if not page_nums:
        return []
    if len(page_nums) > max_pages:
        step = len(page_nums) / max_pages
        page_nums = [page_nums[int(i * step)] for i in range(max_pages)]
    res = []
    doc = pymupdf.open(pdf_path)
    try:
        deck_dec = is_decodable("\n".join((p.get_text() or "") for p in doc))
        for n in page_nums:
            if not (1 <= n <= doc.page_count):
                continue
            d = diagnose_page(doc[n - 1], deck_decodable=deck_dec, do_ocr=do_ocr)
            d["page"] = n
            d["deck_fonts_decodable"] = deck_dec
            res.append(d)
    finally:
        doc.close()
    return res


# ---------------------------------------------------------------------------
# Corpus enumeration / sampling
# ---------------------------------------------------------------------------

def collect_pairs(out_root: str, src_root: str, skip_folders: set[str],
                  min_age: float) -> tuple[list[tuple], list[str]]:
    """Pair every Markdown file with its source PDF, via the frontmatter.

    Files younger than `min_age` seconds are skipped: a conversion may be
    running, and half-written Markdown would read as catastrophic text loss.
    """
    now = time.time()
    by_pdf: dict[str, tuple] = {}
    notes = []
    for dirpath, dirnames, filenames in os.walk(out_root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if not fn.endswith(".md") or fn in ("INDEX.md", "README.md"):
                continue
            md_path = os.path.join(dirpath, fn)
            rel_md = os.path.relpath(md_path, out_root)
            folder = rel_md.split(os.sep)[0]
            if folder in skip_folders:
                continue
            try:
                if now - os.path.getmtime(md_path) < min_age:
                    notes.append(f"skipped (written {now - os.path.getmtime(md_path):.0f}s ago): {rel_md}")
                    continue
                with open(md_path, "r", encoding="utf-8", errors="replace") as fh:
                    head = fh.read(4096)
            except OSError:
                continue
            fm, _ = parse_frontmatter(head + "\n---\n")
            rel_pdf = fm.get("source_pdf", "")
            if not rel_pdf:
                notes.append(f"no source_pdf in frontmatter: {rel_md}")
                continue
            pdf_path = os.path.join(src_root, rel_pdf)
            if not os.path.exists(pdf_path):
                notes.append(f"source PDF missing: {rel_pdf}")
                continue
            job = (md_path, pdf_path, rel_md, rel_pdf)
            # Re-runs leave "<slug>-2.md" duplicates of the same deck. Keep the
            # fullest copy so duplication cannot masquerade as content loss.
            prev = by_pdf.get(rel_pdf)
            if prev is None or os.path.getsize(md_path) > os.path.getsize(prev[0]):
                by_pdf[rel_pdf] = job
    return list(by_pdf.values()), notes


def scan_source(pdf_path: str) -> dict:
    """Source-side check, independent of the Markdown.

    Worth having on its own: it answers "can this deck's text be read at all?"
    while a conversion is mid-flight and the Markdown cannot be trusted, and it
    identifies decks where a coverage ratio near 1.0 would be meaningless
    because neither side holds words.
    """
    pages, _cov, err = pdf_page_text(pdf_path)
    if err:
        return {"pdf": pdf_path, "error": err}
    text = "\n".join(pages)
    return {"pdf": pdf_path, "error": "", "pages": len(pages),
            "alnum": alnum_len(text), "english_rate": round(english_rate(text), 2),
            "decodable": is_decodable(text),
            "text_pages": sum(1 for p in pages if alnum_len(p) >= PAGE_TEXT_BUG_ALNUM)}


def stratified_sample(jobs: list[tuple], n: int, seed: int) -> list[tuple]:
    """Round-robin across conference folders so every folder is represented."""
    if n <= 0 or n >= len(jobs):
        return jobs
    buckets: dict[str, list[tuple]] = defaultdict(list)
    for j in jobs:
        buckets[j[2].split(os.sep)[0]].append(j)
    rng = random.Random(seed)
    for v in buckets.values():
        rng.shuffle(v)
    picked, keys = [], sorted(buckets)
    while len(picked) < n and any(buckets[k] for k in keys):
        for k in keys:
            if buckets[k]:
                picked.append(buckets[k].pop())
                if len(picked) >= n:
                    break
    return picked


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def pct(x) -> str:
    return "n/a" if x is None else f"{x * 100:5.1f}%"


def quantiles(vals: list[float]) -> dict:
    if not vals:
        return {}
    s = sorted(vals)

    def q(p):
        return s[min(len(s) - 1, int(p * len(s)))]
    return {"min": s[0], "p05": q(0.05), "p25": q(0.25), "median": q(0.50),
            "p75": q(0.75), "p95": q(0.95), "max": s[-1],
            "mean": sum(s) / len(s), "n": len(s)}


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown", help="Markdown corpus root")
    ap.add_argument("--src", default=".", help="root holding the source PDF folders")
    ap.add_argument("--sample", type=int, default=0,
                    help="audit at most N decks, spread across all conference "
                         "folders (0 = every deck)")
    ap.add_argument("--seed", type=int, default=1234)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--skip-folder", action="append", default=None,
                    help="conference folder to ignore (default: 'DEF CON 34', "
                         "whose sources are not in the repo)")
    ap.add_argument("--min-age", type=float, default=45.0,
                    help="ignore Markdown written in the last N seconds (a "
                         "conversion may be mid-write)")
    ap.add_argument("--ratio-flag", type=float, default=0.60,
                    help="flag decks whose structural text is below this "
                         "fraction of the PDF text layer")
    ap.add_argument("--worst", type=int, default=15, help="rows in the worst-N tables")
    ap.add_argument("--diagnose-top", type=int, default=10,
                    help="decks to diagnose page-by-page in sections 2 and 3")
    ap.add_argument("--diagnose-pages", type=int, default=6,
                    help="pages to open per diagnosed deck")
    ap.add_argument("--no-ocr", action="store_true",
                    help="skip the OCR step of the page diagnosis (faster, but "
                         "cannot prove an image-only page is text-free)")
    ap.add_argument("--json", default="", help="write the full report as JSON here")
    ap.add_argument("--source-scan", action="store_true",
                    help="scan the source PDFs only (no Markdown needed) and "
                         "report decks whose text layer does not decode to "
                         "language — usable while a conversion is mid-write")
    args = ap.parse_args()

    skip = set(args.skip_folder) if args.skip_folder is not None else {"DEF CON 34"}

    if args.source_scan:
        return source_scan_report(args, skip)
    jobs, notes = collect_pairs(args.out, args.src, skip, args.min_age)
    total_available = len(jobs)
    jobs = stratified_sample(jobs, args.sample, args.seed)

    t0 = time.time()
    if args.workers > 1:
        import multiprocessing as mp
        with mp.Pool(args.workers) as pool:
            rows = pool.map(audit_deck, jobs, chunksize=1)
    else:
        rows = [audit_deck(j) for j in jobs]
    elapsed = time.time() - t0

    ok = [r for r in rows if not r["error"]]
    bad = [r for r in rows if r["error"]]
    scored = [r for r in ok if r["ratio_struct"] is not None]

    print("=" * 100)
    print(f"COVERAGE AUDIT  —  {len(rows)} decks audited of {total_available} available "
          f"(folders skipped: {', '.join(sorted(skip)) or 'none'})  [{elapsed:.1f}s]")
    print("=" * 100)
    for n in notes[:10]:
        print(f"  note: {n}")
    if len(notes) > 10:
        print(f"  note: ... and {len(notes) - 10} more")
    if bad:
        print(f"\n  {len(bad)} decks could not be audited:")
        for r in bad[:10]:
            print(f"    {r['error']}  {r['markdown']}")

    by_folder: dict[str, list] = defaultdict(list)
    for r in scored:
        by_folder[r["markdown"].split(os.sep)[0]].append(r)

    # --- 1. coverage ratio ---------------------------------------------------
    qs = quantiles([r["ratio_struct"] for r in scored])
    qt = quantiles([r["ratio_total"] for r in scored])
    print("\n" + "-" * 100)
    print("1. TEXT-LAYER COVERAGE  (markdown structural alnum chars / PDF get_text alnum chars,")
    print("   the PDF side deduplicated per page so overlay builds do not read as loss)")
    print("-" * 100)
    no_layer = [r for r in ok if not r["pdf_alnum"]]
    print(f"  decks scored: {qs.get('n', 0)}   "
          f"(unscoreable: {len(no_layer)} decks whose PDF has no text layer at all — "
          f"image-only, so OCR is the only possible source)")
    for r in sorted(no_layer, key=lambda r: -r["pages"])[:5]:
        print(f"      no text layer: {r['pages']:4d}pg  md_alnum="
              f"{r['struct_alnum'] + r['ocr_alnum']:6d}  {r['markdown']}")
    print("  structural-only ratio: " + "  ".join(
        f"{k}={qs[k]:.3f}" for k in ("min", "p05", "p25", "median", "mean", "p75", "p95", "max") if k in qs))
    print("  incl. OCR text ratio : " + "  ".join(
        f"{k}={qt[k]:.3f}" for k in ("min", "p05", "p25", "median", "mean", "p75", "p95", "max") if k in qt))
    flagged = sorted([r for r in scored if r["ratio_struct"] < args.ratio_flag],
                     key=lambda r: r["ratio_struct"])
    dup = sum(r["duplicate_draw_chars"] for r in ok)
    print(f"  duplicate draws collapsed out of the PDF side: {dup} chars "
          f"({100.0 * dup / max(1, sum(r['pdf_alnum_raw'] for r in ok)):.1f}% of raw get_text)")
    print(f"\n  decks below --ratio-flag {args.ratio_flag}: {len(flagged)} "
          f"({100.0 * len(flagged) / max(1, len(scored)):.1f}%)")
    print(f"\n  worst {args.worst} decks by structural coverage:")
    print(f"    {'ratio':>7} {'+ocr':>6} {'pdf_chars':>10} {'md_chars':>9} {'pg':>4} {'empty':>6}  deck")
    for r in flagged[:args.worst]:
        print(f"    {r['ratio_struct']:7.3f} {r['ratio_total']:6.3f} {r['pdf_alnum']:10d} "
              f"{r['struct_alnum']:9d} {r['pages']:4d} {r['empty_slides']:6d}  {r['markdown']}")

    # A ratio near 1.0 only proves the Markdown kept as many characters as the
    # PDF holds -- not that either side is readable. Decks whose fonts carry no
    # ToUnicode map pass that test while carrying no words at all.
    garbled = sorted([r for r in ok if r["pdf_decodable"] is False],
                     key=lambda r: -r["pdf_alnum"])
    fffd = sorted([r for r in ok if r["md_replacement_chars"] > 200],
                  key=lambda r: -r["md_replacement_chars"])
    print(f"\n  decks whose PDF text layer does not decode to language "
          f"(subset fonts with no ToUnicode): {len(garbled)}")
    for r in garbled[:args.worst]:
        print(f"    eng/1k={r['pdf_english_rate']:6.2f} pdf_chars={r['pdf_alnum']:7d} "
              f"md_U+FFFD={r['md_replacement_chars']:6d} ocr_chars={r['ocr_alnum']:7d} "
              f"pg={r['pages']:4d}  {r['markdown']}")
    print(f"\n  decks whose Markdown contains >200 U+FFFD replacement characters "
          f"(unreadable text written into the corpus): {len(fffd)}")
    for r in fffd[:args.worst]:
        print(f"    U+FFFD={r['md_replacement_chars']:6d}  md_eng/1k={r['md_english_rate']:6.2f} "
              f"pg={r['pages']:4d}  {r['markdown']}")

    print("\n  per-folder median structural ratio:")
    for f in sorted(by_folder):
        fq = quantiles([r["ratio_struct"] for r in by_folder[f]])
        low = sum(1 for r in by_folder[f] if r["ratio_struct"] < args.ratio_flag)
        print(f"    {fq['median']:.3f}  (min {fq['min']:.3f}, n={fq['n']:3d}, "
              f"below-flag {low:3d})  {f}")

    # --- 2. empty slides -----------------------------------------------------
    print("\n" + "-" * 100)
    print("2. EMPTY SLIDES  (`## Slide N` with no body at all)")
    print("-" * 100)
    tot_slides = sum(r["slides"] for r in ok)
    tot_empty = sum(r["empty_slides"] for r in ok)
    tot_dropped = sum(r["dropped_pages"] for r in ok)
    tot_readable = sum(r["dropped_readable_pages"] for r in ok)
    print(f"  slides: {tot_slides}   empty: {tot_empty} ({100.0 * tot_empty / max(1, tot_slides):.1f}%)"
          f"\n  empties whose source page HAS a text layer: {tot_dropped} "
          f"({100.0 * tot_dropped / max(1, tot_empty):.1f}% of empties)"
          f"\n  ... of those, text that decodes to real language: {tot_readable} "
          f"(unambiguous drops); the rest are unmappable-font pages")
    census: dict[str, int] = defaultdict(int)
    for r in ok:
        for k, v in r["empty_census"].items():
            census[k] += v
    print("\n  why each empty slide is empty (every empty slide, judged from the source):")
    for k, v in sorted(census.items(), key=lambda kv: -kv[1]):
        print(f"    {v:5d} ({100.0 * v / max(1, tot_empty):5.1f}%)  {k}")

    worst_empty = sorted([r for r in ok if r["slides"] >= 5],
                         key=lambda r: (-(r["empty_share"] or 0), -r["slides"]))
    print(f"\n  worst {args.worst} decks by share of empty slides:")
    print(f"    {'empty%':>7} {'empty':>6} {'slides':>7} {'w/textlayer':>12} {'readable':>9}  deck")
    for r in worst_empty[:args.worst]:
        print(f"    {pct(r['empty_share']):>7} {r['empty_slides']:6d} {r['slides']:7d} "
              f"{r['dropped_pages']:12d} {r['dropped_readable_pages']:9d}  {r['markdown']}")

    diag_empty = []
    for r in worst_empty[:args.diagnose_top]:
        pdf_path = os.path.join(args.src, r["source_pdf"])
        d = diagnose_deck(pdf_path, r["empty_slide_nums"], args.diagnose_pages,
                          do_ocr=not args.no_ocr)
        diag_empty.append({"deck": r["markdown"], "pdf": r["source_pdf"],
                           "empty_slides": r["empty_slides"], "slides": r["slides"],
                           "pages": r["pages"], "diagnosis": d})
    print_diagnoses(diag_empty)

    # --- 3. starved decks ----------------------------------------------------
    print("\n" + "-" * 100)
    print("3. STARVED DECKS  (many pages, almost no markdown)")
    print("-" * 100)
    cpp = quantiles([r["chars_per_page"] for r in ok])
    print("  markdown alnum chars/page across corpus: " + "  ".join(
        f"{k}={cpp[k]:.0f}" for k in ("min", "p05", "p25", "median", "mean", "p75", "p95", "max") if k in cpp))
    med = cpp.get("median", 0)
    starved = sorted([r for r in ok if r["pages"] >= 15],
                     key=lambda r: r["chars_per_page"])
    below = sum(1 for r in starved if r["chars_per_page"] < 0.25 * med)
    print(f"  decks with >=15 pages and <25% of median chars/page ({0.25 * med:.0f}): {below}")
    print(f"\n  worst {args.worst}:")
    print(f"    {'md_c/pg':>8} {'pdf_c/pg':>9} {'pg':>4} {'md_chars':>9} {'pdf_chars':>10} "
          f"{'ratio':>7} {'lossy_pg':>9}  deck")
    for r in starved[:args.worst]:
        rs = r["ratio_struct"]
        print(f"    {r['chars_per_page']:8.1f} {r['pdf_chars_per_page']:9.1f} {r['pages']:4d} "
              f"{r['struct_alnum'] + r['ocr_alnum']:9d} {r['pdf_alnum']:10d} "
              f"{('%.3f' % rs) if rs is not None else '   n/a':>7} {r['lossy_pages']:9d}  "
              f"{r['markdown']}")

    diag_starved = []
    for r in starved[:args.diagnose_top]:
        pdf_path = os.path.join(args.src, r["source_pdf"])
        # Only pages the Markdown under-covers get diagnosed. A deck can be
        # starved simply because its slides are three words and a picture, and
        # probing pages it faithfully converted would manufacture findings.
        nums = r["empty_slide_nums"] or r["lossy_page_nums"]
        d = diagnose_deck(pdf_path, nums, args.diagnose_pages, do_ocr=not args.no_ocr)
        diag_starved.append({"deck": r["markdown"], "pdf": r["source_pdf"],
                             "empty_slides": r["empty_slides"], "slides": r["slides"],
                             "pages": r["pages"], "chars_per_page": r["chars_per_page"],
                             "lossy_pages": r["lossy_pages"],
                             "ratio_struct": r["ratio_struct"], "diagnosis": d})
    print_diagnoses(diag_starved)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"rows": rows, "notes": notes,
                       "quantiles": {"ratio_struct": qs, "ratio_total": qt,
                                     "chars_per_page": cpp},
                       "diagnosis_empty": diag_empty,
                       "diagnosis_starved": diag_starved}, fh, indent=1)
        print(f"\nJSON report written to {args.json}")
    return 0


def source_scan_report(args, skip: set[str]) -> int:
    pdfs = []
    for dirpath, dirnames, filenames in os.walk(args.src):
        dirnames[:] = [d for d in dirnames
                       if not d.startswith(".") and d not in {"markdown", "tools"}]
        rel_dir = os.path.relpath(dirpath, args.src)
        if rel_dir.split(os.sep)[0] in skip:
            continue
        for fn in sorted(filenames):
            if fn.lower().endswith(".pdf"):
                pdfs.append(os.path.join(dirpath, fn))
    pdfs.sort()
    pdfs = stratified_sample([(p, p, os.path.relpath(p, args.src), p) for p in pdfs],
                             args.sample, args.seed)
    paths = [j[0] for j in pdfs]

    t0 = time.time()
    if args.workers > 1:
        import multiprocessing as mp
        with mp.Pool(args.workers) as pool:
            rows = pool.map(scan_source, paths, chunksize=1)
    else:
        rows = [scan_source(p) for p in paths]

    good = [r for r in rows if not r["error"]]
    undec = sorted([r for r in good if r["decodable"] is False],
                   key=lambda r: -r["alnum"])
    notext = [r for r in good if r["alnum"] == 0]
    print("=" * 100)
    print(f"SOURCE SCAN — {len(good)} PDFs read directly ({time.time() - t0:.1f}s)")
    print("=" * 100)
    print(f"  no text layer at all (OCR is the only route): {len(notext)}")
    print(f"  text layer present but not decodable to language: {len(undec)}")
    for r in undec:
        print(f"    eng/1k={r['english_rate']:6.2f}  chars={r['alnum']:8d}  "
              f"pages={r['pages']:4d}  {os.path.relpath(r['pdf'], args.src)}")
    rates = sorted(r["english_rate"] for r in good if r["alnum"] >= DECODABLE_MIN_CHARS)
    if rates:
        q = quantiles(rates)
        print("\n  english-word rate per 1000 chars across decks with a text layer: "
              + "  ".join(f"{k}={q[k]:.1f}" for k in ("min", "p05", "median", "mean", "max")))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=1)
        print(f"\nJSON report written to {args.json}")
    return 0


def print_diagnoses(entries: list[dict]) -> None:
    for e in entries:
        counts: dict[str, int] = defaultdict(int)
        for d in e["diagnosis"]:
            counts[d["verdict"]] += 1
        verdicts = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        extra = ""
        if e.get("ratio_struct") is not None:
            extra = f", coverage {e['ratio_struct']:.3f}, {e.get('lossy_pages', 0)} under-covered pages"
        print(f"\n  * {e['deck']}")
        print(f"      {e['pages']} pages, {e['empty_slides']}/{e['slides']} empty slides{extra}"
              f"   probe: {verdicts or 'NO under-covered pages — markdown matches source'}")
        for d in e["diagnosis"]:
            print(f"      p{d['page']:<4} {d['verdict']:<38} "
                  f"textlayer={d['text_layer_alnum']:<6} ascii={d['ascii_frac']:<5} "
                  f"imgcov={d['image_coverage']:.2f} "
                  f"imgs={d['n_images']:<3} draw={d['n_drawings']:<5} "
                  f"ocr={d['ocr_alnum']:<5} conf={d['ocr_conf']:.0f}")
            if d["text_layer_sample"]:
                print(f"            text: {d['text_layer_sample'][:120]!r}")
            elif d["ocr_sample"]:
                print(f"            ocr : {d['ocr_sample'][:120]!r}")


if __name__ == "__main__":
    raise SystemExit(main())
