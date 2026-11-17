# Brand assets

Version 0.1, 18 November 2026. Draft for review (see `docs/brand-guidelines.md` for the rules and what is confirmed).

| File | What it is |
| --- | --- |
| `tokens.json` | **Source of truth.** Every colour (light and dark), type style, space, radius, stroke, shadow and opacity. Byte-identical export of the design-system artifact, 18 Nov 2026. |
| `tokens.css` | CSS custom properties and type classes, **generated** from `tokens.json`. Do not edit by hand. |
| `logos/` | The 8 logo SVGs (marks, wordmarks, lockups). Inks are fixed in each file. Byte-identical to the artifact. |

## Changing a token

1. Edit `tokens.json`.
2. Run `python3 scripts/build_tokens.py`.
3. `python3 scripts/build_tokens.py --check` exits 1 if `tokens.css` is stale (use it in CI).

Keep `tokens.json` in step with the design-system artifact (https://claude.ai/artifact/DRZLvr6GwRJSaThHXB2pe5) or say which one now leads.

## Using the CSS

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;700&family=JetBrains+Mono:wght@400;500&family=Newsreader:ital,wght@0,400;1,400&display=swap">
<link rel="stylesheet" href="/brand/tokens.css">
```

- Every token is a variable named `--nz-<token>`: `var(--nz-sky-ink)`, `var(--nz-space-5)`, `var(--nz-radius)`.
- Type styles are both variables (`--nz-body-size`, `--nz-body-line`, `--nz-body-weight`, `--nz-body-family`, plus `-tracking` and `-style` where set) and classes (`.nz-type-body`, `.nz-type-h2`, `.nz-type-label`). `.nz-type-label` adds uppercase; `.nz-type-data` adds tabular figures.
- The light theme ("Paper") is the default on `:root`. The dark theme ("Ink") is **opt-in**: put `data-theme="dark"` on a cover, closer, social card or data view. There is deliberately no automatic `prefers-color-scheme` switch; whether the site follows the reader's system setting is open (`docs/open-questions.md` §1).
- The class prefix `nz-` matches the component stylesheet in the artifact (`components/bundle.css`), which is not yet in the repo.

Fonts are loaded from Google Fonts here; self-hosting is open (`docs/open-questions.md` §1).
