#!/usr/bin/env python3
"""vision_review_index.py — Record which slides were read by a vision model.

`verify_uncertain.py` marks a corrected block in place, which tells a reader
looking at one document that its text was checked. It does not answer the
question you actually ask of an archive: *what has been verified, and what
hasn't.* That needs a list.

The corpus is the authority on which blocks were reviewed -- a block carries
the label because a model read its page. Verdicts live alongside in
`vision_review.jsonl`, written when the review ran, so a slide the reviewer
called "accurate" is distinguishable from one it had to rebuild from scratch.
A slide can be listed here and still be wrong; what the list guarantees is
that a model looked at the page rather than trusting Tesseract.

Usage:
    python3 tools/vision_review_index.py --out markdown \
        --record tools/vision_review.jsonl > markdown/VISION_VERIFIED.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from verify_uncertain import VISION_LABEL  # noqa: E402

SLIDE_RE = re.compile(r"(?m)^## Slide (\d+)$")
FM_RE = re.compile(r"(?m)^(\w+): (.*)$")

VERDICT_ORDER = {"badly-mangled": 0, "minor-errors": 1, "mostly-accurate": 2,
                 "accurate": 3}

# Review effort was aimed at the classes of talk whose exact values matter most
# to someone building an offensive or defensive tool: an address, a GUID or a
# registry path that is one character wrong is worse than useless. Grouping is
# keyword-matched against the talk title, so it is a reading aid rather than a
# taxonomy -- a talk can sit under two headings, or under none while still
# being reviewed.
TOPICS = [
    ("Windows, Active Directory and Entra",
     r"windows|active directory|entra|azure ad|kerberos|ntlm|secureboot|"
     r"uefi|bitlocker|defender|powershell|registry|biometric|hello"),
    ("Cloud and API",
     r"cloud|aws|azure|gcp|kubernetes|k8s|container|ecs|iam|s3|oauth|"
     r"api|serverless|saas|tenant"),
    ("Web and browser",
     r"web|browser|chrome|webkit|javascript|xss|csrf|http|url|dom|"
     r"extension|wasm|webassembly|websql"),
    ("Zero-day, RCE and novel exploitation",
     r"zero.?day|0.?day|rce|remote code|preauth|exploit|privilege escalation|"
     r"lpe|sandbox escape|use.after.free|heap|jit|rop|shellcode|cve"),
    ("Firmware, hardware and embedded",
     r"firmware|hardware|bootloader|baseband|usb|bluetooth|ble|nfc|"
     r"soc|mcu|jtag|glitch|fault injection|side.channel|plc|ics|scada"),
]


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    return {m.group(1): m.group(2).strip().strip('"')
            for m in FM_RE.finditer(text[:end if end > 0 else 0])}


def reviewed_slides(text: str) -> list[int]:
    """Slide numbers whose blocks carry the vision-read label."""
    slides = [(m.start(), int(m.group(1))) for m in SLIDE_RE.finditer(text)]
    out = []
    for m in re.finditer(re.escape(VISION_LABEL), text):
        num = 0
        for pos, n in slides:
            if pos < m.start():
                num = n
            else:
                break
        out.append(num)
    return sorted(set(out))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown")
    ap.add_argument("--record", default="tools/vision_review.jsonl")
    args = ap.parse_args()

    verdicts: dict[tuple[str, int], str] = {}
    if os.path.exists(args.record):
        for line in open(args.record, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                verdicts[(r["markdown"], r["slide"])] = r.get("verdict", "")

    rows, total = [], 0
    for dirpath, dirnames, filenames in os.walk(args.out):
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            text = open(path, encoding="utf-8").read()
            if VISION_LABEL not in text:
                continue
            rel = os.path.relpath(path, args.out)
            fm = frontmatter(text)
            slides = reviewed_slides(text)
            total += len(slides)
            vs = [verdicts.get((rel, s), "") for s in slides]
            rows.append((fm.get("conference_full", ""), fm.get("title", rel),
                         slides, vs, int(fm.get("ocr_unreliable_blocks", 0) or 0)))

    counts: dict[str, int] = {}
    for _c, _t, _s, vs, _r in rows:
        for v in vs:
            counts[v or "unrecorded"] = counts.get(v or "unrecorded", 0) + 1

    print("# Vision-verified slides")
    print()
    print("Every slide listed here had its page image read by a vision model and")
    print("compared against what OCR produced for it. The verdict is that model's")
    print("judgement of the OCR text, not of the slide.")
    print()
    print(f"**{total} slides across {len(rows)} documents.**")
    print()
    if counts:
        print("| Verdict | Slides | Meaning |")
        print("|---|---:|---|")
        meaning = {
            "badly-mangled": "OCR text was unusable — rebuilt from the page",
            "minor-errors": "structure held; individual characters or lines wrong",
            "mostly-accurate": "small corrections only",
            "accurate": "OCR was already correct; text confirmed, not changed",
            "unrecorded": "reviewed before verdicts were recorded",
        }
        for v, n in sorted(counts.items(), key=lambda kv: VERDICT_ORDER.get(kv[0], 9)):
            print(f"| {v} | {n} | {meaning.get(v, '')} |")
        print()
    print("## Coverage by subject")
    print()
    print("Grouped by keyword match on the talk title, so a talk can appear")
    print("under more than one heading or under none. Counts are slides.")
    print()
    for heading, pattern in TOPICS:
        hits = [(c, t, s) for c, t, s, _v, _r in rows
                if re.search(pattern, t, re.I)]
        if not hits:
            continue
        n = sum(len(s) for _c, _t, s in hits)
        print(f"### {heading} — {len(hits)} talks, {n} slides")
        print()
        for conf, title, slides in sorted(hits):
            print(f"- **{title}** ({conf}) — slide"
                  f"{'s' if len(slides) > 1 else ''} "
                  f"{', '.join(str(x) for x in slides)}")
        print()

    print("## Every verified slide")
    print()
    print("| Conference | Talk | Slides read | Verdicts | Blocks still OCR-only |")
    print("|---|---|---|---|---:|")
    for conf, title, slides, vs, rest in sorted(rows):
        seen = sorted({v for v in vs if v}, key=lambda v: VERDICT_ORDER.get(v, 9))
        s = ", ".join(str(x) for x in slides)
        print(f"| {conf} | {title.replace('|', '/')} | {s} | "
              f"{', '.join(seen) or '—'} | {rest} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
