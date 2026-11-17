# Bappenas — Rancangan Akhir RPJPN 2025-2045 (Indonesia Emas 2045) — RAG-ready extraction, PART 1 of 3

Source: `Bappenas-Emas-2045-Plan-1-142-Preview.pdf` — PDF pages 1-142 of the 335-page *Rancangan Akhir Rencana
Pembangunan Jangka Panjang Nasional 2025-2045*, the annex to the draft RPJPN law, Kementerian PPN/Bappenas.
Bahasa Indonesia. **Fully rasterised** (one 3200×4526 JPEG per page, no text layer). Every page carries the
watermark **"TIDAK UNTUK DIKUTIP / Kementerian PPN/Bappenas"** (not for citation) — kept in
`metadata.citation_restriction` of every record.

This part covers the front matter and **Bab I–IV in full** (printed pages i–131). Bab V (regional development,
printed 131-310) and Bab VI (implementation framework) are in parts 2-3 and should be processed with the same
pipeline so the three parts share one `doc_id` and one schema.

## Files

| File | What it is |
|---|---|
| `chunks.jsonl` | **201 embedding units**: 144 text chunks (section text split at paragraph boundaries, ≤ ~2.6k chars, median 2.1k) + 57 figure records (one per Grafik/Gambar/Tabel and per chapter-opener infographic). This is the file to embed. |
| `sections.jsonl` | 54 section-level records (1.1, 2.1.3, 4.2.1 …) with the full OCR'd text of each section and `[[FIGURE: …]]` placeholders where figures sit in the flow. Use for "give me the whole section" retrieval or re-chunking. |
| `figures.json` | The 57 figure/table descriptions on their own (same content as the figure chunks, easier to browse). |
| `markdown/*.md` | One Markdown file per Bab (7-160 kB each; 20-45k tokens). Body text with each figure rendered as a block-quote (summary, visual description, relationships, `structured_data` JSON). **Drop a single file into Claude/DeepSeek chat to work on one chapter.** |
| `pages/page_NNN.jpg` | All 142 PDF pages plus `page_16a.jpg` (printed p.11, supplied separately) at 1600 px long side. `NNN` = PDF page. |
| `figures/*.png` | Crops of every figure/table at 200 dpi, named `pNNN_<FigureId>.png`. Multi-page tables also have full-page crops (`page_096.png` etc.). |
| `page_map.json` | PDF page → printed page number. |

## Record schema

### Text chunk (`chunk_type: "text"`)
```
chunk_id          bappenas-rpjpn-2025-2045-draft-<section>-<NN>   e.g. ...-4-2-1-03
doc_id            bappenas-rpjpn-2025-2045-rancangan-akhir
part              part1_pdf_pages_1-142
chapter           I | II | III | IV | front_matter
section           1.1 | 2.1.3 | 4.0 (chapter intro) | bab_IV_opener | front_matter
section_title     Indonesian heading verbatim
heading_path      "Bab IV — Transformation toward Indonesia Emas > 4.2.1 Iptek, Inovasi, dan Produktivitas Ekonomi"
seq / n_in_section   position of this chunk within its section
pdf_pages / printed_pages / page_images
text_id           verbatim Indonesian text (OCR, de-hyphenated, paragraphs joined across page breaks). Decimal commas as printed (21,6 persen).
figures_referenced   figure ids whose caption falls inside this chunk
embed_text        heading_path + "\n\n" + text_id   ← embed this
metadata          document-level fields incl. citation_restriction
```

### Figure chunk (`chunk_type: "figure"`)
```
figure_id         "Grafik 1.1.3" | "Gambar 3.4.1" | "Tabel 4.2.2" | "Bab IV opener"
figure_type       chart | table | table_graphic | infographic | concept | map | chapter_infographic
title_id / title_en
visual_description_id / _en     what the graphic shows and how it is laid out
structured_data   every number, series, table row, phase, list item as JSON (dot decimals, units explicit). "~" marks values read off a chart axis rather than printed.
relationships     explicit edges for flows/hierarchies (e.g. "Misi 2 -> IE4..IE8")
summary_en        2-5 English sentences carrying the key numbers
figure_image      path of the crop
embed_text        heading_path + figure id/title + summary_en + visual_description_en + structured_data (truncated)
```

## What is in the figures (the parts Norantz will score against)

The **45 headline indicators with 2025 baselines and 2045 targets** are fully captured as rows in
`Tabel 4.1.1` (social, 17 rows), `Tabel 4.2.2` (economic, 23 rows), `Tabel 4.3.1` (governance, 5 rows),
`Tabel 4.4.1` (law/stability/diplomacy, 13 rows); `Tabel 4.5.1` (IE13-17) starts on the first page of part 2.
The five top-level 2045 targets are in `Gambar 3.4.1`; the growth-path assumptions (6-7 % average growth,
MIT exit 2038/2041, manufacturing 21.9 → 26.6 → 30.0 → 28.0 % of GDP, middle class 38 → 80 %) are in
`Grafik 4.2.1`, `Gambar 4.2.1`, `Gambar 4.2.2`; the GHG pathway (annual 1.50 → 0.55 GtCO2e, NZE 2060) in
`Grafik 4.5.1`; the ten megatrend assumptions in `Gambar 2.1.1`; the 20 game changers in `Gambar 3.7.1`;
the 8 missions / 17 directions (IE1-IE17) in `Gambar 3.5.1-3.5.2`.

## Suggested ingestion (same as the Keynote folder)

1. Embed `embed_text` of every record in `chunks.jsonl` with a multilingual model (bge-m3, multilingual-e5-large).
2. Store the whole record as payload. At generation time give the LLM `heading_path`, `text_id` (text chunks) or
   `summary_en` + `structured_data` (figure chunks), plus `page_images` so the UI can show the page.
3. Hybrid/BM25 index over `text_id`, `title_id`, `summary_en` to catch exact numbers ("30.300" / "30,300") and codes ("IE16", "RPJMN").
4. Optional row-level index over `structured_data.rows` of the four indicator tables for precise lookups
   ("2045 target for tax ratio?") — each row already has `arah`, `no`, `indikator`, `baseline_2025`, `target_2045`.
5. Surface `metadata.citation_restriction` in any answer that quotes this document.

## Caveats

- **Printed page 11 is missing from the PDF** (PDF p.16 = printed 10, p.17 = printed 12). It was supplied afterwards
  as a separate image and is included as pseudo PDF page **`16a`** (`pages/page_16a.jpg`), carrying Grafik 1.1.6 (IKLH),
  Grafik 1.1.7 (padi & perikanan) and Gambar 1.1.2 (infrastructure 2014-2022) plus its five lines of body text,
  slotted into section 1.1 between pages 16 and 17. Grafik 1.1.7 has no printed data labels, so its values are `~` estimates.
- PDF pages 131, 133, 138, 140 are duplicates of 130, 132, 137, 139 (skipped); pages 71-72 are blank.
- Printed page numbers are not read on every page (chapter openers, some figure pages); `page_map.json` has `null`
  there. Pages 26-27 (= printed 21-22), 32 (27), 66 (61), 85 (78), 89 (82), 93 (86), 99 (92) were fixed by hand.
- Numbers in `structured_data` that are only readable from a chart axis (not printed) are prefixed "~".
  Check-marks in `Tabel 4.2.1` (industry × corridor matrix) are approximate for multi-row cells.
- The `Tabel 2.3.1` Sulawesi cell repeats its sentence twice in the source; the "Baseline 2025" column in all
  indicator tables is itself a **projection**, per the table footnote.
- OCR: Tesseract 5 `ind` at 200 dpi, body-text accuracy is high; residual errors are mostly in italic English
  terms. Figure-internal text was excluded from the body and read separately by a vision model.
- This is the **final draft** (`Rancangan Akhir`) annex, undated (data through 2022/early 2023). The RPJPN
  2025-2045 was enacted as **UU No. 59 Tahun 2024** (promulgated 13 September 2024, Lembaran Negara 2024 No. 194).
  The enacted vision already differs from this draft: law = "NKRI yang **Bersatu**, Berdaulat, Maju, dan
  Berkelanjutan"; draft = "NKRI yang Berdaulat, Maju, dan Berkelanjutan". Indicator baselines/targets may also
  have moved — record which version a scenario review is scored against, and treat the enacted annex as the
  authoritative one once obtained.
