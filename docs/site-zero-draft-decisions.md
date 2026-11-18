# Site zero draft: design and build decisions

Version 0.2, 18 November 2026. Draft for review. 0.2 adds Z33-Z50: the generative-AI notice and the full drafts of Method, Editorial standards, For report authors, Corrections and changelog, and the five legal pages.

Every design, brand and build call made to get the site from architecture v0.1 (`docs/site-architecture.md`) to a clickable zero draft (`site/`). None is confirmed. Each is a proposal for the owner to accept, change or reject. Accepted rows move into `docs/decisions.md` (as S-rows); rejected ones are reversed in the code.

How to review: open `site/index.html` in a browser (no server needed), or run `python3 -m http.server -d site` and go to `http://localhost:8000`. Check on a phone width and in dark mode too.

## Build and structure

| # | Decision | Why | Rejected |
| --- | --- | --- | --- |
| Z1 | **Static generator in Python, standard library only** (`scripts/build_site.py`). Sources in `site-src/` (page fragments, catalogue, partials, CSS, JS); output in `site/`, committed. `--check` exits 1 if `site/` is stale, like the token build. | The repo has no package manager; the token build already sets this pattern. One shell for every page stops the header and footer drifting across 89 files. | A framework (Eleventy, Astro): adds Node tooling before the site is agreed. Hand-written HTML per page: the shell would drift. |
| Z2 | **Relative links that end in `index.html`.** | The draft opens from disk, from any static host and from a sub-folder, with no server. | Root-absolute clean addresses (`/reports/`). Switch when hosting is chosen; the generator makes that one change. |
| Z3 | **Pilot pages moved** from `pages/` to `site-src/pages/reports/{slug}.html`. Only the per-page site bar, `<head>` and footer were removed; the generator adds the shared ones. **Content not changed**: header, sections, glyph sprite, draft notes and script are byte-for-byte as before. | The pilots now share navigation, footer and logo placement with the rest of the site. | Leaving `pages/` as is and copying: two copies of each page. |
| Z4 | **`report-page.css` stays the shared component sheet** and loads on every page; `site.css` adds the shell and the site-page components. | It already holds the type, chips, tables, notes and glyph styles every page needs. | Splitting it into base and report sheets now: churn before the bundle question (open questions §1) is settled. |
| Z5 | **The pilots' draft bar becomes a site-wide draft band** under the masthead, keeping its text and the "Show draft notes" toggle on report pages. Other pages say "Zero draft 0.1 · Not for publication · Placeholder content marked". | One place on every page says what is draft. | Draft text inside the masthead. |
| Z6 | **New draft tag `[PLACEHOLDER]`** for invented or empty content, styled like `[GAP]`, `[TRIAL]` and `[STRAIN]`. | Keeps the existing tags meaning what they meant on the pilots. | Reusing `[GAP]`. |

## Shell: masthead, breadcrumbs, footer

| # | Decision | Why | Rejected |
| --- | --- | --- | --- |
| Z7 | **Masthead**: lockup left (34px high, 30px on phones; the pilots used 40px), main navigation (Reports, Countries, Method, About), language switch right (EN ES ID, mono, current one on a `paper-3` pill). Current section underlined in `sky-ink`. Hairline rule below. | Architecture's navigation; a slimmer lockup so the report header stays the first thing read. | A larger lockup; a coloured bar. |
| Z8 | **No menu button on phones.** The four items sit on a second row, spread across the width. | Four short words fit at 360px; nothing is hidden. | Hamburger menu. |
| Z9 | **Breadcrumbs** in mono under the draft band: report pages read Reports / Country / Report. | The reader arriving from search can see where the page sits. | None. |
| Z10 | **Footer on Ink** (`data-theme="dark"`, as the pilots had) with a hairline top rule, the pilots' blurb and motto, and four columns: Norantz, About, Use, Legal. Base row: "Norantz, by Plural Futures" linking to `https://pluralfutures.com` (**address to confirm**) and "© 2026 Plural Futures". | Architecture's footer list. The rule keeps the footer distinct when the reader is in dark mode. | A paper footer. |
| Z11 | **Every page `noindex`**; favicon is the Sky mark. | Not public. | — |

## Home

| # | Decision | Why | Rejected |
| --- | --- | --- | --- |
| Z12 | **Hero**: overline, "Towards where?" in `display-xl`, a lead on what Norantz does, the campaign line "Are the futures we planned still pointing the right way?". The **spectrum sits in its own panel** beside the text (below it on phones) with the Sky mark, never behind text (B12). | Brand: display-xl and the spectrum are allowed on the home hero; the campaign line is for the home hero. | Spectrum as a full-bleed background. |
| Z13 | **Latest reviews as cards**: country and type label, short title, the page's tip finding verbatim, "Reviewed as of" date and coverage. | The tip is the iceberg's top layer; coverage always beside the finding (P5). | Cards with tallies. |
| Z14 | **One Ember call to action**, "Get updates", in a `paper-2` block at the end of Home. Ember pill with ink text (5.2:1, brand §4). On Updates, "Sign up" is that page's one Ember button; Contact uses the quiet outline button. | B6: one Ember per screen. | Ember in the masthead. |
| Z15 | **Site pages speak as "we"**; report pages keep "this page" and "the review". | Natural on About, Contact and Updates. **Owner to confirm** the voice. | "Norantz" in the third person throughout. |

## Reports, map and countries

| # | Decision | Why | Rejected |
| --- | --- | --- | --- |
| Z16 | **The catalogue is a data file** (`site-src/catalogue.json`) driving the Reports list, map, country pages, Home cards and counts. | One record per report (architecture "catalogue record"); counts can never disagree with the list. | Lists written by hand. |
| Z17 | **Both pilots shown as "Reviewed"**, and the 2017 *Visi Indonesia 2045* deck as "Reviewed", paired on the Indonesia page. Flagged on Home. | Previews the launch state. Neither page is published or human-reviewed. | Showing them as "Review under way" (true today, but leaves nothing to preview). |
| Z18 | **Six ASEAN reports listed as "Listed, not yet reviewed"** from the secondary synthesis: Vietnam 2035, AmBisyon Natin 2040, Thailand's National Strategy 2018–2037, Shared Prosperity Vision 2030, Wawasan Brunei 2035, Lao Vision 2030. Type and force "To classify"; each row flagged. Singapore (continuous scenario work, no single report), Myanmar (MSDP, a medium-term plan) and Cambodia 2040 (think-tank led) left out until method decision 15 settles scope. | Shows the catalogue with real-looking breadth without classifying anything from secondary text. | Leaving the catalogue at the two pilots. |
| Z19 | **Schematic map**: a graticule with one point per country at its capital, no land or borders, cropped to Europe and South-East Asia. Points link to country pages; a country with several reports shows its count inside the mark. | Avoids choosing a disputed-borders convention (architecture open item 2) and never shades countries (B3, B14, S7). Needs no map data. | A world basemap; a choropleth. Revisit when the basemap is chosen. |
| Z20 | **Review-state marks as proposed in the architecture**: solid Sky disc (reviewed), dotted Sky ring in the brand's round-dot dash (under way), Loam outline ring (listed). Counts by state above the list and the map, with a "not a score" line. | S7 and B9. Not tested with readers (open item 9). | — |
| Z21 | **Reports page**: map above the list on wide screens; on phones, List and Map tabs with List first. Six filters (country, region, type, status today, review state, horizon band), two to a row on phones, a "Clear filters" button and a live "Showing N of M" line. Without JavaScript all rows show. `?country=` preselects a filter. | Architecture: list is the main phone view; filters as listed. | Filters hidden behind a button on phones. |
| Z22 | **A country page for every listed country**, generated: header, reports in date order, links between reports, and a source-pack placeholder. | S11; keeps map points from leading nowhere. | Country pages for the two pilot countries only. |
| Z23 | **Register pages are placeholders** (`/reports/{slug}/register/`) for the two reviewed reports. **Fixed-version pages (`/v{n}/`) not built**: no version exists yet. | S10 needs the version scheme first. | Fake v1 pages. |

## Other pages

| # | Decision | Why | Rejected |
| --- | --- | --- | --- |
| Z24 | **Method page** written as a first public draft from method v0.2: the two tracks, the nine steps with the AI's part and the person's check, source tiers, and every label with its glyph (sprite copied from the Indonesia page into `site-src/partials/glyphs.html`). | Most of it is already settled text; it gives the reader the "How to read this page" long form the spec wants. | A placeholder only. |
| Z25 | **About, Editorial standards, For report authors, Press, FAQ** drafted from the brand, evidence and decision records; every policy not yet agreed (funding, selection, election policy, right of reply, licence) is a `[PLACEHOLDER]` naming its open item. | Readable now, and the open items are visible where they bite. | Lorem ipsum. |
| Z26 | **Corrections and changelog** as a dated table; seeded with the two page drafts. | Shape of the log is clear; content waits on the version scheme. | — |
| Z27 | **Forms are inert** (`data-placeholder`): submitting shows a note and sends nothing. Updates has email, topics and language (S9); Contact has one form with a route selector and three route cards. | No provider chosen (open item 8). | Three separate contact forms. |
| Z28 | **Legal pages are skeletons** structured to the Spanish basis in the architecture (LSSI-CE art. 10 fields, GDPR and LOPDGDD rights, AEPD), with `[to add]` fields and a lawyer-check note. Cookies page states the aim of no consent banner (cookie-free analytics). | S13; nothing legal is invented. | Generic templates. |
| Z29 | **404 at the site root** (`site/404.html`). | Most static hosts pick it up there. | — |
| Z30 | **Data and citation** shows a downloads table, a citation pattern ("Norantz (2026). *Title: a second reading*, version N, reviewed as of date. Plural Futures. [fixed address]") and the extraction schema. CC BY 4.0 floated as a licence in a placeholder. | Researchers' route (S1). | — |

## Languages

| # | Decision | Why | Rejected |
| --- | --- | --- | --- |
| Z31 | **Every site page exists at `/es/` and `/id/` as a stub**: translated masthead, draft band and footer, a short "not yet translated" message and a link to the English page. **Report pages exist only in English and the report's own language** (España 2050 in Spanish, Indonesia Emas 2045 in Indonesian), also as stubs; the switch on other report pages goes to that language's Reports page. `hreflang` alternates on every page. | S8 (addresses from launch) and method decision 12 (report pages in English and the report's language). | English only in the zero draft. |
| Z32 | **Spanish and Indonesian interface strings are machine drafts** (in `scripts/build_site.py`, `T`), including the motto ("Leer con generosidad. Comprobar con rigor." / "Membaca dengan murah hati. Memeriksa dengan teliti."). | Lets the owner see the chrome in each language. **A native speaker must check them**; brand open question 5 (name line and descriptor translations) is untouched. | — |

## Zero draft 0.2: generative AI, policy pages, legal pages

The owner asked that every page make clear the analysis is done with generative AI, may contain errors, and is meant as a conversation starter and a starting point for deeper, human-led discussion and analysis.

| # | Decision | Why | Rejected |
| --- | --- | --- | --- |
| Z33 | **A "Made with generative AI" notice on every review page**, added by the shell between the breadcrumbs and the report header, with links to "How AI is used" and "Report an error". The same notice sits on Home and on Reports. Sky-ink left rule on a surface box, no Ember. Translated (machine drafts) on ES and ID pages. | The owner's brief. Placed above the report name so no one reads a finding before the caveat. Added by the shell, so the pilot pages' content stays unchanged. | A modal or a dismissible banner (readers click through without reading); a line in the footer only (too easy to miss). |
| Z34 | **A one-line AI statement in every footer**, in italics under the blurb. | Every page, including policy and legal pages, carries the caveat. | — |
| Z35 | **Standard wording of the caveat**: "This analysis was drafted by generative AI and may contain errors. It is meant to start a conversation and to be a starting point for deeper, human-led discussion and analysis, not a final judgement." Reused in Method, Standards, Authors, Corrections, Terms, Legal notice and the FAQ. | One sentence everyone sees the same way. | Different wording per page. |
| Z36 | **New tag use: `[TRIAL]` marks a drafted policy position the owner must accept** (response times, the election window, conflict-of-interest rules, the version scheme, the licence, retention periods). `[PLACEHOLDER]` stays for missing facts (company details, providers, addresses). | Matches the existing meaning of [TRIAL], "a new judgement". | A new tag. |
| Z37 | **Method page rewritten as the public form of method v0.2** in 13 numbered sections with a sticky contents list: what a review is for and is not; how generative AI is used, what people check, and a table of seven error types with what is done about each; the five questions; kinds of report; the register and the unstated-assumption checklist; the steps for both tracks; sources; what has changed; the required-rate test; labels; counts not scores; versions; limits. | The owner asked for a full build; most of it is settled method text. The error table makes "may contain errors" concrete. | Linking to the internal method document only. |
| Z38 | **Proposed rule: nothing is published until a named person has signed off its readings and page**; every page names that person. Stated as [TRIAL] in Method and Standards. | Makes "human-led" real, and is what the pilots lack today. | Publishing AI-only drafts labelled as such. |
| Z39 | **Name the AI models and versions per review** and publish the step instructions: left as [PLACEHOLDER] in Method. | Transparency; not yet settled. | — |
| Z40 | **Editorial standards in 12 numbered rules**: purpose; intent first (four beats); describe, do not grade (a "we write / we do not write" table); evidence; generative AI disclosure and accountability; impartiality; elections; independence; languages; corrections and replies; complaints; yearly review. | Pulls the brand, evidence and decision rules into one public page. | — |
| Z41 | **Election policy default**: no first review, and no new version that changes readings, of a country's report in the six weeks before a national election there; corrections continue. [TRIAL] | Fills site open item 5 with a concrete proposal. It sets the España 2050 launch date. | No policy; a longer window. |
| Z42 | **Independence default**: no funder or partner sees a review before publication; any link between Norantz or Plural Futures and a report's authors or publishers is declared at the top of the page; reviewers with a close link do not work on it. [TRIAL] | Trust in a site that reviews governments. | — |
| Z43 | **Complaints**: acknowledged in 5 working days, answered in 20, with escalation to a Plural Futures director who did not work on the review. [TRIAL] | A route beyond the error form. | — |
| Z44 | **Right of reply process** (fills P11 and site open item 6): draft page, register and sources sent to the publisher and lead authors at least 15 working days before first publication; replies up to 600 words, published unedited within 10 working days, in English or the report's language; factual errors corrected, differences of reading shown side by side; an offer of a conversation. [TRIAL] | Frames the review as the start of a conversation with the authors. | Publishing without notice; letting authors approve the review. |
| Z45 | **Version scheme** (fills S10): corrections and clarifications are minor versions (v1.1) at the same address with a dated note; updates and any change of reading are whole versions (v2) at a new fixed address; withdrawals keep the page up with a notice. [TRIAL] | Keeps citations true when a reading changes. | Every change a new address. |
| Z46 | **Changelog seeded with the real draft history** (from the commit log), labelled pre-publication. | Shows the log's format with true entries. | Invented entries. |
| Z47 | **Legal pages drafted in full** under Spanish law, with every company fact as `[...]` and a lawyer-review note at the top of each: legal notice (LSSI-CE art. 10, IP with quotation under LPI art. 32, liability, jurisdiction); privacy (GDPR arts 13-14 and LOPDGDD: purposes table with legal basis and retention, AI use, processors, transfers, rights, AEPD, age 14); cookies (none set); terms; accessibility. **Spanish is proposed as the binding text.** | Owner asked for a full build; structure follows the architecture's legal table. **Not legal advice.** | Leaving skeletons. |
| Z48 | **Terms of use open with the generative-AI clause** in a callout, before who we are. Licence for reviews and registers: **CC BY 4.0** [TRIAL], with a request (not a condition) not to turn counts into scores. Reports, quotes, official data and logos excluded. | The caveat is the term readers most need. CC BY suits a conversation-starter aim. | CC BY-NC; all rights reserved. |
| Z49 | **Privacy: no personal data used to train AI; AI-assisted handling of messages only through a no-retention provider with a person sending every answer** [TRIAL]. **Fonts to be self-hosted before launch**, because Google Fonts sends visitors' IP addresses to Google; both privacy and cookie pages say so. | Google Fonts IP transfer is a known GDPR issue in the EU. | Keeping Google Fonts and adding it as a processor. |
| Z50 | **Accessibility statement**: "partly conformant" with WCAG 2.1 AA until audited; states what is done and four known limits; says RD 1112/2018 does not apply and Ley 11/2023 is being checked. | Honest status before an audit. | Claiming full conformance. |

Also changed in 0.2: two FAQ entries ("Is the analysis accurate?", "How should I use a review?"), the draft band reads "Zero draft 0.2", and long pages have a tighter gap between sections.

## Checked

Built and checked in Chromium on 18 Nov 2026 (0.1, then again for 0.2): 89 pages, no console errors, no horizontal scroll at 390px and 1280px, every internal link and anchor resolves. Light and dark checked on Home, Reports, a report page, Updates. Not checked: screen reader, keyboard order, print, Safari.
