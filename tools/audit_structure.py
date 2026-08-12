#!/usr/bin/env python3
"""Structural and schema integrity audit for the converted Markdown corpus.

Checks that the Markdown tree under --out and the manifest agree with each
other and with the source PDFs:

  1. manifest <-> disk pairing, in both directions
  2. YAML frontmatter present, parseable, complete, correctly typed
  3. "## Slide N" headings match the frontmatter `pages` count and run 1..N
  4. no empty / truncated files (unterminated frontmatter, odd ``` fences)
  5. slug collisions: two source PDFs sharing one output file, one source PDF
     written to several output files, and orphan files nothing points at
  6. `source_pdf` paths resolve on disk (sources under an --expect-absent
     prefix -- DEF CON 34 lives in a GitHub release -- are counted apart)

Exit status is 0 when every check passes and 1 when anything failed, so this
can gate CI or a post-conversion smoke test.

    python3 tools/audit_structure.py --out markdown
    python3 tools/audit_structure.py --out markdown --json report.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from collections import defaultdict

try:
    import yaml
except ImportError:  # pragma: no cover - environment guard
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

# Generated navigation, not talk content.
NON_TALK_FILES = {"README.md", "INDEX.md", "VERIFICATION.md",
                  "VISION_VERIFIED.md", "UNVERIFIED.md"}

# The corpus is no longer only slide decks. Transcripts and workshop material
# are converted by different tools into their own manifests, and auditing
# against manifest.jsonl alone reported all 123 of them as orphans on disk --
# 245 problems that were entirely the audit's own blind spot.
COMPANION_MANIFESTS = ("transcripts.jsonl", "workshops.jsonl")

# key -> (accepted types, human name). bool is excluded from the int types
# explicitly below, since in Python `True` is an int.
REQUIRED_FIELDS = {
    "title": "str",
    "speakers": "list",
    "conference": "str",
    "conference_full": "str",
    "year": "int",
    "source_pdf": "str",
    "pages": "int",
    "sha256": "str",
    "text_chars": "int",
    "ocr_pages": "int",
    "has_ocr": "bool",
}

# A transcript has no pages and a workshop has no source PDF, so demanding the
# slide-deck keys of them reports a document as broken for not being a slide
# deck. Each source type is held to the keys that mean something for it.
REQUIRED_BY_TYPE = {
    "transcript": {"title": "str", "speakers": "list", "conference": "str",
                   "conference_full": "str", "year": "int", "sha256": "str",
                   "text_chars": "int", "words": "int",
                   "duration_seconds": "int"},
    "workshop-materials": {"title": "str", "speakers": "list",
                           "conference": "str", "conference_full": "str",
                           "sha256": "str", "text_chars": "int",
                           "files_included": "int"},
}

SLIDE_RE = re.compile(r"^##\s+Slide\s+(\d+)\s*$")
# CommonMark fence rules: a backtick fence opens on ``` plus an info string that
# contains no backticks, and closes on a bare run of >= that many backticks.
FENCE_OPEN_BACKTICK = re.compile(r"^\s{0,3}(`{3,})([^`]*)$")
FENCE_OPEN_TILDE = re.compile(r"^\s{0,3}(~{3,})(.*)$")
FENCE_CLOSE_BACKTICK = re.compile(r"^\s{0,3}(`{3,})\s*$")
FENCE_CLOSE_TILDE = re.compile(r"^\s{0,3}(~{3,})\s*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def type_name(value) -> str:
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    if isinstance(value, list):
        return "list"
    if isinstance(value, dict):
        return "dict"
    if value is None:
        return "null"
    return type(value).__name__


def read_text(path: str, retries: int = 2, delay: float = 0.4) -> str:
    """Read a file, tolerating a writer that is mid-flush.

    A concurrent conversion can leave a file momentarily empty or half
    written; re-read before believing what we saw.
    """
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                return fh.read()
        except OSError as exc:  # pragma: no cover - transient
            last_err = exc
            if attempt < retries:
                time.sleep(delay)
    raise last_err  # type: ignore[misc]


def split_frontmatter(text: str):
    """Return (raw_yaml, body, error) for a file whose text is `text`."""
    if not text.strip():
        return None, "", "file is empty"
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None, text, "no opening '---' frontmatter delimiter on line 1"
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return "\n".join(lines[1:idx]), "\n".join(lines[idx + 1:]), None
    return None, "", "frontmatter opened but never closed (truncated file)"


class BodyScan:
    """Result of walking a file body once."""

    def __init__(self):
        self.slides: list[int] = []       # '## Slide N' outside fenced blocks
        self.slides_raw: list[int] = []   # every '## Slide N' line
        self.fence_markers = 0            # opening + closing fence lines seen
        self.open_at_eof = False          # body ends inside a fenced block
        self.open_line = 0                # line number of the dangling opener
        self.open_text = ""               # text of the dangling opener


def scan_body(body: str) -> BodyScan:
    scan = BodyScan()
    in_fence = False
    marker_char = ""
    marker_len = 0
    for lineno, line in enumerate(body.splitlines(), 1):
        if in_fence:
            closer = (FENCE_CLOSE_BACKTICK if marker_char == "`"
                      else FENCE_CLOSE_TILDE).match(line)
            if closer and len(closer.group(1)) >= marker_len:
                in_fence = False
                scan.fence_markers += 1
            elif SLIDE_RE.match(line):
                scan.slides_raw.append(int(SLIDE_RE.match(line).group(1)))
            continue

        opener = FENCE_OPEN_BACKTICK.match(line) or FENCE_OPEN_TILDE.match(line)
        if opener:
            in_fence = True
            marker_char = opener.group(1)[0]
            marker_len = len(opener.group(1))
            scan.fence_markers += 1
            scan.open_line, scan.open_text = lineno, line.strip()[:60]
            continue

        m = SLIDE_RE.match(line)
        if m:
            scan.slides.append(int(m.group(1)))
            scan.slides_raw.append(int(m.group(1)))

    scan.open_at_eof = in_fence
    return scan


def rel_md_paths(out_root: str) -> list[str]:
    found = []
    for root, dirs, files in os.walk(out_root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in files:
            if not name.endswith(".md") or name in NON_TALK_FILES:
                continue
            found.append(os.path.relpath(os.path.join(root, name), out_root))
    return sorted(found)


# --------------------------------------------------------------------------
# audit
# --------------------------------------------------------------------------
class Audit:
    def __init__(self, out_root: str, src_root: str, manifest_path: str,
                 expect_absent):
        self.out_root = out_root
        self.src_root = src_root
        self.manifest_path = manifest_path
        # One prefix was enough when only DEF CON 34 came from a release;
        # DEF CON 33's talks and workshops arrive the same way.
        if isinstance(expect_absent, str):
            expect_absent = [expect_absent]
        self.expect_absent = tuple(p for p in (expect_absent or []) if p)
        # category -> list of "path: detail" strings
        self.problems: dict[str, list[str]] = defaultdict(list)
        self.stats: dict[str, int] = {}
        self.notes: dict[str, list[str]] = defaultdict(list)

    def fail(self, category: str, detail: str) -> None:
        self.problems[category].append(detail)

    # -- manifest ---------------------------------------------------------
    def load_manifest(self, use_partial: bool = False):
        records, bad = [], 0
        sources = [self.manifest_path]
        partial = self.manifest_path + ".partial"

        # pdf2md streams finished decks to <manifest>.partial and only writes
        # the real manifest at the end, so its presence means a conversion is
        # running and the tree underneath us is a moving target.
        if os.path.exists(partial):
            self.notes["conversion-in-flight"].append(
                f"{partial} exists: a conversion is streaming results, so disk "
                "state is mid-flight"
                + ("; its records are included" if use_partial
                   else "; re-run with --partial to include them"))
            if use_partial:
                sources.append(partial)

        for companion in COMPANION_MANIFESTS:
            path = os.path.join(os.path.dirname(self.manifest_path), companion)
            if os.path.exists(path):
                sources.append(path)

        if not os.path.exists(self.manifest_path):
            self.fail("manifest-unreadable",
                      f"{self.manifest_path}: manifest file not found"
                      + (" (a conversion is in flight; only .partial exists)"
                         if os.path.exists(partial) else ""))
            sources = [p for p in sources if p != self.manifest_path]

        for source in sources:
            with open(source, "r", encoding="utf-8") as fh:
                for lineno, line in enumerate(fh, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError as exc:
                        bad += 1
                        self.fail("manifest-bad-json", f"{source}:{lineno}: {exc}")
        self.stats["manifest_records"] = len(records)
        self.stats["manifest_bad_json_lines"] = bad
        return records

    # -- check 1 & 5 ------------------------------------------------------
    def check_pairing(self, records, disk_files):
        ok_records = [r for r in records if r.get("status") == "ok"]
        self.stats["manifest_ok"] = len(ok_records)
        self.stats["manifest_not_ok"] = len(records) - len(ok_records)
        self.stats["disk_md_files"] = len(disk_files)

        for rec in records:
            if rec.get("status") != "ok":
                self.fail("manifest-status-not-ok",
                          f"{rec.get('source_pdf', '?')}: status="
                          f"{rec.get('status')!r} error={rec.get('error', '')[:120]!r}")

        claimed: dict[str, list[str]] = defaultdict(list)
        missing_on_disk = 0
        for rec in ok_records:
            md = rec.get("markdown")
            src = rec.get("source_pdf", "?")
            if not md:
                self.fail("manifest-no-markdown-field",
                          f"{src}: record has status ok but no 'markdown' path")
                continue
            claimed[md].append(src)
            if not os.path.exists(os.path.join(self.out_root, md)):
                missing_on_disk += 1
                self.fail("missing-markdown-file",
                          f"{md}: referenced by manifest ({src}) but not on disk")
        self.stats["manifest_ok_missing_file"] = missing_on_disk

        # check 5a: two source PDFs -> one output file
        for md, srcs in sorted(claimed.items()):
            if len(srcs) > 1:
                self.fail("slug-collision-shared-output",
                          f"{md}: claimed by {len(srcs)} source PDFs: "
                          + "; ".join(sorted(srcs)))

        disk_set = set(disk_files)
        orphans = sorted(disk_set - set(claimed))
        self.stats["orphan_files"] = len(orphans)
        for path in orphans:
            self.fail("orphan-markdown-file",
                      f"{path}: on disk but no manifest record points at it")
        return ok_records, claimed, orphans

    # -- checks 2, 3, 4 ---------------------------------------------------
    def check_files(self, disk_files):
        """Parse every Markdown file; returns {rel_path: frontmatter dict}."""
        fm_by_path: dict[str, dict] = {}
        counts = defaultdict(int)

        for rel in disk_files:
            path = os.path.join(self.out_root, rel)
            try:
                text = read_text(path)
            except OSError as exc:
                self.fail("unreadable-file", f"{rel}: {exc}")
                continue

            raw, body, err = split_frontmatter(text)
            if err:
                # A concurrent writer can be caught mid-file: look again
                # before calling it broken.
                time.sleep(0.5)
                try:
                    text = read_text(path)
                except OSError as exc:
                    self.fail("unreadable-file", f"{rel}: {exc}")
                    continue
                raw, body, err = split_frontmatter(text)
            if err:
                counts["truncated"] += 1
                category = ("empty-file" if err == "file is empty"
                            else "truncated-or-no-frontmatter")
                self.fail(category, f"{rel}: {err}")
                continue

            try:
                meta = yaml.safe_load(raw)
            except yaml.YAMLError as exc:
                counts["yaml_error"] += 1
                self.fail("frontmatter-unparseable",
                          f"{rel}: YAML error: {str(exc).splitlines()[0]}")
                continue
            if not isinstance(meta, dict):
                counts["yaml_error"] += 1
                self.fail("frontmatter-unparseable",
                          f"{rel}: frontmatter parsed to "
                          f"{type_name(meta)}, expected a mapping")
                continue
            fm_by_path[rel] = meta
            counts["frontmatter_ok"] += 1

            self._check_schema(rel, meta, counts)
            self._check_body(rel, meta, body, counts)

        for key, value in counts.items():
            self.stats[f"files_{key}"] = value
        return fm_by_path

    def _check_schema(self, rel, meta, counts):
        required = REQUIRED_BY_TYPE.get(meta.get("source_type"), REQUIRED_FIELDS)
        missing = [k for k in required if k not in meta]
        if missing:
            counts["missing_keys"] += 1
            self.fail("frontmatter-missing-keys",
                      f"{rel}: missing {', '.join(missing)}")

        nulls = [k for k in required if k in meta and meta[k] is None]
        if nulls:
            counts["null_values"] += 1
            self.fail("frontmatter-null-value",
                      f"{rel}: required key(s) present but null: "
                      + ", ".join(f"{k} (want {required[k]})" for k in nulls))

        wrong = []
        for key, want in required.items():
            if key not in meta or meta[key] is None:
                continue
            value = meta[key]
            got = type_name(value)
            if want == "int" and got != "int":
                wrong.append(f"{key}={value!r} ({got}, want int)")
            elif want == "str" and got != "str":
                wrong.append(f"{key}={value!r} ({got}, want str)")
            elif want == "list" and got != "list":
                wrong.append(f"{key}={value!r} ({got}, want list)")
            elif want == "bool" and got != "bool":
                wrong.append(f"{key}={value!r} ({got}, want bool)")
        if isinstance(meta.get("speakers"), list):
            bad = [s for s in meta["speakers"] if not isinstance(s, str)]
            if bad:
                wrong.append(f"speakers has {len(bad)} non-string entries")
        if wrong:
            counts["wrong_types"] += 1
            self.fail("frontmatter-wrong-types", f"{rel}: " + "; ".join(wrong))

        bad_values = []
        pages = meta.get("pages")
        if isinstance(pages, int) and not isinstance(pages, bool) and pages < 1:
            bad_values.append(f"pages={pages} (must be >= 1)")
        sha = meta.get("sha256")
        if isinstance(sha, str) and not SHA256_RE.match(sha):
            bad_values.append(f"sha256={sha!r} (not 64 lowercase hex chars)")
        for key in ("text_chars", "ocr_pages"):
            val = meta.get(key)
            if isinstance(val, int) and not isinstance(val, bool) and val < 0:
                bad_values.append(f"{key}={val} (must be >= 0)")
        ocr, has_ocr = meta.get("ocr_pages"), meta.get("has_ocr")
        if isinstance(ocr, int) and not isinstance(ocr, bool) and isinstance(has_ocr, bool):
            if bool(ocr) != has_ocr:
                bad_values.append(f"has_ocr={has_ocr} but ocr_pages={ocr}")
        if isinstance(ocr, int) and isinstance(pages, int) and not isinstance(ocr, bool) \
                and not isinstance(pages, bool) and ocr > pages:
            bad_values.append(f"ocr_pages={ocr} exceeds pages={pages}")
        if isinstance(meta.get("speakers"), list) and not meta["speakers"]:
            bad_values.append("speakers is an empty list")
        if bad_values:
            counts["bad_values"] += 1
            self.fail("frontmatter-bad-values", f"{rel}: " + "; ".join(bad_values))

    def _check_body(self, rel, meta, body, counts):
        scan = scan_body(body)
        slides = scan.slides

        if not body.strip():
            counts["empty_body"] += 1
            self.fail("empty-body", f"{rel}: frontmatter present but no body")
            return

        pages = meta.get("pages")
        pages_ok = isinstance(pages, int) and not isinstance(pages, bool)

        if scan.open_at_eof or scan.fence_markers % 2:
            # A stray fence-looking line in slide content (e.g. "```|" inside a
            # table) leaves the block unclosed without the file being truncated.
            # Distinguish that from a genuinely cut-off file: if the headings
            # swallowed by the dangling fence restore the expected count, the
            # content is intact and the fence marker is the defect.
            stray = (pages_ok and len(scan.slides_raw) == pages
                     and len(slides) != pages)
            counts["unbalanced_fences"] += 1
            category = "stray-fence-marker" if stray else "unbalanced-code-fences"
            self.fail(category,
                      f"{rel}: {scan.fence_markers} fence markers; block opened "
                      f"at body line {scan.open_line} ({scan.open_text!r}) is "
                      f"never closed"
                      + ("; slide headings are all present, so the file is not "
                         "truncated" if stray else ""))
            if stray:
                slides = scan.slides_raw

        if not pages_ok:
            return  # already reported as a type problem

        if len(slides) != pages:
            counts["slide_count_mismatch"] += 1
            self.fail("slide-count-mismatch",
                      f"{rel}: {len(slides)} '## Slide N' headings but "
                      f"pages={pages}")
        expected = list(range(1, pages + 1))
        if slides != expected:
            dupes = sorted({n for n in slides if slides.count(n) > 1})
            gaps = sorted(set(expected) - set(slides))
            extra = sorted(set(slides) - set(expected))
            detail = []
            if dupes:
                detail.append(f"duplicate slide numbers {dupes[:10]}")
            if gaps:
                detail.append(f"missing slide numbers {gaps[:10]}"
                              + (f" (+{len(gaps) - 10} more)" if len(gaps) > 10 else ""))
            if extra:
                detail.append(f"out-of-range slide numbers {extra[:10]}")
            if not detail and slides != sorted(slides):
                detail.append("slide numbers out of order")
            if detail:
                counts["slide_sequence_broken"] += 1
                self.fail("slide-sequence-broken", f"{rel}: " + "; ".join(detail))

    # -- check 5b ---------------------------------------------------------
    def check_duplicate_conversions(self, fm_by_path):
        """One source PDF written to several Markdown files on disk."""
        by_source: dict[str, list[str]] = defaultdict(list)
        for rel, meta in fm_by_path.items():
            src = meta.get("source_pdf")
            if isinstance(src, str) and src:
                by_source[src].append(rel)
        dupes = {s: sorted(p) for s, p in by_source.items() if len(p) > 1}
        self.stats["sources_with_multiple_outputs"] = len(dupes)
        for src, paths in sorted(dupes.items()):
            self.fail("duplicate-conversion",
                      f"{src}: converted into {len(paths)} files: "
                      + ", ".join(paths))
        return dupes

    # -- check 6 ----------------------------------------------------------
    def check_sources(self, ok_records):
        present = absent_expected = absent_unexpected = 0
        for rec in ok_records:
            # A transcript's source is an audio recording and a workshop's is a
            # directory of code; neither has a PDF to resolve.
            if rec.get("source_type") in REQUIRED_BY_TYPE:
                continue
            src = rec.get("source_pdf")
            if not isinstance(src, str) or not src:
                self.fail("manifest-no-source-pdf",
                          f"{rec.get('markdown', '?')}: record has no source_pdf")
                continue
            if os.path.exists(os.path.join(self.src_root, src)):
                present += 1
            elif src.startswith(self.expect_absent):
                absent_expected += 1
                self.notes["expected-absent-source"].append(src)
            else:
                absent_unexpected += 1
                self.fail("missing-source-pdf",
                          f"{src}: referenced by manifest but not on disk")
        self.stats["source_pdf_present"] = present
        self.stats["source_pdf_absent_expected"] = absent_expected
        self.stats["source_pdf_absent_unexpected"] = absent_unexpected

    # -- run --------------------------------------------------------------
    def run(self, use_partial: bool = False):
        records = self.load_manifest(use_partial)
        disk_files = rel_md_paths(self.out_root)
        ok_records, _claimed, _orphans = self.check_pairing(records, disk_files)
        fm_by_path = self.check_files(disk_files)
        self.check_duplicate_conversions(fm_by_path)
        self.check_sources(ok_records)
        return self.problems


CHECK_LAYOUT = [
    ("1. manifest <-> disk pairing", [
        "manifest-unreadable", "manifest-bad-json", "manifest-status-not-ok",
        "manifest-no-markdown-field", "missing-markdown-file",
        "orphan-markdown-file",
    ]),
    ("2. frontmatter schema", [
        "unreadable-file", "frontmatter-unparseable",
        "frontmatter-missing-keys", "frontmatter-null-value",
        "frontmatter-wrong-types", "frontmatter-bad-values",
    ]),
    ("3. slide headings vs pages", [
        "slide-count-mismatch", "slide-sequence-broken",
    ]),
    ("4. empty / truncated files", [
        "empty-file", "truncated-or-no-frontmatter", "empty-body",
        "unbalanced-code-fences", "stray-fence-marker",
    ]),
    ("5. slug collisions & duplicates", [
        "slug-collision-shared-output", "duplicate-conversion",
    ]),
    ("6. source PDFs on disk", [
        "manifest-no-source-pdf", "missing-source-pdf",
    ]),
]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Audit structural/schema integrity of the Markdown corpus.")
    ap.add_argument("--out", default="markdown",
                    help="Markdown output root to audit (default: markdown)")
    ap.add_argument("--src", default=None,
                    help="repo root that source_pdf paths are relative to "
                         "(default: parent of --out)")
    ap.add_argument("--manifest", default=None,
                    help="manifest path (default: <out>/manifest.jsonl)")
    ap.add_argument("--expect-absent", action="append", default=None,
                    help="source_pdf prefix whose files are legitimately not in "
                         "the repo; repeatable. Defaults to the DEF CON drops, "
                         "which are distributed as release assets rather than "
                         "committed. Pass '' to disable.")
    ap.add_argument("--partial", action="store_true",
                    help="also read <manifest>.partial, the stream a conversion "
                         "writes while it is still running")
    ap.add_argument("--max-list", type=int, default=20,
                    help="max failing entries printed per category (default: 20)")
    ap.add_argument("--json", dest="json_out", default=None,
                    help="also write the full report as JSON to this path")
    args = ap.parse_args(argv)

    out_root = os.path.abspath(args.out)
    if not os.path.isdir(out_root):
        print(f"error: --out directory not found: {out_root}", file=sys.stderr)
        return 2
    src_root = os.path.abspath(args.src) if args.src else os.path.dirname(out_root)
    manifest = args.manifest or os.path.join(out_root, "manifest.jsonl")

    expect_absent = (args.expect_absent if args.expect_absent is not None
                     else ["DEF CON 34/", "DEF CON 33/", "DEF CON 33 workshops/"])
    audit = Audit(out_root, src_root, manifest, expect_absent)
    problems = audit.run(use_partial=args.partial)

    print("=" * 74)
    print(f"Structural audit: {out_root}")
    print(f"  manifest : {manifest}")
    print(f"  sources  : {src_root}")
    print("=" * 74)
    print("\nCounts")
    for key in sorted(audit.stats):
        print(f"  {key:34s} {audit.stats[key]:,}")

    total = sum(len(v) for v in problems.values())
    print("\nChecks")
    for title, categories in CHECK_LAYOUT:
        hits = sum(len(problems.get(c, ())) for c in categories)
        print(f"  [{'FAIL' if hits else ' OK '}] {title}"
              + (f"  ({hits} problem{'s' if hits != 1 else ''})" if hits else ""))

    if total:
        print("\nFailures")
        for title, categories in CHECK_LAYOUT:
            for cat in categories:
                items = problems.get(cat)
                if not items:
                    continue
                print(f"\n  {cat}  ({len(items)})")
                for item in items[: args.max_list]:
                    print(f"    - {item}")
                if len(items) > args.max_list:
                    print(f"    ... and {len(items) - args.max_list} more")

    if audit.notes:
        print("\nNotes")
        if audit.notes.get("expected-absent-source"):
            n = len(audit.notes["expected-absent-source"])
            print(f"  expected-absent sources (not an error): {n} under "
                  f"{list(audit.expect_absent)!r}")
        for line in audit.notes.get("conversion-in-flight", ()):
            print(f"  {line}")

    print("\n" + "=" * 74)
    print(f"RESULT: {'PROBLEMS FOUND' if total else 'CLEAN'} "
          f"({total} problem{'s' if total != 1 else ''} across "
          f"{len([c for c in problems if problems[c]])} categories)")
    print("=" * 74)

    if args.json_out:
        report = {
            "out_root": out_root,
            "manifest": manifest,
            "src_root": src_root,
            "stats": dict(audit.stats),
            "problem_counts": {k: len(v) for k, v in problems.items() if v},
            "problems": {k: v for k, v in problems.items() if v},
            "notes": {k: v for k, v in audit.notes.items()},
            "total_problems": total,
        }
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
        print(f"JSON report written to {args.json_out}")

    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
