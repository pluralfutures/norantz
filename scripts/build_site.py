#!/usr/bin/env python3
"""Build the Norantz zero-draft site.

Version 0.1, 18 November 2026. Draft for review.

Reads site-src/ and writes a static site to site/ (standard library only):

  site-src/pages/**.html     one fragment per English page; the path is the address
                             (index.html -> /, method.html -> /method/,
                             about/funding.html -> /about/funding/)
  site-src/partials/*.html   pieces the generator fills (country page, register, glyphs)
  site-src/catalogue.json    every listed report and country
  site-src/assets/           CSS and JS, copied to site/assets/
  brand/tokens.css, brand/logos/   copied to site/assets/

Every page gets the same masthead, draft band, breadcrumbs and footer. Each fragment
starts with  <!--meta {json} -->  giving title, description, nav and options.
Spanish and Indonesian pages (/es/, /id/) are stubs that point to the English page,
except a report's page in the report's own language, which is also a stub for now.

Links are relative and end in index.html, so the output opens from disk, from any
static host and from a sub-folder without a server.

Usage:
  python3 scripts/build_site.py           build site/
  python3 scripts/build_site.py --check   exit 1 if site/ is out of date
"""

import html
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "site-src"
OUT = ROOT / "site"

FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;"
         "12..96,600;12..96,700&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,"
         "opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap")

LANGS = ["en", "es", "id"]
LANG_HTML = {"en": "en-GB", "es": "es", "id": "id"}

# Interface strings. Spanish and Indonesian are machine drafts, to be checked by a native speaker.
T = {
    "en": {
        "reports": "Reports", "countries": "Countries", "method": "Method", "about": "About",
        "main_nav": "Main", "lang_nav": "Language", "skip": "Skip to content",
        "by": "By Plural Futures", "crumbs": "You are here",
        "blurb": "Norantz (Basque for “towards where?”) is a second reading of national futures, "
                 "by Plural Futures. It reads each report on its own terms, describes rather than grades, "
                 "and shows its sources, coverage, and method on every page.",
        "motto": "Read generously. Check rigorously.",
        "f_site": "Norantz", "f_about": "About", "f_use": "Use", "f_legal": "Legal",
        "funding": "Funding and selection", "standards": "Editorial standards",
        "authors": "For report authors", "corrections": "Corrections and changelog", "press": "Press",
        "data": "Data and citation", "updates": "Get updates", "faq": "FAQ", "contact": "Contact",
        "notice": "Legal notice", "privacy": "Privacy", "terms": "Terms of use", "cookies": "Cookies",
        "accessibility": "Accessibility",
        "endorse": "Norantz, by Plural Futures",
        "rights": "© 2026 Plural Futures",
        "zero": "Zero draft 0.1 · 18 Nov 2026 · Not for publication · Placeholder content marked",
        "notes": "Show draft notes",
    },
    "es": {
        "reports": "Informes", "countries": "Países", "method": "Método", "about": "Acerca de",
        "main_nav": "Principal", "lang_nav": "Idioma", "skip": "Ir al contenido",
        "by": "Por Plural Futures", "crumbs": "Está aquí",
        "blurb": "Norantz (en euskera, “¿hacia dónde?”) es una segunda lectura de los futuros "
                 "nacionales, por Plural Futures. Lee cada informe en sus propios términos, describe en lugar "
                 "de calificar y muestra sus fuentes, su cobertura y su método en cada página.",
        "motto": "Leer con generosidad. Comprobar con rigor.",
        "f_site": "Norantz", "f_about": "Acerca de", "f_use": "Usar las revisiones", "f_legal": "Legal",
        "funding": "Financiación y selección", "standards": "Normas editoriales",
        "authors": "Para los autores", "corrections": "Correcciones y cambios", "press": "Prensa",
        "data": "Datos y citas", "updates": "Recibir novedades", "faq": "Preguntas frecuentes",
        "contact": "Contacto", "notice": "Aviso legal", "privacy": "Privacidad",
        "terms": "Condiciones de uso", "cookies": "Cookies", "accessibility": "Accesibilidad",
        "endorse": "Norantz, por Plural Futures",
        "rights": "© 2026 Plural Futures",
        "zero": "Borrador cero 0.1 · 18 nov 2026 · No publicar · Traducción automática por revisar",
        "notes": "Mostrar notas",
        "stub_label": "Página aún no traducida",
        "stub_h": "Esta página todavía no está en español",
        "stub_p": "La versión en inglés está disponible.",
        "stub_link": "Leer en inglés",
    },
    "id": {
        "reports": "Laporan", "countries": "Negara", "method": "Metode", "about": "Tentang",
        "main_nav": "Utama", "lang_nav": "Bahasa", "skip": "Langsung ke isi",
        "by": "Oleh Plural Futures", "crumbs": "Posisi Anda",
        "blurb": "Norantz (bahasa Basque untuk “ke mana?”) adalah pembacaan kedua atas masa depan "
                 "nasional, oleh Plural Futures. Setiap laporan dibaca menurut tujuannya sendiri, digambarkan "
                 "tanpa dinilai, dan setiap halaman menunjukkan sumber, cakupan, dan metodenya.",
        "motto": "Membaca dengan murah hati. Memeriksa dengan teliti.",
        "f_site": "Norantz", "f_about": "Tentang", "f_use": "Gunakan tinjauan", "f_legal": "Hukum",
        "funding": "Pendanaan dan pemilihan", "standards": "Standar editorial",
        "authors": "Untuk penulis laporan", "corrections": "Koreksi dan catatan perubahan", "press": "Pers",
        "data": "Data dan sitasi", "updates": "Dapatkan kabar terbaru", "faq": "Tanya jawab",
        "contact": "Kontak", "notice": "Pemberitahuan hukum", "privacy": "Privasi",
        "terms": "Ketentuan penggunaan", "cookies": "Cookie", "accessibility": "Aksesibilitas",
        "endorse": "Norantz, oleh Plural Futures",
        "rights": "© 2026 Plural Futures",
        "zero": "Draf nol 0.1 · 18 Nov 2026 · Bukan untuk publikasi · Terjemahan mesin, perlu diperiksa",
        "notes": "Tampilkan catatan",
        "stub_label": "Halaman belum diterjemahkan",
        "stub_h": "Halaman ini belum tersedia dalam bahasa Indonesia",
        "stub_p": "Versi bahasa Inggris sudah tersedia.",
        "stub_link": "Baca dalam bahasa Inggris",
    },
}

NAV = [("reports", "reports/"), ("countries", "countries/"), ("method", "method/"), ("about", "about/")]
FOOTER = [
    ("f_site", [("reports", "reports/"), ("countries", "countries/"), ("method", "method/"), ("about", "about/")]),
    ("f_about", [("funding", "about/funding/"), ("standards", "about/standards/"), ("authors", "about/authors/"),
                 ("corrections", "about/corrections/"), ("press", "about/press/")]),
    ("f_use", [("data", "data/"), ("updates", "updates/"), ("faq", "faq/"), ("contact", "contact/")]),
    ("f_legal", [("notice", "legal/notice/"), ("privacy", "legal/privacy/"), ("terms", "legal/terms/"),
                 ("cookies", "legal/cookies/"), ("accessibility", "legal/accessibility/")]),
]

STATE = {
    "reviewed": ("Reviewed", "A published review exists"),
    "underway": ("Review under way", "Work started, not published"),
    "listed": ("Listed, not yet reviewed", "In the catalogue only"),
}

esc = html.escape


# ---------------------------------------------------------------- addresses

def depth(route):
    """Number of folders below the site root for a route such as 'es/about/funding/'."""
    return route.count("/")


def rel(from_route, to_route):
    """Relative link from one page to another, ending in index.html."""
    return "../" * depth(from_route) + to_route + "index.html"


def asset(from_route, path):
    return "../" * depth(from_route) + "assets/" + path


def lang_route(lang, route):
    return route if lang == "en" else f"{lang}/{route}"


def out_file(route):
    return OUT / route / "index.html" if route != "404" else OUT / "404.html"


# ---------------------------------------------------------------- data

CAT = json.loads((SRC / "catalogue.json").read_text(encoding="utf-8"))
COUNTRIES = {c["slug"]: c for c in CAT["countries"]}
REPORTS = CAT["reports"]
BY_SLUG = {r["slug"]: r for r in REPORTS}


def reports_for(country):
    return sorted([r for r in REPORTS if r["country"] == country], key=lambda r: r["year"])


def state_counts():
    return {k: sum(1 for r in REPORTS if r["state"] == k) for k in STATE}


def horizon_band(h):
    return "to-2035" if h <= 2035 else ("2036-2045" if h <= 2045 else "after-2045")


# ---------------------------------------------------------------- pieces

def state_mark(state, size=16):
    """Review-state mark: solid Sky (reviewed), dotted Sky (under way), Loam outline (listed)."""
    r = size / 2 - 2
    c = size / 2
    cls = {"reviewed": "nz-sm-reviewed", "underway": "nz-sm-underway", "listed": "nz-sm-listed"}[state]
    return (f'<svg class="nz-glyph nz-sm {cls}" width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
            f'aria-hidden="true"><circle cx="{c}" cy="{c}" r="{r}"/></svg>')


def state_counts_html(route, compact=False):
    counts = state_counts()
    items = "".join(
        f'<span class="nz-tally-item" role="listitem">{state_mark(k)}<b>{counts[k]}</b> {STATE[k][0]}</span>'
        for k in STATE)
    total = len(REPORTS)
    ncountries = len({r["country"] for r in REPORTS})
    return (f'<div class="nz-tally" role="list">{items}</div>'
            f'<p class="nz-source">{total} reports listed from {ncountries} countries · '
            f'Counts by review state, not a score · Scope rule not yet agreed (method decision 15)</p>')


def report_href(route, r):
    if r.get("page"):
        h = rel(route, r["page"])
        return h + ("#top" if r.get("paired") else "")
    return None


def report_row(route, r):
    c = COUNTRIES[r["country"]]
    href = report_href(route, r)
    name = f'<a href="{href}">{esc(r["short"])}</a>' if href else esc(r["short"])
    full = "" if r["title"] == r["short"] else (
        f'<p class="nz-rrow-full" lang="{r["title_lang"]}"><cite>{esc(r["title"])}</cite></p>')
    meta = " · ".join([
        esc(r["publisher"]), f'Published {esc(r["year"])}', f'Looks ahead to {r["horizon"]}',
        f'Force when published: {esc(r["force"].lower() if r["force"] != "To classify" else "to classify")}',
        f'Status today: {esc(r["status_today"].lower())}'])
    state_line = STATE[r["state"]][0]
    if r["state"] == "reviewed" and r.get("reviewed_as_of"):
        state_line += f' · as of {r["reviewed_as_of"]}'
    extra = ""
    if r.get("paired"):
        extra += '<p class="nz-body-s">Read beside its successor on the Indonesia Emas 2045 page.</p>'
    if r.get("tip"):
        extra += f'<p class="nz-rrow-tip">{esc(r["tip"])}</p>'
    if not r.get("verified", True):
        extra += ('<p class="nz-note"><b>[PLACEHOLDER]</b> Listed from a secondary synthesis. '
                  'Classify from the primary text before publishing.</p>')
    return (
        f'<li class="nz-rrow" data-country="{r["country"]}" data-region="{esc(c["region"])}" '
        f'data-type="{esc(r["type"])}" data-status="{esc(r["status_today"])}" data-state="{r["state"]}" '
        f'data-horizon="{horizon_band(r["horizon"])}">'
        f'<div class="nz-rrow-mark">{state_mark(r["state"], 18)}</div>'
        f'<div class="nz-rrow-body">'
        f'<p class="nz-label">{esc(c["name"])} · {esc(r["type"])}</p>'
        f'<h3 class="nz-h3">{name}</h3>{full}'
        f'<p class="nz-rrow-meta">{meta}</p>'
        f'<p class="nz-rrow-state nz-rs-{r["state"]}">{state_line}</p>{extra}'
        f'</div></li>')


def report_list(route, reports=None):
    reports = reports if reports is not None else sorted(
        REPORTS, key=lambda r: ({"reviewed": 0, "underway": 1, "listed": 2}[r["state"]],
                                COUNTRIES[r["country"]]["name"], -int(r["year"]) if r["year"].isdigit() else 0))
    return '<ol class="nz-rlist" id="report-list">' + "".join(report_row(route, r) for r in reports) + "</ol>"


def options(values):
    return "".join(f'<option value="{esc(v)}">{esc(lbl)}</option>' for v, lbl in values)


def filters():
    countries = sorted({r["country"] for r in REPORTS}, key=lambda s: COUNTRIES[s]["name"])
    regions = sorted({COUNTRIES[r["country"]]["region"] for r in REPORTS})
    types = sorted({r["type"] for r in REPORTS})
    statuses = sorted({r["status_today"] for r in REPORTS})
    sel = [
        ("country", "Country", [(c, COUNTRIES[c]["name"]) for c in countries]),
        ("region", "Region", [(x, x) for x in regions]),
        ("type", "Type", [(x, x) for x in types]),
        ("status", "Status today", [(x, x) for x in statuses]),
        ("state", "Review state", [(k, v[0]) for k, v in STATE.items()]),
        ("horizon", "Horizon", [("to-2035", "To 2035"), ("2036-2045", "2036 to 2045"),
                                 ("after-2045", "After 2045")]),
    ]
    out = ['<form class="nz-filters" id="report-filters" aria-label="Filter the reports">']
    for key, label, vals in sel:
        out.append(f'<label class="nz-filter"><span class="nz-label">{label}</span>'
                   f'<select data-filter="{key}"><option value="">All</option>{options(vals)}</select></label>')
    out.append('<button type="reset" class="nz-btn-quiet">Clear filters</button></form>'
               f'<p class="nz-source" id="filter-count" aria-live="polite">Showing {len(REPORTS)} of {len(REPORTS)} reports</p>')
    return "".join(out)


# Schematic map: graticule and points only. No basemap until the disputed-borders
# convention is chosen (site architecture open item 2). Equirectangular, lon -20..140, lat -20..55.
LON0, LON1, LAT0, LAT1 = -20, 140, -15, 52


def map_svg(route, small=False):
    W = 900
    k = W / (LON1 - LON0)
    H = (LAT1 - LAT0) * k
    x = lambda lon: (lon - LON0) * k
    y = lambda lat: (LAT1 - lat) * k
    parts = [f'<svg class="nz-map{" nz-map-small" if small else ""}" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
             f'aria-labelledby="map-title-{int(small)}"><title id="map-title-{int(small)}">Schematic map of the '
             f'listed reports: one mark per country, shaped by review state. The list gives the same information.</title>']
    for lon in range(-15, LON1 + 1, 15):
        parts.append(f'<line class="nz-map-grid" x1="{x(lon):.1f}" y1="0" x2="{x(lon):.1f}" y2="{H:.1f}"/>')
    for lat in range(-15, LAT1 + 1, 15):
        cls = "nz-map-eq" if lat == 0 else "nz-map-grid"
        parts.append(f'<line class="{cls}" x1="0" y1="{y(lat):.1f}" x2="{W}" y2="{y(lat):.1f}"/>')
    if not small:
        for lat in (0, 30, 45):
            parts.append(f'<text class="nz-map-tick" x="6" y="{y(lat) - 6:.1f}">{lat}°{"N" if lat else ""}</text>')
    parts.append(f'<text class="nz-map-region" x="{x(-15):.1f}" y="{y(48):.1f}">Europe</text>')
    parts.append(f'<text class="nz-map-region" x="{x(62):.1f}" y="{y(-5):.1f}">South-East Asia</text>')
    for slug, c in COUNTRIES.items():
        rs = reports_for(slug)
        if not rs:
            continue
        st = min((r["state"] for r in rs), key=["reviewed", "underway", "listed"].index)
        cx, cy = x(c["lon"]), y(c["lat"])
        r = 8 if not small else 10
        href = rel(route, f"countries/{slug}/")
        n = len(rs)
        lab = c["name"] + (f" ({n})" if n > 1 else "")
        anchor, dx, dy = {"right": ("start", r + 6, 4), "left": ("end", -(r + 6), 4),
                          "below": ("middle", 0, r + 16)}[c["label"]]
        label = "" if small else (f'<text class="nz-map-label" x="{cx + dx:.1f}" y="{cy + dy:.1f}" '
                                  f'text-anchor="{anchor}">{esc(lab)}</text>')
        count = (f'<text class="nz-map-count" x="{cx:.1f}" y="{cy + 4:.1f}" text-anchor="middle">{n}</text>'
                 if n > 1 else "")
        parts.append(f'<a href="{href}" aria-label="{esc(c["name"])}: {n} report{"s" if n > 1 else ""}">'
                     f'<circle class="nz-map-pt nz-sm-{st}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r}"/>'
                     f'{count}{label}</a>')
    parts.append("</svg>")
    return "".join(parts)


def map_key():
    return ('<div class="nz-mapkey">' + "".join(
        f'<span class="nz-key-row">{state_mark(k)}<span class="nz-body-s">{STATE[k][0]}</span></span>'
        for k in STATE) + "</div>")


def latest_cards(route):
    rs = [r for r in REPORTS if r["state"] == "reviewed" and r.get("tip")]
    out = ['<ul class="nz-cards">']
    for r in rs:
        c = COUNTRIES[r["country"]]
        out.append(
            f'<li class="nz-card"><a class="nz-card-link" href="{rel(route, r["page"])}">'
            f'<p class="nz-label">{esc(c["name"])} · {esc(r["type"])}</p>'
            f'<h3 class="nz-h3">{esc(r["short"])}</h3>'
            f'<p class="nz-card-tip">{esc(r["tip"])}</p>'
            f'<p class="nz-card-foot"><span class="nz-asof">Reviewed as of {r["reviewed_as_of"]}</span>'
            f'<span class="nz-source">{esc(r["coverage"])}</span></p></a></li>')
    out.append("</ul>")
    return "".join(out)


def country_list(route):
    out = ['<ul class="nz-clist">']
    for slug, c in sorted(COUNTRIES.items(), key=lambda kv: kv[1]["name"]):
        rs = reports_for(slug)
        states = ", ".join(f"{sum(1 for r in rs if r['state'] == k)} {STATE[k][0].lower()}"
                           for k in STATE if any(r["state"] == k for r in rs))
        marks = "".join(state_mark(r["state"]) for r in rs)
        out.append(f'<li class="nz-crow"><a href="{rel(route, f"countries/{slug}/")}">'
                   f'<span class="nz-crow-name">{esc(c["name"])}</span>'
                   f'<span class="nz-crow-marks">{marks}</span>'
                   f'<span class="nz-source">{len(rs)} report{"s" if len(rs) > 1 else ""} · {states} · {esc(c["region"])}</span>'
                   f'</a></li>')
    out.append("</ul>")
    return "".join(out)


def links_html(route, r):
    if not r.get("related"):
        return ""
    items = []
    for rel_ in r["related"]:
        o = BY_SLUG[rel_["slug"]]
        items.append(f'{rel_["relation"]} <cite>{esc(o["short"])}</cite> ({esc(o["year"])})')
    return "; ".join(items)


# ---------------------------------------------------------------- shell

def masthead(route, lang, nav, alt):
    t = T[lang]
    lr = lambda r: rel(route, lang_route(lang, r))
    navitems = "".join(
        f'<li><a href="{lr(r)}"{" aria-current=\"page\"" if key == nav else ""}>{t[key]}</a></li>'
        for key, r in NAV)
    langs = "".join(
        f'<li><a href="{rel(route, alt[l])}" hreflang="{LANG_HTML[l]}" lang="{LANG_HTML[l]}"'
        f'{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a></li>' for l in LANGS)
    return f'''<a class="nz-skip" href="#main">{t["skip"]}</a>
<header class="nz-masthead">
  <div class="nz-masthead-inner">
    <a class="nz-lockup" href="{lr("")}" aria-label="Norantz, by Plural Futures: home">
      <picture>
        <source srcset="{asset(route, "logos/norantz-lockup-paper.svg")}" media="(prefers-color-scheme: dark)">
        <img src="{asset(route, "logos/norantz-lockup-ink.svg")}" alt="Norantz" width="203" height="40">
      </picture>
      <span class="nz-endorse">{t["by"]}</span>
    </a>
    <nav class="nz-nav" aria-label="{t["main_nav"]}"><ul>{navitems}</ul></nav>
    <nav class="nz-langs" aria-label="{t["lang_nav"]}"><ul>{langs}</ul></nav>
  </div>
</header>'''


def draftband(lang, text, toggle):
    t = T[lang]
    tog = (f'<label class="nz-toggle"><input type="checkbox" id="show-notes" checked> {t["notes"]}</label>'
           if toggle else "")
    return (f'<div class="nz-draftband" role="note"><div class="nz-draftband-inner">'
            f'<span>{esc(text)}</span>{tog}</div></div>')


def crumbs_html(route, lang, crumbs):
    if not crumbs:
        return ""
    items = []
    for i, (label, r) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{esc(label)}</li>')
        else:
            items.append(f'<li><a href="{rel(route, lang_route(lang, r))}">{esc(label)}</a></li>')
    return (f'<nav class="nz-crumbs nz-site" aria-label="{T[lang]["crumbs"]}"><ol>'
            + "".join(items) + "</ol></nav>")


def footer(route, lang):
    t = T[lang]
    cols = []
    for head, links in FOOTER:
        lis = "".join(f'<li><a href="{rel(route, lang_route(lang, r))}">{t[k]}</a></li>' for k, r in links)
        cols.append(f'<div class="nz-fcol"><p class="nz-label">{t[head]}</p><ul>{lis}</ul></div>')
    return f'''<footer class="nz-footer nz-sitefooter" data-theme="dark">
  <div class="nz-footer-inner">
    <div class="nz-fbrand">
      <div class="nz-lockup">
        <img src="{asset(route, "logos/norantz-lockup-paper.svg")}" alt="Norantz" width="203" height="40">
        <span class="nz-endorse">{t["by"]}</span>
      </div>
      <p>{t["blurb"]}</p>
      <p class="nz-label">{t["motto"]}</p>
    </div>
    <div class="nz-fcols">{"".join(cols)}</div>
    <div class="nz-fbase">
      <a href="https://pluralfutures.com">{t["endorse"]}</a>
      <span>{t["rights"]}</span>
    </div>
  </div>
</footer>'''


def page(route, lang, meta, body, alt):
    title = meta["title"]
    if "· Norantz" not in title and route not in ("", "es/", "id/"):
        title += " · Norantz"
    hreflangs = "".join(
        f'<link rel="alternate" hreflang="{LANG_HTML[l]}" href="{rel(route, alt[l])}">' for l in LANGS)
    wrap = meta.get("wrap", True)
    content = (f'<main class="nz-site nz-page" id="main">\n{body}\n</main>' if wrap
               else f'<div id="main">\n{body}\n</div>')
    body_class = meta.get("body_class", "")
    return f'''<!doctype html>
<html lang="{LANG_HTML[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta.get("description", ""))}">
<meta name="robots" content="noindex">
<!-- Generated by scripts/build_site.py from site-src/. Do not edit by hand. -->
{hreflangs}
<link rel="icon" href="{asset(route, "logos/norantz-mark-sky.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{asset(route, "tokens.css")}">
<link rel="stylesheet" href="{asset(route, "report-page.css")}">
<link rel="stylesheet" href="{asset(route, "site.css")}">
</head>
<body{f' class="{body_class}"' if body_class else ""}>
{masthead(route, lang, meta.get("nav"), alt)}
{draftband(lang, meta.get("draft") or T[lang]["zero"], meta.get("notes_toggle", False))}
{crumbs_html(route, lang, meta.get("crumbs"))}
{content}
{footer(route, lang)}
<script src="{asset(route, "site.js")}"></script>
</body>
</html>
'''


# ---------------------------------------------------------------- fragments

META_RE = re.compile(r"\A<!--meta (\{.*?\}) -->\n", re.S)


def read_fragment(path):
    text = path.read_text(encoding="utf-8")
    m = META_RE.match(text)
    if not m:
        sys.exit(f"{path}: missing <!--meta {{...}} --> on the first line")
    return json.loads(m.group(1)), text[m.end():]


def route_for(path):
    p = path.relative_to(SRC / "pages").as_posix()
    if p == "index.html":
        return ""
    if p == "404.html":
        return "404"
    if p.endswith("/index.html"):
        return p[: -len("index.html")]
    return p[: -len(".html")] + "/"


def fill(body, route):
    """Replace {{tokens}} in a fragment."""
    subs = {
        "root": "../" * depth(route),
        "latest_cards": lambda: latest_cards(route),
        "state_counts": lambda: state_counts_html(route),
        "map": lambda: map_svg(route),
        "map_small": lambda: map_svg(route, small=True),
        "map_key": map_key,
        "filters": filters,
        "report_list": lambda: report_list(route),
        "country_list": lambda: country_list(route),
        "glyphs": lambda: (SRC / "partials" / "glyphs.html").read_text(encoding="utf-8"),
        "n_reports": lambda: str(len(REPORTS)),
    }

    def rep(m):
        v = subs.get(m.group(1))
        if v is None:
            sys.exit(f"unknown token {{{{{m.group(1)}}}}} in a fragment for /{route}")
        return v() if callable(v) else v

    return re.sub(r"\{\{([a-z_]+)\}\}", rep, body)


def build(out):
    global OUT
    OUT = out
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    pages = {}  # route -> (meta, body)
    for f in sorted((SRC / "pages").rglob("*.html")):
        meta, body = read_fragment(f)
        if meta.get("report"):
            r = BY_SLUG[meta["report"]]
            c = COUNTRIES[r["country"]]
            meta.setdefault("crumbs", [["Reports", "reports/"], [c["name"], f'countries/{r["country"]}/'],
                                       [r["short"], r["page"]]])
            meta.setdefault("wrap", False)
        pages[route_for(f)] = (meta, body)

    # Country pages and register pages from partials.
    ctpl_meta, ctpl = read_fragment(SRC / "partials" / "country.html")
    for slug, c in COUNTRIES.items():
        rs = reports_for(slug)
        meta = dict(ctpl_meta, title=f'{c["name"]}: national reports',
                    description=f'Every listed national vision or scenario report for {c["name"]}.',
                    crumbs=[["Countries", "countries/"], [c["name"], f"countries/{slug}/"]])
        links = [f'<li>{links_html("", r)}</li>' for r in rs if links_html("", r) and r["state"] != "listed"]
        body = (ctpl.replace("{{country}}", esc(c["name"]))
                .replace("{{region}}", esc(c["region"]))
                .replace("{{count}}", f'{len(rs)} report{"s" if len(rs) > 1 else ""}')
                .replace("{{links}}", ('<ul>' + "".join(dict.fromkeys(links)) + '</ul>') if links else
                         '<p>No links between reports recorded yet.</p>')
                .replace("{{extra}}", c.get("extra", "")))
        pages[f"countries/{slug}/"] = (meta, body.replace("{{country_reports}}", "{{country_reports:" + slug + "}}"))

    rtpl_meta, rtpl = read_fragment(SRC / "partials" / "register.html")
    for r in REPORTS:
        if r["state"] == "reviewed" and not r.get("paired"):
            c = COUNTRIES[r["country"]]
            meta = dict(rtpl_meta, title=f'{r["short"]}: full register',
                        description=f'Every claim, goal and commitment logged for {r["short"]}.',
                        crumbs=[["Reports", "reports/"], [r["short"], r["page"]], ["Register", r["page"] + "register/"]])
            body = (rtpl.replace("{{short}}", esc(r["short"])).replace("{{coverage}}", esc(r["coverage"]))
                    .replace("{{as_of}}", r["reviewed_as_of"]).replace("{{report_page}}", r["page"]))
            pages[r["page"] + "register/"] = (meta, body)

    # Alternates: every page exists in every language (stubs), except report pages
    # (and their registers), which exist in English and the report's own language.
    def own_lang(route):
        for r in REPORTS:
            if r.get("page") and not r.get("paired") and route.startswith(r["page"]):
                return {"es": "es", "id": "id"}.get(r["title_lang"])
        return "all"

    def alternates(route):
        ol = own_lang(route)
        alt = {}
        for l in LANGS:
            if l == "en" or ol == "all" or ol == l:
                alt[l] = lang_route(l, route) if route != "404" else lang_route(l, "")
            else:
                alt[l] = lang_route(l, "reports/")
        return alt

    written = []
    for route, (meta, body) in pages.items():
        body = fill(body, route)
        body = re.sub(r"\{\{country_reports:([a-z-]+)\}\}",
                      lambda m: report_list(route, reports_for(m.group(1))), body)
        out_route = route if route != "404" else "404"
        html_ = page(route if route != "404" else "", "en", meta, body, alternates(route))
        f = out_file(out_route)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html_, encoding="utf-8")
        written.append(route)

        # Language stubs.
        if route == "404":
            continue
        ol = own_lang(route)
        for l in ("es", "id"):
            if ol != "all" and ol != l:
                continue
            lroute = lang_route(l, route)
            t = T[l]
            stub_meta = {"title": meta["title"].split(" · ")[0], "description": meta.get("description", ""),
                         "nav": meta.get("nav")}
            stub = (f'<section class="nz-stub"><p class="nz-label">{t["stub_label"]}</p>'
                    f'<h1 class="nz-h1">{t["stub_h"]}</h1>'
                    f'<p class="nz-lead">{t["stub_p"]}</p>'
                    f'<p><a href="{rel(lroute, route)}" hreflang="en-GB">{t["stub_link"]}: '
                    f'<span lang="en-GB">{esc(stub_meta["title"])}</span></a></p>'
                    f'<p class="nz-note"><b>[PLACEHOLDER]</b> Every page exists at its {l.upper()} address from launch '
                    f'(decision S8). Translations are not written; interface labels are machine drafts.</p></section>')
            f = out_file(lroute)
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(page(lroute, l, stub_meta, stub, alternates(route)), encoding="utf-8")

    # Assets.
    adir = OUT / "assets"
    adir.mkdir(exist_ok=True)
    for f in (SRC / "assets").iterdir():
        shutil.copy2(f, adir / f.name)
    shutil.copy2(ROOT / "brand" / "tokens.css", adir / "tokens.css")
    shutil.copytree(ROOT / "brand" / "logos", adir / "logos")
    (OUT / ".nojekyll").write_text("")
    return written


def tree(d):
    return {p.relative_to(d).as_posix(): p.read_bytes() for p in d.rglob("*") if p.is_file()}


def main():
    if "--check" in sys.argv:
        with tempfile.TemporaryDirectory() as tmp:
            build(Path(tmp) / "site")
            fresh = tree(Path(tmp) / "site")
            current = tree(ROOT / "site") if (ROOT / "site").exists() else {}
            if fresh != current:
                changed = sorted(set(fresh) ^ set(current) | {k for k in fresh if current.get(k) != fresh[k]})
                print("site/ is stale; run python3 scripts/build_site.py. First differences:", *changed[:10], sep="\n  ")
                sys.exit(1)
        print("site/ is up to date")
        return
    written = build(ROOT / "site")
    n = sum(1 for _ in (ROOT / "site").rglob("index.html"))
    print(f"Built {n} pages ({len(written)} English) into site/")


if __name__ == "__main__":
    main()
