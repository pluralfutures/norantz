# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Norantz

*Towards where?* A second reading of national futures. An endorsed sub-brand of Plural Futures ("Norantz, by Plural Futures").

Norantz is a public website that reviews past national vision and scenario reports against what has happened since. For each report it asks: which assumptions held, where things stand against the goals, what has changed since publication, and which recommendations to revisit. The review is done by AI in a repeatable, scalable way, with named human checkpoints.

Handover written 18 November 2026, when work moved from the claude.ai project "NBD-Norantz" to this repo. Read this file, then `docs/decisions.md` and `docs/open-questions.md`. Full brand rules: `docs/brand-guidelines.md`.

## Who it is for

| Reader | Wants | Reads |
| --- | --- | --- |
| General reader, educated non-specialist. **Reference reader: a junior management consultant.** Often on a phone. | What the report was, why it mattered, where things stand | Top of the page, one or two sections |
| Policymaker or adviser | What is new since the report, which assumptions are under pressure, which advice to revisit | Top, then §10 (what has changed) and §12 (recommendations) |
| Policy researcher | Evidence behind each rating, sources, something citable | Down to the register, then the download |
| Report authors and publishers | A fair reading | Right of reply on every page (§16) |

## Repo structure

The repo mirrors the claude.ai project layout, except that the Indonesia analysis docs the project keeps under `claude/indonesia-2045-*.md` live here in `Indonesia-Emas-2045-Analysis/`. Project docs still cite the `claude/` paths; read them as that folder.

| Path | What it holds |
| --- | --- |
| `CLAUDE.md`, `docs/` | This handover: brand, decisions, open questions |
| `Indonesia-Emas-2045-Analysis/` | Indonesia register, source pack, evidence clusters A/B/D, change scan, page draft 0.1. `register.md`, `source-pack.md` and `evidence-cluster-a.md` are byte-identical duplicates of the `indonesia-*` files |
| `claude/scenario-review-method.md` | **The method, v0.2.** Stages N1-N9 (visions) and E1-E8 (scenario sets), register classes, status scales, change scan, required-rate test, 20 open decisions |
| `claude/report-page-spec.md` | **Public page spec, v0.2.** 18 sections (0-17) in four parts, design principles, open questions |
| `claude/report-page-template.md` | Fill-in skeleton, **still v0.1** (out of step with spec v0.2) |
| `claude/espana-2050-page-draft.md`, `claude/template-test-espana-2050.md` | First pilot: España 2050 test fill (template v0.1) and what broke |
| `claude/indonesia-2045-review-scope.md`, `claude/indonesia-2045-three-document-analysis.md` | Second pilot: scope and the three-document analysis (rest in `Indonesia-Emas-2045-Analysis/`) |
| `claude/handoff-indonesia-2045-2026-11-17.md` | Confirmed Indonesia decisions (§3) and the order of work |
| `claude/uu59-2024-enacted-annex-reconciliation.md`, `claude/perpres-12-2025-rpjmn-standing-check.md`, `claude/visi-2045-oration-2017-extraction-plan.md` | Indonesia version control, standing check, 2017-deck extraction plan |
| `BahanPaparanMPPN-VisiIndonesia2045-25September2017.pdf` | The 2017 oration deck PDF (the only source PDF in the repo) |
| `brand/tokens.json`, `brand/logos/` | Design tokens (colour, type, spacing, radius, stroke, shadow, opacity) and the 8 logo SVGs, exported byte-identical from the design-system artifact on 18 Nov. `tokens.json` is the source of truth |
| `brand/tokens.css`, `scripts/build_tokens.py` | CSS variables (`--nz-*`) and type classes (`.nz-type-*`) **generated** from `tokens.json`; never edit the CSS by hand. Usage in `brand/README.md` |
| `claude/norantz-brand-guideline.md` | One-page brand summary (full version now in `docs/brand-guidelines.md`) |
| `Indonesia-*/` | Source extractions, one folder per document. The 2017 oration, the RPJPN draft and the keynote hold `chunks.jsonl` (plus `slides.md`, `*-figures.json`, `glossary.json`, `README.md` where present). The enacted UU 59/2024 and the RPJMN 2025-2029 are single text-layer files (`uu59-2024-lampiran-text.md`, `ringkasan-text.md`) whose headers give source URL, page layout and citation form |
| `ASEAN National Foresight Scenario Reports.md` | Secondary synthesis of ASEAN reports (stored as text; the original name ended `.docx`) |

## Commands

There is no website code, package manager, test suite or linter yet. The only build step is the token generator (Python 3, standard library only):

```bash
python3 scripts/build_tokens.py          # regenerate brand/tokens.css from brand/tokens.json
python3 scripts/build_tokens.py --check  # exit 1 if tokens.css is stale
```

Run `--check` after any change to `brand/tokens.json`. The three duplicate pairs in `Indonesia-Emas-2045-Analysis/` must stay byte-identical: edit both, then confirm with `cmp register.md indonesia-2045-register.md` (and likewise `source-pack.md` / `indonesia-source-pack.md`, `evidence-cluster-a.md` / `indonesia-2045-evidence-cluster-a.md`).

Source-extraction schema (agreed, keep it): one record per page or slide; numbers verbatim from the PDF text layer; anything read off a chart or image prefixed `~` and **never rated**; keep both `pdf_page` and printed page; visual descriptions in Indonesian and English describe logic, not colour.

## Brand rules, short form

- **Read generously. Check rigorously.** State the authors' intent before what changed. Nothing grades a government, an author or a report.
- **Colour tells time; shape tells status.** Loam `#96685C` = what the report said (then). Sky `#42C0EB` = what the evidence shows (now), the signature ink. Text-safe versions: `loam-ink #6E4A40`, `sky-ink #0E6A8C`.
- **No traffic lights.** Status is shape plus a word, in ink, Loam and Sky only. Never red, amber, green.
- **Dotted = expected or planned. Solid = observed.**
- **Ember `#EB6541`** for one call to action per screen at most. Never in data or status.
- Paper `#FBF7F1`, ink `#241A17`. Spectrum only on covers, the home hero and scenario-range bands. Never behind text, never on a vision page.
- Type: **Bricolage Grotesque** (display, headings), **Newsreader** (all reading text, 18px/1.7, 680px measure), **JetBrains Mono** (labels, dates, sources, figures).
- No overall score, no percentages, no grades. Counts by label, always beside coverage and the "not yet reviewed" count.
- No photographs of politicians or officials. No emoji, no exclamation marks.

## Writing and tone

- **The consulting iceberg.** Tip: one finding, ≤25 words. Above the waterline: ≤120-word summary plus three dated findings. Section headings are action titles (findings, ≤15 words). Evidence below. Every layer stands alone.
- **Four beats for every finding:** intent → then (with page ref) → now (dated, sourced) → so what.
- **Figure, then label:** "11.3% in 2025 against a path of 9.8%: behind", never "Behind: 11.3%".
- Sentences average ≤20 words, none over 35. One idea per paragraph.
- Describe, do not grade: "below the path", "the report does not discuss", "worth revisiting", "under pressure from". Never "failed", "missed", "wrong", "scorecard", "verdict". Full word list in `docs/brand-guidelines.md` §6.
- On the page say "a vision" / "a scenario set" / "what has changed since publication". Keep "normative", "exploratory", "change scan" for the method.
- British spelling, sentence case, Oxford comma, numerals for all figures.
- **Working docs** follow the same plain style: a version line ("Version 0.x, date. Draft for review."), tables over prose, findings as facts about the text and the data. Tag weak points in page drafts with **[GAP]** (not held, left empty), **[TRIAL]** (new judgement) and **[STRAIN]** (forced into the wrong shape).

## Evidence rules (non-negotiable)

- Ratings rest on **Tier 1** only (statistics offices, central banks, finance ministries, IMF, World Bank, WTO, ILO, APO). Tier 2 (think tanks) for context and trends. **Media never supports a rating**; it may flag candidates or carry an official figure, which must then be verified at source.
- Every figure carries an "as of" date and a URL.
- 2025 "baselines" in plans are projections: replace them with 2025 outturns where published, showing both.
- Indonesia: cite the enacted law as **"UU No. 59 Tahun 2024, Lampiran, printed p. N"** (PDF page = printed + 37). Never cite the draft.

## Where things stand (18 Nov 2026)

- **Method v0.2** and **page spec v0.2** written; most open decisions have proposed defaults, few are agreed.
- **España 2050** (pilot 1, hybrid, quantified, advisory): 102-item register, 6 of 9 clusters tested, page test-filled on template v0.1. 14 proposed fixes not applied. No change scan or commitment pass yet.
- **Indonesia Emas 2045** (pilot 2, RPJPN 2025-2045 / UU 59/2024, in force, early-horizon variant, paired with the superseded 2017 deck): register validated (35 claims, 87 goal rows, 37 commitments); clusters A, B, D evidenced; change scan run once (X1-X12); **page draft 0.1 complete** to spec v0.2. No rating has been reviewed by a person.
- **Brand v0.1** built as a design system artifact (tokens, 15 components, logo SVGs): https://claude.ai/artifact/DRZLvr6GwRJSaThHXB2pe5. Four brand decisions confirmed by the owner; the rest is draft for review.
- No website code exists yet. Tokens (JSON and generated CSS) and logos are in `brand/`; the 15 components are static HTML/CSS (prefix `nz-`) still only in the artifact, no JS bundle.

## Next steps, in order

1. Indonesia: verify the "verify at source" figures, run the second change-scan collection, recover the missing change-scan URLs, then a human review of every "weakened", "behind" and "not supported" rating.
2. Fold the Indonesia method notes (handoff §7: proposals 21-23, standing-check departures, definition drift, baseline replacement) and the seven spec notes at the end of the page draft into method v0.3 and spec v0.3.
3. Close method decisions 1 (thresholds), 2 (horizon split) and 15 (scope) first; then re-rate España 2050.
4. Update the template and the España page to spec v0.3; rebuild one page in the brand system to test the iceberg and status rules visually.
5. Indonesia clusters C, E, F, G; then pilot 3 (Vietnam 2035 or AmBisyon Natin 2040, classified from the primary text).
6. Settle the name risk (trademark and domain check) before buying a domain.

Ask the owner before changing anything listed as confirmed in `docs/decisions.md`.
