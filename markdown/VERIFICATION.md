# Verification log

What has actually been checked in this corpus, and how. Kept honest on purpose:
a talk listed here was verified **on the slides named**, not end to end, and
anything not listed has not been verified at all.

Nothing in this file is inferred. Every entry is either a page image read
against the extracted text, or a mechanical check whose command is given.

---

## Why only part of the corpus can be verified this way

Extraction happens two ways, and only one of them can be wrong:

| Path | Volume | Can it be wrong? |
|---|---|---|
| **Structural** — reads the PDF's own text stream | ~76% of corpus text | **No.** The characters are the file's own bytes, not a guess. Reading *order* can be imperfect; the characters cannot. |
| **OCR** — renders the page and reads the pixels | ~24% (10,486 blocks) | **Yes.** This is where every character error lives. |
| **Transcripts** — speech recognition output | 3.5M chars | Wording can be misheard; no OCR involved. |

So verification targets OCR blocks. Vision-checking structural text would confirm
layout, not accuracy.

---

## Mechanical checks — whole corpus, reproducible

These ran over every deck. Commands are in `tools/`; re-run them against any build.

| Check | Result | Command |
|---|---|---|
| Every manifest record has its file, and vice versa | **705/705, 0 orphans** | `tools/audit_structure.py` |
| Slide headings match source page count | **46,118 = 46,118, no gaps** | `tools/audit_structure.py` |
| Frontmatter parses, required keys present, types correct | **705/705** | `tools/audit_structure.py` |
| No truncated files or unbalanced code fences | **1 found, fixed** | `tools/audit_structure.py` |
| Output filename collisions | **0 unintended** (25 real, distinct sources) | `tools/audit_structure.py` |
| Text-layer coverage vs source PDF | median **1.016** — no systematic loss | `tools/audit_coverage.py` |
| Conference / edition / year correctness | **0 mismatches in 705** | `tools/audit_metadata.py` |
| Credential-shaped strings | **47 found, redacted** | `tools/redact_corpus.py --dry-run` |

---

## Vision verification — page images read against extracted text

**199 slides across 94 documents** have had their page image read by a vision
model and compared against the OCR text. Every one is listed by talk and slide
number in [VISION_VERIFIED.md](VISION_VERIFIED.md), with the verdict the
reviewer reached; regenerate it with `tools/vision_review_index.py`.

The verdicts are not reassuring, and they are not meant to be:

| Verdict | Slides | Meaning |
|---|---:|---|
| badly-mangled | 139 | OCR text was unusable — rebuilt from the page |
| minor-errors | 53 | structure held; individual characters or lines wrong |
| accurate | 7 | OCR was already correct; text confirmed, not changed |

Seven slides in 199 came back clean. These are the blocks the converter itself
flagged as unreliable — a deliberately adverse sample, not a random one — so
the ratio measures the flag's precision, not the corpus's. It says the flag is
finding the right pages.

### Do the reviewers agree with each other?

Two reviewers independently read the same twelve pages of the ACE3 USB-C
controller talk, without seeing each other's output. Token overlap:

| Comparison | Overlap |
|---|---|
| Reviewer A vs reviewer B, same page | **0.75 – 0.95** |
| Either reviewer vs the OCR text | 0.13 – 0.28 |

Two readings that agree with each other and disagree with the OCR are evidence
that the page says what the reviewers say it says. It is not proof — both could
misread the same character the same way — but it rules out the failure that
would matter most, which is a reviewer inventing plausible text.

### Individual findings

Each row means: the page was rendered, read, and compared to what the converter
produced for it.

| Deck | Slide | What was checked | Verdict |
|---|---|---|---|
| Apple macOS Kernel Exploitation with MIE (BH USA 2026) | 4 | Apple MIE blog screenshot, clipped at the slide edge | **Accurate** — OCR reproduced the visible text exactly; the apparent truncation is in the slide itself, not the extraction |
| AMD Sinkclose Ring -2 Privilege Escalation (Hexacon 2024) | 37 | Terminal output + hex dump, white-on-black | **Accurate after filtering** — every narrative line correct (`TSEG Base : bf000000`, `SMM Base : bfea8000`, `-> remapping BAR2 to overlap TSEG`); the mangled hex rows were correctly removed |
| AMD Sinkclose Ring -2 Privilege Escalation (Hexacon 2024) | 13 | Register-layout diagram (vector, text layer) | **Accurate** — extracted as a table by the structural pass, no OCR involved |
| BLE Theft Auto (DEF CON 34) | 8 | Photo + satellite map, no readable text | **Fixed** — had produced 12 lines of noise (`) ez g / Jealetas .`); now yields only the real title |
| gpwn: Wiretapping Fiber ISP Deployments (BH USA 2026) | 5 | Photograph of fibre splicing, no text | **Correct to be empty** — nothing to extract; OCR correctly returned nothing |
| One Bug to Rule Them All: Stably Exploiting a Preauth RCE (BH Asia 2025) | 26 | Wireshark capture + WinDbg heap leak, **flagged risky** | **Mixed, and the flag was right** — see below |

#### Detail: "One Bug to Rule Them All", slide 26 (flagged `ocr_unreliable`)

Read against the rendered page. What the converter got **right**:

- Title `Leak heap address` — exact
- `Hex value ~ 018887000259` — the slide's find-bar shows `01 88 87 00 02 59`; every
  digit correct, only the spaces lost
- `3d267954-eeb7-11d1-b94e-00c04fa3080d` — a 36-character DCERPC interface GUID,
  **character-perfect**
- `Response: call_id: 8611, Fragment: Single` — exact

What it got **wrong**, all in numeric fields:

| Slide shows | OCR produced |
|---|---|
| `192.168.80.128` | `192.168.808.128` — invalid IP |
| `150` (packet length) | `15@` |
| `Ctx: 0` | `Ctx: @` |

This is the documented pattern exactly: identifiers and prose survive, bare numerals
degrade. It is also evidence the risk flag works — this block was marked
`ocr_unreliable` before I looked at it, and it does contain wrong values while the
narrative around them is sound.

#### Detail: "UnOAuthorized: Privilege Escalation to Global Administrator", slide 96 (flagged `ocr_unreliable`)

A PowerShell session listing Entra directory roles and their GUIDs. Read against
the rendered page.

Correct: the command line `Get-MgDirectoryRole | Select-Object -Property
DisplayName,ID` is exact, and `User Administrator
77414df4-e2ff-42df-8a7d-58df04e65885` is character-perfect across all 36 GUID
characters.

Wrong, in the same block:

| Slide shows | OCR produced |
|---|---|
| `DisplayName` | `DispLayName` |
| `128284a5-9a9e-49c3-a460-fd25554f8c45` | `128284a5-9a9e—-49c3-al60-Fd25554F8c45` |
| `70ddedcfdc86` | `7Oddedcfdc86` |

**And two rows are missing entirely — including the one the slide exists to make.**
`Global Administrator  ae81c4d9-3b45-445b-896a-64aa7085db93` is boxed in red on
the page as the escalation target, and it is not in the output. The second
command and its results are gone too.

This is the honest cost of filtering: the quality gates that remove mangled hex
also remove real lines when OCR reads them poorly, and here they removed the most
important line on the slide. The block is flagged `ocr_unreliable`, which is the
correct signal — but "unreliable" means *incomplete* as well as *inaccurate*.
For a slide that matters, read the source PDF.

### Ground-truth spot checks by sampling agent

31 further OCR blocks were re-rendered and compared. Summary of verdicts:
**4 accurate, 3 mostly accurate, 7 partly mangled, 3 garbage** (remainder read
for coherence only). Full detail in the commit history.

Established failure modes, with examples:

- **Prose, headings, code on light backgrounds** — near-exact. A 256-character
  RSA modulus and a git diff with blob hashes both came out character-perfect.
- **Hex dumps, disassembly, memory tables** — wrong often, and plausibly:
  `00000118` → `80000118`, `0013ecb0` → `0013ecbO`. Row/column structure is lost.
- **Hashes** — off-by-one characters observed in an MD5 and a SHA-256.
- **Figures** — silent digit substitution: `16.59%` → `16.50%`.
- **Cross-region fusion** — the worst mode: text from unrelated parts of a slide
  fused into one line that never existed on the page.

This is why blocks dense in hex or tabular data now carry an explicit warning and
are counted per document as `ocr_unreliable_blocks`.

---

## Blocks that could not be vision-verified

| Deck | Blocks | Reason |
|---|---:|---|
| CoDe16: 16 Zero-Day Vulnerabilities Affecting CODESYS Framework | 17 | Every attempt to review these pages was stopped by the model API's cyber safeguards, at three different batch sizes, once before any page was read. The trigger is the deck's subject — ICS/OT zero-days — not any individual slide. |

These blocks remain OCR-only and keep their `ocr_unreliable` flag, so they are
identifiable rather than silently trusted. Reviewing them needs an account
enrolled in Anthropic's Cyber Verification Program, which exists for exactly
this kind of published security research.

## A defect in the review pipeline itself, found and fixed

Worth recording, because it went wrong quietly and the corpus had to be
repaired rather than rebuilt.

`verify_uncertain.py --extract` numbered its work list from zero on every run.
Review runs in batches against a corpus that is still being converted, so the
work list gets regenerated while corrections are in flight — and renumbering
re-points every id at a different block. Eleven batches written before one such
regeneration were applied afterwards, which wrote 105 correct transcriptions
into 57 documents they had never looked at.

It was caught by measuring, not by reading: a correction should share
vocabulary with the OCR text it replaces. The eleven stale batches had a median
token overlap of **0.01** with the blocks their ids now named. Batches written
after the regeneration scored **0.55–0.95**. That is not a borderline
signal.

Repair, in order: every mis-targeted block was restored from the extracted text
captured in the work list; the earlier batches were relocated to their correct
blocks by matching their text against the corpus (104 of 105 found — one block
was lost and is back to OCR text, unflagged as verified); labels were rebuilt
from block content rather than batch order; and frontmatter counts were
recomputed. Verified afterwards: 0 documents with duplicate frontmatter keys,
0 documents whose `vision_verified_blocks` disagrees with the labels in the
body.

Three separate bugs are fixed in the tool so this cannot recur:

- an id is now bound to (document, slide) permanently, and reviewed blocks stay
  in the work list rather than being renumbered away
- `--apply` refuses ids that are not in the current work list instead of editing
  whichever block holds that number
- labelling is positional, so a block is marked reviewed because it was read —
  the old code used `str.replace(..., 1)`, which marked the *first* flagged
  block in the document

## Known defects, not fixed

| Issue | Scale | Why not fixed |
|---|---|---|
| Black Hat's `AS-23-` filenames drop subtitles and keep one surname | 36 decks | Lossy in the source archive, not in conversion. `PMFault` is really *"PMFault: Voltage Fault Injection on Server Platforms Through the PMBus"*; `["Bai"]` is really three people. Recovering it means reading titles off slide 1 — a separate job with its own error modes. |
| `MoustachedBouncer AitM-Powered…` parses as a speaker | 1 deck | Genuinely ambiguous — it reads exactly like a two-word name. Corrected via `tools/metadata_overrides.json` instead. |
| Two source PDFs are mis-filed by the archive | 2 decks | The filename describes a different talk. Corrected via `tools/metadata_overrides.json`, with the discrepancy written into `content_note`. |
| Three files in the DEF CON 33 workshop archives will not decompress | 3 files | Damaged in the published RARs, not here. `ShellcodeHarness.exe`, `xss_python_swift_rest_api_server.py` and `OpenStack_Swift_server_setup-Optional.md` yield zero bytes under both 7-Zip and `unar`, which fail at the same offsets. Everything else in those archives extracted. |
| Exact values inside OCR blocks | ~11% of OCR characters | Tesseract cannot resolve `0`/`O`/`@`/`Q` in slide screenshots at any DPI tested; 400 DPI scored *worse* than 200. Flagged rather than silently trusted. |

---

## How to use this

- Filter on `ocr_unreliable_blocks: 0` for documents whose text is safe to quote.
- Treat any value inside an OCR block as approximate; `source_pdf` names the file
  to check against.
- Transcripts (`source_type: transcript`) contain no OCR at all.
