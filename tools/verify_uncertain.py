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

OCR_LABEL = "> Recovered by OCR"
VISION_LABEL = ("> Read by a vision model from the page image "
                "(replacing unreliable OCR)")

BLOCK_RE = re.compile(
    r"(?P<intro>> (?:Recovered by OCR|Read by a vision model from the page image "
    r"\(replacing unreliable OCR\))[^\n]*\n)\n(?P<fence>```text\n(?P<body>.*?)\n```)",
    re.S)
SLIDE_RE = re.compile(r"(?m)^## Slide (\d+)$")


def blocks_in(md_path: str, text: str | None = None,
              include_reviewed: bool = True) -> list[tuple[int, str, int, int]]:
    """Return (slide_no, block_text, start, end) for each unreliable block.

    Blocks already read by a vision model are matched too, so that re-running
    --apply lands on the same blocks instead of silently skipping them; the
    caller decides what to do with a block that has already been reviewed.
    """
    body = text if text is not None else open(md_path, encoding="utf-8").read()
    slides = [(m.start(), int(m.group(1))) for m in SLIDE_RE.finditer(body)]
    out = []
    for m in BLOCK_RE.finditer(body):
        if "dense hex" not in m.group("intro"):
            continue
        if not include_reviewed and m.group("intro").startswith(VISION_LABEL):
            continue
        slide = 0
        for pos, num in slides:
            if pos < m.start():
                slide = num
            else:
                break
        out.append((slide, m.group("body"), m.start("body"), m.end("body")))
    return out


def set_key(text: str, key: str, value: str) -> str:
    """Set a frontmatter key exactly once, collapsing any duplicates.

    --apply is run repeatedly as review batches land. A blind regex insert adds
    a second copy of the key each time, which turns valid frontmatter into YAML
    with duplicate keys, so writing a key means replacing every occurrence of
    it and keeping the first.
    """
    line = f"{key}: {value}"
    pat = re.compile(rf"(?m)^{re.escape(key)}: .*\n")
    hits = list(pat.finditer(text))
    if hits:
        # Keep the first copy's position; drop the rest.
        for m in reversed(hits[1:]):
            text = text[:m.start()] + text[m.end():]
        return pat.sub(line + "\n", text, count=1)
    anchor = re.search(r"(?m)^ocr_unreliable_blocks: .*\n", text)
    if anchor:
        return text[:anchor.end()] + line + "\n" + text[anchor.end():]
    end = text.find("\n---", 4)          # close of the frontmatter block
    return text[:end] + "\n" + line + text[end:]


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

    # Ids must survive re-extraction. Review runs in batches against a corpus
    # that is still being built, so --extract gets re-run while corrections are
    # in flight; numbering from zero each time silently re-points every id at a
    # different block, and a correction then overwrites the wrong slide. So an
    # id is bound to (document, slide) for good, and blocks already reviewed
    # stay in the file -- flagged, not renumbered -- so their ids are never
    # handed to anything else.
    prev_path = os.path.join(work, "tasks.jsonl")
    prev = []
    if os.path.exists(prev_path):
        prev = [json.loads(l) for l in open(prev_path, encoding="utf-8") if l.strip()]
    prev_by_key = {(p["markdown"], p["slide"]): p for p in prev}
    used = {p["id"] for p in prev}
    next_id = max((int(p["id"]) for p in prev if p["id"].isdigit()), default=-1) + 1

    def mint(key: tuple[str, int]) -> str:
        nonlocal next_id
        if key in prev_by_key:
            return prev_by_key[key]["id"]
        while f"{next_id:05d}" in used:
            next_id += 1
        new = f"{next_id:05d}"
        used.add(new)
        return new

    tasks, missing = [], 0
    for rec in recs:
        md_path = os.path.join(out_root, rec["markdown"])
        if not os.path.exists(md_path):
            continue
        pdf_path = resolve_source(rec["source_pdf"], src_roots)
        if not pdf_path:
            missing += 1
            continue
        for slide, text, _, _ in blocks_in(md_path, include_reviewed=False):
            key = mint((rec["markdown"], slide))
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

    fresh = {t["id"] for t in tasks}
    retained = [dict(p, reviewed=True) for p in prev if p["id"] not in fresh]
    with open(prev_path, "w", encoding="utf-8") as fh:
        for t in sorted(tasks + retained, key=lambda x: x["id"]):
            fh.write(json.dumps(t, ensure_ascii=False) + "\n")

    print(f"{len(tasks)} unreliable blocks rendered into {work}/pages")
    if retained:
        print(f"  ({len(retained)} previously reviewed blocks kept, ids unchanged)")
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

    by_doc: dict[str, dict[int, str]] = {}
    unknown = 0
    for line in open(corr_path, encoding="utf-8"):
        if not line.strip():
            continue
        c = json.loads(line)
        t = tasks.get(c["id"])
        if not t:
            unknown += 1
            continue
        if not (c.get("text") or "").strip():
            continue
        by_doc.setdefault(t["markdown"], {})[t["slide"]] = c["text"].strip()
    if unknown:
        # An id with no task is a correction written against a different work
        # list. Applying it would edit whichever block now holds that number.
        print(f"REFUSING {unknown} corrections whose id is not in this work list",
              file=sys.stderr)

    changed, docs = 0, 0
    for rel, wanted in by_doc.items():
        path = os.path.join(out_root, rel)
        if not os.path.exists(path):
            continue
        body = open(path, encoding="utf-8").read()
        # Reset every review label first. Applying in batches otherwise leaves
        # labels from an earlier run attached to blocks this run did not touch,
        # and makes the whole operation depend on how the batches were split.
        body = body.replace(VISION_LABEL, OCR_LABEL)

        applied = 0
        # Right to left, so offsets earlier in the file stay valid.
        for slide, _old, start, end in reversed(blocks_in(path, body)):
            if slide not in wanted:
                continue
            body = body[:start] + wanted[slide] + body[end:]
            applied += 1
        # Label the reviewed blocks, again right to left and by position, so a
        # block is labelled because it was reviewed and not because it happened
        # to come first in the document.
        for slide, _old, start, _end in reversed(blocks_in(path, body)):
            if slide not in wanted:
                continue
            intro = body.rfind(OCR_LABEL, 0, start)
            if intro != -1:
                body = (body[:intro] + VISION_LABEL
                        + body[intro + len(OCR_LABEL):])

        reviewed = body.count(VISION_LABEL)
        remaining = max(0, len(blocks_in(path, body)) - reviewed)
        body = set_key(body, "ocr_unreliable_blocks", str(remaining))
        body = set_key(body, "vision_verified_blocks", str(reviewed))
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
        changed += applied
        docs += 1

    print(f"Applied {changed} corrected blocks across {docs} documents")
    return 0


def cmd_record(work: str, record: str) -> int:
    """Merge this round's verdicts into the durable review record.

    The work directory is scratch -- page images, task lists, one file per
    reviewer -- and does not survive the session. What has to survive is which
    slide was read and what the reviewer concluded, so that a later reader can
    tell a slide confirmed correct from one rebuilt out of garbage.
    """
    tasks = {t["id"]: t for t in
             (json.loads(l) for l in open(os.path.join(work, "tasks.jsonl"),
                                          encoding="utf-8") if l.strip())}
    rows: dict[tuple[str, int], dict] = {}
    if os.path.exists(record):
        for line in open(record, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                rows[(r["markdown"], r["slide"])] = r

    added = 0
    for name in sorted(os.listdir(work)):
        if not (name.startswith("corrections_") and name.endswith(".jsonl")):
            continue
        for line in open(os.path.join(work, name), encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                c = json.loads(line)
            except json.JSONDecodeError:
                continue                  # a reviewer still writing its file
            t = tasks.get(c["id"])
            if not t or not (c.get("text") or "").strip():
                continue
            key = (t["markdown"], t["slide"])
            if key not in rows:
                added += 1
            rows[key] = {"markdown": t["markdown"], "slide": t["slide"],
                         "verdict": c.get("verdict", ""), "title": t.get("title", "")}

    with open(record, "w", encoding="utf-8") as fh:
        for key in sorted(rows):
            fh.write(json.dumps(rows[key], ensure_ascii=False) + "\n")
    print(f"{len(rows)} reviewed slides recorded in {record} ({added} new)")
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
    ap.add_argument("--record", metavar="PATH", default="",
                    help="merge this round's verdicts into a durable record")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    if args.extract:
        roots = [os.path.abspath(x) for x in (args.src or ["."])]
        return cmd_extract(os.path.abspath(args.out), os.path.abspath(args.work),
                           roots, args.limit)
    if args.apply:
        return cmd_apply(os.path.abspath(args.out), os.path.abspath(args.work))
    if args.record:
        return cmd_record(os.path.abspath(args.work), os.path.abspath(args.record))
    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
