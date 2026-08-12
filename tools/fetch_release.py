#!/usr/bin/env python3
"""
fetch_release.py — Download and unpack conference material published as a GitHub release.

media.defcon.org is unreachable from some environments (a corporate proxy, a
sandboxed CI runner), and DEF CON's own bundles contain files larger than
GitHub's 100 MB per-file limit. The workaround is to publish the material as a
split 7-Zip archive attached to a release in this repository; this fetches it
back and reassembles it.

Multi-part volumes (`name.7z.001`, `.002`, …) are downloaded in full and only
the first is handed to 7-Zip, which pulls in the rest. Each asset is verified
against the SHA-256 digest GitHub records for it, so a truncated transfer fails
loudly instead of producing a corrupt archive.

Usage:
    python3 tools/fetch_release.py --list
    python3 tools/fetch_release.py --tag defcon-33-presentations --dest "DEF CON 33"
    python3 tools/fetch_release.py --tag defcon-33-transcripts --dest "DEF CON 33 transcripts"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

API = "https://api.github.com/repos/{owner}/{repo}/releases"
UA = "conference-archive-fetch/1.0"


def api_get(url: str) -> object:
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json", "User-Agent": UA})
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token and token != "proxy-injected":
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def download(url: str, dest: str, expect_sha: str | None, retries: int = 4) -> None:
    """Fetch one asset, resuming a partial file and verifying its digest."""
    if os.path.exists(dest) and expect_sha and _sha256(dest) == expect_sha:
        print(f"    have  {os.path.basename(dest)}")
        return
    for attempt in range(retries):
        try:
            if shutil.which("curl"):
                cmd = ["curl", "-fL", "--retry", "3", "--retry-delay", "2",
                       "-A", UA, "-o", dest, url]
                if subprocess.run(cmd).returncode != 0:
                    raise RuntimeError("curl failed")
            else:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=600) as r, open(dest, "wb") as fh:
                    shutil.copyfileobj(r, fh)
            if expect_sha:
                got = _sha256(dest)
                if got != expect_sha:
                    raise RuntimeError(f"digest mismatch: {got[:12]} != {expect_sha[:12]}")
            print(f"    ok    {os.path.basename(dest)} "
                  f"({os.path.getsize(dest) / 1e6:.1f} MB)")
            return
        except Exception as exc:  # noqa: BLE001
            if attempt == retries - 1:
                raise
            print(f"    retry {attempt + 1}: {exc}", file=sys.stderr)


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def extract(first_part: str, dest: str) -> bool:
    exe = shutil.which("7z") or shutil.which("7zz")
    if not exe:
        print("7-Zip not found; install p7zip-full to unpack.", file=sys.stderr)
        return False
    os.makedirs(dest, exist_ok=True)
    proc = subprocess.run([exe, "x", "-y", first_part], cwd=dest,
                          capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stdout[-1500:], file=sys.stderr)
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--owner", default="tech-antidote")
    ap.add_argument("--repo", default="Conferences")
    ap.add_argument("--tag", help="release tag to fetch")
    ap.add_argument("--dest", help="directory to unpack into (default: the tag)")
    ap.add_argument("--work", default="", help="where to keep downloaded parts")
    ap.add_argument("--list", action="store_true", help="list releases and exit")
    ap.add_argument("--keep-parts", action="store_true",
                    help="keep the downloaded archive volumes after unpacking")
    args = ap.parse_args()

    releases = api_get(API.format(owner=args.owner, repo=args.repo) + "?per_page=100")
    if args.list or not args.tag:
        for r in releases:  # type: ignore[union-attr]
            assets = r.get("assets", [])
            total = sum(a["size"] for a in assets)
            ready = all(a["state"] == "uploaded" for a in assets)
            print(f"  {r['tag_name']:32s} {len(assets):3d} assets  {total / 1e9:5.2f} GB"
                  f"  {'ready' if ready else 'INCOMPLETE'}")
        return 0

    rel = next((r for r in releases if r["tag_name"] == args.tag), None)  # type: ignore[union-attr]
    if not rel:
        print(f"No release tagged {args.tag}", file=sys.stderr)
        return 1

    dest = args.dest or args.tag
    work = args.work or os.path.join(dest, "_parts")
    os.makedirs(work, exist_ok=True)

    assets = sorted(rel["assets"], key=lambda a: a["name"])
    print(f"{args.tag}: {len(assets)} assets, "
          f"{sum(a['size'] for a in assets) / 1e9:.2f} GB")
    for a in assets:
        digest = (a.get("digest") or "").replace("sha256:", "") or None
        download(a["browser_download_url"], os.path.join(work, a["name"]), digest)

    # Hand 7-Zip only the first volume of each archive; it finds the rest.
    firsts = [a["name"] for a in assets
              if a["name"].endswith(".001") or
              (a["name"].endswith((".7z", ".zip", ".rar")) and ".7z." not in a["name"])]
    if not firsts:
        print(f"No archive volumes found; assets left in {work}")
        return 0

    ok = True
    for name in firsts:
        print(f"  extracting {name} ...")
        if not extract(os.path.abspath(os.path.join(work, name)), dest):
            ok = False
    if ok and not args.keep_parts:
        shutil.rmtree(work, ignore_errors=True)

    n = sum(len(f) for _, _, f in os.walk(dest))
    print(f"\n{dest}: {n} files unpacked")
    print(f"Next:\n  python3 tools/pdf2md.py --src {dest!r} --out markdown")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
