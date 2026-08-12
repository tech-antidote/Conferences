#!/usr/bin/env python3
"""
verify_uncertain.py — Prepare (and apply) vision review of unreliable OCR blocks.

Tesseract cannot read a hex dump off a slide screenshot. Measured against ground
truth it turns `00000118` into `80000118` and drops the row a talk was built
around, and no DPI or preprocessing fixes it -- 400 DPI scored *worse* than 200.
A vision model reading the rendered page can read those slides correctly, so the
blocks the converter flags as unreliable are exactly the ones worth sending to
one.

This does the mechanical half of that:

  `--extract`  finds every block flagged `ocr_unreliable`, renders its page to
               PNG, and writes a work list pairing each image with the text
               currently in the corpus.

  `--apply`    reads the corrected transcriptions back and rewrites those blocks,
               recording in frontmatter that the page was read by a vision model
               rather than OCR'd.

The review itself is done by whatever reads the work list -- an agent, a batch
API call, or a person. Nothing here calls a model.

Usage:
    python3 tools/verify_uncertain.py --extract --out markdown --work review/
    python3 tools/verify_uncertain.py --apply   --out markdown --work review/
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

os.environ.setdefault("PYMUPDF_MESSAGE", "path:" + os.devnull)
import pymupdf  # noqa: E402

# Enough resolution for a model to read small monospace text without producing
# images so large they dominate a context window.
RENDER_DPI = 150
MAX_EDGE = 2200

BLOCK_RE = re.compile(
    r"(?P<intro>> Recovered by OCR[^\n]*\n)\n(?P<fence>```text\n(?P<body>.*?)\n```)",
    re.S)
SLIDE_RE = re.compile(r"(?m)^## Slide (\d+)$")


def blocks_in(md_path: str) -> list[tuple[int, str, int, int]]:
    """Return (slide_no, block_text, start, end) for each unreliable block."""
    body = open(md_path, encoding="utf-8").read()
    slides = [(m.start(), int(m.group(1))) for m in SLIDE_RE.finditer(body)]
    out = []
    for m in BLOCK_RE.finditer(body):
        if "dense hex" not in m.group("intro"):
            continue
        slide = 0
        for pos, num in slides:
            if pos < m.start():
                slide = num
            else:
                break
        out.append((slide, m.group("body"), m.start("body"), m.end("body")))
    return out


def render(pdf_path: str, page_no: int, dest: str) -> bool:
    try:
        doc = pymupdf.open(pdf_path)
        if page_no < 1 or page_no > doc.page_count:
            doc.close()
            return False
        page = doc[page_no - 1]
        dpi = RENDER_DPI
        long_in = max(page.rect.width, page.rect.height) / 72.0
        if long_in and long_in * dpi > MAX_EDGE:
            dpi = max(90, int(MAX_EDGE / long_in))
        page.get_pixmap(dpi=dpi).save(dest)
        doc.close()
        return True
    except Exception:  # noqa: BLE001
        return False


def resolve_source(rel: str, roots: list[str]) -> str | None:
    """Find a deck's PDF across several roots.

    Sources are not all in one place: repo decks sit in the checkout, while DEF
    CON material is unpacked from a release elsewhere.
    """
    for root in roots:
        cand = os.path.join(root, rel)
        if os.path.exists(cand):
            return cand
        # Fall back to basename search one level down, for re-layouts.
        alt = os.path.join(root, os.path.basename(rel))
        if os.path.exists(alt):
            return alt
    return None


def cmd_extract(out_root: str, work: str, src_roots: list[str], limit: int) -> int:
    manifest = os.path.join(out_root, "manifest.jsonl")
    if not os.path.exists(manifest):
        print(f"No manifest at {manifest}", file=sys.stderr)
        return 1
    recs = [json.loads(l) for l in open(manifest, encoding="utf-8") if l.strip()]
    recs = [r for r in recs if r.get("status") == "ok"
            and (r.get("ocr_unreliable_blocks") or 0) > 0]

    os.makedirs(os.path.join(work, "pages"), exist_ok=True)
    tasks, missing = [], 0
    for rec in recs:
        md_path = os.path.join(out_root, rec["markdown"])
        if not os.path.exists(md_path):
            continue
        pdf_path = resolve_source(rec["source_pdf"], src_roots)
        if not pdf_path:
            missing += 1
            continue
        for slide, text, _, _ in blocks_in(md_path):
            key = f"{len(tasks):05d}"
            png = os.path.join(work, "pages", f"{key}.png")
            if not render(pdf_path, slide, png):
                continue
            tasks.append({
                "id": key, "markdown": rec["markdown"], "slide": slide,
                "image": os.path.relpath(png, work),
                "title": rec.get("title", ""), "conference": rec.get("conference_full", ""),
                "current_ocr": text,
            })
            if limit and len(tasks) >= limit:
                break
        if limit and len(tasks) >= limit:
            break

    with open(os.path.join(work, "tasks.jsonl"), "w", encoding="utf-8") as fh:
        for t in tasks:
            fh.write(json.dumps(t, ensure_ascii=False) + "\n")

    print(f"{len(tasks)} unreliable blocks rendered into {work}/pages")
    if missing:
        print(f"  ({missing} decks skipped: source PDF not present locally)")
    print(f"Work list: {os.path.join(work, 'tasks.jsonl')}")
    print("\nEach task pairs a page image with the text currently in the corpus.")
    print("Write corrections to corrections.jsonl as {\"id\": ..., \"text\": ...},")
    print("then re-run with --apply.")
    return 0


def cmd_apply(out_root: str, work: str) -> int:
    tasks = {t["id"]: t for t in
             (json.loads(l) for l in open(os.path.join(work, "tasks.jsonl"),
                                          encoding="utf-8") if l.strip())}
    corr_path = os.path.join(work, "corrections.jsonl")
    if not os.path.exists(corr_path):
        print(f"No corrections at {corr_path}", file=sys.stderr)
        return 1

    by_doc: dict[str, list[tuple[int, str]]] = {}
    for line in open(corr_path, encoding="utf-8"):
        if not line.strip():
            continue
        c = json.loads(line)
        t = tasks.get(c["id"])
        if not t or not (c.get("text") or "").strip():
            continue
        by_doc.setdefault(t["markdown"], []).append((t["slide"], c["text"].strip()))

    changed = 0
    for rel, fixes in by_doc.items():
        path = os.path.join(out_root, rel)
        if not os.path.exists(path):
            continue
        body = open(path, encoding="utf-8").read()
        wanted = dict(fixes)
        # Replace right to left so earlier offsets stay valid.
        for slide, _text, start, end in reversed(blocks_in(path)):
            if slide not in wanted:
                continue
            new = wanted[slide]
            body = body[:start] + new + body[end:]
        # Re-label the blocks that were reviewed.
        for slide in wanted:
            body = body.replace(
                "> Recovered by OCR", "> Read by a vision model from the page image "
                "(replacing unreliable OCR)", 1)
        body = re.sub(r"(?m)^ocr_unreliable_blocks: \d+$",
                      f"ocr_unreliable_blocks: 0\nvision_verified_blocks: {len(fixes)}",
                      body, count=1)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
        changed += len(fixes)

    print(f"Applied {changed} corrected blocks across {len(by_doc)} documents")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown")
    ap.add_argument("--src", action="append", default=None,
                    help="root the source_pdf paths resolve against; repeatable")
    ap.add_argument("--work", default="review", help="working directory")
    ap.add_argument("--extract", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    if args.extract:
        roots = [os.path.abspath(x) for x in (args.src or ["."])]
        return cmd_extract(os.path.abspath(args.out), os.path.abspath(args.work),
                           roots, args.limit)
    if args.apply:
        return cmd_apply(os.path.abspath(args.out), os.path.abspath(args.work))
    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
