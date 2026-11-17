# Bappenas "Visi Indonesia 2045" oration deck (26 Sep 2017) — RAG-ready extraction

Source: `BahanPaparanMPPN-VisiIndonesia2045-25September2017.pdf` — slides of the Minister of National Development
Planning / Head of Bappenas's *Orasi Ilmiah* at FEB Universitas Indonesia, Jakarta, 26 September 2017.
48 pages, native PowerPoint export (Acrobat PDFMaker 15), Bahasa Indonesia, **real text layer**, no citation
watermark (`metadata.citation_restriction = null`). `doc_id = bappenas-visi-2045-oration-2017`.

This is the **2017 vintage** of the 2045 vision; the 2023 RPJPN 2025-2045 draft and Keynote folders in this
project are its successors. Records carry `structured_data.comparable_to` pointers to the RPJPN figures/tables
that revise the same quantity.

## Files

| File | What it is |
|---|---|
| `chunks.jsonl` | **48 records, one per slide**, all `embed: true` (no duplicate pages). Same schema as the Keynote folder plus `section_en`, `figure_images`. |
| `glossary.json` | 51 acronyms → Indonesian expansion + English gloss; each chunk carries the subset present in it. |
| `structured_data.json` | The `structured_data` of every slide on its own (numbers, tables, phase lists), keyed by page. |
| `slides.md` | Same content as one Markdown file (120 kB) for eyeballing or dropping into a chat. |
| `pages/page-NN.jpg` | 200-dpi page renders (2667×1500), NN = PDF page = printed slide number. |
| `figures/pNN_rasterK_WxH.png` | The 40 raster images embedded in the deck (charts, maps, photos) at native resolution. Vector charts (p9, p10, p23, p34, p35, p38) are not here — use the page render. |

## How it was extracted (differs from the two OCR'd documents)

1. **Text**: taken verbatim from the PDF text layer (`pdftotext` / `pdfplumber`), not OCR. `text_id` is assembled
   from the slide's text boxes in reading order; decimal commas kept as printed (`28.934`, `6,4%`).
2. **Tables** on p11–12 (GDP rankings, 6 × 16 rows) were parsed programmatically from the text layer.
3. **Vision pass** (one per slide, page image + text boxes): reading order, `slide_type`, visual descriptions,
   `relationships`, and `structured_data` values that exist only in raster images or unlabeled charts.
4. **Validator**: every number in `text_id` is checked against the raw text layer of its page. Pass, with two
   declared exceptions — p8 map shares (21/23/59/55/6/7/7/8/4/4/3/3 %) and p19 timeline years — both read from
   raster images and flagged as such in `visual_description`.

## Record schema (`chunks.jsonl`)

```
chunk_id               bappenas-visi-2045-oration-2017-pNN
doc_id / pdf_page / printed_slide_number / page_image / embed / duplicate_of
slide_type             cover | text | concept | chart | table | infographic | map | text_with_map | section_divider | closing
section / section_en   front_matter | vision_pillars | megatrends_demography | economic_scenario |
                       human_capital_sdm_iptek | sustainable_economy | equity_pemerataan | governance_security | closing
title_id / title_en
text_id                verbatim slide text (text layer), reading order; chart axes/legends summarised in [brackets]
visual_description_id / _en   what the graphic shows; raster-read values live here and in structured_data
structured_data        numbers, tables, phases as JSON — dot decimals, units explicit, "~" = read off a chart
entities / relationships / summary_en / keywords_en / glossary
figure_images          raster crops for this page (from figures/)
embed_text             EN keywords + EN summary + ID title + ID text + EN visual description  ← embed this
metadata               document-level fields (event, date, language, vintage, relation to RPJPN draft)
```

## What Norantz will score against (the 2017 assumptions and targets)

| Quantity | 2017 deck value | Slide | RPJPN 2025-2045 draft counterpart |
|---|---|---|---|
| Avg GDP growth 2016-2045 (high scenario) | 6.4 %/yr (phases 6 / 7 / 6.3 %) | 9, 10 | Grafik 4.2.1 (6-7 %) |
| GDP per capita 2045 | USD 28,934 (baseline scenario 19,794) | 9, 10 | Tabel 4.2.2 |
| High-income / MIT exit | 2034-2035 | 10 | 2038 / 2041 |
| World GDP rank 2045 | #4 MER and PPP (PwC: #4 by 2050) | 11, 12 | Gambar 3.4.1 (top-5) |
| Investment share of GDP | 39 % | 9, 24 | Tabel 4.2.2 |
| Industry share of GDP | 32 % (growth 7.8-8.1 %/yr) | 9, 26 | Gambar 4.2.1 (manufacturing 28-30 %) |
| Export world share / rank | 2.0 % / #10 | 31 | Tabel 4.2.2 |
| Population 2045 / urban share | 318.7 m / 69.1 % | 7, 8 | — |
| Dependency-ratio minimum | 46.9 % in 2028-2031 | 7 | — |
| Poverty 2045 / Gini | 0.02 % / ~0.34 (with redistribution) | 34, 35 | Tabel 4.1.1 |
| Eastern Indonesia share of economy | 25.1 % by 2045 (19.5 % in 2015) | 37 | Bab V |
| Regional growth targets | Maluku 9.0, Papua 8.3, Sulawesi 7.4, Bali-NT 7.2, Kalimantan 6.9, Sumatra 6.4, Java 6.1 %/yr | 38 | Bab V |
| Renewables share | 23 % (2025), 31 % (2050) | 23 | Tabel 4.5.1 |
| GHG | −41 % vs baseline by 2030 (29 % + 12 %) | 32 | Grafik 4.5.1 (NZE 2060) |
| R&D spending | 1.5-2.0 % of GDP by 2045 (0.08 % in 2013) | 15 | Tabel 4.2.2 |
| Education | 12 yrs schooling (2026-35), tertiary APK 60 %, 90 % workforce ≥ secondary | 14 | Tabel 4.1.1 |
| Employment | unemployment 3-4 %, formal 85 %, non-agri 89 % | 25 | Tabel 4.2.2 |
| Tourism | 85 m foreign tourists | 28 | Tabel 4.2.2 |
| Maritime sectors | 30 % of GDP | 29 | — |
| Farmer productivity | 4.2× 2015 level by 2045 | 36 | — |

## Suggested ingestion (same as the other two folders)

1. Embed `embed_text` with a multilingual model (bge-m3, multilingual-e5-large); one vector per record.
2. Store the whole record as payload; at generation time pass `title_id`, `text_id`, `visual_description_en`,
   `structured_data`, `summary_en` and `page_image`.
3. Hybrid/BM25 over `text_id` + `summary_en` + `entities` for exact numbers (`28.934` / `28,934`) and acronyms.
4. Optional row index over `structured_data` of p11/p12 (GDP ranking rows) and p38 (regional targets).
5. No citation restriction on this document, but it is a 2017 draft-stage deck; cite as "Bappenas, Visi Indonesia
   2045, Orasi Ilmiah FEB UI, 26 Sep 2017".

## Caveats

- Unlabeled charts: p34 poverty bars, p35 Gini curves, p41 wastewater area chart and p6 growth-rate lines carry
  no printed values; `structured_data` gives `~` readings from the axis.
- p32 emission charts are low-resolution rasters; only the headline figures (41 %, 832/360 MtCO2e) are reliable.
- p19 (Kebudayaan) is a single raster image; all its text was transcribed by vision.
- p26 says industry growth 8,1 %/yr while p9's table says 7,8 % — both preserved as printed.
- p15 GCI table is reproduced as printed (Korea rank 26 listed above Malaysia rank 18; India score 4.52).
- Source typos kept in `text_id` (`keanakeragamanan` p32, `melalu` p38, `Kutznet's` p35, `Amerika Utra` p6).
- Several slides use third-party projections (UN WPP, PwC 2017, WHO 2012, RUEN/DEN 2016, Riskesdas 2013);
  `structured_data.source` records this so the review can separate Bappenas assumptions from borrowed data.
