# Pages that could not be verified

Ranges the full-page review could not read, and how to finish them.

Every other page listed in [VISION_VERIFIED.md](VISION_VERIFIED.md) had its
image read against the extracted text. The pages below did not, so they carry
whatever the first-pass converter produced — which, measured across the twelve
documents read end to end so far, is wrong about **96%** of the time. Treat them
as unread, not as clean.

Each was attempted and stopped by the model API's real-time cyber safeguards.
The trigger is subject matter, not any individual slide: in every case other
ranges of the same document reviewed normally. Where a range was retried on a
second model, that is noted — switching model recovered three of five such
ranges and failed on two.

---

## Open ranges

| Document | Pages | Attempts | Notes |
|---|---|---|---|
| `DEF CON 34/def-con-34-jian-zhou-lei-lu-one-chain-to-own-them-all-breaking-ai-infrastructures-azraelxuemo-v3.md` | 118–130 | Opus ×1, Sonnet ×1 | 130 of 143 pages verified. 79–91 was recovered on a second model; this range was not. |
| `BlackHat_USA_2026_Slides/dion-blazakisjosh-mainebruce-dang-apple-macos-kernel-exploitation-with-mie-building-on-the-ashes-of-100-vulnerabilities.md` | 45–58 | Opus ×1, Sonnet ×1 | 44 of 58 pages verified. Blocked before any page of this range was read. |
| `Black Hat USA 2023 slides/…code16-16-zero-day-vulnerabilities-affecting-codesys-framework…` | 17 flagged OCR blocks | Opus ×4 | Older flagged-block workflow, not full-page. Blocked at three different batch sizes, once before any page was read. |

Counts and page lists are also in each document's own frontmatter
(`vision_unreviewed_pages`) and in `markdown/manifest.jsonl`, so they can be
filtered mechanically rather than read out of this file.

---

## Re-running one of these

The work directories live in a session scratchpad and do not survive, so start
by re-extracting. From the repo root:

```bash
# 1. Render every page of the document to PNG and build a work list.
#    --src is repeatable; DEF CON sources ship as release assets rather than
#    being committed, so point at wherever you unpacked them.
python3 tools/verify_document.py --extract \
    --doc "markdown/<path from the table above>" \
    --src . --src /path/to/defcon/sources \
    --work review-doc/

# 2. Review. For each page, read work/pages/pNNN.png against the page's
#    current_markdown in work/tasks.jsonl, and append one JSON line per page to
#    work/corrections_A.jsonl:
#      {"slide": 46, "verdict": "accurate"}
#      {"slide": 47, "verdict": "minor-errors", "markdown": "<corrected body>"}
#    Omit "markdown" when the page is already correct. Verdicts are
#    accurate / minor-errors / badly-mangled.

# 3. Apply. Idempotent, so it is safe to re-run as more batches land.
cat review-doc/corrections_*.jsonl > review-doc/corrections.jsonl
python3 tools/verify_document.py --apply \
    --doc "markdown/<same path>" --work review-doc/

# 4. Record the verdicts and rebuild the indexes. refresh_manifest must run
#    first: the manifest is written once by the converter, so without it the
#    review is invisible to anything that filters on manifest.jsonl.
python3 tools/refresh_manifest.py --out markdown
python3 tools/build_index.py --out markdown
python3 tools/vision_review_index.py --out markdown \
    --record tools/vision_review.jsonl > markdown/VISION_VERIFIED.md
```

Then update the document's `vision_verified_pages`, drop the pages from its
`vision_unreviewed_pages`, and delete its row above.

### What the reviewer should be told

The instructions that produced the rest of this corpus, in case they are useful
verbatim:

> Compare the page image against `current_markdown`. Check that every piece of
> text on the page is present and correct — reading order, tables as tables,
> code and terminal output exact to the character, and nothing silently dropped:
> diagram labels, callouts, footers, statistics, side panels, small print. Crop
> and upscale with PIL rather than guessing. Watch for text the converter
> **invented** — a heading or line not on the page is worse than one dropped;
> check especially whether content belongs to a neighbouring build of the same
> slide. Preserve the author's own typos. Never summarise or reorder. Drop the
> converter's `> Recovered by OCR` banner, which is scaffolding rather than
> slide content.

Splitting a document across reviewers at 12–15 pages each worked well; each
writes its own `corrections_<LETTER>.jsonl` so they do not collide.

---

## What to expect

Across the twelve documents read end to end, per-page verdicts were:

| Verdict | Share |
|---|---:|
| badly-mangled | 34% |
| minor-errors | 62% |
| accurate | 4% |

The failures that matter most are not character errors. They are whole dropped
regions — a talk's headline statistic, an allow-list, a call trace, a findings
table — and content the converter **invented**, which no reader can detect
without the page in front of them. Both are documented with examples in
[VERIFICATION.md](VERIFICATION.md).
