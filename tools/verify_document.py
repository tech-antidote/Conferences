#!/usr/bin/env python3
"""
verify_document.py — Read every page of one document against its source.

`verify_uncertain.py` reviews the blocks the converter *flagged*. That is the
efficient thing to do across a 956-document corpus, but it cannot answer "is
this talk right?", because the failures it never flagged are exactly the ones
it does not know about: a structural pass that dropped a column, a diagram
whose labels never made it into the text layer, a slide the extractor rendered
as prose when it was a table.

So this takes one document and reviews all of it. Every page is rendered and
paired with the Markdown the converter produced for that page, and the reviewer
is asked whether the text is what the page says -- not whether OCR was
plausible.

    python3 tools/verify_document.py --extract --doc markdown/<talk>.md \\
        --src . --src /path/to/sources --work review-doc/
    python3 tools/verify_document.py --apply --doc markdown/<talk>.md \\
        --also markdown/<duplicate>.md --work review-doc/

`--also` writes the same corrections to a second document. Conference archives
publish the same deck twice under different names often enough that reviewing
the pages once and applying twice is worth doing.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

os.environ.setdefault("PYMUPDF_MESSAGE", "path:" + os.devnull)
import pymupdf  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_uncertain import resolve_source, set_key  # noqa: E402
from pdf2md import SLIDE_EXTS, slides_to_pdf  # noqa: E402

# Higher than the flagged-block pass: a full review is reading body text and
# diagram labels, not just picking hex out of a screenshot.
RENDER_DPI = 170
MAX_EDGE = 2600

SLIDE_RE = re.compile(r"(?m)^## Slide (\d+)$")
LABEL = "> Page read against the source by a vision model"


def frontmatter_end(text: str) -> int:
    return text.find("\n---", 3) + len("\n---") if text.startswith("---") else 0


def sections(text: str) -> list[tuple[int, int, int]]:
    """Return (slide_no, body_start, body_end) for each slide section."""
    marks = [(m.start(), m.end(), int(m.group(1))) for m in SLIDE_RE.finditer(text)]
    out = []
    for i, (_start, end, num) in enumerate(marks):
        stop = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((num, end, stop))
    return out


def render(page, dest: str) -> None:
    dpi = RENDER_DPI
    long_in = max(page.rect.width, page.rect.height) / 72.0
    if long_in and long_in * dpi > MAX_EDGE:
        dpi = max(100, int(MAX_EDGE / long_in))
    page.get_pixmap(dpi=dpi).save(dest)


def cmd_extract(doc: str, roots: list[str], work: str, only: str) -> int:
    text = open(doc, encoding="utf-8").read()
    m = re.search(r'(?m)^source_pdf: "(.*)"$', text)
    if not m:
        print(f"{doc}: no source_pdf in frontmatter", file=sys.stderr)
        return 1
    pdf_path = resolve_source(m.group(1), roots)
    if not pdf_path:
        print(f"{m.group(1)}: source not found under {roots}", file=sys.stderr)
        return 1

    # Eleven decks in this corpus ship as .pptx. PyMuPDF opens one as a single
    # blank page rather than failing, so --extract silently produced a one-page
    # work list and a white image, and the reviewers reading it had nothing to
    # compare against. Route slide formats through LibreOffice, exactly as the
    # converter does, so the page images are the real slides.
    if os.path.splitext(pdf_path)[1].lower() in SLIDE_EXTS:
        os.makedirs(work, exist_ok=True)
        rendered = slides_to_pdf(pdf_path, os.path.join(work, "render"))
        if not rendered:
            print(f"{pdf_path}: LibreOffice could not render this deck",
                  file=sys.stderr)
            return 1
        print(f"rendered {os.path.basename(pdf_path)} via LibreOffice")
        pdf_path = rendered

    wanted = None
    if only:
        wanted = set()
        for part in only.split(","):
            part = part.strip()
            if "-" in part:
                a, b = part.split("-", 1)
                wanted.update(range(int(a), int(b) + 1))
            elif part:
                wanted.add(int(part))

    os.makedirs(os.path.join(work, "pages"), exist_ok=True)
    by_slide = {n: text[s:e].strip() for n, s, e in sections(text)}
    pdf = pymupdf.open(pdf_path)
    tasks = []
    for idx in range(pdf.page_count):
        slide = idx + 1
        if wanted and slide not in wanted:
            continue
        png = os.path.join(work, "pages", f"p{slide:03d}.png")
        render(pdf[idx], png)
        tasks.append({
            "id": f"p{slide:03d}", "slide": slide,
            "image": os.path.relpath(png, work),
            "current_markdown": by_slide.get(slide, ""),
        })
    pdf.close()

    with open(os.path.join(work, "tasks.jsonl"), "w", encoding="utf-8") as fh:
        for t in tasks:
            fh.write(json.dumps(t, ensure_ascii=False) + "\n")
    print(f"{len(tasks)} pages rendered from {os.path.basename(pdf_path)}")
    print(f"Work list: {os.path.join(work, 'tasks.jsonl')}")
    return 0


def apply_to(doc: str, fixes: dict[int, str], verified: int) -> int:
    text = open(doc, encoding="utf-8").read()
    written = 0
    for num, start, end in reversed(sections(text)):
        if num not in fixes:
            continue
        body = fixes[num].strip()
        if body == text[start:end].strip():
            continue
        text = text[:start] + "\n\n" + body + "\n\n" + text[end:]
        written += 1
    text = set_key(text, "vision_verified_pages", str(verified))
    # "changed" means "the vision review rewrote this page", which is a property
    # of the review, not of when apply happened to run. Count the corrections
    # that carry replacement text, not the pages that differed on this pass --
    # otherwise a second apply of the same work list (done for race-safety)
    # zeroes the count, since nothing differs the second time.
    text = set_key(text, "vision_verified_pages_changed", str(len(fixes)))
    with open(doc, "w", encoding="utf-8") as fh:
        fh.write(text)
    return written


def drop_lines(body: str, patterns: list[re.Pattern]) -> tuple[str, int]:
    """Remove whole lines matching any pattern, and tidy the gap."""
    if not patterns:
        return body, 0
    kept, dropped = [], 0
    for line in body.splitlines():
        if any(p.search(line) for p in patterns):
            dropped += 1
            continue
        kept.append(line)
    if not dropped:
        return body, 0
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip(), dropped


def cmd_apply(doc: str, also: list[str], work: str, drop: list[str]) -> int:
    corr = os.path.join(work, "corrections.jsonl")
    if not os.path.exists(corr):
        print(f"No corrections at {corr}", file=sys.stderr)
        return 1
    # A document split across reviewers gets one judgement call answered several
    # times, and they do not always agree. On a 94-page deck reviewed by six
    # people, one restored the slide-master DLP stamp the converter drops
    # everywhere and five did not -- leaving the deck inconsistent with itself
    # depending on who held which page. Merging is where that has to be settled,
    # because it is the only point that sees all of the reviewers at once.
    patterns = [re.compile(p) for p in drop]
    fixes, reviewed, verdicts = {}, set(), {}
    dropped_lines = 0
    for line in open(corr, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            c = json.loads(line)
        except json.JSONDecodeError:
            continue
        slide = int(c["slide"]) if "slide" in c else int(c["id"].lstrip("p"))
        reviewed.add(slide)
        verdicts[slide] = c.get("verdict", "")
        if (c.get("markdown") or "").strip():
            body, n = drop_lines(c["markdown"], patterns)
            dropped_lines += n
            fixes[slide] = body
    if dropped_lines:
        print(f"normalised away {dropped_lines} line(s) matching --drop-line")

    for target in [doc] + list(also):
        n = apply_to(target, fixes, len(reviewed))
        print(f"{os.path.basename(target)}: {len(reviewed)} pages reviewed, "
              f"{n} rewritten")
    counts: dict[str, int] = {}
    for v in verdicts.values():
        counts[v or "unrecorded"] = counts.get(v or "unrecorded", 0) + 1
    print("verdicts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--doc", required=True)
    ap.add_argument("--also", action="append", default=[],
                    help="apply the same corrections to this document too")
    ap.add_argument("--src", action="append", default=None)
    ap.add_argument("--work", default="review-doc")
    ap.add_argument("--pages", default="", help="subset, e.g. '1-10,42'")
    ap.add_argument("--extract", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--drop-line", action="append", default=[], metavar="REGEX",
                    help="drop correction lines matching this regex, so one "
                         "reviewer's judgement on template chrome does not "
                         "leave the document inconsistent with itself; "
                         "repeatable")
    args = ap.parse_args()

    if args.extract:
        roots = [os.path.abspath(x) for x in (args.src or ["."])]
        return cmd_extract(args.doc, roots, os.path.abspath(args.work), args.pages)
    if args.apply:
        return cmd_apply(args.doc, args.also, os.path.abspath(args.work),
                         args.drop_line)
    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
