#!/usr/bin/env python3
"""Audit the accuracy -- not the completeness -- of corpus metadata.

`pdf2md.py` derives title/speakers from the source *filename*, and the archive
mixes four naming conventions:

  a) "<Speakers>_<Title>.pdf"                speakers joined by " & " or ", "
  b) "<Speakers>-<Title>.pdf"                plain hyphen instead of underscore
  c) "AS-23-Surname-Title-Words[-wp].pdf"    Black Hat's own archive naming
  d) "DEF CON 34 - Speakers - Title - var"   trailing variant marker

Convention (b) is the dangerous one: hyphens also live inside names
("Ahmad-Reza Sadeghi") and inside title words ("AitM-Powered", "In-Depth"), so a
split can land mid-title and hand a chunk of the title to `speakers`. This script
looks for the resulting damage rather than for missing fields.

Checks
  speakers    entries that cannot be personal names (title fragments, prose,
              absurd length, bare lowercase words)
  titles      leftover version/document markers ("-wp", "v2 Pro", "(2)"),
              speaker names, file-extension debris, truncation
  conference  conference / edition / year / conference_full vs. the folder name,
              plus the "AS-23-" style year+region prefix inside Black Hat
              filenames as an independent witness
  content     title plausibility against the first slides of the markdown body
  duplicates  distinct decks that are really the same talk

Nothing is rewritten; every finding is advisory.

Usage:
    python3 tools/audit_metadata.py --out markdown
    python3 tools/audit_metadata.py --out markdown --checks content --sample 60
    python3 tools/audit_metadata.py --out markdown --json report.json
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict

ALL_CHECKS = ("speakers", "titles", "conference", "content", "duplicates")

# --------------------------------------------------------------------------
# Frontmatter loading
# --------------------------------------------------------------------------

FM_LIST_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
FM_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def _scalar(raw: str):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        return [m.group(1).replace('\\"', '"') for m in FM_LIST_RE.finditer(raw)]
    if len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"':
        return raw[1:-1].replace('\\"', '"')
    if raw in ("null", "~", ""):
        return None
    if raw in ("true", "false"):
        return raw == "true"
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


def load_markdown(path: str) -> dict | None:
    """Parse one converted deck. None when the file is absent or mid-write.

    A reconversion may be writing into the tree while the audit runs, so a
    truncated or half-flushed file is expected noise, not a metadata defect.
    """
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    rec: dict = {}
    for line in text[4:end].split("\n"):
        m = FM_KEY_RE.match(line)
        if m:
            rec[m.group(1)] = _scalar(m.group(2))
    if "title" not in rec or "source_pdf" not in rec:
        return None
    rec["_body"] = text[end + 4:]
    rec["_path"] = path
    return rec


def collect(out_dir: str) -> tuple[list[dict], list[str], dict[str, list[str]]]:
    """Return (records, unreadable_paths, source_pdf -> [markdown paths]).

    Records are deduplicated on `source_pdf`: a reconversion in flight writes a
    "<slug>-2.md" beside the file it is replacing, and both describe one deck.
    The newest `converted_at` wins so the audit judges current output.
    """
    found: list[dict] = []
    unreadable: list[str] = []
    for dirpath, _dirs, files in os.walk(out_dir):
        for name in sorted(files):
            if not name.endswith(".md") or name in ("INDEX.md", "README.md"):
                continue
            path = os.path.join(dirpath, name)
            rec = load_markdown(path)
            if rec is None:
                unreadable.append(path)
            else:
                found.append(rec)
    by_source: dict[str, list[dict]] = defaultdict(list)
    for rec in found:
        by_source[rec.get("source_pdf") or rec["_path"]].append(rec)
    records = []
    for src, group in by_source.items():
        group.sort(key=lambda r: r.get("converted_at") or "", reverse=True)
        records.append(group[0])
    records.sort(key=lambda r: r.get("source_pdf") or "")
    shadowed = {src: sorted(r["_path"] for r in g)
                for src, g in by_source.items() if len(g) > 1}
    return records, unreadable, shadowed


# --------------------------------------------------------------------------
# Check 1 -- speakers that are not names
# --------------------------------------------------------------------------

# Function words. A personal name may legitimately be "Or Yair", "Hang An" or
# "A Ben", so a stopword alone never condemns an entry -- it only counts when the
# entry is also too long to be a name.
STOPWORDS = set("""
a an the and or of for to in on at by with from via as is are was were be been
being how why what when where which that this these those it its your our their
my his her not no all more most new using use over under after before out up
down about across against between during than then there here into onto
""".split())

# Words that begin the right-hand half of a wrongly split compound. When a title
# fragment lands in `speakers`, the *title* usually starts with one of these.
COMPOUND_TAILS = set("""
based powered driven aware only level party grade free depth isolation platform
trained oriented side chain time world source code layer facing bit core end
scale defined enabled assisted related specific style like man middle
""".split())


# Words describing the session, not the person.
SESSION_WORDS = {"keynote", "workshop", "panel", "talk", "briefing", "training",
                 "demo", "arsenal", "tutorial"}


def _tokens(text: str) -> list[str]:
    return [t.strip(".,:;()[]'\"") for t in text.split() if t.strip(".,:;()[]'\"")]


def speaker_defects(rec: dict) -> list[dict]:
    """Flag `speakers` entries that cannot be a person."""
    out = []
    for entry in rec.get("speakers") or []:
        words = _tokens(entry)
        lowered = [w.lower() for w in words]
        reasons = []
        # A name is short. Anything past five words is prose.
        if len(words) > 5:
            reasons.append(f"{len(words)} words -- too long for a name")
        if len(entry) > 45:
            reasons.append(f"{len(entry)} characters -- too long for a name")
        # Function words only matter once the entry is already multi-word prose;
        # "Or Yair" and "Hang An" must survive.
        hits = [w for w in lowered if w in STOPWORDS]
        if hits and len(words) > 3:
            reasons.append("contains function words: " + ", ".join(sorted(set(hits))))
        if re.search(r"\.(pdf|pptx|ppt|key|docx|zip)$", entry, re.I):
            reasons.append("file-extension debris")
        # A hyphen glued to a capitalised run is the signature of a split that
        # landed inside the title ("Or Yair-Magicdot" style), but only when the
        # entry is longer than a name.
        if re.search(r"\S-\S", entry) and len(words) > 3:
            reasons.append("hyphen-joined title fragment")
        # "Solar Designer-Keynote": a session-kind word glued to a real name.
        for piece in re.split(r"[-_]", entry):
            if piece.strip().lower() in SESSION_WORDS:
                reasons.append(f"session-kind word {piece.strip()!r} glued to "
                               "the name")
        if len(words) == 1 and entry.islower() and entry.isalpha() and len(entry) > 14:
            reasons.append("single lowercase word, too long for a handle")
        if reasons:
            out.append({"speaker": entry, "reasons": reasons,
                        "source_pdf": rec.get("source_pdf"),
                        "title": rec.get("title")})
    if not (rec.get("speakers") or []):
        out.append({"speaker": "", "reasons": ["no speakers parsed"],
                    "source_pdf": rec.get("source_pdf"),
                    "title": rec.get("title")})
    return out


def orphan_title_head(rec: dict) -> dict | None:
    """Catch the mirror image: a real name kept, but the title decapitated.

    "MoustachedBouncer AitM-Powered Surveillance via Belarus ISPs" splits at the
    hyphen inside "AitM-Powered", so `speakers` looks name-shaped while `title`
    begins with the orphaned tail "Powered ...".
    """
    # Only the hyphen convention can split inside a word. An underscore or a
    # DEF CON " - " filename that happens to start its title with "Core" or
    # "Time" is not evidence of anything.
    stem = os.path.splitext(os.path.basename(rec.get("source_pdf") or ""))[0]
    if "_" in stem or BH_PREFIX_RE.match(stem) or rec.get("conference") == "DEF CON":
        return None
    title = rec.get("title") or ""
    first = _tokens(title)[:1]
    if not first:
        return None
    if first[0].lower() in COMPOUND_TAILS:
        return {"source_pdf": rec.get("source_pdf"), "title": title,
                "speakers": rec.get("speakers"),
                "reason": f"title starts with compound tail {first[0]!r} -- "
                          "the filename was split inside a hyphenated word"}
    return None


def speakers_leaked_into_title(rec: dict) -> dict | None:
    """A speaker separator recurring after the split point means names were lost.

    "<Speakers>_<Title>" splits on the first underscore. When the speaker list
    itself is separated by " _ ", only the first name is captured and the rest
    are carried into the title.
    """
    stem = os.path.splitext(os.path.basename(rec.get("source_pdf") or ""))[0]
    if "_" not in stem:
        return None
    tail = stem.split("_", 1)[1]
    if not re.search(r"\s_", tail):
        return None
    # "..., IoT, _Compressed" is a document marker, not a second speaker.
    rest = [s.strip() for s in re.split(r"\s_", tail)[1:]]
    if all(s.split()[0].lower().strip("_") in KNOWN_DOC_WORDS
           for s in rest if s.split()):
        return None
    return {"source_pdf": rec.get("source_pdf"), "title": rec.get("title"),
            "speakers": rec.get("speakers"),
            "reason": "the filename uses ' _ ' as its speaker separator, so "
                      "only the first name was captured and the remaining "
                      "speakers were left at the front of the title"}


# --------------------------------------------------------------------------
# Check 2 -- titles carrying markers that belong to the file, not the talk
# --------------------------------------------------------------------------

DOC_MARKER = r"wp|whitepaper|white\s?paper|paper|slides?|deck|compressed|updated|draft"
# A version marker only counts when a separator introduces it, so that "in V8"
# and "the V8 Heap Sandbox" -- V8 being a JavaScript engine, not a revision --
# stay out of the results.
VERSION_MARKER = r"v\d+(?:[. ]\d+)*(?:\s+\w+)?"

TITLE_MARKER_RES = [
    ("document-kind suffix", re.compile(rf"[-_]({DOC_MARKER})$", re.I)),
    ("version marker", re.compile(rf"[-_(]({VERSION_MARKER})\)?$", re.I)),
    ("duplicate-copy suffix", re.compile(r"\(\s*\d+\s*\)\s*$")),
    ("file-extension debris", re.compile(r"\.(pdf|pptx|ppt|key|docx|zip)\b", re.I)),
    ("underscore debris", re.compile(r"_")),
    # A venue name or a build date in the title is filename bookkeeping that the
    # variant-stripper failed to recognise ("... - 2026 08 05 DEF CON").
    ("venue/date marker",
     re.compile(r"\b(DEF\s*CON|Black\s*Hat|BlackHat|BHASIA|Hexacon|"
                r"OffensiveCon)\b|\b20\d{2}[ ._-]\d{2}[ ._-]\d{2}\b")),
]

BARE_MARKER_RE = re.compile(rf"^(?:{DOC_MARKER}|{VERSION_MARKER})$", re.I)

# Archives truncate long filenames, and the title inherits the cut. DEF CON's
# media server caps the stem far shorter than Black Hat's does.
LENGTH_CAP = {"DEF CON": 149}
DEFAULT_LENGTH_CAP = 200


def title_defects(rec: dict) -> list[dict]:
    title = (rec.get("title") or "").strip()
    base = os.path.basename(rec.get("source_pdf") or "")
    stem = os.path.splitext(base)[0]
    found = []
    if BARE_MARKER_RE.match(title):
        found.append(f"title is nothing but a file marker ({title!r})")
    for label, rx in TITLE_MARKER_RES:
        m = rx.search(title)
        if m:
            found.append(f"{label}: {m.group(0).strip()!r}")
    # Speaker names must not survive into the title.
    for sp in rec.get("speakers") or []:
        if len(sp) > 4 and sp.lower() in title.lower():
            found.append(f"contains speaker name {sp!r}")
    found.extend(_underscore_hints(stem))
    found.extend(_truncation_hints(title, stem, base,
                                   rec.get("conference") or ""))
    if not found:
        return []
    return [{"source_pdf": rec.get("source_pdf"), "title": title,
             "reasons": found}]


KNOWN_DOC_WORDS = {"wp", "whitepaper", "paper", "slides", "slide", "compressed",
                   "updated", "deck", "draft"}


def _underscore_hints(stem: str) -> list[str]:
    """Underscores past the first one are lost information.

    "<Speakers>_<Title>" splits on the *first* underscore only; every later one
    is flattened into a space. That silently rewrites "Bad io_uring" as
    "Bad io uring", turns the emoticon "(0_o)" into "(0 o)", leaves unrecognised
    document markers ("_workshop", "_Article") glued to the title, and -- when a
    speaker list itself uses " _ " as its separator -- pushes every speaker after
    the first into the title.
    """
    if "_" not in stem:
        return []
    segments = stem.split("_", 1)[1].split("_")
    while len(segments) > 1 and segments[-1].strip().lower() in KNOWN_DOC_WORDS:
        segments.pop()
    if len(segments) < 2:
        return []
    extra = [s.strip() for s in segments[1:]]
    if all(s.lower() in KNOWN_DOC_WORDS or len(s.split()) <= 2 for s in extra) \
            and any(s.lower() not in KNOWN_DOC_WORDS for s in extra):
        kind = "unstripped document marker or flattened underscore"
    else:
        kind = "flattened underscore"
    return [f"{kind}: filename carries {len(segments) - 1} further "
            f"underscore(s) ({', '.join(repr(s) for s in extra)}) that became "
            "spaces in the title"]


# A trailing single capital or capital+letter is a word sliced in half
# ("... and Container E", "... without Breaking a Ci"). All-caps acronyms and
# real two-letter words ("... the Mind Behind It") are excluded by name.
MIDWORD_TAIL_RE = re.compile(r"(?:^|\s)([A-Z][a-z]?)$")
REAL_SHORT_WORDS = {"A", "I", "It", "Is", "In", "On", "At", "To", "We", "Me",
                    "My", "Of", "Or", "As", "By", "Do", "Go", "If", "So", "Up",
                    "Us", "Be", "He", "No", "An", "Am", "Ai", "Id", "Ok"}

ADVISORY = "(advisory) "


def _truncation_hints(title: str, stem: str, base: str, series: str) -> list[str]:
    out = []
    m = MIDWORD_TAIL_RE.search(title)
    if m and m.group(1) not in REAL_SHORT_WORDS and len(title.split()) > 3:
        out.append(f"title ends mid-word ({m.group(1)!r})")
    # A trailing comma or hyphen is a cut, not punctuation an author chose.
    # "...on RISC-V" is deliberately excluded: a one-letter suffix after a hyphen
    # is as often a real name as a truncation, so it is not evidence on its own.
    if title.endswith(",") or title.endswith("-"):
        out.append("title ends on a dangling separator")
    # The filename hit the archive's length limit and nothing was stripped after
    # the title, so whatever the cut removed is missing from the title too. This
    # is circumstantial -- a title can end exactly at the cap -- so it is
    # advisory and is counted separately.
    cap = LENGTH_CAP.get(series, DEFAULT_LENGTH_CAP)
    if len(base.encode()) >= cap + 4 and stem.endswith(title):
        out.append(f"{ADVISORY}filename is at the archive length cap "
                   f"({len(base.encode())} bytes) with the title flush against "
                   "the cut -- verify against the slides")
    return out


# --------------------------------------------------------------------------
# Check 3 -- conference / edition / year vs. the containing folder
# --------------------------------------------------------------------------

BH_PREFIX_RE = re.compile(r"^(AS|US|EU)-?(\d{2})-", re.I)
BH_REGION = {"AS": "ASIA", "US": "USA", "EU": "Europe"}


def expected_conference(folder: str) -> dict:
    """What the folder name says the deck is, computed independently of pdf2md."""
    flat = folder.lower().replace("_", " ").replace("-", " ")
    squashed = flat.replace(" ", "")
    ym = re.search(r"\b(?:19|20)\d{2}\b", flat)
    year = int(ym.group(0)) if ym else None

    if "blackhat" in squashed:
        series = "Black Hat"
        if "usa" in flat:
            edition = "USA"
        elif "asia" in flat:
            edition = "ASIA"
        elif "europe" in flat:
            edition = "Europe"
        else:
            edition = ""
    elif "defcon" in squashed:
        # DEF CON numbers editions instead of years, so `year` stays null and the
        # edition number carries the identity.
        series = "DEF CON"
        num = re.search(r"\b(\d{1,2})\b", folder)
        edition = num.group(1) if num else ""
        year = None
    elif "offensivecon" in squashed:
        series, edition = "OffensiveCon", ""
        if year is None:
            m = re.search(r"offensivecon(\d{2})", squashed)
            if m:
                year = 2000 + int(m.group(1))
    elif "recon" in squashed:
        series, edition = "REcon", ""
    elif "hexacon" in squashed:
        series, edition = "Hexacon", ""
    else:
        series, edition = folder.title(), ""

    full = " ".join(x for x in (series, edition, str(year) if year else "") if x)
    return {"conference": series, "edition": edition, "year": year,
            "conference_full": full}


def conference_defects(rec: dict) -> list[dict]:
    src = rec.get("source_pdf") or ""
    folder = src.split("/")[0]
    want = expected_conference(folder)
    out = []
    for key in ("conference", "edition", "year", "conference_full"):
        got = rec.get(key)
        if got != want[key]:
            out.append({"source_pdf": src, "field": key, "is": got,
                        "should_be": want[key],
                        "why": f"folder {folder!r}"})
    # conference_full must be exactly its own parts joined.
    parts = [rec.get("conference") or "", rec.get("edition") or "",
             str(rec.get("year")) if rec.get("year") else ""]
    rebuilt = " ".join(p for p in parts if p)
    if rebuilt != (rec.get("conference_full") or ""):
        out.append({"source_pdf": src, "field": "conference_full",
                    "is": rec.get("conference_full"), "should_be": rebuilt,
                    "why": "does not equal conference + edition + year"})
    # Black Hat's own filenames carry region+year; an independent witness.
    m = BH_PREFIX_RE.match(os.path.basename(src))
    if m:
        reg = BH_REGION[m.group(1).upper()]
        yr = 2000 + int(m.group(2))
        if rec.get("edition") != reg:
            out.append({"source_pdf": src, "field": "edition",
                        "is": rec.get("edition"), "should_be": reg,
                        "why": f"filename prefix {m.group(0)!r}"})
        if rec.get("year") != yr:
            out.append({"source_pdf": src, "field": "year",
                        "is": rec.get("year"), "should_be": yr,
                        "why": f"filename prefix {m.group(0)!r}"})
    return out


# --------------------------------------------------------------------------
# Check 4 -- title vs. the slides themselves
# --------------------------------------------------------------------------

SLIDE_RE = re.compile(r"^##\s+Slide\s+\d+\s*$", re.M)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9']+")


def _norm(word: str) -> str:
    word = unicodedata.normalize("NFKD", word)
    return "".join(c for c in word if not unicodedata.combining(c)).lower()


def first_slides(body: str, count: int = 2) -> str:
    """Text of the first `count` slides, minus the generated header block."""
    starts = [m.start() for m in SLIDE_RE.finditer(body)]
    if not starts:
        return body[:1500]
    end = starts[count] if len(starts) > count else len(body)
    return body[starts[0]:end]


def content_score(rec: dict, slides: int = 2) -> dict:
    """Fraction of the title's content words that appear in the opening slides."""
    title_words = {_norm(w) for w in WORD_RE.findall(rec.get("title") or "")}
    title_words = {w for w in title_words if w not in STOPWORDS and len(w) > 2}
    text = first_slides(rec.get("_body") or "", slides)
    body_words = {_norm(w) for w in WORD_RE.findall(text)}
    if not title_words:
        return {"score": 0.0, "matched": 0, "total": 0, "excerpt": text[:600]}
    hit = title_words & body_words
    return {"score": len(hit) / len(title_words), "matched": len(hit),
            "total": len(title_words), "missing": sorted(title_words - hit),
            "excerpt": text[:600]}


# --------------------------------------------------------------------------
# Check 5 -- the same talk under two filenames
# --------------------------------------------------------------------------

def dedupe_key(rec: dict) -> str:
    title = _norm(re.sub(r"[^A-Za-z0-9 ]+", " ", rec.get("title") or ""))
    title = re.sub(rf"\b(?:{DOC_MARKER}|{VERSION_MARKER})\b", " ", title, flags=re.I)
    title = re.sub(r"\s+", " ", title).strip()
    people = ",".join(sorted(_norm(s) for s in (rec.get("speakers") or [])))
    return f"{people}|{title}"


def duplicate_groups(records: list[dict]) -> list[list[dict]]:
    buckets = defaultdict(list)
    for rec in records:
        buckets[dedupe_key(rec)].append(rec)
    groups = [g for g in buckets.values() if len(g) > 1]
    groups.sort(key=lambda g: g[0].get("source_pdf") or "")
    return groups


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="markdown",
                    help="converted corpus directory (default: markdown)")
    ap.add_argument("--checks", default="all",
                    help="comma-separated subset of " + ",".join(ALL_CHECKS))
    ap.add_argument("--sample", type=int, default=60,
                    help="decks to cross-check against slide content (0 = all)")
    ap.add_argument("--slides", type=int, default=2,
                    help="how many leading slides to read for the content check")
    ap.add_argument("--threshold", type=float, default=0.34,
                    help="content overlap below this is reported for review")
    ap.add_argument("--excerpts", action="store_true",
                    help="print the slide text behind each content finding")
    ap.add_argument("--seed", type=int, default=0, help="sampling seed")
    ap.add_argument("--json", help="also write the full report as JSON here")
    args = ap.parse_args(argv)

    checks = ALL_CHECKS if args.checks == "all" else tuple(
        c.strip() for c in args.checks.split(",") if c.strip())

    if not os.path.isdir(args.out):
        print(f"error: {args.out!r} is not a directory", file=sys.stderr)
        return 2

    records, unreadable, shadowed = collect(args.out)
    report: dict = {"corpus": args.out, "decks": len(records),
                    "unreadable": unreadable, "shadowed_slugs": shadowed}

    print(f"corpus: {args.out}")
    print(f"decks (unique source_pdf): {len(records)}")
    if unreadable:
        print(f"unreadable / mid-write files skipped: {len(unreadable)}")
    if shadowed:
        print(f"source_pdf values written to >1 markdown file: {len(shadowed)} "
              "(in-flight reconversion artefact, not a metadata defect)")

    if "speakers" in checks:
        rows, orphans, leaked = [], [], []
        for rec in records:
            rows.extend(speaker_defects(rec))
            o = orphan_title_head(rec)
            if o:
                orphans.append(o)
            l = speakers_leaked_into_title(rec)
            if l:
                leaked.append(l)
        report["speakers"] = rows
        report["orphan_title_heads"] = orphans
        report["speakers_leaked_into_title"] = leaked
        real = [r for r in rows if r["reasons"] != ["no speakers parsed"]]
        empty = [r for r in rows if r["reasons"] == ["no speakers parsed"]]
        print(f"\n== speakers that are not names: {len(real)}")
        for r in real:
            print(f"  {r['speaker']!r}")
            print(f"      reasons: {'; '.join(r['reasons'])}")
            print(f"      file:    {r['source_pdf']}")
        print(f"\n== decks with no speakers parsed: {len(empty)}")
        for r in empty:
            print(f"  {r['source_pdf']}")
        print(f"\n== titles decapitated by a mid-word split: {len(orphans)}")
        for o in orphans:
            print(f"  title={o['title']!r} speakers={o['speakers']}")
            print(f"      {o['reason']}")
            print(f"      file: {o['source_pdf']}")
        print(f"\n== speakers left inside the title: {len(leaked)}")
        for o in leaked:
            print(f"  title={o['title']!r} speakers={o['speakers']}")
            print(f"      {o['reason']}")
            print(f"      file: {o['source_pdf']}")

    if "titles" in checks:
        rows = []
        for rec in records:
            rows.extend(title_defects(rec))
        report["titles"] = rows
        hard = [r for r in rows
                if any(not x.startswith(ADVISORY) for x in r["reasons"])]
        soft = [r for r in rows if r not in hard]
        print(f"\n== titles carrying filename debris: {len(hard)}")
        for r in hard:
            print(f"  {r['title']!r}")
            for reason in r["reasons"]:
                print(f"      {reason}")
            print(f"      file: {r['source_pdf']}")
        print(f"\n== titles flush against the archive length cap "
              f"(advisory, verify): {len(soft)}")
        for r in soft:
            print(f"  {r['title']!r}")
            print(f"      file: {r['source_pdf']}")

    if "conference" in checks:
        rows = []
        for rec in records:
            rows.extend(conference_defects(rec))
        report["conference"] = rows
        print(f"\n== conference/edition/year mismatches: {len(rows)}")
        for r in rows:
            print(f"  {r['source_pdf']}")
            print(f"      {r['field']}: is {r['is']!r}, should be "
                  f"{r['should_be']!r} ({r['why']})")
        if not rows:
            counts = Counter(r.get("conference_full") for r in records)
            for name, n in sorted(counts.items()):
                print(f"  ok  {name}: {n} decks")

    if "content" in checks:
        pool = list(records)
        random.Random(args.seed).shuffle(pool)
        if args.sample:
            pool = pool[:args.sample]
        scored = []
        for rec in pool:
            s = content_score(rec, args.slides)
            s.update({"source_pdf": rec.get("source_pdf"),
                      "title": rec.get("title")})
            scored.append(s)
        scored.sort(key=lambda s: s["score"])
        low = [s for s in scored if s["score"] < args.threshold]
        report["content"] = scored
        print(f"\n== title vs. slide content: {len(scored)} decks checked, "
              f"{len(low)} below overlap {args.threshold}")
        for s in low:
            print(f"  overlap {s['score']:.2f} ({s['matched']}/{s['total']}) "
                  f"{s['title']!r}")
            print(f"      file: {s['source_pdf']}")
            if args.excerpts:
                snippet = " ".join(s["excerpt"].split())[:400]
                print(f"      slides: {snippet}")

    if "duplicates" in checks:
        groups = duplicate_groups(records)
        report["duplicates"] = [[r.get("source_pdf") for r in g] for g in groups]
        print(f"\n== duplicate talks (same speakers + title): {len(groups)} groups, "
              f"{sum(len(g) for g in groups)} files")
        for g in groups:
            print(f"  {g[0].get('title')!r} -- {g[0].get('speakers')}")
            for rec in g:
                print(f"      {rec.get('source_pdf')}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=1, default=str)
        print(f"\nJSON report written to {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
