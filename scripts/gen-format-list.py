#!/usr/bin/env python3
"""
Erzeugt die Tabellen in docs/admin/formatliste*.md aus der Formatliste von Anton.

Die Liste lebt in ../anton.test (config/format-list.php, Namen und Bedingungen in
resources/lang/<locale>/format-list.php). Sie ist die maschinenlesbare Fassung der
Format-Seiten (formate-*.md, anton#687); was Anton prüft, soll hier stehen,
PUID für PUID (anton#690). Die Prosa über dem Block bleibt Handarbeit.

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/gen-format-list.py           # schreibt in die Seiten
    python3 scripts/gen-format-list.py --check   # nur prüfen, Exit 1 bei Drift

Braucht PHP auf dem Rechner, um die PHP-Dateien zu lesen; kein DDEV.
"""
import json
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
ANTON = DOCS.parent / "anton.test"
BEGIN = "<!-- BEGIN generated format list -->"
END = "<!-- END generated format list -->"

PAGES = {"de": DOCS / "docs" / "admin" / "formatliste.md", "en": DOCS / "docs" / "admin" / "formatliste.en.md"}
HEADERS = {
    "de": ("Stufe", "Format", "Bedingung", "PUIDs", "Seite"),
    "en": ("Level", "Format", "Condition", "PUIDs", "Page"),
}
CATEGORIES = ["image", "pdf", "text", "spreadsheet", "presentation", "audio", "video", "other"]


def php_json(expression: str) -> dict:
    out = subprocess.run(["php", "-r", f"echo json_encode({expression});"], capture_output=True, text=True, check=True, cwd=ANTON)
    return json.loads(out.stdout)


def block(locale: str, entries: list[dict], lang: dict) -> str:
    level_h, format_h, cond_h, puid_h, page_h = HEADERS[locale]
    lines = [BEGIN, ""]
    for category in CATEGORIES:
        rows = [e for e in entries if e["category"] == category]
        if not rows:
            continue
        lines += [f"### {lang['categories'][category]}", "", f"| {level_h} | {format_h} | {cond_h} | {puid_h} | {page_h} |", "|---|---|---|---|---|"]
        for e in rows:
            names = lang["entries"].get(e["key"], {})
            page = e.get("page") or ""
            # formate-uebrige has a section per kind, not one #formate.
            anchor = {"container": "container", "xml": "xml"}.get(e["key"], "formate")
            link = f"[{page}]({page}.md#{anchor})" if page else ""
            puids = ", ".join(f"`{p}`" for p in e["puids"])
            lines.append(f"| {lang['levels'][e['level']]} | {names.get('name', e['key'])} | {names.get('condition', '')} | {puids} | {link} |")
        lines.append("")
    lines.append(END)
    return "\n".join(lines)


def main() -> int:
    check = "--check" in sys.argv
    entries = php_json("(require 'config/format-list.php')['entries']")
    drift = False
    for locale, page in PAGES.items():
        lang = php_json(f"require 'resources/lang/{locale}/format-list.php'")
        text = page.read_text(encoding="utf-8")
        start, end = text.index(BEGIN), text.index(END) + len(END)
        new = text[:start] + block(locale, entries, lang) + text[end:]
        if new != text:
            drift = True
            if not check:
                page.write_text(new, encoding="utf-8")
    if check and drift:
        print("Formatliste weicht von anton.test ab: python3 scripts/gen-format-list.py")
        return 1
    print("Formatliste ist aktuell." if not drift or not check else "")
    return 0


if __name__ == "__main__":
    sys.exit(main())
