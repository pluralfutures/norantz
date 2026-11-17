# Bappenas Keynote "Indonesia Emas 2045" — RAG-ready extraction

Source: `Bappenas-Keynote-Emas-2045.pdf` — Keynote speech, Minister of National Development
Planning / Head of Bappenas, Musrenbangnas for RPJPN 2025-2045, Bali, 22 May 2023. 26 pages,
fully rasterised (no text layer), Bahasa Indonesia. Every slide carries the watermark
**"Tidak untuk Dikutip"** (not for citation) — kept in `metadata.citation_restriction`.

## Files

| File | What it is |
|---|---|
| `chunks.jsonl` | 26 records, one per PDF page. 24 are `embed: true`; pages 7 and 18 are pixel-duplicates of 6 and 17 and are marked `embed: false` with `duplicate_of`. |
| `glossary.json` | 56 acronyms/terms → Indonesian expansion + English gloss. Each chunk also carries the subset of glossary entries that appear in it. |
| `slides.md` | Same content rendered as one markdown file (useful for eyeballing, or as an alternative ingestion format). |
| `pages/slide_NN.jpg` | Native-resolution page images (3200×1800), 1-based, matching `pdf_page`. Keep them next to the index so the answer layer can show the original slide. |

## Record schema (`chunks.jsonl`)

```
chunk_id               bappenas-keynote-2045-pNN
pdf_page               1..26   (physical page in the PDF)
printed_slide_number   number printed on the slide (differs from pdf_page after the duplicate on p7); null for cover/closing/appendix
page_image             relative path to the JPG
embed                  bool — false for the two duplicate pages
duplicate_of           chunk_id of the original, or null
slide_type             cover | text | diagram | chart | infographic | concept | map | heatmap | table | text_with_map | closing | section_divider | duplicate
section                front_matter | achievements_2014_2022 | global_challenges | development_capital | approach_shift | vision_2045 | grand_strategy | vision_targets | transformation_agenda | social_transformation | economic_transformation | governance_transformation | development_phases | regional_inequality | regional_priorities | central_regional_alignment | appendix
title_id / title_en    slide title, Indonesian verbatim / English
text_id                ALL readable slide text, verbatim Indonesian, hierarchy kept as bullets. Decimal commas preserved as on the slide (21,6%).
visual_description_id  what the diagram/chart/map shows and means (Indonesian)
visual_description_en  same, English
structured_data        tables, chart series, hierarchies, graph edges as JSON. Numbers normalised to dots (21.6), units explicit.
entities               numbers-with-context, programme names, acronyms (mixed ID/EN, dot decimals)
relationships          explicit edges for flows/hierarchies ("Misi 2 Transformasi Ekonomi -> IE4..IE8")
summary_en             2-6 sentence English summary carrying the key numbers
keywords_en            English retrieval keywords
glossary               {acronym: {id, en}} for acronyms present in this chunk
embed_text             the string to embed: EN keywords + EN summary + ID title + ID text + ID visual description
metadata               document-level fields (author, event, date, language, citation restriction, underlying source)
```

## Suggested ingestion

1. Embed `embed_text` with a multilingual model (bge-m3, multilingual-e5-large, or any
   embedding model that handles Indonesian). One vector per record where `embed == true`.
   This gives English *and* Indonesian queries a path to each slide without duplicating vectors.
2. Store the whole record as the payload; at generation time pass `title_id`, `text_id`,
   `visual_description_en`, `structured_data` and `summary_en` to the LLM, plus `page_image`
   so the UI can show the slide.
3. If your store supports hybrid/BM25, index `text_id` + `summary_en` + `entities` for lexical
   matching — this catches exact numbers ("30.300", "30,300") and acronyms ("IE16", "RPJMD").
4. Optional second index for `structured_data` rows (e.g. one row per province on p16, one row per
   indicator on p26) if users will ask precise lookup questions ("GRDP per capita of Maluku in 2022").
5. Surface `metadata.citation_restriction` in answers that quote this source.

## Caveats

- p19 heatmap severities are read from dot colours (ordinal 0-4); the slide publishes no numbers.
- p20 thematic map of Maluku: labels are too small to transcribe fully; `structured_data.map_features_partial` lists what is legible.
- p26 footnote (b): the 2005 HDI baseline (72.80) uses the old method and is not comparable with 2010-2022 values.
- Pages 7 and 18 are duplicates; `printed_slide_number` is therefore offset from `pdf_page` by 1 after p6 and by 2 after p18.
