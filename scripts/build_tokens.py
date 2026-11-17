"""Generate brand/tokens.css from brand/tokens.json.

Usage: python3 scripts/build_tokens.py [--check]

tokens.json is the source of truth (exported from the Norantz design-system
artifact). Never edit tokens.css by hand: change tokens.json and re-run.
With --check, exit 1 if tokens.css is out of date (for CI).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "brand" / "tokens.json"
OUT = ROOT / "brand" / "tokens.css"
PREFIX = "nz"

ALIAS = re.compile(r"^\{([A-Za-z0-9][A-Za-z0-9_.-]*)\}$")
NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")


def var(name):
    return f"--{PREFIX}-{name}"


def css_value(value, color_names):
    """Turn a token value into CSS, resolving {alias} to var()."""
    if isinstance(value, (int, float)):
        return repr(value) if isinstance(value, float) else str(value)
    m = ALIAS.match(value)
    if m:
        target = m.group(1)
        if target not in color_names:
            raise SystemExit(f"alias to missing colour token: {value}")
        return f"var({var(target)})"
    return value


def themed(tokens, theme_ids, color_names):
    """Split token values into {theme_id: [(name, css)]}; first theme is the default."""
    out = {t: [] for t in theme_ids}
    first = theme_ids[0]
    for tok in tokens:
        v = tok["value"]
        if not isinstance(v, dict):
            v = {first: v}
        for t in theme_ids:
            if t in v:
                out[t].append((tok["name"], css_value(v[t], color_names)))
            elif t == first:
                raise SystemExit(f"{tok['name']} has no value for default theme {first}")
    return out


def build(data):
    color = data["color"]
    theme_ids = [t["id"] for t in color["themes"]]
    first = theme_ids[0]
    color_names = {t["name"] for t in color["tokens"]}

    seen = set()
    for fam, block in data.items():
        if isinstance(block, dict) and "tokens" in block:
            for tok in block["tokens"]:
                n = tok["name"]
                if not NAME.match(n) or n in seen:
                    raise SystemExit(f"bad or duplicate token name: {n}")
                seen.add(n)

    by_theme = {t: [] for t in theme_ids}
    for fam in ("color", "shadow"):
        if fam in data:
            for t, rows in themed(data[fam]["tokens"], theme_ids, color_names).items():
                by_theme[t].extend(rows)

    plain = []
    for fam in ("spacing", "radius", "stroke", "opacity"):
        for tok in data.get(fam, {}).get("tokens", []):
            plain.append((tok["name"], css_value(tok["value"], color_names)))

    typ = data["type"]
    fonts = [(f"font-{k}", v) for k, v in typ["families"].items()]
    styles = []
    for group in typ["groups"]:
        fam = group["family"]
        for s in group["styles"]:
            n = s["name"]
            rows = [
                (f"{n}-family", f"var({var('font-' + fam)})"),
                (f"{n}-size", s["fontSize"]),
                (f"{n}-line", css_value(s["lineHeight"], color_names)),
                (f"{n}-weight", css_value(s["fontWeight"], color_names)),
            ]
            if "letterSpacing" in s:
                rows.append((f"{n}-tracking", s["letterSpacing"]))
            if "fontStyle" in s:
                rows.append((f"{n}-style", s["fontStyle"]))
            styles.append((n, s.get("usage", ""), rows))

    L = []
    w = L.append
    w(f"/* {data['name']} — generated from tokens.json by scripts/build_tokens.py. Do not edit. */")
    w("")
    w(f"/* Default theme: {first} ({color['themes'][0]['name']}). Other themes: set data-theme on any element. */")
    w(":root {")
    for n, v in by_theme[first]:
        w(f"  {var(n)}: {v};")
    w("")
    for n, v in plain:
        w(f"  {var(n)}: {v};")
    w("")
    for n, v in fonts:
        w(f"  {var(n)}: {v};")
    for n, _, rows in styles:
        w("")
        for rn, rv in rows:
            w(f"  {var(rn)}: {rv};")
    w("}")
    for t, meta in zip(theme_ids[1:], color["themes"][1:]):
        w("")
        w(f"/* {meta['name']} theme: covers, closers, social cards, data view at night. Opt-in only. */")
        w(f'[data-theme="{t}"] {{')
        for n, v in by_theme[t]:
            w(f"  {var(n)}: {v};")
        w(f"  color-scheme: {t};")
        w("}")

    w("")
    w("/* Type styles as classes. Usage notes come from tokens.json. */")
    for n, usage, rows in styles:
        w("")
        if usage:
            w(f"/* {usage} */")
        w(f".{PREFIX}-type-{n} {{")
        w(f"  font-family: var({var(n + '-family')});")
        w(f"  font-size: var({var(n + '-size')});")
        w(f"  line-height: var({var(n + '-line')});")
        w(f"  font-weight: var({var(n + '-weight')});")
        names = {rn for rn, _ in rows}
        if f"{n}-tracking" in names:
            w(f"  letter-spacing: var({var(n + '-tracking')});")
        if f"{n}-style" in names:
            w(f"  font-style: var({var(n + '-style')});")
        if "uppercase" in usage.lower():
            w("  text-transform: uppercase;")
        if n == "data":
            w("  font-variant-numeric: tabular-nums;")
        w("}")
    return "\n".join(L) + "\n"


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    css = build(data)
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != css:
            print("brand/tokens.css is out of date; run python3 scripts/build_tokens.py")
            sys.exit(1)
        print("brand/tokens.css is up to date")
        return
    OUT.write_text(css, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(css.splitlines())} lines)")


if __name__ == "__main__":
    main()
