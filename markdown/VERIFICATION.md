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

## Known defects, not fixed

| Issue | Scale | Why not fixed |
|---|---|---|
| Black Hat's `AS-23-` filenames drop subtitles and keep one surname | 36 decks | Lossy in the source archive, not in conversion. `PMFault` is really *"PMFault: Voltage Fault Injection on Server Platforms Through the PMBus"*; `["Bai"]` is really three people. Recovering it means reading titles off slide 1 — a separate job with its own error modes. |
| `MoustachedBouncer AitM-Powered…` parses as a speaker | 1 deck | Genuinely ambiguous — it reads exactly like a two-word name. Corrected via `tools/metadata_overrides.json` instead. |
| Two source PDFs are mis-filed by the archive | 2 decks | The filename describes a different talk. Corrected via `tools/metadata_overrides.json`, with the discrepancy written into `content_note`. |
| Exact values inside OCR blocks | ~11% of OCR characters | Tesseract cannot resolve `0`/`O`/`@`/`Q` in slide screenshots at any DPI tested; 400 DPI scored *worse* than 200. Flagged rather than silently trusted. |

---

## How to use this

- Filter on `ocr_unreliable_blocks: 0` for documents whose text is safe to quote.
- Treat any value inside an OCR block as approximate; `source_pdf` names the file
  to check against.
- Transcripts (`source_type: transcript`) contain no OCR at all.
