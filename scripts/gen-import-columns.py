#!/usr/bin/env python3
"""
Erzeugt die Spaltentabelle des Tabellen-Imports in docs/user/import.md und
docs/user/import.en.md aus `php artisan anton:import-columns` (anton.test).

Die Tabelle kommt aus derselben Quelle wie die Hilfe im Reiter «Dokumentation»
in Anton (Anton\\Services\\Import\\ColumnReference): Namen, Aliase, Pflicht,
Art, Trennzeichen aus den Regeln des Imports, die Beschreibungen aus Antons
Sprachdateien. Hilfe und Doku widersprachen sich, weil beide von Hand
gepflegt wurden (Kritik Marc, 24.11.2026).

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/gen-import-columns.py           # beide Seiten schreiben
    python3 scripts/gen-import-columns.py --check   # nur prüfen, Exit 1 bei Drift

Setzt voraus, dass DDEV in ../anton.test läuft. Die Trennzeichen sind die des
Mandanten kr, also die Vorgaben einer neuen Installation.
"""
import argparse
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
ANTON = DOCS.parent / "anton.test"
BEGIN = "<!-- BEGIN generated import columns -->"
END = "<!-- END generated import columns -->"
PAGES = {"de": DOCS / "docs/user/import.md", "en": DOCS / "docs/user/import.en.md"}


def table(locale: str) -> str:
    out = subprocess.run(
        ["ddev", "exec", "php", "artisan", "anton:import-columns", "--env=kr", f"--locale={locale}"],
        cwd=ANTON, capture_output=True, text=True, check=True, timeout=120,
    ).stdout
    lines = [line for line in out.splitlines() if line.startswith("|")]
    if len(lines) < 3:
        raise SystemExit(f"anton:import-columns ({locale}) gab keine Tabelle aus")
    return "\n".join(lines) + "\n"


def replaced(text: str, block: str, page: Path) -> str:
    if BEGIN not in text or END not in text:
        raise SystemExit(f"{page}: Marken {BEGIN} / {END} fehlen")
    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{BEGIN}\n\n{block}\n{END}{tail}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    drift = False
    for locale, page in PAGES.items():
        text = page.read_text()
        new = replaced(text, table(locale), page)
        if new != text:
            drift = True
            if not args.check:
                page.write_text(new)
                print(f"{page.relative_to(DOCS)}: Spaltentabelle aktualisiert")
    if args.check and drift:
        print("Spaltentabelle weicht von anton:import-columns ab", file=sys.stderr)
        return 1
    if not drift:
        print("Spaltentabelle: keine Änderung nötig")
    return 0


if __name__ == "__main__":
    sys.exit(main())
