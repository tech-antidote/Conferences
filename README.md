# Conferences

Security conference presentation slides, plus a Markdown conversion of the whole
archive built for LLM/RAG ingestion.

## Markdown corpus

[`markdown/`](markdown/) holds every deck converted to Markdown — one file per
talk, with YAML frontmatter for metadata filtering and `## Slide N` headings as
natural chunk boundaries.

- [`markdown/README.md`](markdown/README.md) — corpus overview and ingestion notes
- [`markdown/INDEX.md`](markdown/INDEX.md) — every talk, by conference, with speakers
- `markdown/manifest.jsonl` — one JSON record per talk; drive ingestion from this

Rebuild or extend it with the tools in [`tools/`](tools/):

```bash
pip install pymupdf pymupdf4llm
sudo apt-get install -y tesseract-ocr tesseract-ocr-eng   # OCR gap-fill

python3 tools/pdf2md.py --src . --out markdown            # convert everything
python3 tools/build_index.py --out markdown               # regenerate the index
```

[`tools/README.md`](tools/README.md) documents why the converter is built the way
it is — in short, these are slide decks, not papers: median text density is 169
characters per page, and 17% of pages carry images with no text layer at all, so
a plain text-extraction pipeline silently emits empty files for entire talks.

## Adding DEF CON

DEF CON publishes its presentations on `media.defcon.org`.
[`tools/fetch_defcon.py`](tools/fetch_defcon.py) mirrors a year's material —
preferring the single `.rar` bundle and falling back to walking the directory
index — after which the normal converter runs over it:

```bash
python3 tools/fetch_defcon.py --year 34 --dry-run   # inspect the remote layout
python3 tools/fetch_defcon.py --year 34             # mirror into "DEF CON 34"
python3 tools/pdf2md.py --src "DEF CON 34" --out markdown
python3 tools/build_index.py --out markdown
```

Both the mirror and the conversion are resumable, so an interrupted run picks up
where it stopped.

## Slides in this repository

- BlackHat USA 2026 (August 1-6)

- BlackHat USA 2025 (August 2-7)

- Offensivecon 2025 (May 16-17)

- Black Hat Asia 2025 (1-4 April)

- Black hat Europe 2024 (9-12 December)

- Hexacon 2024 Slides (4-5 October)

- Black Hat USA 2024 slides (3-8 August)

- REcon 2024 Slides (28-30 Jun)

- Offensivecon 2024 (May 10-11)
  
- Blackhat Asia 2024 (April 16-19)

- Blackhat Asia 2023

- Offensivecon 2023

- Blackhat USA 2023

- Recon 2023

- Blackhat Europe 2023
