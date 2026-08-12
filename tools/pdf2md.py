#!/usr/bin/env python3
"""
pdf2md.py — Convert security-conference slide decks (PDF) into LLM-ingestible Markdown.

Why this design (see tools/README.md for the full rationale):

Conference slide decks are NOT papers. They are text-sparse, image-dense, and a
large share of their real technical content -- terminal output, source code,
disassembly, network diagrams, exploit flow charts -- lives inside raster images
with no text layer at all. A naive `pdftotext`-style extraction silently drops
that content and produces a corpus that *looks* fine but is missing the payload.

So this converter runs two passes per page:

  1. STRUCTURAL PASS (PyMuPDF4LLM) -- reads the PDF's own content stream. No ML,
     no GPU, milliseconds per page. Recovers real headings, bold/emphasis, lists,
     tables and reading order.

  2. OCR GAP-FILL PASS (Tesseract) -- triggered only for pages that come back
     text-poor *and* are visually image-dominated. Those pages get rendered at
     high DPI and OCR'd, recovering the screenshot/code content the structural
     pass cannot see. Gating on both conditions avoids burning hours OCR-ing
     title slides and stock photography.

Output is one Markdown file per deck:
  - YAML frontmatter carrying retrieval metadata that survives chunking
  - `## Slide N` headings, giving any chunker clean, semantically-real split points
  - OCR text fenced in a labelled block so downstream consumers can tell
    high-confidence text from OCR-confidence text
  - companion `_tools.txt` / `_code.txt` sidecar files folded in as a final section

Usage:
    python3 tools/pdf2md.py --src . --out markdown
    python3 tools/pdf2md.py --src "DEF CON 34" --out markdown --workers 4
    python3 tools/pdf2md.py --src . --out markdown --no-ocr      # fast structural-only
"""

from __future__ import annotations

import argparse
import collections
import csv
import datetime as _dt
import io
import hashlib
import json
import multiprocessing as mp
import os
import re
import subprocess
import sys
import traceback

# PyMuPDF is noisy on malformed PDFs (and conference decks are frequently
# malformed). Silence the C-level warnings; we record real failures ourselves.
os.environ.setdefault("PYMUPDF_MESSAGE", "path:" + os.devnull)

# We already parallelise across documents, so let each Tesseract run stay
# single-threaded. Measured: identical character yield, without four worker
# processes each spawning an OpenMP pool and oversubscribing the CPU.
os.environ.setdefault("OMP_THREAD_LIMIT", "1")

import pymupdf  # noqa: E402
import pymupdf4llm  # noqa: E402

pymupdf.TOOLS.mupdf_display_errors(False)

# PyMuPDF4LLM >= 1.28 ships a GNN layout engine. Keep it on: measured on a
# text-rich deck it recovers 12,870 characters against the legacy parser's 3,313
# -- it fixes reading order and picks up text the legacy path drops entirely
# (speaker attribution lines, text inside figures) for ~0.13s/page.
#
# Its *built-in* picture OCR is a different matter and we turn it off below. It
# costs a further ~0.58s/page and, because every conference slide carries a
# logo, it OCRs that logo into garbage ("EQ<br>blackhat<br>USA 20253") on every
# single page. Across 40k slides that is systematic retrieval noise. Our own
# full-page OCR pass recovers the same real content, gated to pages that need it.
try:
    pymupdf4llm.use_layout(True)
    _LAYOUT = True
except Exception:  # noqa: BLE001 - pymupdf-layout not installed
    _LAYOUT = False

# ---------------------------------------------------------------------------
# Tunables
# ---------------------------------------------------------------------------

# A page with less than this many extracted characters is a candidate for OCR.
OCR_TEXT_THRESHOLD = 140

# ...but only if images cover at least this fraction of the page. Together these
# two gates mean "the page clearly carries content, and that content is pixels".
OCR_IMAGE_COVERAGE = 0.20

# Render DPI for OCR. 200 is the sweet spot for slide-sized text: 150 loses
# small monospace terminal output, 300 doubles the time for little gain.
OCR_DPI = 200

# Some decks use oversized canvases (a 26-inch-wide slide is not rare), which at
# 200 DPI renders a 5000px monster that Tesseract crawls over for no extra
# accuracy. Cap the long edge and back the DPI off to suit.
OCR_MAX_EDGE_PX = 3000

# Discard OCR results shorter than this -- almost always noise from a photo.
OCR_MIN_YIELD = 25

# Tesseract returns something for almost any image, and on a photograph or a
# low-resolution screenshot that something is noise (") ez g / Jealetas . / & ts
# Py"). Length alone does not catch it: noise is frequently longer than the real
# text on the page. Noise in a retrieval corpus is worse than absence, since it
# gets indexed, retrieved and quoted back as content.
#
# These two ratios separate noise from real technical OCR with a wide margin,
# measured on corpus samples:
#                         short tokens (<=2)   tokens >=4 chars
#     real technical OCR       0.00-0.19           0.67-0.77
#     noise                    0.84-1.00           0.00-0.05
#
# Filtering runs per line, because the two are mixed: a terminal-output slide
# yields real lines ("-> remapping BAR2 to overlap TSEG") alongside OCR-mangled
# hex dump rows ("| ff ff ff fr fF fF TF"). Dropping whole blocks would lose the
# narrative; keeping them would put wrong hex digits in the corpus.
OCR_LINE_SHORT_RATIO = 0.60
OCR_LINE_WORD_RATIO = 0.20
OCR_BLOCK_SHORT_RATIO = 0.50
OCR_BLOCK_WORD_RATIO = 0.25
OCR_MIN_TOKENS_PER_LINE = 3

# Tesseract reports how sure it is per word, and it is well calibrated here.
# Measured on a terminal-screenshot slide: correctly-read words averaged 94.5,
# while hex bytes it mangled averaged 59.2, with the worst ("Qxd071402@",
# "@xd0714000") at 0.0-2.5.
#
# Confidence alone is not enough -- at a threshold of 70 it also drops the
# correctly-read "SMM Base : bfea8000" (62.5) and keeps a mangled row (78.9) --
# so it runs alongside the structural test above. A low floor catches what
# structure misses without discarding correct-but-unusual lines.
OCR_MIN_LINE_CONFIDENCE = 60.0

# Per-page OCR timeout (seconds) so one pathological page cannot wedge a worker.
OCR_TIMEOUT = 90

SKIP_DIRS = {".git", ".github", "markdown", "tools", "node_modules", "__pycache__"}

# Slide formats LibreOffice can turn into PDF. Converting them and then running
# the normal two-pass pipeline is deliberate: a python-pptx text dump would read
# shape text only and miss exactly what matters here -- the code screenshots and
# diagrams that the OCR pass exists to recover.
SLIDE_EXTS = {".pptx", ".ppt", ".odp", ".key"}

# LibreOffice refuses to run two instances against one user profile, so each
# worker gets its own. Without this, parallel conversions fail intermittently.
SOFFICE_TIMEOUT = 300


# ---------------------------------------------------------------------------
# Filename / metadata parsing
# ---------------------------------------------------------------------------

# The repo convention is "<Speakers>_<Title>.pdf", speakers separated by
# " & " or ", ". Sidecars add a trailing "_tools" / "_code" / "_poc" marker.
SIDECAR_SUFFIXES = (
    "_tools", "_code", "_poc", "_plugin", "_cheatsheet", "_scripts",
    "_demo", "_paper", "_whitepaper", "_appendix",
)

CONF_YEAR_RE = re.compile(r"(19|20)\d{2}")


def slugify(text: str, maxlen: int = 120) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:maxlen].strip("-").lower() or "untitled"


def parse_conference(folder: str) -> dict:
    """Turn a folder name like 'BlackHat_USA_2025_Slides' into structured fields."""
    raw = folder.replace("_", " ").replace("-", " ")
    raw = re.sub(r"\bslides?\b", "", raw, flags=re.I).strip()
    year_m = CONF_YEAR_RE.search(raw)
    if year_m:
        year = int(year_m.group(0))
        name = CONF_YEAR_RE.sub("", raw)
    else:
        # Folders like "OffensiveCon25" glue a two-digit year to the series name.
        # Requiring the digits to touch a letter keeps "DEF CON 34" -- an edition
        # number, not a year -- from being read as 2034.
        short = re.search(r"(?<=[A-Za-z])(\d{2})\b", raw)
        year = 2000 + int(short.group(1)) if short else None
        name = raw[:short.start()] + raw[short.end():] if short else raw
    name = re.sub(r"\s+", " ", name).strip()

    # Normalise the series so retrieval on "Black Hat" matches every spelling.
    low = name.lower().replace(" ", "")
    if low.startswith("blackhat"):
        region = name.lower().replace("blackhat", "").replace("black hat", "").strip()
        series = "Black Hat"
        edition = region.upper() if region.lower() in ("usa", "asia") else region.title()
    elif low.startswith("offensivecon"):
        series, edition = "OffensiveCon", ""
    elif low.startswith("recon"):
        series, edition = "REcon", ""
    elif low.startswith("hexacon"):
        series, edition = "Hexacon", ""
    elif "defcon" in low or "def con" in low:
        # DEF CON numbers its editions rather than using the year, and the digits
        # were stripped above as a non-year. Put the edition back so the corpus
        # says "DEF CON 34" instead of a bare, unfilterable "DEF CON".
        series = "DEF CON"
        num = re.search(r"\b(\d{1,2})\b", folder)
        edition = num.group(1) if num else ""
        # DEF CON 1 was 1993, and the editions have run annually since, so the
        # edition fixes the year. Deriving it keeps `year` usable as an integer
        # filter across the whole corpus instead of null for every DEF CON talk.
        if edition:
            year = 1992 + int(edition)
    else:
        series, edition = name.title(), ""

    if series == "DEF CON" and edition:
        # The edition already names the event ("DEF CON 34"); appending the
        # derived year as well would read "DEF CON 34 2026".
        display = f"DEF CON {edition}"
    else:
        display = " ".join(x for x in (series, edition, str(year) if year else "") if x)
    return {"conference": series, "edition": edition, "year": year,
            "conference_full": display.strip(), "source_folder": folder}


# Black Hat's own archive naming: "AS-23-Surname-Title-Words[-wp].pdf", where the
# region/year prefix is followed by the presenting author's surname. Files using
# it carry no underscore, so the repo's "Speakers_Title" rule would hand back a
# dash-mangled title and no speaker at all.
# The dash after the region is sometimes missing ("AS23-Xing-..."), so it is
# optional here.
BH_OFFICIAL_RE = re.compile(r"^(?:AS|US|EU)-?\d{2}-(.+)$", re.I)

# A third in-repo convention: "<Speakers>-<Title>" with a plain hyphen instead of
# the usual underscore ("Allyn Stott-The Fault in Our Metrics", "Csaba Fitzl &
# Wojciech Reguła-The Final Chapter"). Splitting on the first hyphen that follows
# a name-shaped run and precedes a capital letter recovers both halves; requiring
# the left side to look like names keeps hyphenated titles intact.
HYPHEN_CANDIDATE_RE = re.compile(r"-(?=[A-Z])")


def _hyphen_split(stem: str) -> tuple[str, str] | None:
    """Split "<Speakers>-<Title>" at the right hyphen, or None if none fits.

    Candidates are tried right to left. Hyphens also occur inside personal names
    ("Ahmad-Reza Sadeghi") and inside title words ("AitM-Powered"), and the
    leftmost match is usually one of those; the rightmost split whose left side
    still reads as a speaker list is the one that separates names from title.
    """
    positions = [m.start() for m in HYPHEN_CANDIDATE_RE.finditer(stem)]
    for pos in reversed(positions):
        left, right = stem[:pos].strip(), stem[pos + 1:].strip()
        if 3 <= len(left) <= 120 and len(right) >= 8 and _looks_like_names(left):
            return left, right
    return None


SPEAKER_SPLIT_RE = re.compile(r"\s*&\s*|\s*,\s*|\s+and\s+")


def _looks_like_names(text: str) -> bool:
    """True when a string reads as a speaker list rather than prose.

    Every speaker in the list has to look like a person, not just the string as
    a whole: an earlier version accepted anything containing "&", so a title
    with a hyphen in it ("... Modern Web-Based App Sandbox From Site-Isolation
    Perspective") got split at the wrong hyphen and half the title was filed as
    a speaker.
    """
    parts = [p.strip() for p in SPEAKER_SPLIT_RE.split(text) if p.strip()]
    if not parts:
        return False
    for part in parts:
        words = part.split()
        # Personal names run one to five words. Anything longer is prose.
        if not 1 <= len(words) <= 5:
            return False
        # Names are capitalised; all-lowercase handles ("emptynebuli",
        # "redshiftzero") are common at these conferences and also fine.
        if not all(w[:1].isupper() or not w[:1].isalpha() or w.islower() for w in words):
            return False
    return True

# Suffixes conference archives append to distinguish supporting material.
DOC_KIND_SUFFIXES = {
    "wp": "whitepaper", "whitepaper": "whitepaper", "paper": "whitepaper",
    "slides": "slides", "compressed": "slides", "updated": "slides",
    "article": "article", "materials": "materials", "workshop": "workshop",
}


# DEF CON's media server names files
# "DEF CON 34 - Speakers - Title - variant", where the trailing segment is an
# internal marker: a version ("v1", "v2 Pro"), a document kind ("Slides v1",
# "Whitepaper v1"), a speaker handle ("hevnsnt", "azraelxuemo v3") or a truncated
# fragment ("rever", "slash esca"). Titles themselves can contain " - ", and one
# file carries its whole title in that trailing slot, so the marker cannot simply
# be dropped by position -- it is only discarded when it actually looks like one.
DEFCON_FILE_RE = re.compile(r"^DEF\s*CON\s+\d{1,2}\s+-\s+(.+)$", re.I)

DEFCON_VARIANT_RE = re.compile(
    r"""^(
        [vV]\d+([. ]\d+)*(\s+\w+)?          # v1, v2 Pro, v0 1
        | (slides?|whitepaper|wp|final|draft|updated|deck)\b.*
        | .*\b[vV]\d+(\s*\(\d+\))?$         # "In60 Whitepaper v1", "pipeline v1 (2)"
    )$""",
    re.X,
)


def _is_defcon_variant(segment: str) -> bool:
    """True when a trailing segment is a version/handle marker, not part of the title."""
    seg = segment.strip()
    if not seg:
        return True
    if DEFCON_VARIANT_RE.match(seg):
        return True
    # Short, title-less fragments ("m", "these", "hevnsnt", "slash esca") are
    # A date/venue tail ("2026 08 05 DEF CON") is a filing marker, not a title.
    if re.match(r"^\d{4}[ ._-]\d{2}[ ._-]\d{2}\b", seg) or re.search(r"\bDEF\s*CON\b$", seg, re.I):
        return True
    # truncation artefacts. Real titles stranded in this slot are much longer.
    return len(seg) <= 20 and len(seg.split()) <= 3


def parse_speakers_title(stem: str, defcon_style: bool = False) -> tuple[list[str], str]:
    # Most DEF CON files carry the "DEF CON NN - " prefix, but a handful in the
    # same drop omit it and start straight at the speaker names. Inside a DEF CON
    # folder, accept both; the flag keeps this dash-splitting away from the other
    # conferences, whose filenames use underscores.
    defcon = DEFCON_FILE_RE.match(stem)
    if defcon or (defcon_style and " - " in stem):
        remainder = defcon.group(1) if defcon else stem
        parts = [p.strip() for p in remainder.split(" - ")]
        if len(parts) >= 2 and _is_defcon_variant(parts[-1]):
            parts = parts[:-1]
        if len(parts) >= 2:
            speakers = [s.strip() for s in re.split(r"\s*,\s*|\s+&\s+|\s+and\s+", parts[0])
                        if s.strip()]
            return speakers, " - ".join(parts[1:]).strip()
        if parts:
            return [], parts[0]

    official = BH_OFFICIAL_RE.match(stem)
    if official and "_" not in stem:
        parts = [p for p in official.group(1).split("-") if p]
        # Trailing marker such as "-wp" describes the document, not the title.
        if parts and parts[-1].lower() in DOC_KIND_SUFFIXES:
            parts = parts[:-1]
        if len(parts) >= 2:
            # First token is the presenting author's surname; the rest is the title.
            return [parts[0]], " ".join(parts[1:])
        if parts:
            return [], parts[0]

    # Some filenames separate the speakers themselves with " _ " and then the
    # title with a bare "_". Normalising the spaced form to "&" first keeps all
    # the speakers instead of filing the 2nd onward into the title.
    working = re.sub(r"\s+_\s+", " & ", stem)

    if "_" in working:
        speaker_part, title_part = working.split("_", 1)
    else:
        # No underscore: try the hyphen convention before giving up on speakers.
        hy = _hyphen_split(working)
        if hy:
            speaker_part, title_part = hy
        else:
            speaker_part, title_part = "", working

    # If the left-hand side does not read as people, the split was wrong: the
    # whole stem is the title and this deck simply has no speaker in its name.
    if speaker_part and not _looks_like_names(speaker_part):
        speaker_part, title_part = "", working

    speakers = [s.strip() for s in SPEAKER_SPLIT_RE.split(speaker_part) if s.strip()]

    # Drop trailing archive markers. They appear as "..._wp", "...-WP" or a
    # "(2)" copy suffix; an underscore *inside* a title is meaningful and stays
    # ("Bad io_uring", "(0_o)").
    title = title_part.strip()
    changed = True
    while changed:
        changed = False
        title = re.sub(r"\s*\(\d+\)$", "", title).strip()
        for sep in ("_", "-"):
            head, found, tail = title.rpartition(sep)
            if found and head and tail.strip().lower() in DOC_KIND_SUFFIXES:
                title, changed = head.strip(), True
    return speakers, title or stem


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# OCR
# ---------------------------------------------------------------------------

_TESSERACT: str | None = None


def tesseract_path() -> str | None:
    global _TESSERACT
    if _TESSERACT is None:
        from shutil import which
        _TESSERACT = which("tesseract") or ""
    return _TESSERACT or None


_OCR_ALNUM_RE = re.compile(r"[^A-Za-z0-9]")


def _ocr_ratios_are_noise(text: str, short_max: float, word_min: float) -> bool:
    toks = text.split()
    if not toks:
        return True
    short = sum(1 for t in toks if len(t) <= 2) / len(toks)
    word = sum(1 for t in toks if len(_OCR_ALNUM_RE.sub("", t)) >= 4) / len(toks)
    return short > short_max and word < word_min


def _ocr_line_is_noise(line: str) -> bool:
    # Short lines carry too little signal to judge alone; the block-level check
    # catches them.
    if len(line.split()) < OCR_MIN_TOKENS_PER_LINE:
        return False
    return _ocr_ratios_are_noise(line, OCR_LINE_SHORT_RATIO, OCR_LINE_WORD_RATIO)


_LONG_HEX_RE = re.compile(r"\b(?:0x)?[0-9a-fA-F]{6,}\b")


def _ocr_block_is_risky(text: str) -> bool:
    """True for blocks whose exact values should not be trusted.

    Audited against ground truth, hex dumps, disassembly listings and
    label/value tables fail in a way confidence does not predict: the glyphs
    look legible, so the score stays high, while individual bytes change
    ("00000118" -> "80000118") and the two-dimensional structure is flattened.
    Prose and code on a light background, by contrast, come out near-exact.
    """
    if len(_LONG_HEX_RE.findall(text)) >= 4:
        return True
    toks = text.split()
    if not toks:
        return False
    # A table that lost its labels reads as mostly bare numbers.
    numeric = sum(1 for t in toks if re.fullmatch(r"[0-9a-fA-F.,:|xX%-]+", t))
    return numeric / len(toks) > 0.55 and len(toks) >= 12


def ocr_page(page: "pymupdf.Page") -> tuple[str, float, float, bool]:
    """Render and OCR a page.

    Returns (text, mean confidence). Empty text on any failure -- OCR is
    best-effort and must never take a document down with it.
    """
    exe = tesseract_path()
    if not exe:
        return "", 0.0, 0.0, False
    try:
        dpi = OCR_DPI
        long_in = max(page.rect.width, page.rect.height) / 72.0
        if long_in > 0 and long_in * dpi > OCR_MAX_EDGE_PX:
            dpi = max(120, int(OCR_MAX_EDGE_PX / long_in))
        pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
        png = pix.tobytes("png")
        proc = subprocess.run(
            # --oem 1 = LSTM engine only: faster and more accurate on screen
            # captures than the default combined legacy+LSTM mode.
            [exe, "stdin", "stdout", "--psm", "3", "--oem", "1", "-l", "eng", "tsv"],
            input=png, capture_output=True, timeout=OCR_TIMEOUT,
        )
        tsv = proc.stdout.decode("utf-8", "replace")
    except subprocess.TimeoutExpired:
        # Report it: silently returning nothing here made slow pages vanish from
        # the corpus with no trace that anything had been attempted.
        return "", 0.0, 0.0, True
    except Exception:
        return "", 0.0, 0.0, False

    # Rebuild lines from the TSV, carrying each line's mean confidence.
    grouped: "collections.OrderedDict[tuple, list[tuple[str, float]]]" = collections.OrderedDict()
    try:
        reader = csv.DictReader(io.StringIO(tsv), delimiter="\t")
        for row in reader:
            word = (row.get("text") or "").strip()
            if not word:
                continue
            try:
                conf = float(row.get("conf", -1))
            except ValueError:
                continue
            if conf < 0:
                continue
            key = (row.get("block_num"), row.get("par_num"), row.get("line_num"))
            grouped.setdefault(key, []).append((word, conf))
    except Exception:
        return "", 0.0, 0.0, False

    kept, confs = [], []
    all_confs = [c for words in grouped.values() for _, c in words]
    for words in grouped.values():
        line = " ".join(w for w, _ in words)
        mean = sum(c for _, c in words) / len(words)
        # Two independent tests, because neither alone is sufficient: structure
        # catches mangled hex that scores confidently, confidence catches noise
        # that happens to look structured.
        if mean < OCR_MIN_LINE_CONFIDENCE or _ocr_line_is_noise(line):
            continue
        kept.append(line)
        confs.extend(c for _, c in words)

    raw_conf = sum(all_confs) / len(all_confs) if all_confs else 0.0
    out = "\n".join(kept).strip()
    if len(out) < OCR_MIN_YIELD or _ocr_ratios_are_noise(out, OCR_BLOCK_SHORT_RATIO,
                                                         OCR_BLOCK_WORD_RATIO):
        return "", 0.0, raw_conf, False
    return out, (sum(confs) / len(confs) if confs else 0.0), raw_conf, False


def image_coverage(page: "pymupdf.Page") -> float:
    """Fraction of the page area covered by raster images (clamped to 1.0)."""
    try:
        parea = abs(page.rect.width * page.rect.height)
        if parea <= 0:
            return 0.0
        covered = 0.0
        for blk in page.get_text("dict").get("blocks", []):
            if blk.get("type") == 1:  # image block
                x0, y0, x1, y1 = blk.get("bbox", (0, 0, 0, 0))
                covered += abs((x1 - x0) * (y1 - y0))
        return min(covered / parea, 1.0)
    except Exception:
        return 0.0


# ---------------------------------------------------------------------------
# Secret redaction
# ---------------------------------------------------------------------------

# OFF BY DEFAULT -- the corpus is verbatim unless you pass --redact.
#
# Security talks are full of credentials: demo AWS keys on a slide, a token in a
# screenshotted terminal, a private key in an exploit walkthrough. Converting the
# slides lifts those strings out of a PDF (which scanners ignore) and into plain
# text files (which they do not), so a verbatim corpus will trip GitHub push
# protection and needs the detected secrets allowed via the URL in the rejection
# message.
#
# The trade-off: verbatim output is faithful to the source and keeps keys usable
# as searchable artefacts (they are indicators in their own right); redaction
# trades that for a corpus that pushes cleanly and cannot republish a credential
# that turned out not to be a throwaway. Each pattern keeps its identifying
# prefix, so "AKIA[REDACTED:aws-access-key-id]" still shows what stood there.
SECRET_PATTERNS: list[tuple[str, "re.Pattern[str]", int]] = [
    ("aws-access-key-id",
     re.compile(r"\b((?:A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA))[A-Z0-9]{16}\b"), 1),
    ("github-token", re.compile(r"\b(gh[pousr]_)[A-Za-z0-9]{36,255}\b"), 1),
    ("slack-token", re.compile(r"\b(xox[baprs]-)[A-Za-z0-9-]{10,}\b"), 1),
    ("google-api-key", re.compile(r"\b(AIza)[0-9A-Za-z_\-]{35}\b"), 1),
    ("stripe-key", re.compile(r"\b((?:sk|rk)_live_)[0-9A-Za-z]{20,}\b"), 1),
    ("openai-key", re.compile(r"\b(sk-)[A-Za-z0-9]{32,}\b"), 1),
    ("private-key-block",
     re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"
                r".*?-----END (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----", re.S), 0),
]


def redact_secrets(text: str) -> tuple[str, int]:
    """Mask credential-shaped strings. Returns (text, number of redactions)."""
    total = 0
    for label, pattern, keep_group in SECRET_PATTERNS:
        def _sub(m: "re.Match[str]", _label=label, _keep=keep_group) -> str:
            prefix = m.group(_keep) if _keep else ""
            return f"{prefix}[REDACTED:{_label}]"
        text, n = pattern.subn(_sub, text)
        total += n
    return text, total


# ---------------------------------------------------------------------------
# Markdown cleanup
# ---------------------------------------------------------------------------

def tidy(md: str) -> str:
    """Normalise PyMuPDF4LLM output without destroying structure."""
    # PyMuPDF4LLM annotates text found inside figures; keep the text, drop the
    # HTML comment scaffolding, which only wastes tokens.
    md = md.replace("<!-- Start of picture text -->", "").replace("<!-- End of picture text -->", "")
    md = re.sub(r"</?mark>", "", md)          # highlight spans -> plain text
    md = md.replace("<br>", "\n")
    md = re.sub(r"[ \t]+\n", "\n", md)         # trailing whitespace
    md = re.sub(r"\n{3,}", "\n\n", md)         # runs of blank lines
    md = re.sub(r"(?m)^-----+$", "", md)       # page-break rules; we add our own
    # A line of extracted text that happens to start with three backticks opens a
    # code fence that nothing closes, and a strict parser then swallows the rest
    # of the document as code. One slide's table cell ("```|") did exactly that.
    # Escaping the first backtick keeps the characters while defusing the fence.
    md = re.sub(r"(?m)^(\s*)```", r"\1\\```", md)
    return md.strip()


def yaml_escape(v) -> str:
    if v is None:
        return '""'
    s = str(v)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_list(items) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(yaml_escape(i) for i in items) + "]"


# ---------------------------------------------------------------------------
# Core conversion
# ---------------------------------------------------------------------------

def soffice_path() -> str | None:
    from shutil import which
    return which("soffice") or which("libreoffice")


def slides_to_pdf(src_path: str, workdir: str) -> str | None:
    """Render a PowerPoint/Impress/Keynote deck to PDF. Returns the PDF path."""
    exe = soffice_path()
    if not exe:
        return None
    profile = os.path.join(workdir, "lo-profile")
    try:
        proc = subprocess.run(
            [exe, "--headless", "--norestore", "--invisible",
             f"-env:UserInstallation=file://{profile}",
             "--convert-to", "pdf", "--outdir", workdir, src_path],
            capture_output=True, timeout=SOFFICE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return None
    if proc.returncode != 0:
        return None
    produced = os.path.join(
        workdir, os.path.splitext(os.path.basename(src_path))[0] + ".pdf")
    return produced if os.path.exists(produced) else None


# Some decks cannot be described correctly from their filename because the
# archive pairs the wrong name with the file, or the document was retitled after
# filing. Those corrections are curated in metadata_overrides.json, each one
# confirmed by reading the document itself, and applied here.
_OVERRIDES: dict | None = None


def load_overrides() -> dict:
    global _OVERRIDES
    if _OVERRIDES is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "metadata_overrides.json")
        try:
            with open(path, "r", encoding="utf-8") as fh:
                _OVERRIDES = {k: v for k, v in json.load(fh).items()
                              if not k.startswith("_")}
        except Exception:  # noqa: BLE001 - overrides are optional
            _OVERRIDES = {}
    return _OVERRIDES


def _existing_source(md_path: str) -> str | None:
    """The `source_pdf` recorded in an already-written Markdown file, if any."""
    try:
        with open(md_path, "r", encoding="utf-8") as fh:
            for _ in range(40):  # frontmatter only; never scan a whole deck
                line = fh.readline()
                if not line:
                    break
                if line.startswith("source_pdf:"):
                    return line.split('"')[1]
    except (OSError, IndexError):
        pass
    return None


def find_sidecars(pdf_path: str) -> list[tuple[str, str]]:
    """Companion .txt files shipped next to a deck (tool lists, PoC URLs, code)."""
    base = os.path.splitext(pdf_path)[0]
    folder = os.path.dirname(pdf_path)
    stem = os.path.basename(base)
    out = []
    try:
        entries = os.listdir(folder)
    except OSError:
        return out
    for name in sorted(entries):
        if not name.lower().endswith(".txt"):
            continue
        nstem = os.path.splitext(name)[0]
        if nstem == stem or any(nstem == stem + sfx for sfx in SIDECAR_SUFFIXES) \
                or (nstem.startswith(stem + "_") and len(nstem) - len(stem) < 24):
            try:
                with open(os.path.join(folder, name), "r", encoding="utf-8", errors="replace") as fh:
                    body = fh.read().strip()
                if body:
                    out.append((name, body))
            except OSError:
                pass
    return out


def convert_one(job: tuple) -> dict:
    pdf_path, src_root, out_root, do_ocr, do_redact = job
    rel = os.path.relpath(pdf_path, src_root)
    folder = rel.split(os.sep)[0] if os.sep in rel else ""
    conf = parse_conference(folder)
    stem = os.path.splitext(os.path.basename(pdf_path))[0]
    speakers, title = parse_speakers_title(stem, defcon_style=conf["conference"] == "DEF CON")

    override = load_overrides().get(rel.replace(os.sep, "/"))
    content_note = ""
    if override:
        title = override.get("title", title)
        speakers = override.get("speakers", speakers)
        content_note = " ".join(x for x in (override.get("note", ""),
                                            override.get("conference_note", "")) if x)

    result = {
        "source_pdf": rel, "status": "ok", "error": "",
        **conf, "title": title, "speakers": speakers,
    }

    tmpdir = None
    try:
        digest = sha256_file(pdf_path)
        render_path = pdf_path
        if os.path.splitext(pdf_path)[1].lower() in SLIDE_EXTS:
            import tempfile
            tmpdir = tempfile.mkdtemp(prefix="slides2pdf-")
            render_path = slides_to_pdf(pdf_path, tmpdir)
            if not render_path:
                result.update(status="failed",
                              error="LibreOffice could not render this deck to PDF "
                                    "(install libreoffice-impress for .pptx support)")
                return result
        doc = pymupdf.open(render_path)
        if doc.needs_pass:
            doc.close()
            result.update(status="encrypted", error="password protected")
            return result
        n_pages = doc.page_count

        # Structural pass over the whole document at once. use_ocr=False keeps
        # the layout engine's per-picture OCR off; pass 2 below does OCR better
        # and only where it is needed (see the note at the top of this file).
        try:
            chunks = pymupdf4llm.to_markdown(
                doc, page_chunks=True, write_images=False,
                show_progress=False, use_ocr=False,
            )
        except TypeError:
            # Older pymupdf4llm without the layout engine: no use_ocr kwarg.
            chunks = pymupdf4llm.to_markdown(doc, page_chunks=True, write_images=False,
                                             show_progress=False)

        bodies: list[str] = []
        ocr_raw: dict[int, tuple[str, float, float]] = {}
        struct_chars = 0
        redactions = 0
        ocr_timeouts = 0

        # Pass A: structural text, and OCR for the pages that need it.
        for idx, chunk in enumerate(chunks):
            body = tidy(chunk.get("text", "") or "")
            if do_redact:
                body, nred = redact_secrets(body)
                redactions += nred
            struct_chars += len(body)
            bodies.append(body)

            if do_ocr and len(body) < OCR_TEXT_THRESHOLD and idx < n_pages:
                page = doc[idx]
                if image_coverage(page) >= OCR_IMAGE_COVERAGE:
                    otext, oconf, raw_conf, timed_out = ocr_page(page)
                    if timed_out:
                        ocr_timeouts += 1
                    if otext and do_redact:
                        otext, nred = redact_secrets(otext)
                        redactions += nred
                    # Only keep OCR that adds something the structural pass missed.
                    if otext and len(otext) > len(body):
                        ocr_raw[idx] = (otext, oconf, raw_conf)

        doc.close()

        # Pass B: strip slide furniture. A conference logo or footer sits on every
        # page, and OCR renders it differently each time -- "black hat" came out
        # as "bisek hat" 606 times, "pisek hat" 170. Any line repeating across a
        # large share of a deck's OCR'd pages is decoration, not content, and
        # dropping it removes a systematic source of noise that per-line quality
        # tests cannot catch (those junk lines look like ordinary words).
        if len(ocr_raw) >= 4:
            counts: "collections.Counter[str]" = collections.Counter()
            for text, _, _ in ocr_raw.values():
                counts.update({ln.strip() for ln in text.splitlines() if ln.strip()})
            boiler = {ln for ln, n in counts.items()
                      if n >= max(3, int(0.30 * len(ocr_raw)))}
            if boiler:
                for idx, (text, kept_conf, page_conf) in list(ocr_raw.items()):
                    kept = [ln for ln in text.splitlines() if ln.strip() not in boiler]
                    trimmed = "\n".join(kept).strip()
                    if len(trimmed) < OCR_MIN_YIELD:
                        del ocr_raw[idx]
                    else:
                        ocr_raw[idx] = (trimmed, kept_conf, page_conf)

        # Pass C: assemble.
        parts, ocr_pages, ocr_chars = [], 0, 0
        ocr_confs: list[float] = []
        risky_blocks = 0
        for idx, body in enumerate(bodies):
            section = [f"## Slide {idx + 1}", ""]
            if body:
                section.append(body)
            entry = ocr_raw.get(idx)
            if entry:
                otext, oconf, page_conf = entry
                ocr_pages += 1
                ocr_chars += len(otext)
                ocr_confs.append(oconf)
                risky = _ocr_block_is_risky(otext)
                if risky:
                    risky_blocks += 1
                if body:
                    section.append("")
                # The confidence shown is measured over the text that survived
                # filtering, so it reads higher than the page as a whole; the raw
                # page figure is given too, and it is the honest one.
                warn = (f"> Recovered by OCR — confidence {oconf:.0f}/100 on the text "
                        f"kept, {page_conf:.0f}/100 across the whole page. Wording is "
                        f"approximate.")
                if risky:
                    warn += (" **This block contains dense hex, addresses or tabular "
                             "data: individual values are frequently misread and its "
                             "row/column structure is not preserved. Do not quote exact "
                             "values from it — check the source PDF.**")
                else:
                    warn += " Verify exact values against the source PDF."
                section += ["", warn, "", "```text", otext, "```"]
            parts.append("\n".join(section).rstrip())

        sidecars = find_sidecars(pdf_path)
        if sidecars:
            block = ["## Companion resources", ""]
            for name, body in sidecars:
                if do_redact:
                    body, nred = redact_secrets(body)
                    redactions += nred
                block += [f"### `{name}`", "", "```text", body, "```", ""]
            parts.append("\n".join(block).rstrip())

        total_chars = struct_chars + ocr_chars
        out_dir = os.path.join(out_root, folder) if folder else out_root
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, slugify(stem) + ".md")

        # Two different decks can slugify identically (a talk's slides and its
        # whitepaper, or long titles truncated to the same prefix). Disambiguate
        # with a short hash of the source path rather than a running counter:
        # the counter depended on what was already on disk, so re-running over a
        # previous output wrote "<slug>-2.md" beside the original instead of
        # replacing it. Hashing the source makes each deck's destination stable
        # across runs, so a re-run overwrites its own file and only genuinely
        # different sources get a suffix.
        if os.path.exists(out_path) and _existing_source(out_path) not in (None, rel):
            out_path = os.path.join(
                out_dir, f"{slugify(stem)}-{hashlib.sha256(rel.encode()).hexdigest()[:6]}.md")

        fm = [
            "---",
            f"title: {yaml_escape(title)}",
            f"speakers: {yaml_list(speakers)}",
            f"conference: {yaml_escape(conf['conference'])}",
            f"conference_full: {yaml_escape(conf['conference_full'])}",
            f"edition: {yaml_escape(conf['edition'])}",
            f"year: {conf['year'] if conf['year'] else 'null'}",
            f"source_pdf: {yaml_escape(rel)}",
            f"pages: {n_pages}",
            f"sha256: {yaml_escape(digest)}",
            f"text_chars: {total_chars}",
            f"ocr_pages: {ocr_pages}",
            f"has_ocr: {'true' if ocr_pages else 'false'}",
            f"redacted_secrets: {redactions}",
            f"ocr_confidence: {round(sum(ocr_confs) / len(ocr_confs), 1) if ocr_confs else 'null'}",
            f"ocr_unreliable_blocks: {risky_blocks}",
            f"ocr_timeouts: {ocr_timeouts}",
            *( [f"content_note: {yaml_escape(content_note)}"] if content_note else [] ),
            f"companion_files: {yaml_list([n for n, _ in sidecars])}",
            f"extractor: {yaml_escape('pymupdf4llm ' + pymupdf.__version__ + ' + tesseract' if ocr_pages else 'pymupdf4llm ' + pymupdf.__version__)}",
            f"converted_at: {yaml_escape(_dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))}",
            "---",
            "",
        ]

        header = [f"# {title}", ""]
        if speakers:
            header.append(f"**Speakers:** {', '.join(speakers)}  ")
        header.append(f"**Conference:** {conf['conference_full']}  ")
        header.append(f"**Source:** `{rel}` ({n_pages} pages)")
        header.append("")

        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(fm))
            fh.write("\n".join(header))
            fh.write("\n\n")
            fh.write("\n\n".join(p for p in parts if p.strip()))
            fh.write("\n")

        result.update(
            status="ok", pages=n_pages, sha256=digest, text_chars=total_chars,
            ocr_pages=ocr_pages, markdown=os.path.relpath(out_path, out_root),
            companion_files=[n for n, _ in sidecars], redacted_secrets=redactions,
            ocr_confidence=(round(sum(ocr_confs) / len(ocr_confs), 1) if ocr_confs else None),
            ocr_unreliable_blocks=risky_blocks, ocr_timeouts=ocr_timeouts,
            content_note=content_note or None,
        )
        return result

    except Exception as exc:  # noqa: BLE001 - one bad deck must not kill the run
        result.update(status="failed", error=f"{type(exc).__name__}: {exc}",
                      traceback=traceback.format_exc(limit=3))
        return result
    finally:
        if tmpdir:
            import shutil as _shutil
            _shutil.rmtree(tmpdir, ignore_errors=True)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def collect_pdfs(src_root: str, include_slides: bool = True) -> list[str]:
    found = []
    for dirpath, dirnames, filenames in os.walk(src_root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext == ".pdf" or (include_slides and ext in SLIDE_EXTS):
                found.append(os.path.join(dirpath, fn))
    return sorted(found)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default=".", help="root directory to scan for PDFs")
    ap.add_argument("--out", default="markdown", help="output directory for Markdown")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2)),
                    help="parallel worker processes")
    ap.add_argument("--no-ocr", action="store_true",
                    help="skip the OCR gap-fill pass (much faster, lossy on screenshots)")
    ap.add_argument("--limit", type=int, default=0, help="convert at most N PDFs (smoke test)")
    ap.add_argument("--manifest", default="", help="manifest path (default: <out>/manifest.jsonl)")
    ap.add_argument("--no-slides", action="store_true",
                    help="skip .pptx/.ppt/.odp decks instead of rendering them "
                         "to PDF via LibreOffice")
    ap.add_argument("--redact", action="store_true",
                    help="mask credential-shaped strings (AWS/GitHub/Slack keys, "
                         "PEM blocks). Off by default: output is verbatim, which "
                         "may require allowing secrets in GitHub push protection.")
    ap.add_argument("--force", action="store_true",
                    help="re-convert decks already recorded in the manifest")
    args = ap.parse_args()

    src_root = os.path.abspath(args.src)
    out_root = os.path.abspath(args.out)
    os.makedirs(out_root, exist_ok=True)
    manifest_path = args.manifest or os.path.join(out_root, "manifest.jsonl")

    pdfs = collect_pdfs(src_root, include_slides=not args.no_slides)
    if args.limit:
        pdfs = pdfs[: args.limit]
    if not pdfs:
        print(f"No PDFs found under {src_root}", file=sys.stderr)
        return 1

    # Resume: a full corpus run takes hours, so never redo finished work. A deck
    # counts as done only if the manifest says ok AND its Markdown still exists.
    previous: dict[str, dict] = {}
    if not args.force:
        # .partial holds results streamed by a run that did not finish; read it
        # too so an interrupted job resumes from where it actually stopped.
        for src in (manifest_path, manifest_path + ".partial"):
            if not os.path.exists(src):
                continue
            with open(src, "r", encoding="utf-8") as fh:
                for line in fh:
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if rec.get("status") == "ok" and rec.get("markdown") and \
                            os.path.exists(os.path.join(out_root, rec["markdown"])):
                        previous[rec["source_pdf"]] = rec
    if previous:
        before = len(pdfs)
        pdfs = [p for p in pdfs if os.path.relpath(p, src_root) not in previous]
        print(f"Resuming: {before - len(pdfs)} decks already converted, "
              f"{len(pdfs)} remaining. Use --force to redo everything.")
        if not pdfs:
            print("Nothing to do.")
            return 0

    do_ocr = not args.no_ocr
    if do_ocr and not tesseract_path():
        print("WARNING: tesseract not found on PATH -- running structural-only. "
              "Install tesseract-ocr to recover text from image-only slides.",
              file=sys.stderr)
        do_ocr = False

    n_slides = sum(1 for p in pdfs if os.path.splitext(p)[1].lower() in SLIDE_EXTS)
    if n_slides and not soffice_path():
        print(f"WARNING: {n_slides} PowerPoint/Impress decks found but LibreOffice is "
              "not installed; they will fail. Install libreoffice-impress, or pass "
              "--no-slides to skip them.", file=sys.stderr)
    print(f"Converting {len(pdfs)} decks ({n_slides} via LibreOffice)  |  workers={args.workers}  "
          f"|  OCR={'on' if do_ocr else 'off'}")
    print(f"  source: {src_root}\n  output: {out_root}", flush=True)

    jobs = [(p, src_root, out_root, do_ocr, args.redact) for p in pdfs]
    records, done, failed = list(previous.values()), 0, 0

    # Stream results to a side log as they land, so an interrupted run (container
    # reclaim, ctrl-c) still leaves a resumable record of everything finished.
    progress_path = manifest_path + ".partial"
    ctx = mp.get_context("fork" if sys.platform != "win32" else "spawn")
    with open(progress_path, "a", encoding="utf-8") as plog, \
            ctx.Pool(processes=args.workers, maxtasksperchild=25) as pool:
        for rec in pool.imap_unordered(convert_one, jobs, chunksize=1):
            done += 1
            rec.pop("traceback", None)
            records.append(rec)
            plog.write(json.dumps(rec, ensure_ascii=False) + "\n")
            plog.flush()
            if rec["status"] != "ok":
                failed += 1
                print(f"  [{done}/{len(pdfs)}] {rec['status'].upper():9s} "
                      f"{rec['source_pdf']}  ({rec.get('error', '')[:70]})", flush=True)
            elif done % 10 == 0 or done == len(pdfs):
                print(f"  [{done}/{len(pdfs)}] ok  ocr_pages={rec.get('ocr_pages', 0):<4d} "
                      f"{rec['source_pdf'][:78]}", flush=True)

    records.sort(key=lambda r: r["source_pdf"])
    with open(manifest_path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if os.path.exists(progress_path):
        os.remove(progress_path)

    ok = [r for r in records if r["status"] == "ok"]
    tot_pages = sum(r.get("pages", 0) for r in ok)
    tot_chars = sum(r.get("text_chars", 0) for r in ok)
    tot_ocr = sum(r.get("ocr_pages", 0) for r in ok)
    print("\n" + "=" * 68)
    print(f"Converted     : {len(ok)}/{len(pdfs)} decks ({failed} failed)")
    print(f"Pages         : {tot_pages:,}")
    print(f"Markdown chars: {tot_chars:,}  (~{tot_chars // 4:,} tokens)")
    print(f"OCR-recovered : {tot_ocr:,} pages")
    print(f"Manifest      : {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
