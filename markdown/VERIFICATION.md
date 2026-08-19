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
| **Structural** — reads the PDF's own text stream | ~76% of corpus text | **The characters cannot be wrong** — they are the file's own bytes. **The document can be.** Reading order, tables, code listings, equations and figures are all reconstructed, and a 55-page zero-OCR paper read end to end needed 54 of its 55 pages rewritten. See the control case below. |
| **OCR** — renders the page and reads the pixels | 11,467 pages | **Yes.** This is where every character error lives. |
| **Transcripts** — speech recognition output | 3.5M chars | Wording can be misheard; no OCR involved. |

Verification therefore targets OCR blocks first. But reading one document end to
end (below) showed that assumption is only half right: the structural pass drops
whole diagrams, tables and terminal panes without any OCR involved, and nothing
flags it when it does.

---

## Mechanical checks — whole corpus, reproducible

These ran over every deck. Commands are in `tools/`; re-run them against any build.

| Check | Result | Command |
|---|---|---|
| Every manifest record has its file, and vice versa | **955/955, 0 orphans** | `tools/audit_structure.py` |
| Slide headings match source page count | **53,957 = 53,957, no gaps** | `tools/audit_structure.py` |
| Frontmatter parses, required keys present, types correct | **955/955** | `tools/audit_structure.py` |
| Speakers attributed | **948/955**; the 7 are 6 DEF CON panels and one talk whose filename carries no name | `tools/audit_structure.py` |
| No truncated files or unbalanced code fences | **0** | `tools/audit_structure.py` |
| Source PDFs resolve | **611 present, 221 expected-absent** (DEF CON drops ship as release assets), **0 unexpectedly missing** | `tools/audit_structure.py` |
| Same PDF published under two names | **5 sources, 10 documents** — cross-linked via `duplicate_of` where reviewed | `tools/audit_metadata.py` |
| Text-layer coverage vs source PDF | median **1.016** — no systematic loss | `tools/audit_coverage.py` |
| Conference / edition / year correctness | **0 mismatches** | `tools/audit_metadata.py` |
| Credential-shaped strings | **redacted, with a stable fingerprint per distinct value** — 1,699 in the DEF CON 33 cloud-forensics lab alone, resolving to 117 distinct keys | `tools/redact_corpus.py --dry-run` |

---

## Vision verification — page images read against extracted text

**452 slides across 126 documents** have had their page image read by a vision
model and compared against the OCR text. Every one is listed by talk and slide
number in [VISION_VERIFIED.md](VISION_VERIFIED.md), with the verdict the
reviewer reached; regenerate it with `tools/vision_review_index.py`.

The verdicts are not reassuring, and they are not meant to be:

| Verdict | Slides | Meaning |
|---|---:|---|
| badly-mangled | 266 | OCR text was unusable — rebuilt from the page |
| minor-errors | 166 | structure held; individual characters or lines wrong |
| accurate | 20 | OCR was already correct; text confirmed, not changed |

Twenty slides in 452 came back clean. These are the blocks the converter itself
flagged as unreliable — a deliberately adverse sample, not a random one — so
the ratio measures the flag's precision, not the corpus's. It says the flag is
finding the right pages.

### One document read end to end

Everything above reviews blocks the converter **flagged**. That is the right
economy across 956 documents, but it cannot answer "is this talk right?",
because the failures it never flagged are the ones it does not know about.

So one talk was read in full: all 57 pages of *Witchcraft Solver: Automated
0day Discovery in Stripped Binaries* (Jonathan Brossard, DEF CON 34), page
image against extracted text, via `tools/verify_document.py`.

**51 of 57 pages were rewritten. 6 were already correct.** The document grew
from 30,452 to 44,089 characters — a third of its final text had been missing.

The flagged-block review would have looked at **one** of those 57 pages. What
the other 50 corrections included:

| Page | What had happened |
|---:|---|
| 6 | Dropped entirely — the extracted text was the single character `6` |
| 48 | The pipeline diagram, which is the method of the talk, was absent; the surviving title read `LVM` for `LLVM` |
| 38 | The Common Criteria chart — 7 assurance levels, 10 technique bars, the arrow marking symbolic execution — absent |
| 43 | The dataset slide lost its title, its DOI badge and the `39,364 binaries` figure; the chroot list was read across columns in the wrong order with two entries dropped |
| 9, 10, 25 | Whole terminal sessions dropped, including both BuildID hashes and the Rocq proof output |
| 35 | Harbor UI: storage quota read as `JOGIB` for `731.98 GiB`, every pull count as `°` for `0`, the `1 - 15 of 682 items` pager gone |
| 44, 45 | Results tables flattened into one-value-per-line dumps; a total shown as `829.9%` where the slide says `29.9% (11,842)` |
| 42 | Title corrupted to "Oblem : Anvill needs a Decompiler to identity functions" |

None of those pages carried an `ocr_unreliable` flag, and several involve no
OCR at all — they are structural-pass failures, which the risk heuristic is not
built to see and cannot be made to see. **The lesson generalises: a document
with `ocr_unreliable_blocks: 0` has not been verified, it has merely not been
flagged.**

Two reviewers separately noted the same source-side defect, which is worth
recording because it limits what any method can recover: this deck's title text
is clipped off the top edge of the page, so on several slides only glyph
descenders survive. Those are marked as clipped rather than guessed.

### A document with no OCR at all — the control case

The deck above was 32% OCR pages, so some of its damage was Tesseract's. The
companion document in the same DEF CON 34 drop is the opposite: 55 pages,
`ocr_pages: 0`, every character taken from the PDF's own text layer. By the
reasoning at the top of this file it should have needed no verification, and
the flagged-block review covered exactly none of it.

**54 of its 55 pages were rewritten.** One was correct.

Not one character error — the text layer is exact, as claimed. Every fault was
structural, and the same handful repeat:

| Failure | Where |
|---|---|
| **Two columns interleaved** — right-column text spliced into the middle of a left-column paragraph or section | pp. 11, 14, 16, 17, 19, 29–32, 36, 38, 39, 42, 44, 51, 52 |
| **`algorithm` / `lstlisting` environments destroyed** — line breaks and indentation gone, gutter line numbers merged into surrounding prose as stray `1 2 3` blocks | pp. 11–14, 17–19, 21, 32, 33, 38, 51–54 |
| **Display equations silently dropped** | p. 27 (CI width), p. 29 (CI₉₅), p. 37 (translation completeness) |
| **Tables mangled** — spanned headers split into `Ret`/`Dec`/`An`/`vill`, floats emitted in the wrong order, literal newlines inside cells | pp. 6, 29, 31, 32, 39 |
| **Content duplicated**, not merely lost | p. 19 (an RTL comment line), p. 33 (a findings paragraph), p. 53 (two lines of Algorithm 8) |
| **URLs split by an inserted space**, breaking every link | 16 across pp. 47–49 |
| **Line-break hyphens not rejoined** — `architectureneutral`, `libjpegturbo`, `RISCV`, `machinereadable` | throughout |

Two of those deserve emphasis. Duplication is worse than loss, because nothing
about the output looks wrong — the document simply asserts something its source
does not. And the algorithms are the contribution of a paper like this one, so
the content that matters most is the content most reliably destroyed.

The table of contents, the lists of figures and tables, and Figure 1 — the
`wsolver` pipeline the whole dissertation builds towards — were all
unreadable.

**This is the control case for the claim at the top of this file.** "Structural
extraction cannot be wrong" is true about characters and false about documents.
A zero-OCR document is not a safe document; it is an unexamined one.

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

### Cross-slide checks that validate themselves

A few slides carry the same fact twice in different encodings. Those are the
strongest evidence a transcription is right, because a misreading would have to
recur consistently across two independently transcribed renderings to survive.

The best instance so far is *Hacking the Hackers* (DEF CON 34). Slide 100 is
decompiler pseudocode with a PEM certificate embedded as a C string literal;
slide 88 is unrelated `curl -vk` output against the same host, transcribed
twelve slides earlier. Base64-decoding slide 100's PEM yields 798 bytes
beginning `30 82 03 1a` — a DER `SEQUENCE` whose own length field reads 794, and
794 + 4 = 798, so the transcription closes on itself. Decoding further:

| Field recovered from slide 100's DER | What slide 88's curl output says |
|---|---|
| `proxy.dtunnel.com.br` twice — issuer equals subject | `self-signed certificate (18)` |
| `notBefore` `250923124625Z` | `start date: Sep 23 12:46:25 2025 GMT` |
| `notAfter` `350802124625Z` | `expire date: Aug  2 12:46:25 2035 GMT` |
| modulus header `02 82 01 01 00` — 2048-bit | `Public key type RSA (2048/112 Bits/secBits)` |
| OID `2a 86 48 86 f7 0d 01 01 0b` | `signed using sha256WithRSAEncryption` |

Five agreements, matching to the second on both timestamps, between two slides
that share no text. The SAN entries `dtunnel.com.br` and `*.dtunnel.com.br`
decode cleanly as well.

Slide 100 validates a second way, without reference to any other slide. Its two
little-endian qword constants `0x4745422d2d2d2d2d` and `0x4954524543204e49`
decode to `-----BEG` and `IN CERTI`; the copy loop writes the string literal at
`local_496 + 6`, overlapping the second constant by two bytes, so the bytes
reassemble to exactly `-----BEGIN CERTIFICATE-----`. One wrong hex digit in
either constant breaks that. (`0x1a4`, the mode handed to `os.WriteFile`, is
0o644.)

Checks like these are worth hunting for, but only where they exist. A reviewer
reporting a check that the slide does not support is worse than reporting none —
see the overclaim described under *Individual findings*.

---

## Blocks that could not be vision-verified

| Deck | Blocks | Reason |
|---|---:|---|
| CoDe16: 16 Zero-Day Vulnerabilities Affecting CODESYS Framework | 17 | Every attempt to review these pages was stopped by the model API's cyber safeguards, at three different batch sizes, once before any page was read. The trigger is the deck's subject — ICS/OT zero-days — not any individual slide. |
| One Chain to Own Them All: Breaking AI Infrastructures (DEF CON 34), pages 118–130 | 13 | Four of the document's eleven review batches were stopped by the same safeguard; the other seven completed normally. Those pages keep their first-pass extraction and are listed in `vision_unreviewed_pages`. |
| !secure: A Single Wrong Negation to Root Linux and Escape Managed Containers (BH USA 2026), pages 34–73 | 40 | Stopped by the cyber safeguard on both models tried: Opus refused before a single page was read, and the Sonnet retry stopped after page 33. Pages 1–33 are reviewed and applied; the rest keep their first-pass extraction and are named in `vision_unreviewed_pages`. |
| Gone in 60 Frames: USB Video Exploitation — slides (DEF CON 34), pages 41–70 | 30 | Same safeguard, same deck family as the whitepaper below. Pages 1–40 are reviewed but not yet applied. |
| Gone in 60 Frames: USB Video Exploitation — whitepaper (DEF CON 34), pages 31–64 | 34 | Two runs stopped at the same point in the document: the first to a network error, the resumed run to the cyber safeguard on Opus. Pages 1–30 are reviewed and applied; the rest keep their first-pass extraction and are named in the document's `content_note`. |

These blocks remain OCR-only and keep their `ocr_unreliable` flag, so they are
identifiable rather than silently trusted. Reviewing them needs an account
enrolled in Anthropic's Cyber Verification Program, which exists for exactly
this kind of published security research.

### Decks that cannot be rendered here at all: the eleven `.pptx` sources

Eleven decks in this corpus ship as PowerPoint rather than PDF.
`verify_document.py` routes those through LibreOffice, exactly as the converter
does, so that the reviewer sees the real slides. **In the environment this
review ran in, LibreOffice cannot convert anything** — `soffice --convert-to
pdf` fails on a plain one-line `.txt` file, so the failure is the installation,
not the decks. Every `.pptx` deck is therefore unrenderable and unverifiable
here, and `--extract` exits rather than producing a blank work list.

That matters more than a missing capability, because there is a tempting
substitute that does not work. One review attempt on *Wrestling with a Python:
Escaping Copilot Studio's AI-Guarded Sandbox* fell back to reading the `.pptx`
XML directly — exact native text per shape, plus the embedded screenshots read
as images. The native text genuinely is character-exact, and the method looks
rigorous. It still produced a document that had to be thrown away: slide 12
came out carrying a "Step 1 / Step 2" HTTP request and a Flask terminal log
with a debugger PIN, none of which is on slide 12. That slide holds two summary
bullets and an architecture diagram, and the invented text appears in no
slide's native text anywhere in the deck. Content read out of embedded images
cannot be attributed to the slide it belongs to without seeing the page, and a
reviewer working without page images will misattribute it while sounding
confident. The review was reverted in full rather than repaired.

**A `.pptx` deck is not verifiable without a working renderer.** Reading its
XML is a different and weaker operation, and must not be recorded as vision
verification.

That conclusion has now been tested twice. A later review wave, not knowing the
history, was pointed at the same talk and independently rediscovered the same
dead end: LibreOffice refused the deck at load (and still refused it after the
package was unpacked and repacked byte-for-byte), so the reviewer again fell
back to slide XML plus embedded images, and again produced a slide 12 carrying
the "Step 1 / Step 2" branch-rename request and the Flask log with
`Debugger PIN: 586-187-756` — the same invented content, on the same slide, by
the same mechanism. It was reverted in full a second time. The failure is
reproducible and belongs to the method, not to one reviewer having a bad run.
Do not retry it; the deck stays unverified until there is a renderer.

The renderer really is the blocker rather than the file: on this environment
`soffice --convert-to pdf` still fails on a plain one-line `.txt`, so nothing
would render regardless of which deck was asked for.

### Text an image is painted over — a second kind of invisible text

`invisible_spans()` catches text drawn in its own background colour. It cannot
catch text an opaque image is drawn on top of, because there the span's bbox
renders as the image — some entirely different colour — so the share of pixels
matching the span's own colour never reaches the threshold. The reader's
experience is identical in both cases: the corpus publishes a line the slide
never shows.

It is not only images. On page 22 of *Lessons from a Decade of Building
Whistleblower Tech* (DEF CON 34), seven grey spans — the whole Solution and
Challenge block, including "No observability in running systems" — sit under a
plain white filled rectangle at `[16.7, 104.2, 472.5, 352.5]` drawn after them
in the content stream. Nothing but a ~2.8 pt sliver of the first two glyphs
escapes it. The converter's check misses this for the same reason: the text is
grey, the pixels are white, so the share never matches. Any later opaque fill
does it — a raster image or a vector rectangle alike — so a detector that looks
only at image blocks, as the measurement below did, is itself incomplete.

*Hacking the Hackers* (DEF CON 34) is the largest single-deck instance found so
far: seven slides — 21, 31, 32, 63, 69, 123 and 124 — carry a title in the text
layer that the page does not show, each a full-bleed screenshot or infographic
with the title textbox painted over. All seven were caught by a reviewer looking
at the rendered page; the mechanical check returned nothing for any of them.
Each now says in place of the dropped title that the slide carries no title of
its own, rather than silently omitting it.

One instance is confirmed. On page 66 of *Sliding into the Flight Deck's DMs*
(DEF CON 34) the text layer carries `Then… nothing for 8 months.` at bbox
`[73.5, 262.7, 306.5, 280.7]`, and an image at `[7.9, 173.8, 712.1, 291.5]` —
drawn later in the content stream — covers it completely. Rendering that
rectangle shows the covering screenshot's own words, not the span's. The line
was removed under the standing rule, and the converter's mechanical check had
returned nothing for that page.

**How much of the corpus this affects is not known.** Two measurements were
attempted and only the second is worth anything:

| Method | 2026 PDFs | Result | Verdict |
|---|---:|---:|---|
| Text bbox inside any image bbox | 169 | 51,102 spans / 138 docs | **Wrong.** Counts every caption sitting on a full-bleed background photo, which is the opposite of hidden. |
| Same, but only when the image block is drawn *after* the text block | 169 | 3,310 spans / 92 docs | **Upper bound.** Correct about draw order, still blind to transparency. |

Spot-checking the second method's hits found both kinds. On *LaunchBreak* the
span reads `https://gitlab.com` while the page at that rectangle renders
"Open myapp?" — genuinely hidden. On the TETRA talk the span reads
`midnightblue.nl` and the page renders `midnightblue.nl` perfectly legibly: the
only thing over it is a translucent watermark. One of two sampled was a false
positive, so 3,310 is an over-count of unknown size.

Filtering on whether the covering image carries an `SMask` does **not**
separate the two — the confirmed true positive's covering image has one as
well, because a fully opaque image may still carry an alpha channel. Deciding
this properly means sampling the covering image's alpha over the span's own
rectangle, which has not been done. Until it is, treat the phenomenon as real
and demonstrated but unquantified, and do not cite 3,310 as a count of hidden
text.

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

- **`vision_verified_pages` is the only field that means a human-equivalent
  reader looked at the page.** Filter on it. Everything else describes what the
  converter thinks it did.
- Do **not** filter on `ocr_unreliable_blocks: 0` as a proxy for "safe to
  quote" — this file used to say you could, and the corpus has since falsified
  it. `Chaining Logical Bugs for Reliable Windows LPE` carries
  `ocr_pages: 0`, `has_ocr: false` and `ocr_unreliable_blocks: 0`, which is as
  clean as this metadata gets. Read against its pages, 73 of its 80 pages
  needed rewriting: 16 badly-mangled, 57 with errors, 7 correct. Nothing was
  flagged because nothing OCR'd; the damage was reading order, shredded code
  blocks, and a provider GUID that lost a hyphen at a line wrap
  (`e46eead8-0c54-44899898-8fa79d059e0e` for
  `e46eead8-0c54-4489-9898-8fa79d059e0e`).
- Treat any value inside an OCR block as approximate; `source_pdf` names the file
  to check against.
- Transcripts (`source_type: transcript`) contain no OCR at all.

The general form: these fields are a record of the converter's own behaviour,
not an assessment of its output. A document is unexamined until something has
read its pages.
