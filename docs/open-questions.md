# Open questions

Everything unresolved, half-finished or ambiguous at handover, 18 November 2026. Grouped by area; within each, the items that block other work come first. Where a doc proposes a default, it is given, but a default is not a decision (see `decisions.md` for what is settled).

---

## 1. Brand

### Open decisions carried from brand v0.1

| # | Question | Proposed default | Blocks |
| --- | --- | --- | --- |
| 1 | **Is the rest of brand v0.1 approved?** Only four points were confirmed (endorsed sub-brand, PF v2, neutral status, name as a question). Positioning, taglines, personality, word list, tokens, components and logo were drafted from them and never reviewed. | Treat as the working standard; owner to review. | Anything public |
| 2 | **Public rating labels**: "Holds", "Goes further", "Holds in part", "Not supported so far", beside register terms Confirmed / Strengthened / Weakened / Invalidated. Also spec open question 1. Page draft 0.1 used the longer "Not supported by evidence so far". | The four short labels; test with readers. Untested on an in-force claim. | Every page |
| 3 | **Endorsement wording**: "by Plural Futures" or "A Plural Futures project". | "by Plural Futures" (lockup text BY PLURAL FUTURES). | Lockup, footer |
| 4 | **The wordmark is a drawn draft**: monoline construction on a 40-unit x-height, 7-unit stroke. Needs a type designer for spacing and the `t`. | Commission before launch. | Launch |
| 5 | **Translations** of the name line ("towards where?") and the descriptor for Spanish, Bahasa Indonesia and others; how the wordmark behaves on language versions. | None proposed. | Language switch |

### Inconsistencies found while writing this handover

- **"loam-soft"** is named in the brand book's dark-theme text but no such token exists. The dark value of `loam` is `#C9A79C`; `docs/brand-guidelines.md` uses that. Rename in the text or add the token.
- **Ember has two roles.** It is the call-to-action ink ("never in data or status") and also listed as one of four scenario inks (`ember` + `scenario-wash-1 #FBE7DE`) on scenario-set pages. A scenario line in Ember is data. Decide whether scenario sets use Ember or another ink.
- **Measure** is stated as both "60-72 characters" / `measure` 680px and "66ch" (inheritance table). Pick one definition for CSS.
- **"Game-changer" is a banned word**, but Indonesia's RPJPN names its 20 measures "game changers" and the page draft uses the term throughout. Decide whether a report's own term may be used as a proper name.
- The brand's illustrative examples (e.g. "Growth holds; the jobs goal is behind its path", "14 of 18") use made-up figures. Keep them out of anything public.

### Not yet built

- Logo SVGs and `tokens.json` are now in `brand/` (checksums match the artifact). `brand/tokens.css` is generated from the tokens by `scripts/build_tokens.py`. Still to do: export the 15 component previews and `components/bundle.css`, which are only in the artifact.
- Fonts are hosted (Google Fonts), no files. Decide whether to self-host (all three faces are open-licence; check before shipping).
- Components are static HTML/CSS previews (`bundle.css`, prefix `nz-`); no JavaScript bundle, no site code, no chart library chosen.
- Not designed visually: home page, country and theme indexes, cross-report comparison view, method page, social cards beyond the rules, deck template. Their structure and content are in `docs/site-architecture.md` v0.1.
- No reader has seen any of it laid out or on a phone.

## 2. Name and launch

1. **Trademark and domain check before buying a domain.** A Gipuzkoa camper-van maker trades as Norantz (4×4 line Ipar; still launching models in 2026). `norantz.org` hosts an academic database on northern Basque grammar; a Berria demolinguistic projection also uses the word in its title. Searches were partial (the first was autocorrected). Needs a trademark lawyer; vehicles and research services usually sit in different classes. Fallback name not chosen.
2. **Native-speaker check** of Norantz's connotations has not been done.
3. **España 2050 launch timing.** The original brief (16 Nov) was to release the España 2050 review before the Spanish general election, for PR. Nothing since confirms the date or whether this still holds. A pre-election release of a review of a government report raises neutrality questions the site's design depends on (method decision 4, "care around elections" in the 16 Nov website brief). Owner to decide.
4. **Funding and selection transparency** (raised in the 16 Nov website brief: visible funding, why these reports and not others) has a page in the site architecture (`/about/funding/`) but no policy yet.

## 2a. Site (`docs/site-architecture.md` v0.1)

| # | Question | Proposed default | Blocks |
| --- | --- | --- | --- |
| 1 | Basemap convention for disputed borders (South China Sea, Kashmir, Western Sahara and others) | Choose one convention and state it under the map | Map |
| 2 | Licence for reviews and data | None proposed (a Creative Commons licence suggested) | Data and citation, Terms |
| 3 | Election policy | None proposed | Editorial standards, España 2050 launch |
| 4 | Right-of-reply process | None proposed (also spec gap §16) | For report authors |
| 5 | Spanish lawyer to confirm the legal pages (S13) and which language version binds | Spanish text binds | Legal |
| 6 | Email provider and analytics tool | Cookie-free analytics, so no banner | Sign-up, Privacy, Cookies |
| 7 | Review-state marks on the map (solid Sky, dotted Sky, Loam outline) | Test with readers | Map |

## 3. Method (`claude/scenario-review-method.md` v0.2)

### Open design decisions

Decisions 1, 2 and 15 should be closed first: 1 and 2 change ratings already made; 15 decides how much of the corpus is in scope.

| # | Decision | Proposed default | Where it stands |
| --- | --- | --- | --- |
| 1 | Rating thresholds | Per item type, set before the evidence pass, recorded in the register | Applied for Indonesia cluster A only (register §11). Not set for B or D, nor for España. |
| 2 | Horizon | Split each rating: tracking to date / still plausible by the horizon year | España test: fitted 2 of 6 themes; needs "already passed" and "does not apply" (standing conditions). |
| 3 | Implied assumptions | Publish, labelled implied, after human validation | Not validated by a person for either pilot. |
| 4 | Missing scenarios | Describe the observed path neutrally; say the report did not model it | Used in both page drafts. |
| 5 | Recommendation relevance | "Revisit" only when a load-bearing item is weakened, invalidated or under pressure | **Gives wrong answers**: España (weakened growth makes productivity proposals more urgent, not less); Indonesia (16 of 20 game changers get the same label because of F9). Template test proposes asking whether evidence weakens or strengthens the case, plus "more urgent". |
| 6 | Coverage before publishing | Publish with untested clusters "not yet reviewed" | Assumed. |
| 7 | Verification | Spot-check every "invalidated"/"behind" figure at the primary source; independent check for headlines | Not done for either pilot. |
| 8 | Report types | Three intake attributes, two tracks | Written; needs agreement. |
| 9 | Country source packs | Build and approve per country before the evidence pass; shared foresight/risk pack for the change scan | Indonesia pack built, not approved. Shared pack has one entry (WEF Global Risks 2026). España has none written down. |
| 10 | Cross-report taxonomy | Shared top level, report-specific clusters beneath; change-scan domains to match | Not drafted. Blocks "related reports". |
| 11 | Public layer | Short findings page plus register | Assumed. |
| 12 | Languages | Report's own language and English at minimum | Site languages set by decision S8 (English, Spanish, Indonesian; `/es/`, `/id/`). Report pages: still the default. Both drafts English only. |
| 13 | Refresh cadence | Fixed cycle, dated versions | No cycle set. Indonesia proposes next review after BPS full-year 2026 release (5 Feb 2027). |
| 14 | Media as evidence | Out of ratings; standing check and candidates only | Confirmed in practice; needs a written line on **media as a carrier of official figures** (both pilots reached Tier-1 figures through news pages). |
| 15 | Scope | Include long-horizon visions; exclude ordinary medium-term plans | Assumed by all work. **Blocks the map** (S7): the catalogue makes the scope public. |
| 16 | Proxies for qualitative goals | Prefer government-adopted indicators; label every proxy; human validation | Untested (pilot 3 would test it). |
| 17 | Superseded visions | Reduced review | Used for Indonesia's 2017 deck. |
| 18 | Change-scan size and repeatability | Fixed sources and domains; two independent runs; at most twelve published | **Only one run** done (Indonesia). |
| 19 | Public wording for goal status | Figure and gap first; test softer labels ("below the path") | Untested with readers. |
| 20 | Change scan on the exploratory track | Coverage reading only | Track never run. |

### Proposals waiting to be folded into the method (v0.3)

- **21** Early-horizon variant (confirmed for Indonesia; not yet written into the method).
- **22** Version control for draft vs enacted texts.
- **23** Citation-restricted sources ("Tidak untuk Dikutip" watermarks). Closed for Indonesia by citing the law; still open in general, and the 2023 keynote and the draft annex still carry the mark.
- Standing check records where the first medium-term plan departs from the vision's own phase path (growth, energy, baselines); the departures carried the information.
- A **"definition drift"** field for indicators whose cut-off changes between plans (middle class, SME share, desa mandiri).
- Projected baselines replaced by outturns as soon as they exist, both values shown.
- The 14 template-test changes from España (`claude/template-test-espana-2050.md`), notably: rate each item on two questions (did the variable move as said; does the argument still hold) with a short qualifier; split omissions into "known at the time and left out" and "arose after publication" (hindsight: España is flagged for not discussing Ukraine, nine months before the invasion).

### Other method gaps

- **Who the human reviewers are, and to what standard.** Checkpoints are informal. No rating in either pilot has been reviewed by a person.
- Time and cost per report never measured.
- The exploratory track (E1-E8) has never been run.
- What counts as "best rate on record" in the required-rate test needs a fixed data source per country.

## 4. Public page (`claude/report-page-spec.md` v0.2)

### Spec open questions

| # | Question | Proposed default |
| --- | --- | --- |
| 1 | Use "Invalidated" publicly? | No; test "Not supported by evidence so far" |
| 2 | Name a single closest scenario in §8? | Only when most elements agree |
| 3 | Do §1 tallies work as a score? | Counts by label, never a percentage, always beside coverage. Indonesia note: "10 of 16 weakened" could still be quoted |
| 4 | Page length on a phone | §1 and §2 open, rest collapsed with jump links; §10 also open for a vision |
| 5 | Status scale for §4 (questions) | Trial still central / changed shape / overtaken. España test asks to add "not yet reviewed" and "more pressing" |
| 6 | Labels per assumption in §7 | Two on the page (rating so far, pressure); horizon view in the register |
| 7 | Do §6 and §7 repeat each other? | Indonesia fill: yes; proposal to keep §6 as the one-screen phone view and collapse §7 by default |
| 8 | Does the §10 challenges list read as criticism? | Keep "in the report?" as a plain fact, always show opportunities beside it, lead with the change |
| 9 | Challenges/opportunities on a phone | Two equal tabs; or one table with a direction column (Indonesia fill suggests testing this) |
| 10 | Superseded vision: full or short page? | Full skeleton with banner, §14 moved up |
| 11 | What to call a "normative" report publicly | "Vision", "scenario set" |

### Notes from the Indonesia fill (end of `claude/indonesia-2045-page-draft.md`)

1. **No slot for a paired predecessor** in spec v0.2. Needed a sub-header, a card in §5, blocks in §8, §9 and §14, and a tally line. Proposal: a predecessor/successor slot in the header and a standard "no longer in force" block in §5 and §9.
2. **§10 is the longest section** even at twelve changes; three changes appear in both lists; "both ways" rows may read as padding.
3. **§12 loses discrimination** when one assumption (F9) underlies most measures. Needs a per-measure delivery check.
4. §6 repeats §7 (see above).
5. "Not supported by evidence so far" used once (O-2, a historical target); unknown for an in-force claim.
6. Tallies: the coverage figure does the protective work.
7. Early-horizon pages centre on "what has changed" rather than "how is it going"; needs a reader test.

### Gaps no method stage fills yet

Commissioner, political moment and decision questions (§3, §4); a rubric for whether a question still matters (§4); plain-language stories for each future (§5); trigger levels (§13); afterlife of an exploratory report (§14); right of reply process: who is contacted, when, how long they have (§16); related reports (needs decision 10); "cite this page", data download and "report an error" (§17) have no implementation.

### Out of step

- `claude/report-page-template.md` is still **v0.1** (17 sections, old numbering, "Scenarios are not predictions" fixed text that is wrong for visions).
- `claude/espana-2050-page-draft.md` follows template v0.1.
- Only the Indonesia draft follows spec v0.2.

## 5. Indonesia Emas 2045 (half-finished)

### Before the page could be published

- **Verify at source** (read through secondary carriers): World Bank Atlas GNI per capita 2025 USD 5,120 (via Katadata and Kemenko Perekonomian; check data.worldbank.org); BPS 2026 quarterly growth and manufacturing shares (BRS PDFs not opened); SNDC 2030 figures 1.35-1.49 Gt (read via Argus, Kompas, IESR, CAT, not the UNFCCC document) and **whether the vision's 1.03 Gt and the SNDC are on the same FOLU basis**; BI cumulative tightening (75 bp or 100 bp depending on carrier; cite BI's own releases); Brent "roughly doubled" (press reports); EMDE share of world output ≈ 60 % PPP (via commentary); historical "best on record" growth figures (1996; 2010-12) in the required-rate test.
- **IKU air-quality target**: OCR reads 97.05, reconciliation doc 87.05 from the page image. Check the page image (PDF page = printed page + 37) before rating.
- **Second change-scan collection run**, from the same source list, without reading run 1 (decision 18).
- **Recover the change-scan URLs** for X3, X4, X5 (KDMP), X8, X9, X10 into `claude/indonesia-2045-change-scan.md` (flagged [GAP] in page §17).
- **Human review** of every rating, especially the ten "weakened", the four "behind" and O-2 "not supported".
- **Right of reply**: Bappenas not contacted.
- **Next review date** not set (proposed 5 Feb 2027); **no public address**, citation text, data download or error channel.

### Not yet done

- Clusters **C** (demography and consuming class: F2, F6a, F6b, 2.1, 2.2, 3.3, O-4), **E** (technology: F7, 1.4, 1.5), **F** (climate and resources: F8, 2.4, 4.1, 1.8), **G** (regional: 5.1, 5.2, 1.6). 17 of 35 claims not reviewed; 82 of 87 goal rows not reviewed; 0 of 37 commitments assessed.
- Rating thresholds for clusters B to G (only cluster A has them).
- **Lampiran II of Perpres 12/2025** (year-by-year matrices): not obtained. JDIH viewer is behind a login; try JDIH Setneg or a regional mirror. Needed only if a rating turns on a yearly milestone. RPJMN CPI 2029 figure 43.7 is marked (LI, unverified).
- §3 of the page: the "Indonesia Emas" branding decision, political sponsor, parliamentary passage, consultation detail and the modelling behind the growth scenarios are not recorded.
- The "without action" case is not quantified beyond the growth paths.

### Ambiguities to settle before rating

- F3: the unit of the −0.66 TFP figure is not printed (read as % a year, APO convention); APO 2025 uses a different method from the edition the law cites.
- F4: the 3.4 % trade figure has no base period or source in the law.
- F7: no source or date for "40 % of jobs".
- F8: the RPJMN's GHG series is on a different basis (18.37 vs 28.12 cumulative, 2025); definitional note needed.
- Manufacturing share has a 2010 classification break; the 2005-22 fall is not one series.
- Tax ratio: computed by DDTC/Kontan from Kemenkeu and BPS; the plan's definition may include natural-resource non-tax revenue.
- Potential growth (1.2) rated on inference (IMF output gap plus growth path); no Tier-1 body publishes a figure.
- Middle class: BPS's own 2025 figure not yet published (X4 rests on Mandiri Institute's processing of Susenas 2025).
- Definitions to check: I-14a SME share (RPJMN definition differs); I-23c desa mandiri.
- KDMP and Danantara figures are ministerial statements; no audited data. MSCI's June 2026 market-integrity concerns were set aside (Tier 3 only).
- The 2017 deck is internally inconsistent (industry growth 7.8 % on slide 9 vs 8.1 % on slide 26; GCI ranks out of order on slide 15). Slide-9 value used.

### Offered, no answer recorded

- Extract the 2019 *Ringkasan Eksekutif Visi Indonesia 2045* (the vintage between the 2017 deck and the 2023 draft: 5.7 % average growth 2016-45, high income by 2036, 319 m population, renewables 30 %, industry 26 % of GDP) into `Indonesia-Bappenas-Ringkasan-Eksekutif-2019/` with a `comparable_to` field.
- Build a single flat table of the 45 headline indicators and the 29 × 34 provincial baselines as the scoring surface.

## 6. España 2050 (half-finished)

- The **fiscal and housing evidence review** (clusters 5 and 6) exists only in an earlier chat (https://claude.ai/chat/75a88482-d8a5-41fa-9b68-362dd9b40d0f), not as a saved doc; its findings are not in the register.
- The pilot register (102 items) is in an artifact (https://claude.ai/artifact/NhRYA5RCxM5XtLTsuT6bk4), not in the repo, and has no class field.
- Clusters not tested: climate timing, the EU-8 benchmark, political delivery (its commitments).
- No change scan; no commitment pass; the report's ~200 proposals were never logged, so recommendations cannot be tied to register items.
- Ratings need a second pass once method decisions 1 and 2 are closed. Six ratings carry qualifiers the scale lacks ("invalidated on level, confirmed on mechanism", "confirmed, provisionally", "invalidated to date", "strengthened as risks", two split ratings). The same evidence gets opposite ratings (migration "invalidated" for F5, "strengthened" for 7.5).
- Several official figures were cited through news pages; verify at source.
- No link to the original report was recorded; §13 (what happened to the report) not researched; authors not invited.

## 7. Repo and data housekeeping

- **Repo vs project, checked 18 Nov.** The five large source files (UU 59/2024 Lampiran text, RPJPN draft part 1 and part 2 chunks, part 2 figures, 2017-deck chunks) are byte-identical to the project. The other files passed spot checks of distinctive lines. Some were rebuilt or retyped in the first upload on 17 Nov (2017-deck `slides.md` and `structured_data.json`, `part1-figures.json`, the `claude/` docs and READMEs) and may still differ in small details, such as a bullet symbol. Diff against the project before relying on exact text.
- **Path mismatch.** The Indonesia analysis docs sit in `Indonesia-Emas-2045-Analysis/` here but are cited as `claude/indonesia-2045-*.md` in the project docs (handoff, page draft, register). Decide whether to move them or update the references.
- **Duplicates.** In `Indonesia-Emas-2045-Analysis/`, `register.md`, `source-pack.md` and `evidence-cluster-a.md` are byte-identical to `indonesia-2045-register.md`, `indonesia-source-pack.md` and `indonesia-2045-evidence-cluster-a.md`. Keep one of each.
- The root `README.md` is a one-line placeholder (`# norantz`).
- The `add-project-files` branch is still on GitHub; deleting it was asked and not answered.
- **Most binary sources are not in the repo.** Present: the 2017 deck PDF (`BahanPaparanMPPN-VisiIndonesia2045-25September2017.pdf`) and `Indonesia-Bappenas-Emas-2045-Keynote/bappenas-keynote-2045-rag.zip`. Missing: the PDFs of UU 59/2024 (salinan), the Ringkasan RPJMN, the keynote and the draft annex parts; page renders and figure crops; the 2017-deck and RPJPN part 1/part 2 RAG zips (sent as files in earlier chats). Decide whether to store them (Git LFS) or keep URLs only. Public URLs: UU 59/2024 https://jdih.kemenkoinfra.go.id/dokumen/file/uu/2024/uu-nomor-59-tahun-2024.pdf; Ringkasan RPJMN https://kinerja.ekon.go.id/perencanaan/download/kementerian-koordinator-bidang-perekonomian-sekretariat-kementerian-koordinator-bidang-perekonomian-2026-rpjmn.pdf.
- The RPJPN draft part 2 file is named pp. 143-344 but printed pages are 132-331; cite printed pages.
- The claude.ai project knowledge base is at about 1.93 of 2.0 MB and hit its cap once on 17 Nov. If the project stays in use alongside the repo, decide which is the source of truth.

## 8. Corpus and next pilots

- No ASEAN report has been classified from its own text. The ASEAN synthesis contains errors (Brunei vision dated 2014, elsewhere 2007; a think-tank series listed beside government reports).
- Pilot 3 candidates: **Vietnam 2035** (normative, quantified, ~10 years elapsed) or **AmBisyon Natin 2040** (qualitative, tests proxies). Neither classified yet. No exploratory pilot candidate with a full public text confirmed.
- Singapore's national scenarios appear unpublished; not confirmed with the publisher.
