# Site architecture

Version 0.1, 17 November 2026. Draft for review.

The structure of the whole public site: which pages exist, what each holds, how they link, and the address pattern. The page for one reviewed report is specified separately in `claude/report-page-spec.md`. Decisions behind this doc are S5 to S12 in `docs/decisions.md`.

## Site map

```
/                         Home
/reports/                 Reports: list and map of every listed report
/reports/{slug}/          Report page (18 sections, spec v0.2)
/reports/{slug}/register/ Full register (data view)
/reports/{slug}/v{n}/     Fixed version, for citation
/countries/               Country index
/countries/{country}/     Country page
/method/                  Method, how to read a review, labels explained
/about/                   About Norantz and Plural Futures
/about/funding/           Funding, and how reports are chosen
/about/standards/         Editorial standards
/about/authors/           For report authors (right of reply)
/about/corrections/       Corrections and changelog
/about/press/             Press
/data/                    Data and citation
/updates/                 Email sign-up
/faq/                     FAQ
/contact/                 Contact, suggest a report, report an error
/legal/privacy/           Privacy
/legal/terms/             Terms of use
/legal/cookies/           Cookies
/legal/accessibility/     Accessibility statement
/legal/notice/            Legal notice, if required (see open items)
```

Every path above also exists under `/es/` and `/id/` (see Languages).

Later, not at launch: `/themes/` and `/themes/{theme}/` (blocked by method decision 10, the shared taxonomy) and a cross-report comparison view.

## Main navigation

| Item | Goes to |
| --- | --- |
| Reports | `/reports/` |
| Countries | `/countries/` |
| Method | `/method/` |
| About | `/about/` |

Header right: language switch. Footer: About pages, FAQ, Contact, Data and citation, Get updates, Legal, "Norantz, by Plural Futures" with a link to Plural Futures.

The section is called **Reports**, not "Scenarios": most national reports are visions, and the site names visions and scenario sets separately (decisions S3, P7).

## Pages

### Home

| Block | Holds |
| --- | --- |
| Hero | The name and its question ("towards where?"), one line on what Norantz does. Spectrum allowed here (B12). |
| Latest reviews | Two or three report cards: title, country, type label, "reviewed as of" date, the at-a-glance tip finding. |
| Map teaser | Small map with the coverage counts, linking to `/reports/`. |
| How it works | Three steps: read the report, check it against the evidence, publish with sources and a right of reply. AI role and human checks named. Links to `/method/`. |
| Get updates | One call to action, in Ember (the only one on the screen). |

### Reports (list and map)

One catalogue of every national vision or scenario report found, whether reviewed or not.

**Review states.** Each report carries exactly one:

| State | Meaning | Proposed mark |
| --- | --- | --- |
| Reviewed | A published review exists | Solid, Sky |
| Review under way | Work started, not published | Dotted, Sky |
| Listed, not yet reviewed | In the catalogue only | Outline, Loam |

The marks follow "colour tells time; shape tells status" and "dotted = planned, solid = observed". They are a proposal, not yet tested.

**Rules.**

- The counts for each state sit beside the map and the list at all times (P5).
- Countries are never filled with a colour by findings or by state. Marks are points or pins. A coloured map would read as a league table (B3, B14).
- On a phone the filterable list is the main view; the map is a second tab.
- Filters: country, region, type (vision, vision with comparison scenarios, scenario set), status today (in force, revised, superseded, lapsed), review state, horizon year.
- A country with several reports shows one mark with a count.
- The basemap convention for disputed borders is chosen once and stated under the map (open item).

**Catalogue record.** Every listed report holds the header fields from spec §0, so it can be listed before it is reviewed:

| Field | Example |
| --- | --- |
| Title (original and English) | *Rencana Pembangunan Jangka Panjang Nasional 2025-2045* |
| Country | Indonesia |
| Publisher | Bappenas |
| Publication year | 2024 |
| Horizon year | 2045 |
| Type | A vision |
| Force when published | Law |
| Status today | In force |
| Original link | URL |
| Language(s) | Indonesian |
| Review state | Review under way |
| Successor or predecessor | *Visi Indonesia 2045* (2017) |

Inclusion follows method decision 15 (scope). The map makes the scope public, so decision 15 must close before the map launches.

### Report page

As `claude/report-page-spec.md` v0.2. Additions from this doc:

- `/reports/{slug}/` always shows the latest version; `/v{n}/` addresses never change, so a citation stays valid.
- The register is its own address, linked from §7 and §17.
- Each report has a share card (B12 sets the spectrum rule for scenario sets).

### Country page

All reports for one country in date order, with how they link (successor, predecessor, paired on one page), their review states and the country's source pack summary when approved. Indonesia is the first case: the 2017 deck and the RPJPN 2025-2045 (decision I2).

### Method

The public form of `claude/scenario-review-method.md`: the two tracks in plain words, what the AI does, what people check and when, the source tiers, the change-scan domains, and every status label with its meaning. Holds the long form of "How to read this page" (spec §2). Linked from §15 of every report page.

### About pages

| Page | Holds | Status of the content |
| --- | --- | --- |
| About | What Norantz is, the name, the relationship to Plural Futures (B1) | Draftable now |
| Funding, and how reports are chosen | Who pays; selection criteria | No policy yet (open questions §2, item 4) |
| Editorial standards | Neutrality, care around elections, AI disclosure, the corrections policy, media never as evidence | Partly written across decisions; election policy open |
| For report authors | Who is contacted, when, how long they have, how a reply is shown (§16) | No process yet (P11) |
| Corrections and changelog | One dated log: new reviews, new versions, corrections, with links | Needs the version scheme |
| Press | How to quote a review fairly (no tallies as scores, give the "as of" date), contacts, logos | Draftable once brand v0.1 is approved |

### Data and citation

Register downloads per report and version, the citation text, the licence, and the source-extraction schema. Licence not chosen (open item).

### Email sign-up

`/updates/`: one form, email only, a choice of what to hear about (new reviews; updates to a report or a country) and the language. Double opt-in. Links to Privacy. The sign-up also appears as the Home call to action and in the footer. Provider not chosen.

### FAQ

Short answers that link out, not new content. Starting set: Is this a ranking? Who writes the reviews? Why use AI? Why this report and not another? Can authors reply? How often are reviews updated? How do I cite a review? How do I report an error?

### Contact

One page, three routes: general contact, suggest a report (feeds the catalogue), report an error (feeds the corrections log).

### Legal

Privacy, terms of use, cookies, accessibility statement. A legal notice (*aviso legal*, *Impressum*) if Plural Futures' place of establishment requires one. Cookie-free analytics would let the cookie page be short and avoid a banner.

Utility pages: 404, and a search across reports (later).

## Languages

| Point | Decision or default |
| --- | --- |
| Languages at launch | English, Spanish, Indonesian (S8) |
| Addresses | English at the root; `/es/` and `/id/` prefixes (S8). English at the root is proposed, not yet confirmed. |
| What is translated | All site pages. Report pages in English and the report's own language (method decision 12). |
| Report slugs | Kept the same across languages, so the switch maps one address to another. |
| Language switch | On every page; goes to the same page in the other language, or to that language's Reports page if no translation exists. |
| Brand | Name line and descriptor translations still open (brand open question 5). |

## Open items

| # | Item | Blocks |
| --- | --- | --- |
| 1 | Close method decision 15 (scope) | Map launch |
| 2 | Basemap convention for disputed borders | Map |
| 3 | Licence for reviews and data | Data and citation, Terms |
| 4 | Funding and selection policy | About: funding |
| 5 | Election policy | Editorial standards, España 2050 launch |
| 6 | Right-of-reply process | For report authors |
| 7 | Legal notice requirement and jurisdiction | Legal |
| 8 | Email provider and analytics tool | Email sign-up, Privacy, Cookies |
| 9 | English at the root, or `/en/` too | Addresses |
| 10 | Test the review-state marks with readers | Map |
| 11 | Shared taxonomy (method decision 10) | Themes, comparison view |
