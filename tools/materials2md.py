#!/usr/bin/env python3
"""
materials2md.py — Package workshop source material into Markdown.

Workshop drops are not slide decks. A DEF CON workshop ships the exploit
scripts, the vulnerable C, the PowerShell, the lab configs — the working code
the room typed along with. For a corpus meant to teach a tool about technique,
that code is at least as valuable as the slides, and unlike slide text it needs
no OCR: it is already exact.

This collects the readable files under each workshop into one Markdown document,
each file in a fenced block tagged with its language, so a model reads it as
code rather than prose. Binaries (`.exe`, `.obj`, compiled artefacts) are listed
by name and size but not inlined — they carry nothing a language model can read,
and embedding megabytes of base64 would drown the corpus.

Slides are handled separately by `pdf2md.py`; run both over a workshop tree.

Usage:
    python3 tools/materials2md.py --src "DEF CON 34 workshops" --out markdown \
        --conference "DEF CON 34"
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf2md import redact_secrets, slugify, yaml_escape, yaml_list  # noqa: E402

# Extension -> fence language. Anything here gets inlined.
LANGS = {
    ".ps1": "powershell", ".psm1": "powershell", ".bat": "bat", ".cmd": "bat",
    ".py": "python", ".rb": "ruby", ".pl": "perl", ".lua": "lua",
    ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp", ".cc": "cpp",
    ".cs": "csharp", ".java": "java", ".go": "go", ".rs": "rust",
    ".js": "javascript", ".ts": "typescript", ".php": "php",
    ".sh": "bash", ".zsh": "bash", ".bash": "bash",
    ".asm": "asm", ".s": "asm", ".nasm": "asm",
    ".sql": "sql", ".html": "html", ".htm": "html", ".xml": "xml",
    ".json": "json", ".yaml": "yaml", ".yml": "yaml", ".toml": "toml",
    ".ini": "ini", ".cfg": "ini", ".conf": "ini", ".env": "ini",
    ".md": "markdown", ".txt": "text", ".log": "text", ".csv": "text",
    ".dockerfile": "dockerfile", ".makefile": "makefile", ".mk": "makefile",
    ".rules": "text", ".yar": "text", ".yara": "text",
}

# Named without an extension but worth inlining.
BARE_NAMES = {"Dockerfile": "dockerfile", "Makefile": "makefile",
              "README": "markdown", "LICENSE": "text", "requirements": "text"}

# Inlined files are capped: a multi-megabyte capture adds bulk, not knowledge.
MAX_INLINE_BYTES = 200_000

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".idea", ".vscode", "venv", ".venv"}


def classify(path: str) -> str | None:
    name = os.path.basename(path)
    ext = os.path.splitext(name)[1].lower()
    if ext in LANGS:
        return LANGS[ext]
    stem = os.path.splitext(name)[0]
    return BARE_NAMES.get(stem) or BARE_NAMES.get(name)


def parse_workshop(name: str) -> tuple[str, list[str]]:
    """Split a workshop directory name into (title, speakers).

    DEF CON files workshops two ways:
      "… - Wes McGrew - Learning to Reverse Engineer … - Student Resources"
      "… - Eric - Eijah - Anderson-Post - Quantum Cryptography for Hackers"
    The second interleaves the speaker's handle between their names, and
    sometimes welds the surname to the title with a hyphen ("Reddy-Words As
    Weapons …"). Treating every segment before the title as one speaker turns
    the handle into part of the talk's name, so the forms are told apart.
    """
    rest = re.sub(r"^DEF\s*CON\s*\d+\s*-\s*Workshops?\s*-\s*", "", name, flags=re.I)
    parts = [p.strip() for p in rest.split(" - ") if p.strip()]
    # Trailing packaging labels ("Student Resources", "… workshop …").
    while len(parts) > 2 and re.search(r"(student\s+)?resources?$|workshop", parts[-1], re.I):
        parts.pop()

    def strip_label(text: str) -> str:
        return re.sub(r"[-\s]*(student\s+)?resources?$", "", text, flags=re.I).strip()

    # Form B: "<First> - <handle> - <Last>[-<Title>] [- <Title>]"
    if (len(parts) >= 3 and len(parts[0].split()) == 1 and len(parts[1].split()) == 1
            and not parts[1].endswith((".", "!", "?"))):
        third = parts[2]
        surname, title = third, " - ".join(parts[3:])
        if "-" in third:
            head, _, tail = third.partition("-")
            if len(tail) > 15:            # a title, not a hyphenated surname
                surname = head.strip()
                title = " - ".join(x for x in (tail.strip(), title) if x)
        speaker = f"{parts[0]} '{parts[1]}' {surname}".strip()
        if title:
            return strip_label(title), [speaker]

    if len(parts) >= 2:
        return (strip_label(" - ".join(parts[1:])),
                [s.strip() for s in re.split(r",| and ", parts[0]) if s.strip()])
    return strip_label(parts[0] if parts else name), []


def collect(root: str) -> dict[str, list[str]]:
    """Group files by their workshop directory (or by file for loose items)."""
    groups: dict[str, list[str]] = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            parts = rel.split(os.sep)
            key = parts[0] if len(parts) > 1 else os.path.splitext(parts[0])[0]
            groups.setdefault(key, []).append(full)
    return groups


def build(workshop: str, files: list[str], root: str, out_root: str,
          conference: str, year: int | None, do_redact: bool) -> dict | None:
    title, speakers = parse_workshop(workshop)
    inlined, skipped, redactions, total = [], [], 0, 0

    for path in sorted(files):
        rel = os.path.relpath(path, root)
        lang = classify(path)
        try:
            size = os.path.getsize(path)
        except OSError:
            continue
        if lang is None or size > MAX_INLINE_BYTES:
            skipped.append((rel, size, "binary" if lang is None else "too large"))
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        if not text.strip():
            continue
        if do_redact:
            text, n = redact_secrets(text)
            redactions += n
        # A fence inside the file would close ours early.
        fence = "`" * max(3, max((len(m) for m in re.findall(r"`+", text)), default=0) + 1)
        inlined.append(f"### `{rel}`\n\n{fence}{lang}\n{text.rstrip()}\n{fence}\n")
        total += len(text)

    if not inlined:
        return None

    os.makedirs(os.path.join(out_root, f"{conference} workshops"), exist_ok=True)
    out_path = os.path.join(out_root, f"{conference} workshops", slugify(workshop) + ".md")
    digest = hashlib.sha256(workshop.encode()).hexdigest()

    fm = [
        "---",
        f"title: {yaml_escape(title)}",
        f"speakers: {yaml_list(speakers)}",
        f"conference: {yaml_escape('DEF CON' if 'DEF CON' in conference else conference)}",
        f"conference_full: {yaml_escape(conference)}",
        f"year: {year if year else 'null'}",
        "source_type: \"workshop-materials\"",
        f"source_dir: {yaml_escape(workshop)}",
        f"files_included: {len(inlined)}",
        f"files_skipped: {len(skipped)}",
        f"text_chars: {total}",
        f"redacted_secrets: {redactions}",
        f"sha256: {yaml_escape(digest)}",
        f"converted_at: {yaml_escape(_dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if speakers:
        fm.append(f"**Speakers:** {', '.join(speakers)}  ")
    fm.append(f"**Conference:** {conference} (workshop materials)  ")
    fm.append(f"**Contents:** {len(inlined)} readable files inlined below. "
              f"This is the workshop's own source material, not slide text — "
              f"no OCR is involved, so the code is exact.")
    fm.append("")
    if skipped:
        fm.append("## Files not inlined")
        fm.append("")
        fm.append("Binaries and oversized artefacts, listed for completeness:")
        fm.append("")
        for rel, size, why in sorted(skipped)[:80]:
            fm.append(f"- `{rel}` — {size / 1024:.0f} KB ({why})")
        if len(skipped) > 80:
            fm.append(f"- …and {len(skipped) - 80} more")
        fm.append("")
    fm.append("## Materials")
    fm.append("")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(fm) + "\n" + "\n".join(inlined))

    return {"workshop": workshop, "status": "ok", "title": title, "speakers": speakers,
            "conference_full": conference, "year": year,
            "markdown": os.path.relpath(out_path, out_root),
            "files_included": len(inlined), "files_skipped": len(skipped),
            "text_chars": total, "redacted_secrets": redactions,
            "source_type": "workshop-materials"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", default="markdown")
    ap.add_argument("--conference", required=True, help='e.g. "DEF CON 34"')
    ap.add_argument("--year", type=int, default=0)
    ap.add_argument("--redact", action="store_true")
    args = ap.parse_args()

    root = os.path.abspath(args.src)
    # Most drops nest everything under one directory named after the event.
    entries = [e for e in os.listdir(root) if not e.startswith(".")]
    if len(entries) == 1 and os.path.isdir(os.path.join(root, entries[0])):
        root = os.path.join(root, entries[0])

    year = args.year or None
    m = re.search(r"(\d{1,2})", args.conference)
    if not year and "DEF CON" in args.conference.upper() and m:
        year = 1992 + int(m.group(1))

    groups = collect(root)
    print(f"{len(groups)} workshop groups under {root}")
    out_root = os.path.abspath(args.out)
    records = []
    for name, files in sorted(groups.items()):
        rec = build(name, files, root, out_root, args.conference, year, args.redact)
        if rec:
            records.append(rec)
            print(f"  {rec['files_included']:3d} files  {rec['title'][:60]}")

    manifest = os.path.join(out_root, "workshops.jsonl")
    existing = []
    if os.path.exists(manifest):
        with open(manifest, encoding="utf-8") as fh:
            existing = [json.loads(l) for l in fh if l.strip()]
        existing = [r for r in existing if r.get("conference_full") != args.conference]
    with open(manifest, "w", encoding="utf-8") as fh:
        for r in existing + records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"\n{len(records)} workshops written")
    print(f"Files inlined : {sum(r['files_included'] for r in records):,}")
    print(f"Characters    : {sum(r['text_chars'] for r in records):,}")
    print(f"Manifest      : {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
