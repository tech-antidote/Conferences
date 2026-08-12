# Conference slides → LLM-ingestible Markdown

This directory holds the conversion pipeline that turns the PDF slide decks in
this repo into Markdown a language model can actually ingest, plus a fetcher for
mirroring DEF CON presentation material.

- `pdf2md.py` — the converter (PDF → Markdown + `manifest.jsonl`)
- `fetch_defcon.py` — mirror DEF CON presentations from `media.defcon.org`

---

## Why this design, and not "just run a PDF-to-Markdown tool"

The received wisdom for PDF→Markdown is to pick the best-scoring converter —
[Docling](https://github.com/docling-project/docling),
[Marker](https://github.com/datalab-to/marker),
[MinerU](https://github.com/opendatalab/MinerU) — and run it over the corpus.
That advice is written for **papers and reports**. This corpus is neither, and
the difference changes the correct answer.

Profiling all 611 decks in this repo (40,183 pages) before choosing anything:

| Measure | Value |
|---|---|
| PDFs | 611 |
| Pages | 40,183 |
| Mean pages per deck | 65.8 |
| Mean characters per page | 334 |
| **Median characters per page** | **169** |
| Pages under 200 chars (text-sparse) | 22,338 (**55.6 %**) |
| **Pages with no text layer but with images** | **6,921 (17.2 %)** |
| Embedded image objects | 149,932 |

Two findings drove the design:

**1. Slide decks are text-sparse by nature.** A median of 169 characters per page
means the average slide is a headline and a picture. Layout-reconstruction
accuracy — the thing the benchmarks measure, and the reason Docling/Marker are
slow — buys very little here. There are no dense multi-column journal layouts or
intricate financial tables to recover. Paying 5–30× the runtime for better
table reconstruction is paying for a problem this corpus does not have.

**2. A sixth of the corpus is invisible to every text-based extractor.**
6,921 pages carry images and no text layer at all. Worse, **seven entire decks
have zero extractable text on every page** — they were exported as flattened
images. Any pure text-extraction pipeline, Docling and Marker included, emits an
*empty or near-empty file* for these and reports success. Among them:

- `Apple macOS Kernel Exploitation with MIE — Building on the Ashes of 100 Vulnerabilities` (58 pp)
- `Scambuster: Social Engineering Scammers at Scale` (90 pp)
- `gpwn: Wiretapping Fiber ISP Deployments` (12 pp)
- `No Tools Required: Post-Injection Exploitation` (46 pp)
- `When Agentic Glue Melts: Exploiting Cloudflare CodeMode` (43 pp)
- `Password Cracking: Past, Present, Future` (Solar Designer keynote, 79 pp)
- `Nakatomi Space` (41 pp)

Silent total loss of whole talks is a much bigger correctness problem than
imperfect table borders. **The binding constraint is coverage, not layout
fidelity.** So the pipeline optimises for coverage first.

### The resulting two-pass design

```
                  ┌──────────────────────────────┐
   PDF page ─────▶│ 1. Structural (PyMuPDF4LLM)  │──▶ headings, bold, lists,
                  │    no ML, ~ms/page, CPU      │    tables, reading order
                  └──────────────┬───────────────┘
                                 │
                   text < 140 chars AND images ≥ 20 % of page?
                                 │ yes
                  ┌──────────────▼───────────────┐
                  │ 2. OCR gap-fill (Tesseract)  │──▶ code, terminal output,
                  │    render 200 DPI → LSTM OCR │    diagram labels, screenshots
                  └──────────────────────────────┘
```

**Pass 1 — structural**, via [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
with its GNN layout engine enabled but its built-in picture OCR turned off. It
reads the PDF's own content stream, so it is exact where a text layer exists,
and it needs no GPU and no model downloads.

That specific configuration was chosen by measurement, not assumption. On a
text-rich 33-page deck (`mTLS: When Certificate Authentication is Done Wrong`):

| Configuration | Time | Chars extracted | Key content recovered |
|---|---:|---:|---|
| Legacy parser (`use_layout(False)`) | 0.04 s/pg | 3,313 | ✗ misses speaker line, figure text |
| Layout engine, built-in OCR **on** (the default) | 0.71 s/pg | 20,651 | ✓ but heavy logo noise |
| Layout engine, built-in OCR **off** | 0.13 s/pg | 12,870 | partial |
| **Layout off-OCR + our gap-fill OCR** | **0.22 s/pg** | **14,131** | **✓** |

Three things this overturned:

1. **The legacy parser is not "good enough".** It extracted a quarter of the
   available text and silently dropped the speaker attribution and all text
   inside figures. The layout engine is worth its 3× cost.
2. **PyMuPDF4LLM's built-in OCR is the expensive part, not the layout model** —
   0.58 of that 0.71 s/pg. And because every conference slide carries a sponsor
   logo, it OCRs that logo into garbage on *every page*
   (`EQ<br>blackhat<br>USA 20253`). Across 40,183 slides that is systematic
   retrieval noise, so it is disabled.
3. **Gated full-page OCR beats per-picture OCR** on both axes: it recovered the
   same key content (speaker name, the RFC 5246 handshake diagram, `ClientHello`)
   at **3.2× the speed** and without the per-slide logo garbage, because it only
   fires on the pages that actually need it — 6 of 33 on this deck.

**Pass 2 — OCR gap-fill**, via Tesseract 5 (LSTM engine). Triggered *only* when a
page is both text-poor and image-dominated. Both gates matter:

- Without the text gate you would re-OCR 40,000 pages that already have perfect text.
- Without the image gate you would spend hours OCR-ing genuinely blank section dividers.

Measured effect on the worst-case deck (`...MIE...`, 58 pages, zero text layer):
structural extraction alone yields **0 characters**; with gap-fill it yields
**17,898 characters across 55 recovered pages**. That deck goes from useless to
usable.

### What this deliberately does not do

**Vector/GPU converters (Docling, Marker, MinerU) were considered and rejected
for the bulk pass.** On 4 CPU cores, Docling's layout + table transformers run
roughly 0.5–1 s per page — 6–11 hours for 40,183 pages, and that is *before*
OCR. Published comparisons put it 5–30× slower than PyMuPDF4LLM per document,
with the advantage concentrated in dense table reconstruction, which this corpus
barely has. It remains the better choice for dense papers, and the whitepapers
occasionally shipped alongside talks are a reasonable place to use it. It is not
the right default for 40k slides on CPU.

**OCR cannot describe a photograph.** A slide showing a technician splicing
fibre at a curbside cabinet contains no text, so Tesseract correctly returns
nothing and the slide appears in the Markdown as a bare `## Slide N`. Recovering
the *meaning* of image-only slides needs a vision-language model captioning each
page render. That is a genuine gap in this corpus, it costs real money at 40k
pages, and it is left as an explicit opt-in rather than silently bundled — see
"Optional: VLM captioning" below.

---

## Output format

One Markdown file per deck, under `markdown/<Conference Folder>/<slug>.md`:

```markdown
---
title: "Apple macOS Kernel Exploitation with MIE ..."
speakers: ["Dion Blazakis", "Josh Maine", "Bruce Dang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Dion Blazakis&....pdf"
pages: 58
sha256: "717065f1889d..."
text_chars: 17898
ocr_pages: 55
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T20:39:48Z"
---
# Apple macOS Kernel Exploitation with MIE ...

**Speakers:** Dion Blazakis, Josh Maine, Bruce Dang
**Conference:** Black Hat USA 2026
**Source:** `...pdf` (58 pages)

## Slide 1
...
```

Choices that matter for retrieval:

- **YAML frontmatter** carries conference, year, speakers and provenance.
  Chunkers strip it, so copy these fields into chunk metadata at ingest — that is
  what makes "show me Black Hat 2026 macOS kernel work" filterable rather than a
  fuzzy vector match.
- **`## Slide N` headings** give any header-aware splitter
  (`MarkdownHeaderTextSplitter` and equivalents) real, semantically meaningful
  boundaries. Slides are natural chunk units; splitting on character count would
  cut mid-slide.
- **OCR text is fenced and labelled** with a warning line. Downstream consumers —
  and the model itself — can tell high-confidence extracted text from
  approximate OCR, which matters when a garbled identifier would otherwise be
  quoted back as fact.
- **`sha256` + `source_pdf`** make every claim traceable to an exact source file,
  and let you detect upstream changes on re-runs.
- **Companion `_tools.txt` / `_code.txt` sidecars** shipped next to a deck are
  folded in under `## Companion resources`. These hold tool URLs and PoC
  pointers — high-value content for a security tool that a PDF-only pipeline
  would drop entirely.
- **`manifest.jsonl`** — one JSON record per deck (status, pages, chars, OCR
  count, output path). Drive ingestion from this rather than globbing the tree.

---

## Usage

```bash
# One-time system dependency (OCR gap-fill); the converter degrades to
# structural-only with a warning if it is missing.
sudo apt-get install -y tesseract-ocr tesseract-ocr-eng

pip install pymupdf pymupdf4llm

# Convert everything in the repo
python3 tools/pdf2md.py --src . --out markdown

# Faster, lossy: skip OCR entirely
python3 tools/pdf2md.py --src . --out markdown --no-ocr

# Convert one conference
python3 tools/pdf2md.py --src "DEF CON 34" --out markdown
```

The run is **resumable**. Results stream to `manifest.jsonl.partial` as they
complete; re-running skips decks already converted. Use `--force` to redo
everything. A full 611-deck run takes roughly 1.5–3 hours on 4 cores, almost all
of it OCR.

### Fetching DEF CON

```bash
python3 tools/fetch_defcon.py --year 34 --dry-run   # inspect remote layout
python3 tools/fetch_defcon.py --year 34             # .rar bundle, else scrape
python3 tools/pdf2md.py --src "DEF CON 34" --out markdown
```

`fetch_defcon.py` tries the single `DEF CON NN presentations.rar` bundle first
(needs `7z`, `unar` or `unrar`; p7zip 23+ reads RAR5 natively) and falls back to
walking the Apache directory index and downloading files individually. Both
paths are resumable.

---

## Credentials in the corpus

**The corpus is verbatim.** Security decks routinely display credentials — demo
AWS keys on a slide, a token in a screenshotted terminal, a private key in an
exploit walkthrough — and the conversion reproduces them exactly as presented.
The Black Hat corpus contains 35 such strings across 4 cloud-security talks, all
AWS access key IDs.

This has a consequence worth knowing before you push anywhere: inside a PDF those
strings are invisible to secret scanners, but as Markdown they are plain text.
**GitHub push protection will reject the push**, naming each detected secret with
a URL to allow it. Allowing them is the deliberate choice to keep the corpus
faithful — the keys are indicators in their own right and searchable as such.

If you would rather not carry them, redaction is available and off by default:

```bash
python3 tools/pdf2md.py --src . --out markdown --redact   # mask during conversion
python3 tools/redact_corpus.py --out markdown             # mask files already converted
python3 tools/redact_corpus.py --out markdown --dry-run   # just report what is there
```

Redaction keeps each match's identifying prefix, so
`AKIA[REDACTED:aws-access-key-id]` still shows what stood there, and records a
`redacted_secrets` count in the frontmatter. Patterns cover AWS access key IDs,
GitHub/Slack/Google/Stripe/OpenAI tokens and PEM private key blocks.

## Optional: VLM captioning for image-only slides

The one thing this pipeline cannot recover is the *meaning* of slides whose
content is a diagram or photograph with no text. To close that gap, render each
image-only page and caption it with a vision model, then append the caption to
the slide section.

The manifest makes the candidate set cheap to find — decks with a high
`ocr_pages` count relative to `pages`, or pages that produced no text from either
pass. Sizing it honestly: roughly 7,000 image-only pages, at a few hundred output
tokens of description each, is a real API bill, so scope it to the decks that
matter to you rather than the whole corpus. Caption text should be written into
the Markdown clearly marked as model-generated description, for the same reason
OCR output is marked — so a downstream model never mistakes a generated
description for something a speaker actually said.

---

## Sources consulted

- [Docling vs Marker vs MinerU: open-source PDF parser benchmark (2026)](https://adityamangal98.medium.com/docling-vs-marker-vs-mineru-the-ultimate-open-source-pdf-parser-benchmark-2026-which-is-best-a36ecbb6c6b1)
- [Best open-source PDF-to-Markdown tools 2026](https://themenonlab.blog/blog/best-open-source-pdf-to-markdown-tools-2026)
- [PyMuPDF4LLM vs Docling for RAG](https://www.file2markdown.ai/blog/pymupdf4llm-vs-docling)
- [OpenDataLoader vs Docling vs Marker vs PyMuPDF4LLM benchmark](https://docs.bswen.com/blog/2026-06-04-benchmark-comparison/)
- [Parsing PDFs for RAG: from MarkItDown to vision-language models](https://medium.com/@jasonyang.algo/parsing-pdfs-for-rag-from-markitdown-to-vision-language-models-5c7fbbf2161a)
- [Improved RAG document processing with Markdown](https://medium.com/data-science/improved-rag-document-processing-with-markdown-426a2e0dd82b)
- [Markdown-first semantics: frontmatter and hidden context for RAG retrieval](https://blog.trysteakhouse.com/blog/markdown-first-semantics-frontmatter-rag-retrieval)
- [Best chunking strategies for RAG (2026)](https://www.firecrawl.dev/blog/best-chunking-strategies-rag)
