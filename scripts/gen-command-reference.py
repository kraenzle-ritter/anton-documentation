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


def artisan_list() -> list[dict]:
    out = subprocess.run(
        ["ddev", "exec", "php", "artisan", "list", "--format=json"],
        cwd=ANTON, capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(out)["commands"]


def build_block(commands: list[dict]) -> str:
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

    lines = [BEGIN]
    ns = None
    for name, desc in rows:
        cur = name.split(":")[0]
        if cur != ns:
            ns = cur
            count = sum(1 for n, _ in rows if n.split(":")[0] == ns)
            lines += [f"\n### {ns}: ({count})\n", "| Befehl | Beschreibung |", "|---|---|"]
        lines.append(f"| `{name}` | {desc} |")
    lines.append(END)
    return "\n".join(lines) + "\n"


def main() -> int:
    check = "--check" in sys.argv
    text = PAGE.read_text()
    if BEGIN not in text or END not in text:
        print(f"Marker {BEGIN} / {END} fehlen in {PAGE}", file=sys.stderr)
        return 2

    block = build_block(artisan_list())
    new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), block.rstrip("\n"),
                 text, flags=re.S)

    if check:
        if new != text:
            print("Referenz ist veraltet — `python3 scripts/gen-command-reference.py` ausführen.")
            return 1
        print("Referenz ist aktuell.")
        return 0

    if new != text:
        PAGE.write_text(new)
        print(f"Referenz aktualisiert: {PAGE}")
    else:
        print("Keine Änderung nötig.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
