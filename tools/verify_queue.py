#!/usr/bin/env python3
"""
verify_queue.py — Order documents for full-page review, and track what is done.

Reading every page of a 956-document corpus is not a single operation; it is a
long queue worked in waves, across sessions, with interruptions. This keeps the
order stable and the progress durable so a wave that dies mid-flight costs one
document rather than the run.

Ordering is by expected damage, highest first, from what the corpus already
knows about itself:

  - OCR density. Pages the converter OCR'd are where character errors live.
  - Subject. Talks whose value is exact strings -- addresses, GUIDs, registry
    paths, command lines -- lose more when a digit turns.
  - Size. Among equals, shorter documents first, so each wave finishes whole
    documents rather than leaving several half-read.

    python3 tools/verify_queue.py --filter 2026 --filter "DEF CON 34" --limit 6
    python3 tools/verify_queue.py --status
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vision_review_index import TOPICS  # noqa: E402

STATE = "tools/verify_queue_state.json"


def load(out_root: str) -> list[dict]:
    path = os.path.join(out_root, "manifest.jsonl")
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def score(rec: dict) -> float:
    pages = max(1, rec.get("pages") or 1)
    ocr = (rec.get("ocr_pages") or 0) / pages
    title = rec.get("title", "")
    topic = sum(1 for _h, pat in TOPICS if re.search(pat, title, re.I))
    # Flagged blocks are direct evidence this document has known-bad text.
    flagged = min(3, rec.get("ocr_unreliable_blocks") or 0)
    return ocr * 4 + topic * 1.5 + flagged - (pages / 400.0)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown")
    ap.add_argument("--filter", action="append", default=[],
                    help="substring of conference_full; repeatable")
    ap.add_argument("--limit", type=int, default=6)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--done", default="", help="mark this markdown path complete")
    args = ap.parse_args()

    state = {}
    if os.path.exists(STATE):
        state = json.load(open(STATE, encoding="utf-8"))

    if args.done:
        state[args.done] = True
        json.dump(state, open(STATE, "w", encoding="utf-8"), indent=1, sort_keys=True)
        print(f"marked done: {args.done}")
        return 0

    recs = load(args.out)
    if args.filter:
        recs = [r for r in recs
                if any(f.lower() in (r.get("conference_full") or "").lower()
                       for f in args.filter)]
    # A document already read end to end never re-enters the queue.
    pending = [r for r in recs
               if not r.get("vision_verified_pages") and not state.get(r["markdown"])]

    if args.status:
        done_pages = sum(r.get("pages", 0) for r in recs if r not in pending)
        print(f"{len(recs) - len(pending)}/{len(recs)} documents verified "
              f"({done_pages:,} of {sum(r.get('pages', 0) for r in recs):,} pages)")
        return 0

    for rec in sorted(pending, key=score, reverse=True)[:args.limit]:
        print(json.dumps({"markdown": rec["markdown"], "pages": rec["pages"],
                          "ocr_pages": rec.get("ocr_pages", 0),
                          "title": rec.get("title", "")[:70]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
