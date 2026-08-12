#!/usr/bin/env python3
"""
test_verify_uncertain.py — Unit tests for the OCR review round-trip.

These are regression tests for defects that actually happened, each of which
corrupted the corpus quietly rather than failing:

  - re-running --extract renumbered the work list, so corrections written
    against an earlier run overwrote blocks nobody had reviewed
  - --apply inserted its frontmatter key with a blind regex, so every batch
    added another copy and the YAML stopped being valid
  - --apply labelled the *first* flagged block in a document rather than the
    one that was read

Run:
    python3 tools/test_verify_uncertain.py
"""

from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("PYMUPDF_MESSAGE", "path:" + os.devnull)
import pymupdf  # noqa: E402

from verify_uncertain import (OCR_LABEL, VISION_LABEL, cmd_apply,  # noqa: E402
                              cmd_extract, set_key)

FAILURES: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"  PASS  {name}")
    else:
        FAILURES.append(name)
        print(f"  FAIL  {name}" + (f"\n        {detail}" if detail else ""))


INTRO = (OCR_LABEL + " — this page is dense hex or tabular data; "
         "values may be wrong\n")


def make_doc(blocks: list[str]) -> str:
    out = ["---", 'title: "Test Talk"', 'conference_full: "Test Con 2025"',
           f"ocr_unreliable_blocks: {len(blocks)}", "---", "", "# Test Talk", ""]
    for i, body in enumerate(blocks, 1):
        out += [f"## Slide {i}", "", INTRO.rstrip("\n"), "", "```text", body,
                "```", ""]
    return "\n".join(out) + "\n"


def build(root: str, blocks: list[str]) -> tuple[str, str, str]:
    out_root = os.path.join(root, "out")
    src_root = os.path.join(root, "src")
    work = os.path.join(root, "work")
    os.makedirs(os.path.join(out_root, "conf"))
    os.makedirs(src_root)

    doc = pymupdf.open()
    for i in range(len(blocks)):
        page = doc.new_page()
        page.insert_text((72, 72), f"page {i + 1}")
    doc.save(os.path.join(src_root, "talk.pdf"))
    doc.close()

    with open(os.path.join(out_root, "conf", "talk.md"), "w", encoding="utf-8") as fh:
        fh.write(make_doc(blocks))
    with open(os.path.join(out_root, "manifest.jsonl"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps({
            "status": "ok", "markdown": "conf/talk.md", "source_pdf": "talk.pdf",
            "title": "Test Talk", "conference_full": "Test Con 2025",
            "ocr_unreliable_blocks": len(blocks)}) + "\n")
    return out_root, src_root, work


def read_doc(out_root: str) -> str:
    return open(os.path.join(out_root, "conf", "talk.md"), encoding="utf-8").read()


def tasks_of(work: str) -> list[dict]:
    return [json.loads(l) for l in
            open(os.path.join(work, "tasks.jsonl"), encoding="utf-8") if l.strip()]


def write_corrections(work: str, pairs: list[tuple[str, str]]) -> None:
    with open(os.path.join(work, "corrections.jsonl"), "w", encoding="utf-8") as fh:
        for tid, text in pairs:
            fh.write(json.dumps({"id": tid, "text": text}) + "\n")


def main() -> int:
    print("set_key")
    doubled = ("---\na: 1\nocr_unreliable_blocks: 3\nvision_verified_blocks: 1\n"
               "vision_verified_blocks: 2\nvision_verified_blocks: 5\n---\nbody\n")
    fixed = set_key(doubled, "vision_verified_blocks", "4")
    check("collapses duplicate keys to one",
          fixed.count("vision_verified_blocks:") == 1, fixed)
    check("keeps the value it was given", "vision_verified_blocks: 4" in fixed)
    check("leaves other keys alone",
          "a: 1" in fixed and "ocr_unreliable_blocks: 3" in fixed)
    added = set_key("---\nocr_unreliable_blocks: 3\n---\nbody\n",
                    "vision_verified_blocks", "2")
    check("adds a missing key exactly once",
          added.count("vision_verified_blocks: 2") == 1, added)

    root = tempfile.mkdtemp()
    try:
        print("\nextract / apply round-trip")
        out_root, src_root, work = build(root, ["AAAA 0000", "BBBB 1111",
                                                "CCCC 2222"])
        cmd_extract(out_root, work, [src_root], 0)
        tasks = tasks_of(work)
        check("one task per flagged block", len(tasks) == 3,
              f"got {len(tasks)}")

        # Correct only the block on slide 2 -- the middle one, so that labelling
        # the first or the last block would both be visibly wrong.
        second = next(t for t in tasks if t["slide"] == 2)
        write_corrections(work, [(second["id"], "corrected middle block")])
        cmd_apply(out_root, work)
        body = read_doc(out_root)

        check("the reviewed block's text is replaced",
              "corrected middle block" in body)
        check("other blocks are untouched",
              "AAAA 0000" in body and "CCCC 2222" in body)
        pos_label = body.find(VISION_LABEL)
        check("exactly one block is labelled reviewed",
              body.count(VISION_LABEL) == 1)
        check("the label sits on the block that was read",
              -1 < body.find("## Slide 2") < pos_label < body.find("## Slide 3"),
              "label attached to the wrong slide")
        check("remaining flagged blocks are counted",
              "ocr_unreliable_blocks: 2" in body)
        check("reviewed blocks are counted",
              "vision_verified_blocks: 1" in body)

        print("\napply is idempotent")
        cmd_apply(out_root, work)
        again = read_doc(out_root)
        check("second run changes nothing", again == body)
        check("no duplicate frontmatter key",
              again.count("vision_verified_blocks:") == 1)

        print("\nids survive re-extraction")
        ids_before = {(t["markdown"], t["slide"]): t["id"] for t in tasks}
        cmd_extract(out_root, work, [src_root], 0)
        after = tasks_of(work)
        by_key = {(t["markdown"], t["slide"]): t["id"] for t in after}
        check("unreviewed blocks keep their ids",
              all(by_key[k] == v for k, v in ids_before.items() if k in by_key),
              f"{ids_before} -> {by_key}")
        check("the reviewed block is retained, not renumbered away",
              by_key.get(("conf/talk.md", 2)) == second["id"])
        check("the reviewed block is marked reviewed",
              any(t["id"] == second["id"] and t.get("reviewed") for t in after))
        check("no id is issued twice",
              len({t["id"] for t in after}) == len(after))

        print("\nunknown ids are refused")
        write_corrections(work, [("99999", "text for a block that is not here")])
        cmd_apply(out_root, work)
        check("a correction with an unknown id edits nothing",
              read_doc(out_root) == body)
    finally:
        shutil.rmtree(root, ignore_errors=True)

    print()
    if FAILURES:
        print(f"{len(FAILURES)} failed: {', '.join(FAILURES)}")
        return 1
    print("all assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
