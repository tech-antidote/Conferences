#!/usr/bin/env python3
"""
clean_ocr.py — Strip OCR noise from a converted corpus, line by line.

Tesseract returns something for almost any image, and on a photograph or a
low-resolution screenshot that something is noise: ") ez g / Jealetas . / & ts
Py". The converter's only guard was length, so noise longer than the page's real
text was kept. Noise in a retrieval corpus is worse than absence -- it is
indexed, retrieved, and quoted back as if it were content.

Filtering has to be per line, not per block, because the two are mixed. A slide
showing terminal output produces blocks like:

    PCI BARs failed                      <- real, worth keeping
    TSEG Base : bf000000                 <- real
    -> remapping BAR2 to overlap TSEG    <- real
    | ff ff ff ff ff fr fF fF fF TF fF   <- OCR-mangled hex dump, worthless

Dropping the whole block loses the narrative; keeping it puts wrong hex digits
in the corpus, which is the failure mode that matters for security research.

Two signals separate them, measured against real corpus samples:

                        short tokens (<=2)   tokens >=4 chars
    real technical OCR        0.00-0.19          0.67-0.77
    noise                     0.84-1.00          0.00-0.05

The gap is wide, so the thresholds sit well inside it and only clear noise is
removed. Hex dump rows score like noise because, once OCR has mangled them, that
is what they are.

Usage:
    python3 tools/clean_ocr.py --out markdown --dry-run
    python3 tools/clean_ocr.py --out markdown
"""

from __future__ import annotations

import argparse
import os
import re
import sys

OCR_BLOCK_RE = re.compile(
    r"(?P<intro>> Text below was recovered by OCR[^\n]*\n\n)```text\n(?P<body>.*?)\n```",
    re.S,
)

# A line is judged only when it has enough tokens to judge; shorter lines ride on
# the block-level verdict instead.
MIN_TOKENS_PER_LINE = 3
LINE_SHORT_RATIO = 0.60
LINE_WORD_RATIO = 0.20

BLOCK_SHORT_RATIO = 0.50
BLOCK_WORD_RATIO = 0.25

# Below this, whatever survived filtering is not worth a block of its own.
MIN_SURVIVING_CHARS = 25

ALNUM_RE = re.compile(r"[^A-Za-z0-9]")


def ratios(text: str) -> tuple[float, float]:
    """(fraction of tokens <=2 chars, fraction of tokens with >=4 alphanumerics)."""
    toks = text.split()
    if not toks:
        return 1.0, 0.0
    short = sum(1 for t in toks if len(t) <= 2) / len(toks)
    word = sum(1 for t in toks if len(ALNUM_RE.sub("", t)) >= 4) / len(toks)
    return short, word


def line_is_noise(line: str) -> bool:
    toks = line.split()
    if len(toks) < MIN_TOKENS_PER_LINE:
        return False
    short, word = ratios(line)
    return short > LINE_SHORT_RATIO and word < LINE_WORD_RATIO


def block_is_noise(text: str) -> bool:
    short, word = ratios(text)
    return short > BLOCK_SHORT_RATIO and word < BLOCK_WORD_RATIO


def clean_block(body: str) -> str | None:
    """Return the cleaned block body, or None if nothing worth keeping remains."""
    kept = [ln for ln in body.splitlines() if not line_is_noise(ln)]
    cleaned = "\n".join(kept).strip()
    if len(cleaned) < MIN_SURVIVING_CHARS or block_is_noise(cleaned):
        return None
    return cleaned


def process(path: str, dry_run: bool) -> tuple[int, int, int]:
    """Returns (blocks seen, blocks dropped, characters removed)."""
    with open(path, encoding="utf-8") as fh:
        original = fh.read()

    seen = dropped = removed = 0

    def _sub(m: "re.Match[str]") -> str:
        nonlocal seen, dropped, removed
        seen += 1
        body = m.group("body")
        cleaned = clean_block(body)
        if cleaned is None:
            dropped += 1
            removed += len(body)
            return ""  # drop the intro line too: nothing was recovered
        removed += len(body) - len(cleaned)
        return m.group("intro") + "```text\n" + cleaned + "\n```"

    updated = OCR_BLOCK_RE.sub(_sub, original)
    # Collapse blank runs left behind by removed blocks.
    updated = re.sub(r"\n{3,}", "\n\n", updated)

    if not dry_run and updated != original:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(updated)
    return seen, dropped, removed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown", help="Markdown corpus directory")
    ap.add_argument("--dry-run", action="store_true", help="report without editing")
    args = ap.parse_args()

    root = os.path.abspath(args.out)
    if not os.path.isdir(root):
        print(f"No such directory: {root}", file=sys.stderr)
        return 1

    files = blocks = dropped = removed = 0
    touched = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            files += 1
            s, d, r = process(os.path.join(dirpath, fn), args.dry_run)
            blocks += s
            dropped += d
            removed += r
            if r:
                touched += 1

    verb = "would remove" if args.dry_run else "removed"
    print(f"Scanned {files} files, {blocks:,} OCR blocks.")
    print(f"{verb} {removed:,} characters of OCR noise from {touched} files "
          f"({dropped:,} blocks emptied entirely).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
