#!/usr/bin/env python3
"""
fetch_defcon.py — Mirror DEF CON presentation materials from the DEF CON media server.

Two acquisition strategies, tried in order by default:

  1. ARCHIVE  -- grab the single `DEF CON NN presentations.rar` bundle and unpack
     it. One request, one file, no rate-limit risk. Needs `7z` (p7zip >= 16 or
     7-Zip 23+, both of which read RAR5 natively) or `unar`/`unrar`.

  2. SCRAPE   -- walk the Apache directory index recursively and pull every
     document individually. Slower and chattier, but it works when the .rar is
     missing, truncated, or when you only want part of the tree. Resumable:
     already-downloaded files are skipped by size.

The media server is plain HTTP/HTTPS with autoindex pages, so the scrape needs
nothing beyond the standard library.

Typical use:

    python3 tools/fetch_defcon.py --year 34 --dest "DEF CON 34"
    python3 tools/pdf2md.py --src "DEF CON 34" --out markdown

Then commit the Markdown. `--dry-run` lists what would be fetched without
downloading, which is the fastest way to confirm the remote layout.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ.get("DEFCON_MEDIA_BASE", "https://media.defcon.org").rstrip("/")
UA = "Mozilla/5.0 (compatible; conference-archive-mirror/1.0)"

# Extensions worth mirroring. Slides are the point, but DEF CON ships whitepapers,
# demo code and extra handouts in the same folders and they are all useful context.
WANTED_EXT = {".pdf", ".txt", ".md", ".zip", ".tar.gz", ".tgz", ".py", ".c",
              ".ps1", ".sh", ".json", ".yaml", ".yml", ".docx", ".pptx"}

# Apache autoindex sort links and parent nav -- never follow these.
SKIP_HREF = re.compile(r"^(\?|/|#|mailto:)")

HREF_RE = re.compile(r'<a\s+[^>]*href="([^"]+)"', re.I)


def fetch(url: str, retries: int = 4, timeout: int = 60) -> bytes:
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001 - retry everything transient
            last = exc
            if attempt < retries - 1:
                wait = 2 ** attempt
                print(f"    retry {attempt + 1}/{retries - 1} in {wait}s ({exc})",
                      file=sys.stderr, flush=True)
                time.sleep(wait)
    raise RuntimeError(f"GET {url} failed after {retries} attempts: {last}")


def list_dir(url: str) -> tuple[list[str], list[str]]:
    """Return (subdirectory URLs, file URLs) from an Apache autoindex page."""
    body = fetch(url).decode("utf-8", "replace")
    dirs, files = [], []
    for raw in HREF_RE.findall(body):
        href = html.unescape(raw)
        if SKIP_HREF.match(href) or href in ("../", "./"):
            continue
        full = urllib.parse.urljoin(url, href)
        if not full.startswith(url):       # never climb out of the subtree
            continue
        (dirs if href.endswith("/") else files).append(full)
    return dirs, files


def walk(url: str, depth: int = 0, max_depth: int = 8) -> list[str]:
    """Depth-first walk of the autoindex, returning every file URL found."""
    if depth > max_depth:
        return []
    indent = "  " * depth
    try:
        dirs, files = list_dir(url)
    except Exception as exc:  # noqa: BLE001
        print(f"{indent}! cannot list {url}: {exc}", file=sys.stderr)
        return []
    keep = [f for f in files
            if os.path.splitext(urllib.parse.unquote(f))[1].lower() in WANTED_EXT]
    print(f"{indent}{urllib.parse.unquote(url.rstrip('/').split('/')[-1])}/  "
          f"({len(keep)} files, {len(dirs)} subdirs)", flush=True)
    out = list(keep)
    for d in dirs:
        out.extend(walk(d, depth + 1, max_depth))
    return out


def download(url: str, dest_root: str, base_url: str, dry_run: bool = False) -> bool:
    rel = urllib.parse.unquote(url[len(base_url):]).lstrip("/")
    dest = os.path.join(dest_root, rel)
    if dry_run:
        print(f"  would fetch {rel}")
        return True

    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    # Resume support: trust an existing file whose size matches the server's.
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
        with urllib.request.urlopen(req, timeout=30) as resp:
            remote_size = int(resp.headers.get("Content-Length") or 0)
    except Exception:  # noqa: BLE001
        remote_size = 0
    if os.path.exists(dest) and remote_size and os.path.getsize(dest) == remote_size:
        return True

    try:
        data = fetch(url)
    except Exception as exc:  # noqa: BLE001
        print(f"  FAILED {rel}: {exc}", file=sys.stderr)
        return False
    tmp = dest + ".part"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, dest)
    print(f"  {len(data) / 1e6:8.2f} MB  {rel}", flush=True)
    return True


# ---------------------------------------------------------------------------
# Archive strategy
# ---------------------------------------------------------------------------

def extractor_for_rar() -> list[str] | None:
    if shutil.which("7z"):
        return ["7z", "x", "-y"]
    if shutil.which("7zz"):
        return ["7zz", "x", "-y"]
    if shutil.which("unar"):
        return ["unar", "-f"]
    if shutil.which("unrar"):
        return ["unrar", "x", "-o+"]
    return None


def try_archive(year: int, dest: str, dry_run: bool) -> bool:
    url = f"{BASE}/DEF%20CON%20{year}/DEF%20CON%20{year}%20presentations.rar"
    print(f"[archive] {urllib.parse.unquote(url)}")
    tool = extractor_for_rar()
    if not tool:
        print("[archive] no RAR extractor found (install p7zip-full / 7zip / unar); "
              "falling back to scrape.", file=sys.stderr)
        return False
    if dry_run:
        print("  (dry run) would download and extract the bundle")
        return True

    os.makedirs(dest, exist_ok=True)
    rar_path = os.path.join(dest, f"DEF CON {year} presentations.rar")
    try:
        # curl streams to disk and resumes a partial transfer; the bundle is large.
        if shutil.which("curl"):
            cmd = ["curl", "-fL", "--retry", "4", "--retry-delay", "2",
                   "-C", "-", "-A", UA, "-o", rar_path, url]
            if subprocess.run(cmd).returncode != 0:
                raise RuntimeError("curl failed")
        else:
            data = fetch(url, timeout=600)
            with open(rar_path, "wb") as fh:
                fh.write(data)
    except Exception as exc:  # noqa: BLE001
        print(f"[archive] download failed: {exc}", file=sys.stderr)
        return False

    print(f"[archive] extracting {rar_path} ...")
    # cwd=dest keeps every extractor writing into the destination tree, so no
    # tool-specific output-directory flag is needed.
    proc = subprocess.run(tool + [os.path.abspath(rar_path)], cwd=dest)
    if proc.returncode != 0:
        print("[archive] extraction failed; falling back to scrape.", file=sys.stderr)
        return False
    os.remove(rar_path)
    return True


# ---------------------------------------------------------------------------
# Scrape strategy
# ---------------------------------------------------------------------------

def try_scrape(year: int, dest: str, dry_run: bool) -> bool:
    # The media server has used both a flat and a doubled path layout across years.
    candidates = [
        f"{BASE}/DEF%20CON%20{year}/DEF%20CON%20{year}%20presentations/",
        f"{BASE}/DEF%20CON%20{year}/DEF%20CON%20{year}%20presentations/"
        f"DEF%20CON%20{year}%20presentations/",
        f"{BASE}/DEF%20CON%20{year}/",
    ]
    base_url = None
    for cand in candidates:
        try:
            dirs, files = list_dir(cand)
        except Exception:  # noqa: BLE001
            continue
        if dirs or files:
            base_url = cand
            print(f"[scrape] root: {urllib.parse.unquote(cand)}")
            break
    if not base_url:
        print(f"[scrape] no reachable index for DEF CON {year}", file=sys.stderr)
        return False

    urls = walk(base_url)
    print(f"[scrape] {len(urls)} files to fetch")
    if not urls:
        return False

    ok = 0
    for i, u in enumerate(urls, 1):
        if i % 25 == 0:
            print(f"  ... {i}/{len(urls)}", flush=True)
        if download(u, dest, base_url, dry_run):
            ok += 1
    print(f"[scrape] {ok}/{len(urls)} files retrieved into {dest}")
    return ok > 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--year", type=int, default=34, help="DEF CON number (default 34)")
    ap.add_argument("--dest", default="", help="destination dir (default 'DEF CON <year>')")
    ap.add_argument("--mode", choices=("auto", "archive", "scrape"), default="auto",
                    help="acquisition strategy (default: archive, then scrape)")
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be fetched without downloading")
    args = ap.parse_args()

    dest = args.dest or f"DEF CON {args.year}"

    if args.mode in ("auto", "archive"):
        if try_archive(args.year, dest, args.dry_run):
            print(f"\nDone. Now run:\n  python3 tools/pdf2md.py "
                  f"--src {dest!r} --out markdown")
            return 0
        if args.mode == "archive":
            return 1

    if try_scrape(args.year, dest, args.dry_run):
        print(f"\nDone. Now run:\n  python3 tools/pdf2md.py --src {dest!r} --out markdown")
        return 0

    print("\nCould not retrieve anything. If you are behind an egress proxy, confirm "
          "media.defcon.org is reachable:\n  curl -sSI https://media.defcon.org/",
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
