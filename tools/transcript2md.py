#!/usr/bin/env python3
"""
transcript2md.py — Convert talk transcripts into Markdown for LLM ingestion.

Transcripts are the other half of a conference archive, and in some ways the
better half: slides carry the diagrams, but the transcript carries the argument
that the speaker actually made. Where a deck gives 169 characters a page, a
45-minute talk gives tens of thousands of words of continuous technical prose,
with no OCR anywhere in the pipeline -- so unlike slide text, none of it is a
guess.

The input is Whisper-style output: one line per segment, each stamped with a
time range. Fed to a model verbatim that is nearly unusable -- the timestamps
outnumber the sentences and shred every paragraph into fragments. So this:

  - drops the per-segment stamps and reflows the text into paragraphs
  - keeps a coarse `## [MM:SS]` heading every few minutes, which both anchors a
    quote back to the recording and gives a chunker real split points
  - de-duplicates the consecutive repeated lines that speech recognition
    produces when a speaker pauses mid-sentence

Usage:
    python3 tools/transcript2md.py --src "DEF CON 33 transcripts" --out markdown --conference "DEF CON 33"
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

# "[00:12.345 --> 00:15.678]  spoken text"
SEG_RE = re.compile(r"^\[(\d+):(\d+(?:\.\d+)?)\s*-->\s*(\d+):(\d+(?:\.\d+)?)\]\s*(.*)$")

# A new heading roughly every this many seconds of talk time.
ANCHOR_SECONDS = 180

# Filenames read "DEF CON 33 - <Title> - <Speakers>": speakers last, which is
# the reverse of the slide archive's convention.
NAME_RE = re.compile(r"^DEF\s*CON\s*(\d+)\s*-\s*(.+)$", re.I)


def parse_name(stem: str) -> tuple[str, list[str], str]:
    """Return (title, speakers, edition)."""
    stem = re.sub(r"\.eng$", "", stem, flags=re.I)
    edition = ""
    m = NAME_RE.match(stem)
    rest = stem
    if m:
        edition, rest = m.group(1), m.group(2)
    if " - " in rest:
        title, _, speaker_part = rest.rpartition(" - ")
    else:
        title, speaker_part = rest, ""
    speakers = [s.strip() for s in speaker_part.split(",") if s.strip()]
    return title.strip() or stem, speakers, edition


def read_segments(path: str) -> list[tuple[float, str]]:
    """Parse a transcript into (start seconds, text) pairs."""
    out: list[tuple[float, str]] = []
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            m = SEG_RE.match(line.rstrip("\n"))
            if not m:
                continue
            start = int(m.group(1)) * 60 + float(m.group(2))
            text = m.group(5).strip()
            if text:
                out.append((start, text))
    return out


def build_body(segments: list[tuple[float, str]]) -> tuple[str, int]:
    """Reflow segments into anchored paragraphs. Returns (markdown, duration)."""
    parts: list[str] = []
    buf: list[str] = []
    last_anchor = -ANCHOR_SECONDS
    prev = ""

    def flush() -> None:
        if buf:
            parts.append(" ".join(buf).strip())
            buf.clear()

    for start, text in segments:
        # Speech recognition repeats a line when a speaker pauses mid-sentence.
        if text == prev:
            continue
        prev = text
        if start - last_anchor >= ANCHOR_SECONDS:
            flush()
            mm, ss = divmod(int(start), 60)
            parts.append(f"\n## [{mm:02d}:{ss:02d}]\n")
            last_anchor = start
        buf.append(text)
        # Keep paragraphs readable rather than one wall per anchor.
        if len(" ".join(buf)) > 900 and text.endswith((".", "?", "!")):
            flush()
    flush()
    duration = int(segments[-1][0]) if segments else 0
    return "\n\n".join(p for p in parts if p.strip()), duration


def convert(path: str, out_root: str, conference: str, edition_year: dict,
            do_redact: bool) -> dict | None:
    stem = os.path.splitext(os.path.basename(path))[0]
    # ".eng.txt" loses only one extension to splitext; drop the language tag too
    # so it does not end up welded onto the slug.
    stem = re.sub(r"\.(eng|en)$", "", stem, flags=re.I)
    title, speakers, edition = parse_name(stem)
    segments = read_segments(path)
    if not segments:
        return {"source": os.path.basename(path), "status": "empty"}

    body, duration = build_body(segments)
    redactions = 0
    if do_redact:
        body, redactions = redact_secrets(body)

    conf_name = conference or (f"DEF CON {edition}" if edition else "Unknown")
    year = edition_year.get(edition) or (1992 + int(edition) if edition.isdigit() else None)

    words = len(body.split())
    out_dir = os.path.join(out_root, conf_name + " transcripts")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, slugify(stem) + ".md")

    with open(path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()

    fm = [
        "---",
        f"title: {yaml_escape(title)}",
        f"speakers: {yaml_list(speakers)}",
        f"conference: {yaml_escape('DEF CON' if 'DEF CON' in conf_name else conf_name)}",
        f"conference_full: {yaml_escape(conf_name)}",
        f"edition: {yaml_escape(edition)}",
        f"year: {year if year else 'null'}",
        "source_type: \"transcript\"",
        f"source_transcript: {yaml_escape(os.path.basename(path))}",
        f"sha256: {yaml_escape(digest)}",
        f"duration_seconds: {duration}",
        f"words: {words}",
        f"text_chars: {len(body)}",
        f"redacted_secrets: {redactions}",
        f"converted_at: {yaml_escape(_dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if speakers:
        fm.append(f"**Speakers:** {', '.join(speakers)}  ")
    fm.append(f"**Conference:** {conf_name}  ")
    fm.append(f"**Source:** automatic speech-recognition transcript "
              f"({duration // 60} min, {words:,} words). Wording follows the "
              f"recording and may contain recognition errors; timestamps anchor "
              f"each section back to the video.")
    fm.append("")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(fm) + "\n" + body + "\n")

    return {"source": os.path.basename(path), "status": "ok", "title": title,
            "speakers": speakers, "conference_full": conf_name, "year": year,
            "markdown": os.path.relpath(out_path, out_root), "words": words,
            "duration_seconds": duration, "text_chars": len(body),
            "sha256": digest, "source_type": "transcript"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="directory of transcript files")
    ap.add_argument("--out", default="markdown", help="Markdown output root")
    ap.add_argument("--conference", default="", help='e.g. "DEF CON 33"')
    ap.add_argument("--pattern", default=".eng.txt",
                    help="transcript filename suffix to convert (default .eng.txt)")
    ap.add_argument("--redact", action="store_true", help="mask credential-shaped strings")
    ap.add_argument("--manifest", default="", help="default <out>/transcripts.jsonl")
    args = ap.parse_args()

    files = []
    for dirpath, dirnames, filenames in os.walk(args.src):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        files += [os.path.join(dirpath, f) for f in filenames if f.endswith(args.pattern)]
    files.sort()
    if not files:
        print(f"No files ending {args.pattern} under {args.src}", file=sys.stderr)
        return 1

    out_root = os.path.abspath(args.out)
    os.makedirs(out_root, exist_ok=True)
    print(f"Converting {len(files)} transcripts -> {out_root}")

    records = []
    for i, f in enumerate(files, 1):
        rec = convert(f, out_root, args.conference, {}, args.redact)
        if rec:
            records.append(rec)
        if i % 20 == 0 or i == len(files):
            print(f"  [{i}/{len(files)}]", flush=True)

    manifest = args.manifest or os.path.join(out_root, "transcripts.jsonl")
    with open(manifest, "w", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    ok = [r for r in records if r["status"] == "ok"]
    print(f"\nConverted {len(ok)}/{len(files)} transcripts")
    print(f"Words   : {sum(r['words'] for r in ok):,}")
    print(f"Chars   : {sum(r['text_chars'] for r in ok):,}")
    print(f"Runtime : {sum(r['duration_seconds'] for r in ok) // 3600} hours of talks")
    print(f"Manifest: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
