#!/usr/bin/env python3
"""
test_pdf2md.py — Unit tests for the metadata parsing in pdf2md.py.

Filename parsing is where this pipeline quietly gets things wrong: a bad split
yields `speakers: []` or a dash-mangled title, the Markdown still looks fine, and
the corpus becomes unfilterable without anything having visibly failed. These
cases are drawn from real filenames across the archive.

Run:
    python3 tools/test_pdf2md.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf2md import parse_conference, parse_speakers_title, slugify  # noqa: E402

SPEAKER_TITLE_CASES = [
    # (filename stem, expected speakers, expected title)
    ("Michael Stepankin_mTLS When Certificate Authentication is Done Wrong",
     ["Michael Stepankin"], "mTLS When Certificate Authentication is Done Wrong"),
    ("Sheng-Hao Ma & Yi-An Lin & Mars Cheng_Attention Is All You Need",
     ["Sheng-Hao Ma", "Yi-An Lin", "Mars Cheng"], "Attention Is All You Need"),
    ("Lukas Gerlach, Daniel Weber, Michael Schwarz_A Security RISC",
     ["Lukas Gerlach", "Daniel Weber", "Michael Schwarz"], "A Security RISC"),
    ("Dion Blazakis&Josh Maine&Bruce Dang_Apple macOS Kernel Exploitation",
     ["Dion Blazakis", "Josh Maine", "Bruce Dang"], "Apple macOS Kernel Exploitation"),
    # Black Hat's own archive convention: region-year-surname-title.
    ("AS-23-Babkin-firmWar-An-Imminent-Threat-to-the-Foundation-of-Computing",
     ["Babkin"], "firmWar An Imminent Threat to the Foundation of Computing"),
    ("AS-23-Kadkoda-Breaking-the-Chain", ["Kadkoda"], "Breaking the Chain"),
    ("AS-23-Wetzels-Nakatomi-Space", ["Wetzels"], "Nakatomi Space"),
    # "-wp" marks a whitepaper and must not leak into the title.
    ("AS-23-Li-Phoenix-Domain-Attack-wp", ["Li"], "Phoenix Domain Attack"),
    # Archive markers on the underscore convention.
    ("Csaba Fitzl_Apple Disk-O Party_Compressed", ["Csaba Fitzl"], "Apple Disk-O Party"),
    # No speaker segment at all.
    ("Some Talk With No Underscore", [], "Some Talk With No Underscore"),
    # "<Speakers>-<Title>" with a plain hyphen instead of an underscore.
    ("Allyn Stott-The Fault in Our Metrics",
     ["Allyn Stott"], "The Fault in Our Metrics"),
    ("Csaba Fitzl & Wojciech Reguła-The Final Chapter",
     ["Csaba Fitzl", "Wojciech Reguła"], "The Final Chapter"),
    # A hyphenated personal name must not be split mid-name: the right-hand
    # hyphen separates names from title, the left one is part of "Ahmad-Reza".
    ("Arun Kanuparthi & Ahmad-Reza Sadeghi-The HackDAC Story",
     ["Arun Kanuparthi", "Ahmad-Reza Sadeghi"], "The HackDAC Story"),
    # A title containing " - " must not lure the split rightwards.
    ("Matthias Frielingsdorf-You Shall Not PASS - Analysing a Spyware Sample",
     ["Matthias Frielingsdorf"], "You Shall Not PASS - Analysing a Spyware Sample"),
    # Black Hat's region prefix sometimes drops the dash ("AS23-" not "AS-23-").
    ("AS23-Xing-Dilemma-In-IoT-Access-Control", ["Xing"], "Dilemma In IoT Access Control"),
    # Long author lists are real and must not trip the too-long-to-be-names guard.
    ("Kai Tu & Yilu Dong & Abdullah Al Ishtiaq & Syed Md Mukit Rashid & Weixuan Wang & "
     "Tianwei Wu & Syed Rafiul Hussain_Cracking the 5G Fortress",
     ["Kai Tu", "Yilu Dong", "Abdullah Al Ishtiaq", "Syed Md Mukit Rashid",
      "Weixuan Wang", "Tianwei Wu", "Syed Rafiul Hussain"], "Cracking the 5G Fortress"),
    # A hyphen inside the TITLE must not be mistaken for the speaker separator.
    # Splitting right-to-left once accepted any left side containing "&", which
    # filed half a title as a speaker.
    ("Bohan Liu & Haibin Shi-The Hole in Sandbox Escape Modern Web-Based App "
     "Sandbox From Site-Isolation Perspective",
     ["Bohan Liu", "Haibin Shi"],
     "The Hole in Sandbox Escape Modern Web-Based App Sandbox From Site-Isolation Perspective"),
    ("Yuhao Jiang & Xinlei Ying-URB Excalibur The New VMware All-Platform VM Escapes",
     ["Yuhao Jiang", "Xinlei Ying"], "URB Excalibur The New VMware All-Platform VM Escapes"),
    ("Sojun Ryu & YeongJae Shin-Voice Phishing Syndicates Unmasked An In-Depth Investigation",
     ["Sojun Ryu", "YeongJae Shin"],
     "Voice Phishing Syndicates Unmasked An In-Depth Investigation"),
    # " _ " separates the speakers; the bare "_" separates speakers from title.
    ("Christian Werling _ Niclas Kuhnapfel _ Oleg Drokin_Jailbreaking an Electric Vehicle",
     ["Christian Werling", "Niclas Kuhnapfel", "Oleg Drokin"],
     "Jailbreaking an Electric Vehicle"),
    # A hyphen-attached document marker is stripped like the underscore form.
    ("Michael Grafnetter_Pass-the-Passkey Family of Attacks-WP",
     ["Michael Grafnetter"], "Pass-the-Passkey Family of Attacks"),
    ("Joshua Reynolds_Automating Malware Deobfuscation with Binary Ninja_workshop",
     ["Joshua Reynolds"], "Automating Malware Deobfuscation with Binary Ninja"),
    # An underscore INSIDE a title is meaningful and must survive.
    ("Zhenpeng Lin_Bad io_uring A New Era of Rooting for Android",
     ["Zhenpeng Lin"], "Bad io_uring A New Era of Rooting for Android"),
    # A filename-copy marker is not part of the title.
    ("Kenneth Miltenberger, Shane Cancilla-Taking on the Dark Fleet in Cyberspace (2)",
     ["Kenneth Miltenberger", "Shane Cancilla"], "Taking on the Dark Fleet in Cyberspace"),
    # No speaker at all: the whole stem is the title, markers aside.
    ("Invisible Ink Privacy Risks of CSS in Browsers and Emails_Compressed",
     [], "Invisible Ink Privacy Risks of CSS in Browsers and Emails"),
]

CONFERENCE_CASES = [
    ("BlackHat_USA_2025_Slides", "Black Hat", 2025, "Black Hat USA 2025"),
    ("Black Hat Asia 2023 slides", "Black Hat", 2023, "Black Hat ASIA 2023"),
    ("BlackHat_Europe_2024_slides", "Black Hat", 2024, "Black Hat Europe 2024"),
    ("BlackHat_USA_2026_Slides", "Black Hat", 2026, "Black Hat USA 2026"),
    ("OffensiveCon25 slides", "OffensiveCon", 2025, "OffensiveCon 2025"),
    ("Hexacon 2024 Slides", "Hexacon", 2024, "Hexacon 2024"),
    ("Recon 2024_Slides", "REcon", 2024, "REcon 2024"),
    # DEF CON numbers editions, not years; edition 34 is 2026 (DEF CON 1 = 1993).
    ("DEF CON 34", "DEF CON", 2026, "DEF CON 34"),
    ("DEF CON 26", "DEF CON", 2018, "DEF CON 26"),
]


def main() -> int:
    failures = []

    def check(cond, msg):
        print(("  PASS  " if cond else "  FAIL  ") + msg)
        if not cond:
            failures.append(msg)

    print("speaker/title parsing:")
    for stem, want_speakers, want_title in SPEAKER_TITLE_CASES:
        speakers, title = parse_speakers_title(stem)
        check(speakers == want_speakers and title == want_title,
              f"{stem[:52]!r} -> {speakers} / {title!r}"
              + ("" if (speakers == want_speakers and title == want_title)
                 else f"   EXPECTED {want_speakers} / {want_title!r}"))

    print("\nconference parsing:")
    for folder, want_series, want_year, want_full in CONFERENCE_CASES:
        got = parse_conference(folder)
        ok = got["conference"] == want_series
        # DEF CON folders carry an edition number, not a calendar year; only
        # assert the year where the folder actually encodes one.
        if want_year and want_year > 1900:
            ok = ok and got["year"] == want_year
        if want_full:
            ok = ok and got["conference_full"] == want_full
        check(ok, f"{folder!r} -> {got['conference']!r} / {got['year']} / "
                  f"{got['conference_full']!r}")

    print("\nfence safety:")
    from pdf2md import tidy
    check("\\```" in tidy("text\n```|\nmore"),
          "a line starting with ``` is escaped so it cannot open an unclosed fence")
    check(tidy("a\nb").count("`") == 0, "ordinary text is left alone")

    print("\nslugify:")
    check(slugify("AS-23-Chen-PMFault") == "as-23-chen-pmfault", "lowercases and keeps dashes")
    check("/" not in slugify("A/B Testing: Attacks & Defenses"), "strips path separators")
    check(slugify("") == "untitled", "empty input yields a usable name")
    check(len(slugify("x" * 300)) <= 120, "truncates very long names")

    print()
    if failures:
        print(f"{len(failures)} assertion(s) FAILED")
        return 1
    print(f"all {len(SPEAKER_TITLE_CASES) + len(CONFERENCE_CASES) + 4} assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
