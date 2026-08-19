#!/usr/bin/env python3
"""
Erzeugt den Referenzblock in docs/admin/console-commands.md aus `php artisan list`.

Die Befehle leben in ../anton.test (app/Console/Commands/); ihre Beschreibungen
laufen der handgeschriebenen Doku sonst davon (zuletzt 87 Befehle im Code, 21
dokumentiert). Dieser Generator hält die *vollständige Referenz* am Ende der
Seite aktuell — die kuratierte Prosa darüber bleibt Handarbeit.

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/gen-command-reference.py           # schreibt in die Seite
    python3 scripts/gen-command-reference.py --check    # nur prüfen, Exit 1 bei Drift

Setzt voraus, dass DDEV im Anton-Repo läuft (Standardpfad ../anton.test).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
PAGE = DOCS / "docs" / "admin" / "console-commands.md"
ANTON = DOCS.parent / "anton.test"

# Die Seite gibt es auch uebersetzt (console-commands.en.md …). Der generierte
# Block ist in allen Sprachen derselbe — die Beschreibungen kommen aus
# `artisan` und sind ohnehin englisch. Uebersetzt wird nur der Tabellenkopf.
TABLE_HEADERS = {
    "de": ("Befehl", "Beschreibung"),
    "en": ("Command", "Description"),
    "fr": ("Commande", "Description"),
    "it": ("Comando", "Descrizione"),
}


def pages() -> list[tuple[Path, str]]:
    """Alle Sprachfassungen der Seite mit ihrem Locale."""
    found = [(PAGE, "de")]
    for path in sorted(PAGE.parent.glob("console-commands.*.md")):
        locale = path.suffixes[-2].lstrip(".")
        if locale in TABLE_HEADERS:
            found.append((path, locale))
    return found

# Admin-relevante Namespaces. Alles andere ist intern (boost:, debugbar:,
# ide-helper: …) oder kundenspezifisch (gf:, gosteli:, ballyana: …).
ADMIN_NAMESPACES = {
    "anton", "media", "sip", "typesense", "resources",
    "inge", "notification", "storage",
}
# Einzelne Befehle, die technisch im Namespace liegen, aber nicht für Admins sind.
SKIP = {
    "anton:baseCommand", "anton:antonseed", "anton:word-export",
    "anton:latex", "anton:test-pages", "anton:import-ead",
}
BEGIN = "<!-- BEGIN generated command reference -->"
END = "<!-- END generated command reference -->"


def artisan_list() -> list[dict] | None:
    """Befehlsliste aus dem Nachbar-Repo. None, wenn Anton nicht erreichbar
    ist (z.B. in der GitHub-CI ohne DDEV) — dann fällt --check auf eine
    reine Strukturprüfung zurück."""
    if not ANTON.is_dir():
        return None
    try:
        out = subprocess.run(
            ["ddev", "exec", "php", "artisan", "list", "--format=json"],
            cwd=ANTON, capture_output=True, text=True, check=True, timeout=120,
        ).stdout
        return json.loads(out)["commands"]
    except (FileNotFoundError, subprocess.SubprocessError, json.JSONDecodeError):
        return None


def build_block(commands: list[dict], locale: str = "de") -> str:
    rows = []
    for c in commands:
        name = c["name"]
        if ":" not in name or name.split(":")[0] not in ADMIN_NAMESPACES:
            continue
        if name in SKIP:
            continue
        desc = " ".join((c.get("description") or "").strip().split()).replace("|", "\\|")
        if len(desc) > 96:
            desc = desc[:94] + "…"
        rows.append((name, desc))
    rows.sort()

    head_name, head_desc = TABLE_HEADERS.get(locale, TABLE_HEADERS["de"])
    lines = [BEGIN]
    ns = None
    for name, desc in rows:
        cur = name.split(":")[0]
        if cur != ns:
            ns = cur
            count = sum(1 for n, _ in rows if n.split(":")[0] == ns)
            lines += [f"\n### {ns}: ({count})\n",
                      f"| {head_name} | {head_desc} |", "|---|---|"]
        lines.append(f"| `{name}` | {desc} |")
    lines.append(END)
    return "\n".join(lines) + "\n"


def structure_ok(text: str) -> bool:
    """Prüft ohne Anton, dass der generierte Block vorhanden, nicht leer und
    tabellenförmig ist. Fängt versehentliches Zerstören des Blocks ab."""
    m = re.search(re.escape(BEGIN) + r"(.*?)" + re.escape(END), text, flags=re.S)
    if not m:
        print(f"Marker {BEGIN} / {END} fehlen.", file=sys.stderr)
        return False
    body = m.group(1)
    rows = [ln for ln in body.splitlines() if ln.startswith("| `")]
    if len(rows) < 10:
        print(f"Generierter Block wirkt beschädigt: nur {len(rows)} Befehlszeilen.",
              file=sys.stderr)
        return False
    return True


def main() -> int:
    check = "--check" in sys.argv
    targets = pages()

    for path, _ in targets:
        text = path.read_text()
        if BEGIN not in text or END not in text:
            print(f"Marker {BEGIN} / {END} fehlen in {path}", file=sys.stderr)
            return 2

    commands = artisan_list()

    if commands is None:
        # Anton nicht erreichbar (CI): nur Strukturprüfung, aber über alle
        # Sprachfassungen — eine zerschossene Uebersetzung faellt sonst durch.
        if check:
            ok = all(structure_ok(p.read_text()) for p, _ in targets)
            print(f"Struktur ok in {len(targets)} Sprachfassung(en) (Anton nicht "
                  "erreichbar — volle Drift-Prüfung braucht DDEV)."
                  if ok else "Struktur fehlerhaft.")
            return 0 if ok else 1
        print("Anton nicht erreichbar (DDEV?) — nichts zu tun.", file=sys.stderr)
        return 2

    stale, written = [], []
    for path, locale in targets:
        text = path.read_text()
        block = build_block(commands, locale)
        new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), block.rstrip("\n"),
                     text, flags=re.S)
        if new == text:
            continue
        if check:
            stale.append(path)
        else:
            path.write_text(new)
            written.append(path)

    if check:
        if stale:
            names = ", ".join(p.name for p in stale)
            print(f"Referenz ist veraltet ({names}) — "
                  "`python3 scripts/gen-command-reference.py` ausführen.")
            return 1
        print(f"Referenz ist aktuell ({len(targets)} Sprachfassung(en)).")
        return 0

    if written:
        print("Referenz aktualisiert: " + ", ".join(str(p) for p in written))
    else:
        print("Keine Änderung nötig.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
