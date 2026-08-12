#!/usr/bin/env python3
"""
find_invisible_text.py — Text the PDF contains but the slide never shows.

A reviewer reading page 7 of "Breaking Trust Boundaries" against its image
found a URL in the Markdown that is nowhere on the slide. It was not an OCR
error and not a hallucination: the author had duplicated a text box across six
slides, and on those six it is drawn in black on a black background. The
converter extracted it because it is really there in the text layer. It is
still wrong to publish, because a reader of the Markdown cannot tell it apart
from something the speaker actually showed -- and invented content is the
failure class no reader can detect without the page in front of them.

The same shape covers white-on-white page furniture, text hidden behind a
full-bleed image, and boxes parked off the visible design.

Detection is by rendering, not by colour arithmetic. Render the span's own
bounding box and ask what share of its pixels are already the span's colour.
Visible text is a minority of its own box -- glyphs cover maybe a third of a
line of type and the rest is background of some other shade. Invisible text has
nowhere to hide: background and glyphs are the same shade, so nearly every
pixel matches.

An earlier version asked for a flat box whose mean matched the span colour,
which is wrong in a way worth recording. A reviewer on a second deck found
"Big Endian" on two slides that show no such text; the flatness rule caught one
and missed the other, because there the box clips a bright element across 0.5%
of its area, which drags min/max to the full 0-255 range. A share does not move
for half a percent of outliers.

Measured over both decks, 1397 spans: the 9 invisible ones score 0.911 and up,
the highest visible span scores 0.493. The threshold sits in an empty gap
rather than on a slope, which is why it needs no per-deck tuning.

    python3 tools/find_invisible_text.py --src BlackHat_USA_2026_Slides
    python3 tools/find_invisible_text.py --src . --out markdown --json hits.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

os.environ.setdefault("PYMUPDF_MESSAGE", "path:" + os.devnull)
import pymupdf  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Sampling resolution for the visibility test. Low enough to be cheap per span,
# high enough that a 10pt glyph still covers several pixels.
PROBE_DPI = 110
# How close a pixel must be to the span's own colour, on a 0-255 luminance
# scale, to count as indistinguishable from it.
MATCH_TOLERANCE = 20
# What share of the box must be indistinguishable before the glyphs count as
# having contributed nothing.
SHARE = 0.85
# Very small boxes render to a handful of pixels where the statistics stop
# meaning anything.
MIN_EDGE = 2.0


def luma(color: int) -> float:
    r, g, b = (color >> 16) & 255, (color >> 8) & 255, color & 255
    return 0.299 * r + 0.587 * g + 0.114 * b


def is_invisible(page, span: dict) -> bool:
    rect = pymupdf.Rect(span["bbox"])
    if rect.is_empty or rect.width < MIN_EDGE or rect.height < MIN_EDGE:
        return False
    try:
        pix = page.get_pixmap(dpi=PROBE_DPI, clip=rect, colorspace=pymupdf.csGRAY)
    except Exception:
        return False
    if not pix.width or not pix.height:
        return False
    s = pix.samples
    if not s:
        return False
    target = luma(span.get("color", 0))
    matching = sum(1 for v in s if abs(v - target) <= MATCH_TOLERANCE)
    return matching / len(s) >= SHARE


def scan(pdf_path: str) -> list[dict]:
    out: list[dict] = []
    try:
        doc = pymupdf.open(pdf_path)
    except Exception as exc:
        return [{"error": str(exc)}]
    try:
        for idx, page in enumerate(doc):
            try:
                blocks = page.get_text("dict")["blocks"]
            except Exception:
                continue
            for blk in blocks:
                for line in blk.get("lines", []):
                    for span in line.get("spans", []):
                        text = span.get("text", "").strip()
                        if not text:
                            continue
                        if is_invisible(page, span):
                            out.append({"page": idx + 1, "text": text})
    finally:
        doc.close()
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default=".", help="directory to scan for PDFs")
    ap.add_argument("--out", default="",
                    help="markdown root; when given, report only hits whose "
                         "text actually reached the converted document. This "
                         "is a substring test, so it cannot tell a hidden '48' "
                         "from the '## Slide 48' heading -- treat it as a way "
                         "to rank documents, not as proof about short strings.")
    ap.add_argument("--json", default="", help="write full results here")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    pdfs = []
    for root, _dirs, files in os.walk(args.src):
        if os.path.basename(root) in (".git", "markdown"):
            continue
        for name in sorted(files):
            if name.lower().endswith(".pdf"):
                pdfs.append(os.path.join(root, name))
    pdfs.sort()
    if args.limit:
        pdfs = pdfs[:args.limit]

    # Where --out is given, a hit only matters if it leaked into the Markdown
    # *this PDF produced*. Asking whether the string appears anywhere in the
    # corpus is a different and much weaker question: a hidden page number "48"
    # appears in hundreds of unrelated talks, and every such hit would be
    # reported as leaked.
    body_of: dict[str, str] = {}
    if args.out:
        manifest = os.path.join(args.out, "manifest.jsonl")
        if not os.path.exists(manifest):
            print(f"--out needs {manifest} to match PDFs to their Markdown",
                  file=sys.stderr)
            return 1
        for line in open(manifest, encoding="utf-8"):
            if not line.strip():
                continue
            rec = json.loads(line)
            src, md = rec.get("source_pdf"), rec.get("markdown")
            if not src or not md:
                continue
            path = os.path.join(args.out, md)
            try:
                body_of[os.path.normpath(src)] = open(path, encoding="utf-8").read()
            except OSError:
                pass

    results, total_hits, docs_hit = {}, 0, 0
    for i, pdf in enumerate(pdfs, 1):
        hits = scan(pdf)
        hits = [h for h in hits if "error" not in h]
        rel = os.path.relpath(pdf, args.src)
        if args.out and hits:
            # The manifest records source_pdf relative to the conversion's own
            # --src, which need not be this scan's --src, so match on the tail.
            key = os.path.normpath(rel)
            body = body_of.get(key)
            if body is None:
                body = next((b for k, b in body_of.items()
                             if k.endswith(os.path.basename(key))), None)
            hits = [h for h in hits if body and h["text"] in body]
        if not hits:
            continue
        docs_hit += 1
        total_hits += len(hits)
        results[rel] = hits
        pages = sorted({h["page"] for h in hits})
        sample = sorted({h["text"] for h in hits})[:3]
        print(f"{rel}")
        print(f"    {len(hits)} span(s) on pages {pages[:12]}"
              + (" ..." if len(pages) > 12 else ""))
        for t in sample:
            print(f"    - {t[:90]!r}")
        sys.stdout.flush()

    print(f"\n{docs_hit} of {len(pdfs)} documents carry invisible text "
          f"({total_hits} spans)")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(results, fh, ensure_ascii=False, indent=1)
        print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
