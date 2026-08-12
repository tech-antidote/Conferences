#!/usr/bin/env python3
"""
redact_corpus.py — Sweep already-converted Markdown for credential-shaped strings.

`pdf2md.py` redacts as it converts, but a corpus produced before that existed --
or one assembled from another source -- still carries whatever the slides showed.
This applies the same patterns to files on disk.

Security conference decks routinely display credentials: demo AWS keys, a token
in a screenshotted terminal, a private key in an exploit walkthrough. Inside a
PDF those strings are invisible to scanners; converted to Markdown they become
plain text that GitHub push protection will reject, and that republishes any
credential which was not in fact a throwaway.

Usage:
    python3 tools/redact_corpus.py --out markdown            # redact in place
    python3 tools/redact_corpus.py --out markdown --dry-run  # report only
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf2md import redact_secrets  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown", help="Markdown corpus directory")
    ap.add_argument("--dry-run", action="store_true", help="report without editing")
    args = ap.parse_args()

    root = os.path.abspath(args.out)
    if not os.path.isdir(root):
        print(f"No such directory: {root}", file=sys.stderr)
        return 1

    scanned = changed = total = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            scanned += 1
            try:
                with open(path, "r", encoding="utf-8") as fh:
                    original = fh.read()
            except OSError as exc:
                print(f"  skip {path}: {exc}", file=sys.stderr)
                continue

            redacted, n = redact_secrets(original)
            if not n:
                continue
            changed += 1
            total += n
            print(f"  {n:3d}  {os.path.relpath(path, root)}")
            if not args.dry_run:
                # Keep the frontmatter counter honest for anything already recorded.
                if "\nredacted_secrets:" in redacted:
                    import re
                    redacted = re.sub(r"(?m)^redacted_secrets: \d+$",
                                      f"redacted_secrets: {n}", redacted, count=1)
                elif redacted.startswith("---\n"):
                    end = redacted.find("\n---\n", 4)
                    if end != -1:
                        redacted = (redacted[:end] + f"\nredacted_secrets: {n}"
                                    + redacted[end:])
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(redacted)

    verb = "would redact" if args.dry_run else "redacted"
    print(f"\nScanned {scanned} files; {verb} {total} secret(s) across {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
