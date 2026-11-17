# Bappenas — Rancangan Akhir RPJPN 2025-2045 (Indonesia Emas 2045) — RAG-ready extraction, PART 2 of 2

Source: `Bappenas-Emas-2045-Plan-143-344.pdf` — PDF pages 143-344 of the 335-page *Rancangan Akhir Rencana
Pembangunan Jangka Panjang Nasional 2025-2045*, the annex to the draft RPJPN law, Kementerian PPN/Bappenas.
Bahasa Indonesia. **Fully rasterised** (one JPEG per page, no text layer). Every page carries the watermark
**"TIDAK UNTUK DIKUTIP / Kementerian PPN/Bappenas"** (not for citation) — kept in `metadata.citation_restriction`
of every record.

This part covers the **tail of Tabel 4.5.1** (rows 37–45 of the headline-indicator table), **Bab V in full**
(regional & infrastructure development, printed pp. 135–310), **Bab VI in full** (implementation & financing,
printed pp. 312–325) and the **Daftar Singkatan** (abbreviations, printed pp. 327–331). Together with
`Indonesia-Bappenas-RPJPN-2025-2045-Draft/part1-*` (front matter + Bab I–IV) the whole annex is covered; both
parts share `doc_id = bappenas-rpjpn-2025-2045-rancangan-akhir` and the same record schema.

> **Page numbering.** The file name says 143-344 but the printed page numbers run **132–331** (PDF p.1 = printed
> 132). Always cite `printed_pages`; `pdf_pages` is 1-based within *this* file.

## Files

| File | What it is |
|---|---|
| `chunks.jsonl` | **236 embedding units**: 183 text chunks (section text split at paragraph boundaries, ≤ 2.6k chars, median 2.4k) + 53 figure records (one per Grafik/Gambar/Tabel and per chapter-opener infographic). This is the file to embed. |
| `sections.jsonl` | 34 section-level records (5.1.2.3, 5.2.1.5, 6.1.2 …) with the full OCR'd text of each section (393k chars in total). Use for "give me the whole section" retrieval or re-chunking. |
| `figures.json` | The 53 figure/table records on their own (same content as the figure chunks, easier to browse). |
| `markdown/*.md` | One Markdown file per Bab: `bab-5-pembangunan-wilayah.md` (690 kB — large because it carries every table as JSON), `bab-6-mengawal-indonesia-emas.md` (30 kB), `bab-4-tabel-4-5-1-lanjutan.md`, `daftar-singkatan.md`. Each figure is rendered in place as a block-quote (summary, visual description, relationships, `structured_data` JSON). **Drop a file into Claude/DeepSeek chat to work on one chapter**; for Bab V you may want to split by region (each `## 5.1.2.x` / `## 5.2.2.x` is self-contained). |
| `pages/page_NNN.jpg` | All 202 pages at 1600 px long side (for the answer UI to show the source page). `NNN` = PDF page. |
| `figures/*.png` | Crops of every figure/table at 200 dpi, named `pNNN_<FigureId>.png`. Multi-page tables have one crop per page (`figure_images` lists them all). |
| `page_map.json` | PDF page → printed page number, plus `duplicate_of` for the five duplicated pages. |

## Record schema (identical to part 1)

### Text chunk (`chunk_type: "text"`)
```
chunk_id          bappenas-rpjpn-2025-2045-draft-<section>-<NN>   e.g. ...-5-2-2-4-03
doc_id            bappenas-rpjpn-2025-2045-rancangan-akhir
part              part2_pdf_pages_143-344
chapter           IV | V | VI | back_matter
section           4.5 | 5.0 (chapter intro) | 5.1.2.3 | 5.2.2.7 | 6.1.4 | bab_V_opener | daftar_singkatan …
section_title     Indonesian heading verbatim
heading_path      "Bab V — Regional and Infrastructure Development toward Indonesia Emas > 5.2.2.4 Arah Kebijakan Wilayah Kalimantan"
seq / n_in_section   position of this chunk within its section
pdf_pages / printed_pages / page_images
text_id           verbatim Indonesian text (OCR, de-hyphenated, paragraphs joined across page breaks, list items one per paragraph). Decimal commas as printed.
figures_referenced   figure ids whose "(Gambar 5.1.8)"-style reference falls inside this chunk
embed_text        heading_path + "\n\n" + text_id   ← embed this
metadata          document-level fields incl. citation_restriction
```

### Figure chunk (`chunk_type: "figure"`)
```
figure_id         "Grafik 5.1.3" | "Gambar 5.2.8" | "Tabel 5.1.10" | "Bab VI opener"
figure_type       map (21) | table (10) | heatmap (7) | chart (5) | concept (5) | infographic (2) | chapter_infographic (2) | table_graphic (1)
caption_id        caption line(s) as OCR'd
title_id / title_en
visual_description_id / _en     what the graphic shows and how it is laid out
structured_data   every number, series, table row, map legend class, corridor theme, policy list as JSON (dot decimals, units explicit)
relationships     explicit edges for flows/hierarchies/spatial assignments ("WM Medan -> Sumatera Utara", "RPJP Nasional -dipedomani-> RPJM Nasional")
summary_en        2-5 English sentences carrying the key numbers
figure_image      path of the (first-page) crop; figure_images lists every page of a multi-page table
embed_text        heading_path + figure id/title + summary_en + visual_description_en + structured_data (truncated)
```

## What is in the figures (the parts Norantz will score against)

**Headline targets.** `Tabel 4.5.1` finishes the 45-indicator table begun in part 1 (rows 37–45: culture, religious
harmony, family quality, gender gap, biodiversity, IKLH, sanitation, waste, energy/food/water resilience, disaster
losses, GHG reduction — each with a 2025 baseline and a 2045 target). `Tabel 5.2.1` gives the three regional
targets (Williamson index 0.778→0.750; KTI share of GDP 21.5→28.5 %; infrastructure stock 46.0→62.0 % of GDP).
`Gambar 5.2.1` gives the **growth and GDP-share trajectory for every island region and for KBI/KTI** in five-year
steps 2022→2040-2045 — the single most checkable regional projection in the document.

**Baselines.** The seven *Potret Pembangunan Wilayah* tables (`Tabel 5.1.2 / .4 / .6 / .8 / .10 / .12 / .14`) carry
**29 indicators × 34 provinces × national value for 2022** (growth, poverty, Gini, IPEI, HDI, unemployment, life
expectancy, stunting, malaria, schooling, APM, JKN/Jamsos coverage, water storage, piped water, sanitation, waste,
housing, electricity, renewables share, 4G, road condition, public-service/transparency/integrity indices, IRBI,
food-security index, food insecurity). Each cell has `value` (float), `printed` (as in the source) and
`bold_in_source` (the source prints provinces that under-/out-perform the national value in red/blue; the scan
does not preserve the colour reliably, so only the emphasis flag is recorded). `Tabel 5.1.1` benchmarks
Indonesia against six countries on ten infrastructure indicators. `Grafik 5.1.3` is the 2015-2022 time series for
housing, piped water, sanitation and urban waste; `Grafik 5.1.4` regional borrowing 2007-2020; `Gambar 5.1.4`
2021 GDP/electricity shares by island.

**Diagnostics.** The seven *Growth Diagnostics* heat tables (`Tabel 5.1.3 / .5 / .7 / .9 / .11 / .13 / .15`) are
colour-dot matrices (province × 8 constraint factors). The dot colours were measured programmatically and stored
as a 0–1 score (green=0 … red=1) plus a 5-bin level; expect ±0.1 / ±1 bin noise at boundaries.

**Policy geography.** Thirteen `Gambar 5.1.x` / `5.2.x` maps (regional-potential maps, theme-and-policy maps,
social- and economic-transformation maps) are transcribed as structured lists: metropolitan areas, PKSN, KEK, KI,
DPP, SKPT, KPPN, technoparks, export hubs, numbered development areas, commodity icons. Where the icon-to-district
assignment was too dense to read reliably the record says so in `structured_data.note`. `Gambar 5.2.3` and the
Bab V opener carry the seven **regional corridor themes**; `Gambar 5.2.2` the **eight disparity issues**.

**Governance.** `Gambar 6.1.1`–`6.1.3` encode the planning-document cascade (RPJPN→RPJMN→RKP→Renstra/Renja,
RPJPD→RPJMD→RKPD), the logframe hierarchy (impact→outcome→output; THIS approach vs SMART indicators) and the
control framework (medium-term/annual × planning/implementation) as node/edge lists.

## Suggested ingestion (same as part 1 and the Keynote folder)

1. Embed `embed_text` of every record in `chunks.jsonl` with a multilingual model (bge-m3, multilingual-e5-large).
2. Store the whole record as payload. At generation time give the LLM `heading_path`, `text_id` (text chunks) or
   `summary_en` + `structured_data` (figure chunks), plus `page_images` so the UI can show the page.
3. Hybrid/BM25 index over `text_id`, `title_id`, `summary_en` to catch exact numbers ("1.684,92" / "1684.92") and
   codes ("PKSN", "IKFD", "3TP").
4. **Row-level index** over `structured_data.rows` of the seven Potret tables (one row per indicator, provinces as
   columns) and over `Gambar 5.2.1.structured_data.regions` for precise lookups ("stunting in NTT 2022?",
   "Kalimantan growth target 2030-2034?").
5. Surface `metadata.citation_restriction` in any answer that quotes this document.

## Caveats

- **Duplicate pages**: PDF pp. 3, 5, 53, 121, 189 are pixel-duplicates of 2, 4, 52, 120, 188 and are skipped
  (`page_map.json` → `duplicate_of`). Printed page numbers therefore run continuously 132…331 with no gaps.
- Printed page numbers are not printed on the two chapter openers (PDF 4, 185); `page_map.json` has `null`.
- The source itself repeats several policy bullets verbatim across regions (e.g. the anti-corruption and
  digital-literacy items in 5.2.2.x) — these are *not* extraction duplicates.
- Source typos are kept as printed (e.g. "logisitik", two consecutive "(vii)" items on printed p. 238, "Zero Delta O").
  Clear OCR errors were corrected (roman numerals "lv)"→"(iv)", "sumbersumber", English abbreviations in the
  Daftar Singkatan); italic English terms in body text may still carry residual OCR errors.
- `Tabel 5.1.10` (Sulawesi) prints row numbers 1–9, 11–30 (no "10"); the record uses the shared 1–29 keys so
  rows align across all seven tables. `Tabel 5.1.14` (Papua) splits road condition into four sub-rows (adds
  "Kota", key `23d`) and uses **pre-pemekaran** data (two provinces) while the maps show six provinces.
- Potret tables: every numeric cell was cross-checked against two independent OCR passes and visually where
  unconfirmed; values the source prints with a stray space ("53,9 0") are normalised ("53,90"). The "Nasional"
  column is taken from the Sumatra table; a few tables print slightly different national figures for the same
  indicator (e.g. growth 5,34 vs 5,31; HDI 72,91 vs 72,80 in Bali-NT) — the per-table value is in `NAS` overrides
  inside the record where it differs.
- Map records: legend classes and named features are exact; *which* district falls in which class is read from
  colour/position and flagged `colour_read` / `approximate` — treat as indicative.
- Growth-diagnostics heatmaps: no numbers are printed in the source; the score is a hue read-out.
- Date/version: this is the **final draft** annex (undated, data through 2022/early 2023). The RPJPN 2025-2045 was
  enacted as **UU No. 59 Tahun 2024**; indicator baselines/targets and the regional trajectories may have moved
  between this draft and the enacted annex — record which version a scenario review is scored against.
