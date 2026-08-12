#!/usr/bin/env python3
"""
test_fetch_defcon.py — Exercise the DEF CON scraper against a local stand-in server.

media.defcon.org is frequently unreachable from CI and from locked-down
environments, and "the script looks right" is not evidence that it works. This
test builds a directory tree shaped like the real media server, serves it with
`http.server` (which emits the same style of autoindex HTML as the real host),
points the scraper at it, and asserts on what actually landed on disk.

Covers the parts that genuinely break in the field: percent-encoded spaces in
DEF CON's path names, recursive descent into per-talk subdirectories, extension
filtering, not following parent/sort links back up the tree, and resume.

Run:
    python3 tools/test_fetch_defcon.py
"""

from __future__ import annotations

import functools
import http.server
import os
import shutil
import socketserver
import sys
import tempfile
import threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TREE = {
    "DEF CON 34/DEF CON 34 presentations/index-marker.txt": "root marker",
    "DEF CON 34/DEF CON 34 presentations/Some Speaker - A Talk With Spaces/"
    "DEFCON-34-Some-Speaker-A-Talk.pdf": "%PDF-1.4 fake slide deck",
    "DEF CON 34/DEF CON 34 presentations/Some Speaker - A Talk With Spaces/"
    "DEFCON-34-Some-Speaker-notes.txt": "companion notes",
    "DEF CON 34/DEF CON 34 presentations/Another Speaker/"
    "DEFCON-34-Another-Speaker-Whitepaper.pdf": "%PDF-1.4 whitepaper",
    "DEF CON 34/DEF CON 34 presentations/Another Speaker/demo.zip": "PK fake archive",
    # Must be ignored: not an extension we mirror.
    "DEF CON 34/DEF CON 34 presentations/Another Speaker/thumbnail.jpg": "JPEGDATA",
    # Must never be fetched: lives outside the presentations subtree.
    "DEF CON 34/DEF CON 34 villages/should-not-fetch.pdf": "%PDF outside subtree",
}


def build_tree(root: str) -> None:
    for rel, body in TREE.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):  # silence per-request logging
        pass


def serve(root: str):
    handler = functools.partial(QuietHandler, directory=root)
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd, httpd.server_address[1]


def main() -> int:
    src = tempfile.mkdtemp(prefix="defcon-src-")
    dest = tempfile.mkdtemp(prefix="defcon-dest-")
    failures: list[str] = []
    try:
        build_tree(src)
        httpd, port = serve(src)
        os.environ["DEFCON_MEDIA_BASE"] = f"http://127.0.0.1:{port}"

        # Import after the env var is set so BASE picks it up.
        import fetch_defcon
        fetch_defcon.BASE = f"http://127.0.0.1:{port}"

        print(f"serving {src} on port {port}")
        ok = fetch_defcon.try_scrape(34, dest, dry_run=False)
        httpd.shutdown()

        def check(cond: bool, msg: str) -> None:
            print(("  PASS  " if cond else "  FAIL  ") + msg)
            if not cond:
                failures.append(msg)

        print("\nassertions:")
        check(ok, "scrape reported success")

        got = set()
        for dp, _, fns in os.walk(dest):
            for fn in fns:
                got.add(os.path.relpath(os.path.join(dp, fn), dest).replace(os.sep, "/"))

        check("Some Speaker - A Talk With Spaces/DEFCON-34-Some-Speaker-A-Talk.pdf" in got,
              "descends into a subdirectory whose name contains spaces")
        check("Some Speaker - A Talk With Spaces/DEFCON-34-Some-Speaker-notes.txt" in got,
              "mirrors companion .txt files alongside slides")
        check("Another Speaker/DEFCON-34-Another-Speaker-Whitepaper.pdf" in got,
              "mirrors a second talk directory")
        check("Another Speaker/demo.zip" in got, "mirrors demo archives")
        check("index-marker.txt" in got, "mirrors files at the presentations root")
        check(not any(g.endswith(".jpg") for g in got),
              "filters out extensions outside WANTED_EXT (.jpg)")
        check(not any("village" in g.lower() or "should-not-fetch" in g for g in got),
              "never climbs out of the presentations subtree")
        check(not any(g.endswith(".part") for g in got),
              "leaves no .part temp files behind")

        target = os.path.join(dest, "Some Speaker - A Talk With Spaces",
                              "DEFCON-34-Some-Speaker-A-Talk.pdf")
        with open(target, encoding="utf-8") as fh:
            check(fh.read() == "%PDF-1.4 fake slide deck", "file contents arrive intact")

        # Resume: a second run must not re-download or corrupt existing files.
        httpd2, port2 = serve(src)
        fetch_defcon.BASE = f"http://127.0.0.1:{port2}"
        before = os.path.getmtime(target)
        fetch_defcon.try_scrape(34, dest, dry_run=False)
        httpd2.shutdown()
        check(os.path.getmtime(target) == before,
              "resume run skips files already present at the right size")

        print()
        if failures:
            print(f"{len(failures)} assertion(s) FAILED")
            return 1
        print("all assertions passed")
        return 0
    finally:
        shutil.rmtree(src, ignore_errors=True)
        shutil.rmtree(dest, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
