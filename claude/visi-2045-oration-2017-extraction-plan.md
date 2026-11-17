# Bappenas "Visi Indonesia 2045" oration deck (26 Sep 2017) — extraction plan for RAG

Source: `BahanPaparanMPPN-VisiIndonesia2045-25September2017.pdf` — slides for the Minister of PPN / Head of
Bappenas's *Orasi Ilmiah* at FEB Universitas Indonesia, Jakarta, 26 September 2017. 48 pages, 960×540 pt
(16:9), Bahasa Indonesia. PDF metadata: author *Dwiputra Ahmad Ramdani*, created 26 Sep 2017 with Acrobat
PDFMaker 15 for PowerPoint.

## 1. What this file is (and why it is easier than the other two)

| | RPJPN draft / Keynote (already done) | This deck |
|---|---|---|
| Origin | Rasterised scans, no text layer | **Native PowerPoint export** |
| Text | Tesseract OCR + vision | **Real text layer, fonts embedded with Unicode maps** — ~93 kB, 0 OCR errors |
| Charts | All read by vision | Mixed: ~60 % native (axis/data labels in text layer), ~40 % pasted raster images |
| Encryption | — | Owner password only (`copy:no`); poppler/pdfplumber ignore it, extraction works |
| Watermark | "Tidak untuk Dikutip" | **None** — public oration, no citation restriction |
| Structure tags | — | `Tagged: yes` in pdfinfo but **no StructTreeRoot**, so no reading-order tree to lean on |

Bottom line: **do not OCR this file.** Take verbatim text from the text layer and use a vision model only
for layout/reading order, visual descriptions and the raster charts.

## 2. Per-page text-layer coverage (pdftotext, words per page)

Dense pages (>100 words): 6, 7, 8, 9, 11, 12, 15, 17, 36, 37, 38, 40, 41, 44, 47.
Near-empty pages (section dividers / icon grids): 1, 13, 19 (Kebudayaan — all content is one raster
infographic), 20, 33, 42, 48.

Values that **do** survive in the text layer (verbatim, decimal commas as on the slide):
- p9 baseline vs high scenario table (5.1 / 6.4 % growth, GDP rank 16 → 8 / 4, USD 3,378 → 19,794 / 28,934)
- p10 GDP-per-capita path 3,377 → 4,719 → 6,701 → 9,715 → 14,214 → 20,460 → 28,934 and phase growth rates
- p11–12 full GDP ranking tables (MER and PPP, 2015/2030/2050, 16 countries each) — these are text, not images
- p23 energy table (EBT 23 % → 31 %, >400 → >1.000 MTOE, >115 → >430 GW, 2.500 → 7.000 kWh)
- p38 regional growth targets (Sumatera 6,4 %, Kalimantan 6,9 %, Sulawesi 7,4 %, Maluku 9 %, Papua 8,3 %, Jawa 6,1 %, Bali-NT 7,2 %)
- p34/p35 chart axes and legends (years 2017–2045, Gini axis 0.32–0.44) — **but not the series values**
- p37 KBI/KTI shares 1983/2013/2015/2045, p44–45 phase labels, p47 foreign-policy nodes

Values that are **only in raster images** (need vision, mark estimates with `~` as in the RPJPN schema):
- p7 population pie (10 ASEAN-share pie), p8 Java/urban map + table, p14 engineer bar chart (Vietnam 9 600 … Singapura 3 450)
- p17 cause-of-death pies and stacked bars (WHO 2012), p19 culture timeline, p21/39/40/41 infrastructure maps
- p32 emission baseline bar chart and 2030 reduction target chart (835×403 / 866×393 px — low resolution, read totals only)
- p34 poverty stacked bars (series values unlabelled — read ~ from axis), p35 Gini curves (two scenarios, unlabelled)

## 3. Recommended pipeline

Same output schema as `Indonesia-Bappenas-Emas-2045-Keynote/` (one record per slide, `chunks.jsonl` +
`pages/` + `glossary.json` + `slides.md`) so the three Bappenas documents share one ingestion path.
`chunk_id = bappenas-visi-2045-oration-2017-pNN`.

### Step A — assets (deterministic, ~1 minute)
```
pdftoppm -r 200 -jpeg -jpegopt quality=85 src.pdf pages/page      # 2667×1500 px, 1-based = pdf_page
pdfimages -png -p src.pdf raw_images/img                           # native-res raster images, per page
pdftotext -f N -l N src.pdf -                                      # per-page text, PowerPoint shape order
```
- Drop the recurring decorative objects (obj 6740 side strip, logos ≤130 px) from `raw_images/`; keep the
  large ones listed in §2 as `figures/pNN_<slug>.png`.
- For **vector** charts (p9, p10, p23, p34, p35, p38) crop the chart region from the 200-dpi page render
  using the bbox of its axis labels from pdfplumber, since `pdfimages` has nothing for them.

### Step B — per-slide text boxes (pdfplumber, deterministic)
Use `pdfplumber` `extract_words()` → cluster into text boxes by proximity (PowerPoint shapes), keep
`(bbox, font_size, bold, text)`. Strip the three constant strings on every slide: `REPUBLIK INDONESIA`
(logo caption, top-right), the slide number (bottom-right), and the Wingdings bullet glyphs (`` → `•`).
Title = largest-font box in the top 15 % of the page. Everything else goes to the LLM with its bbox.

### Step C — one vision-model call per slide (the only non-deterministic step)
Input: the 200-dpi page image **plus** the Step-B text boxes with coordinates. Instruction:
> Produce the Keynote-schema record. `text_id` must be assembled **only** from the supplied text boxes,
> verbatim, in reading order you infer from the image (left→right, top→bottom, following arrows/phases) —
> do not retype or "correct" any number. Use the image for `slide_type`, `visual_description_*`,
> `relationships`, and for `structured_data` of raster charts; prefix every value read off an axis or a
> picture with `~`. Numbers in `structured_data` use dot decimals.

This costs 48 calls, keeps every number exact where the text layer has it, and confines vision error to
the raster-only values. Validation rule: every digit sequence in `text_id` must occur in the raw
`pdftotext` output of that page (cheap script; catches hallucinated numbers).

### Step D — document-level fields
```
metadata: {
  doc_id: "bappenas-visi-2045-oration-2017", author_org: "Kementerian PPN/Bappenas",
  speaker: "Menteri PPN/Kepala Bappenas", event: "Orasi Ilmiah FEB Universitas Indonesia",
  date: "2017-09-26", language: "id", citation_restriction: null,
  scenario_vintage: "Visi Indonesia 2045 (2017) — baseline 2015/2016, horizon 2045",
  relation_to_other_docs: "predecessor of RPJPN 2025-2045; same 2045 targets family, earlier numbers"
}
```
Sections (for the `section` field): front_matter (1–2) · vision_pillars (3–4) · megatrends_demography (5–8)
· economic_scenario (9–12) · human_capital_sdm_iptek (13–19) · sustainable_economy (20–32) ·
equity_pemerataan (33–41) · governance_security (42–47) · closing (48).

## 4. Why this document matters for Norantz scoring

It is the **2017 vintage** of the same 2045 vision that the 2023 RPJPN draft (already extracted) revises.
The pairs worth aligning in `structured_data` so the review layer can diff them: GDP per capita 2045
(28,934 USD here vs RPJPN figures), high-income year (2035 here vs MIT exit 2038/2041 in RPJPN),
GDP rank (#4 by 2045 MER), poverty (0,02 % by 2045), Gini (0,34 then 0,44 ceiling), EBT share
(23 % 2025 / 31 % 2050), emissions (−41 % vs baseline), investment 39 % of GDP, regional growth targets
per island. Add a `comparable_to` field on those records pointing at the RPJPN figure ids
(`Tabel 4.2.2`, `Grafik 4.2.1`, `Grafik 4.5.1`, …) when the RPJPN side is known.

## 5. Caveats to carry into the README

- `pdfinfo` reports `Tagged: yes` but there is no structure tree; reading order must come from layout, not tags.
- p19 (Kebudayaan) is a single raster infographic with four words in the text layer — vision only.
- p11–12 tables have 16 rows per column but column headers are split across text boxes; rebuild as rows
  `{rank, country, gdp_usd_bn}` per year, per basis (MER/PPP), per source (Bappenas vs PwC 2017).
- p32 raster charts are too low-resolution for series values; keep only the printed headline (−41 %, IKLH > 80).
- Source typos are preserved verbatim in `text_id` (e.g. "keanakeragamanan" p32); fix them only in `summary_en`.
- Several slides cite third-party sources (UN WPP 2015, PwC 2017, WHO 2012, RUEN/DEN 2016); capture in
  `structured_data.source` so the review can distinguish Bappenas projections from borrowed ones.
