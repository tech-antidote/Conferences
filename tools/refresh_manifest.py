#!/usr/bin/env python3
"""
refresh_manifest.py — Re-derive the manifest from the Markdown it describes.

`manifest.jsonl` is written once, by the converter. Everything that happens to
a document afterwards -- a vision review rewriting 93 of its 120 pages, a
metadata override correcting its speakers -- edits the Markdown and leaves the
manifest describing a version of the corpus that no longer exists.

That matters because the manifest is the machine-readable face of the archive.
`UNVERIFIED.md` tells a reader they can filter on it instead of reading prose,
and `verify_queue.py` decides what still needs review from it. Both were
quietly wrong: `vision_verified_blocks` was in 123 documents' frontmatter and
in no manifest row at all, so 123 documents' worth of review was invisible to
anyone who trusted the manifest.

So the manifest becomes a function of the corpus rather than of whether
someone remembered to patch it. For every key the document's frontmatter
carries, the frontmatter wins -- it is the artifact, the manifest merely
describes it. Conversion-time facts the frontmatter does not carry (status,
source_folder, any error) are preserved untouched.

One field is added rather than copied. `text_chars` is the converter's record
of how many characters it extracted, and it stays that -- overwriting it would
destroy the only evidence of what the first pass actually produced, and it is
not the same quantity as "how big is this document now" anyway: measured
across the 692 documents no reviewer has touched, counting slide bodies runs
about 5% above it, because the file also carries scaffolding the converter
added after counting. So `body_chars` is written alongside it, measuring the
document as it now stands. Where the two diverge by more than that baseline,
something edited the document after conversion.

    python3 tools/refresh_manifest.py --out markdown
    python3 tools/refresh_manifest.py --out markdown --check
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

SLIDE_RE = re.compile(r"(?m)^## Slide (\d+)$")
FM_LINE_RE = re.compile(r"(?m)^([A-Za-z_][A-Za-z0-9_]*): (.*)$")

# Facts about the conversion run, not about the document. The frontmatter does
# not carry them and must not be allowed to erase them.
MANIFEST_ONLY = {"markdown", "status", "error", "source_folder", "content_note"}


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    out: dict = {}
    for m in FM_LINE_RE.finditer(text[:end]):
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith("[") or raw.startswith("{"):
            try:
                out[key] = json.loads(raw)
                continue
            except json.JSONDecodeError:
                pass
        if raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
            out[key] = json.loads(raw) if raw.count('"') == 2 else raw[1:-1]
        elif raw in ("true", "false"):
            out[key] = raw == "true"
        elif raw == "null" or raw == "":
            out[key] = None
        elif re.fullmatch(r"-?\d+", raw):
            out[key] = int(raw)
        elif re.fullmatch(r"-?\d+\.\d+", raw):
            out[key] = float(raw)
        else:
            out[key] = raw
    return out


def body_chars(text: str) -> int:
    """Characters of slide content, excluding frontmatter and the doc header.

    Companion papers and transcripts carry no `## Slide` markers, so for those
    everything after the frontmatter counts -- a zero would read as "empty"
    rather than "not paginated".
    """
    marks = [(m.start(), m.end()) for m in SLIDE_RE.finditer(text)]
    if not marks:
        end = text.find("\n---", 3) + len("\n---") if text.startswith("---") else 0
        return len(text[end:].strip())
    total = 0
    for i, (_start, end) in enumerate(marks):
        stop = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        total += len(text[end:stop].strip())
    return total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown")
    ap.add_argument("--manifest", default="")
    ap.add_argument("--check", action="store_true",
                    help="report drift and exit non-zero; write nothing")
    args = ap.parse_args()

    path = args.manifest or os.path.join(args.out, "manifest.jsonl")
    if not os.path.exists(path):
        print(f"No manifest at {path}", file=sys.stderr)
        return 1

    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    changed, missing, drift = 0, 0, []
    for row in rows:
        doc = os.path.join(args.out, row.get("markdown") or "")
        if not row.get("markdown") or not os.path.exists(doc):
            missing += 1
            continue
        text = open(doc, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if not fm:
            missing += 1
            continue
        # Never from the frontmatter: the document's own header is written once
        # at conversion and is as stale as the manifest row.
        fm["body_chars"] = body_chars(text)

        touched = []
        for key, value in fm.items():
            if key in MANIFEST_ONLY:
                continue
            if row.get(key) != value or key not in row:
                touched.append(key)
                row[key] = value
        if touched:
            changed += 1
            drift.append((row["markdown"], touched))

    if args.check:
        for name, keys in drift[:20]:
            print(f"{name}: {', '.join(sorted(keys))}")
        if len(drift) > 20:
            print(f"... and {len(drift) - 20} more")
        print(f"{changed}/{len(rows)} rows stale, {missing} unreadable")
        return 1 if changed else 0

    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(tmp, path)
    print(f"{changed}/{len(rows)} rows refreshed"
          + (f", {missing} unreadable" if missing else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
