# Handoff — Indonesia Emas 2045 review (session of 17 November 2026)

For the next session. Read this first, then the docs in §2. Everything cited here is in the project unless marked "workspace only". The decisions in §3 were **confirmed by the project owner on 17 November 2026**; the next session acts on them without re-asking.

## 1. Where things stand in one paragraph

The Indonesia case has a complete source pack. Three Bappenas documents (the 2017 "Visi Indonesia 2045" oration deck, the May 2023 Musrenbangnas keynote, and the Rancangan Akhir RPJPN 2025-2045 annex) are extracted and analysed; the enacted law (UU 59/2024, with the full 334-page annex) has been obtained, its text layer saved to the project, and reconciled against the draft; and the first five-year plan under the vision (Perpres 12/2025, RPJMN 2025-2029) has been read through Bappenas's own summary book and compared with the vision's phase-1 path. Intake (N1) and the standing check are done. The register (N2) exists as a candidate list in the scope doc; the framing decisions it depends on are now confirmed (§3), but the individual F-items and chapter claims have not yet been validated line by line. No evidence pass (N5) has been run.

## 2. Docs to read, in this order

| Doc | What it holds |
| --- | --- |
| `claude/indonesia-2045-review-scope.md` | Profile, candidate register F1-F13 and chapter claims, clusters A-G, change-scan candidates X1-X10, Tier-1 source pack, limits. |
| `claude/indonesia-2045-three-document-analysis.md` | Per document: normative future, key issues, assumptions, date, period; cross-vintage table of what moved 2017 → 2023. |
| `claude/uu59-2024-enacted-annex-reconciliation.md` | Draft vs enacted annex: four overrides, one new internal inconsistency, everything else unchanged. |
| `claude/perpres-12-2025-rpjmn-standing-check.md` | RPJMN 2025-2029 targets verified against the Ringkasan, beside their RPJPN counterparts; register readings; absent-topic additions. |
| `claude/scenario-review-method.md` | Method v0.2: stages N1-N9, register classes and status scales, change scan, required-rate test. |

Source texts in the project (search or read as needed, not cover to cover):

| Folder / doc | Content |
| --- | --- |
| `Indonesia-UU-59-2024-RPJPN-Enacted/uu59-2024-lampiran-text.md` | Full OCR text layer of the enacted law incl. the 334-page Lampiran (812 kB). Body text good; tables/figures garbled — their values are in the reconciliation doc. Citable: "UU No. 59 Tahun 2024, Lampiran, printed p. N" (printed page = PDF page − 37). |
| `Indonesia-Bappenas-RPJMN-2025-2029/ringkasan-text.md` | Full text of the Bappenas Ringkasan RPJMN 2025-2029 (92 pp.), clean text layer, citable. |
| `Indonesia-Bappenas-RPJPN-2025-2045-Draft/` | Draft annex, structured extraction (chunks, figures, 45-indicator tables, provincial baselines). The scoring base per decision 1. |
| `Indonesia-Bappenas-Visi-2045-Oration-2017/` | 2017 deck, one record per slide, structured data per slide. |
| `Indonesia-Bappenas-Emas-2045-Keynote/` | May 2023 keynote (initial-draft figures). Context only. |

## 3. Decisions — confirmed

| # | Decision | Rationale |
| --- | --- | --- |
| 1 | **Score against the draft-annex extractions** (`...RPJPN-2025-2045-Draft/part1-*`, `part2-*`) **with four overrides from the law**: vision reads "NKRI yang Bersatu, Berdaulat, Maju, dan Berkelanjutan"; IKLH 76.49 → 83.00 added to target 5; formal-job-creation share 35 → 80 added to Tabel 4.2.2 (IE4); Tabel 4.5.1 row 42a replaced by four sub-indices (air 78.53 → 87.05, water 72.02 → 77.50, land 77.97 → 79.74, sea water 81.02 → 88.77). **Cite the law**: "UU No. 59 Tahun 2024, Lampiran, printed p. N". | Enacted annex = draft with light edits; the law copy carries no citation restriction, which closes method proposal 23 for this report. |
| 2 | **Tracks.** RPJPN 2025-2045: normative, quantified, in force → **early-horizon variant** (claims tested, change scan in full; goals and commitments listed and shown "not yet reviewed"). 2017 oration deck: **superseded vision → reduced review** (claims and enabling assumptions tested; targets shown with last-known status and marked "no longer in force"). **Pair the two on the page**: the 2017 deck is the only text old enough to have testable dated targets (high-income by 2035; 6.5 % growth needed for 2020-25). | Under two years since enactment; the 2017 deck carries the readable "how did the assumptions fare" story. |
| 3 | **Required-rate test runs both growth paths**: the RPJMN's operative path (5.3 / 6.3 / 7.5 / 7.7 / 8.0 % for 2025-29, mean ≈ 7 %) presented as the operative one, and the vision's phase-1 range (5.6-6.1 %) presented as the floor. | The government steers by the RPJMN; falling below the vision's own range would put the 2045 arithmetic in trouble regardless of the 8 % ambition. |
| 4 | **Middle-class series: use the BPS series the RPJMN uses** (17.13 % in 2024 → 17.50 % 2025 → 20.00 % 2029) for F6 / 3.3 and change-scan X4; footnote the RPJPN's 38 → 80 % as a different cut-off. | Only the BPS series has published outturns; the RPJPN's definition is not stated. |

Two working rules adopted with them:

- **Replace 2025 "baselines" with 2025 outturns** wherever BPS, BI or Kemenkeu have published them; the RPJPN/RPJMN 2025 figures are projections set in 2023-24.
- **Evidence pass starts with cluster A** (growth, potential growth, TFP, investment, GNI per capita), because every other 2045 target is scaled to it. Then B (industrialisation and trade) and D (fiscal and delivery).

## 4. Findings to carry forward

- Ambition was recalibrated between 2017 and 2023, not abandoned: high-income 2035 → 2038/41; GDP rank #4 → #5; industry 32 % → 28 %; investment share dropped while a productivity (TFP) story took its place; poverty relaxed, Gini and KTI tightened; renewables target more than doubled; the dependency-ratio trough moved from 2028-31 to "already passed". COVID broke the 2017 path in its first five years.
- The income target is a range in the text of both draft and law (USD 23,000-30,300) while the figure prints 30,300.
- The RPJMN keeps the vision's structure and 2025 baselines but sets a steeper growth path (8 % by 2029), a far flatter energy path (renewables 23 % by 2029 vs 70 % by 2045), GHG-reduction series on a different basis (18.37 vs 28.12 for 2025), and several revised baselines (TB 272 → 329; employment social security 43 → 32; disabled in formal work 22 → 10; tax ratio 2025 10.24 vs 10.70-11.20; PISA 2025 "baseline" kept at 396/404/416 although the 2022 outturn was 359/366/383). New programmes not in the vision: Makan Bergizi Gratis, free health checks, sekolah unggul, food estates, 3-million houses, Danantara (as a proposed law), a state revenue agency.
- Register readings so far: F10 continuity supported; F1 growth under pressure from above; F9 fiscal space watch; F8 energy/GHG under pressure; F6 middle class settled by decision 4; 5.1 KTI slightly below path (22.4 % vs 23.3 % for 2029).
- One internal inconsistency in the law: annual GHG baseline 36.65 % in Tabel 4.5.1 vs 32.65 % in Grafik 4.5.1 (test against the Grafik).

## 5. Sources obtained and where they live

| Source | In the project | Not in the project | Public URL |
| --- | --- | --- | --- |
| UU 59/2024 salinan incl. Lampiran, 371 pp., not watermarked | Full text layer: `Indonesia-UU-59-2024-RPJPN-Enacted/uu59-2024-lampiran-text.md`; figure/table values: reconciliation doc | PDF and page images (binary files cannot be written to the project by the assistant; the PDF was sent to the owner as a file and re-downloads directly with curl) | `https://jdih.kemenkoinfra.go.id/dokumen/file/uu/2024/uu-nomor-59-tahun-2024.pdf` |
| Ringkasan RPJMN 2025-2029, Bappenas, 92 pp. | Full text: `Indonesia-Bappenas-RPJMN-2025-2029/ringkasan-text.md` | PDF (sent to the owner; re-downloads with curl) | `https://kinerja.ekon.go.id/perencanaan/download/kementerian-koordinator-bidang-perekonomian-sekretariat-kementerian-koordinator-bidang-perekonomian-2026-rpjmn.pdf` |
| Perpres 12/2025 Lampiran I-IV | OCR-grade figures marked (LI) in the standing-check doc | Everything else | `https://jdih.kemenkoinfra.go.id/perpres-no-12-tahun-2025` — viewer behind a login; web-fetch reads Lampiran I to ~p. 193 in 100k-character windows |

If a page image of the law is ever needed (e.g. to re-check a table cell), re-download the PDF and render the page with `pdftoppm`; PDF page = printed page + 37.

## 6. Open items, in order

1. **Register validation (N2):** go through the scope doc §3 F1-F13 and chapter claims one by one; mark each Stated/Implied, keep or drop, and write the "what would challenge it" line where missing. Add: formal-job share 35 → 80 (goal, IE4); four environmental sub-indices (goals, IE15); the 36.65/32.65 inconsistency, the baseline revisions and the PISA baseline gap (N3). Record the middle-class definition note under F6.
2. **Source pack (method decision 9):** build the Indonesia Tier-1 list with the exact series and URLs: BPS (national accounts, Sakernas, Susenas, middle-class series, population projections 2020-2050), BI (potential growth, BoP), Kemenkeu (APBN, tax ratio, debt), Bappenas (RPJMN, evaluation reports), KLH (GHG inventory, NDC), UN WPP 2024, IMF WEO/Article IV, WTO, World Bank WDI/IEP. Tier 2: OECD survey, ADB ADO.
3. **Evidence pass, cluster A (N5):** growth outturns 2023-2026 vs both paths (decision 3); potential-growth estimates vs the plan's ~3.3 % reading; TFP; GFCF and investment growth vs 6.4-6.7 % / 9.65 %; GNI per capita vs USD 5,410 (2025) and 8,000 (2029). Then clusters B and D.
4. **Change scan (N6):** record X1 from the standing-check doc; evidence X2 (US tariffs 2025 and bilateral arrangements), X3 (generative AI vs the "40 % of jobs" framing), X4 (BPS middle-class decline), X5 (MBG, Danantara, Koperasi Desa Merah Putih and other new vehicles), X6 (nickel/downstreaming markets), X7 (growth outturn), X8 (population revisions), X9 (NDC and inventory), X10 (geopolitical access). Fixed domains; Tier 1/2 evidence; five link fields per link; at most twelve published.
5. **Lampiran II of Perpres 12/2025** (year-by-year matrices): try JDIH Setneg or a regional JDIH mirror for a direct PDF, else read through web-fetch windows. Needed only if a rated figure turns on a yearly milestone.
6. **Page draft:** from `claude/report-page-spec.md`, once clusters A, B and D are rated; limits from the scope doc §7 stated up front; 2017 and RPJPN paired per decision 2.

## 7. Method notes to fold into `scenario-review-method.md`

- Proposals 21 (early-horizon variant), 22 (version control for draft vs enacted texts) and 23 (citation-restricted sources) — 23 resolved here by obtaining the enacted text.
- New: when the first medium-term plan under a vision exists, the standing check records where it departs from the vision's own phase path (growth, energy, baselines); this run found the departures, not the continuity, carried the information.
- New: a "definition drift" field for indicators whose cut-off changes between the vision and later plans (middle class, SME share, desa mandiri).
- New: 2025-style "baselines" that are projections get replaced by outturns as soon as they exist, with both values shown.

## 8. Starter prompt for the next session

Copy this into a new chat in the NBD-Norantz project:

> Continue the Indonesia Emas 2045 review. Read `claude/handoff-indonesia-2045-2026-11-17.md` first; its §3 decisions are confirmed — act on them, don't re-ask. Then read `claude/indonesia-2045-review-scope.md` and `claude/scenario-review-method.md`.
>
> Do, in this order, writing each result to the project before starting the next:
>
> 1. **Validate the register (N2).** Produce `claude/indonesia-2045-register.md`: every F-item and chapter claim from the scope doc §3, each with class (claim / goal / commitment), Stated or Implied with page reference, "depends on", and "what would challenge it". Add the items listed in the handoff §6.1. List goals and commitments from the five indicator tables and the 20 game changers as "not yet reviewed". Mark anything you dropped or merged and why.
> 2. **Build the Indonesia source pack.** Produce `claude/indonesia-source-pack.md`: Tier-1 and Tier-2 sources with the exact series names and URLs, per handoff §6.2. Use web search to confirm each URL resolves and note the latest release date of each series.
> 3. **Run the evidence pass for cluster A (N5).** Produce `claude/indonesia-2045-evidence-cluster-a.md` with one evidence-table row per item (Item ID | Report said, with year | Evidence now, with figures and dates | Source and tier | Rating), using Tier-1 sources only for ratings and 2025 outturns in place of the plan's 2025 projections wherever published. Run the required-rate test on growth and GNI per capita against both paths in handoff §3 decision 3. Every figure carries an "as of" date and a URL.
> 4. **Stop and report**: a short note of which assumptions in cluster A are confirmed / weakened / no evidence, which figures you could not verify at Tier 1, and what you propose for cluster B. Do not start cluster B or the change scan without a reply.
>
> Rules: cite the enacted law as "UU No. 59 Tahun 2024, Lampiran, printed p. N", never the draft; values marked "~" in the extractions are not to be rated; media sources may flag candidates but never support a rating; write findings as facts about the text and the data, not as verdicts on the government.
