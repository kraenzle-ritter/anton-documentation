#!/usr/bin/env python3
"""
Erzeugt die Referenzblöcke der Befehle aus `php artisan list`:

* Anton: docs/admin/console-commands.md aus ../anton.test, als Tabelle
  (Befehl, Beschreibung) je Namespace;
* Lotte: docs/lotte/commands.md aus ../lotte, nur `lotte:*`, je Befehl mit
  Aufruf, Argumenten und Optionen.

Die Befehle leben in app/Console/Commands/ der beiden Repos; ihre
Beschreibungen laufen der handgeschriebenen Doku sonst davon (zuletzt 87
Befehle im Code, 21 dokumentiert). Dieser Generator hält die *vollständige
Referenz* am Ende der Seite aktuell — die kuratierte Prosa darüber bleibt
Handarbeit.

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/gen-command-reference.py                  # beide Seiten schreiben
    python3 scripts/gen-command-reference.py --check           # nur prüfen, Exit 1 bei Drift
    python3 scripts/gen-command-reference.py --source lotte    # nur eine Quelle

Setzt voraus, dass DDEV im jeweiligen Repo läuft (Standardpfade ../anton.test
und ../lotte). Befehle, die dort nur in der Arbeitskopie stehen (untracked oder
geändert), bleiben aussen vor — dokumentiert wird, was committet ist.
"""
import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent

BEGIN = "<!-- BEGIN generated command reference -->"
END = "<!-- END generated command reference -->"

# Die Seiten gibt es auch uebersetzt (console-commands.en.md …). Der generierte
# Block ist in allen Sprachen derselbe — die Beschreibungen kommen aus
# `artisan` und sind ohnehin englisch. Uebersetzt wird nur der Tabellenkopf.
TABLE_HEADERS = {
    "de": ("Befehl", "Beschreibung"),
    "en": ("Command", "Description"),
    "fr": ("Commande", "Description"),
    "it": ("Comando", "Descrizione"),
}
# Kopf der Tabelle je Befehl im ausfuehrlichen Stil (Lotte).
DETAIL_HEADERS = {
    "de": ("Argument / Option", "Beschreibung", "Vorgabe"),
    "en": ("Argument / option", "Description", "Default"),
    "fr": ("Argument / option", "Description", "Défaut"),
    "it": ("Argomento / opzione", "Descrizione", "Predefinito"),
}

# Optionen, die jeder Laravel-Befehl hat. Sie stehen nicht bei jedem Befehl.
GLOBAL_OPTIONS = {
    "help", "silent", "quiet", "verbose", "version", "ansi", "no-ansi",
    "no-interaction", "env",
}


@dataclass(frozen=True)
class Source:
    """Ein Repo, dessen Befehle in eine Seite der Doku gehoeren."""

    key: str                 # --source
    label: str               # in Meldungen
    repo: Path
    page: Path
    namespaces: frozenset[str]
    # Befehle ohne Namespace, die trotzdem dazugehoeren. Namenlose Befehle sind
    # sonst ausgeschlossen, weil dort Laravels eigene liegen (migrate, serve …).
    plain: frozenset[str] = frozenset()
    # Einzelne Befehle, die technisch im Namespace liegen, aber nicht dazugehoeren.
    skip: frozenset[str] = frozenset()
    # "table": eine Tabelle je Namespace; "detailed": je Befehl ein Abschnitt.
    style: str = "table"
    # Weniger Eintraege im Block heisst: der Block ist beschaedigt.
    min_entries: int = 10
    artisan: tuple[str, ...] = field(default=("list", "--format=json"))

    def includes(self, name: str) -> bool:
        if name in self.plain:
            return True
        return ":" in name and name.split(":")[0] in self.namespaces


SOURCES = {
    "anton": Source(
        key="anton",
        label="Anton",
        repo=DOCS.parent / "anton.test",
        page=DOCS / "docs" / "admin" / "console-commands.md",
        # Admin-relevante Namespaces. Alles andere ist intern (boost:, debugbar:,
        # ide-helper: …) oder kundenspezifisch (gf:, gosteli:, ballyana: …).
        namespaces=frozenset({
            "anton", "media", "sip", "typesense", "resources",
            "inge", "notification", "storage", "format-policy", "contract",
        }),
        # `matomo` registriert einen Mandanten bei Matomo (Website, Benutzer,
        # Token) und war deshalb in keiner Referenz zu finden, obwohl er zur
        # Einrichtung gehört.
        plain=frozenset({"matomo"}),
        skip=frozenset({
            "anton:baseCommand", "anton:antonseed", "anton:word-export",
            "anton:test-pages", "anton:import-ead",
        }),
    ),
    "lotte": Source(
        key="lotte",
        label="Lotte",
        repo=DOCS.parent / "lotte",
        page=DOCS / "docs" / "lotte" / "commands.md",
        namespaces=frozenset({"lotte"}),
        style="detailed",
        artisan=("list", "lotte", "--format=json"),
    ),
}


def pages(source: Source) -> list[tuple[Path, str]]:
    """Alle Sprachfassungen der Seite mit ihrem Locale."""
    found = [(source.page, "de")]
    stem = source.page.stem
    for path in sorted(source.page.parent.glob(f"{stem}.*.md")):
        locale = path.suffixes[-2].lstrip(".")
        if locale in TABLE_HEADERS:
            found.append((path, locale))
    return found


def artisan_list(source: Source) -> list[dict] | None:
    """Befehlsliste aus dem Nachbar-Repo. None, wenn es nicht erreichbar ist
    (z.B. in der GitHub-CI ohne DDEV) — dann fällt --check auf eine reine
    Strukturprüfung zurück."""
    if not source.repo.is_dir():
        return None
    try:
        out = subprocess.run(
            ["ddev", "exec", "php", "artisan", *source.artisan],
            cwd=source.repo, capture_output=True, text=True, check=True, timeout=120,
        ).stdout
        return json.loads(out)["commands"]
    except (FileNotFoundError, subprocess.SubprocessError, json.JSONDecodeError, KeyError):
        return None


def pending_command_names(source: Source) -> set[str]:
    """Befehle, deren Datei im Repo noch nicht committet ist.

    Der Generator liest `php artisan list` aus dem laufenden DDEV und sieht
    damit die Arbeitskopie — also auch Befehle, die gerade erst entstehen. Die
    gehören nicht in die öffentliche Doku: bis zum Commit können sie noch
    umbenannt oder verworfen werden, und beschrieben wäre dann etwas, das es in
    keinem Stand gibt. Dasselbe gilt für geänderte, aber nicht committete
    Beschreibungen.

    Leere Menge, wenn das Repo kein Git-Repo ist oder git fehlt — dann verhält
    sich der Generator wie bisher.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(source.repo), "status", "--porcelain", "--",
             "app/Console/Commands"],
            capture_output=True, text=True, check=True, timeout=30,
        ).stdout
    except (FileNotFoundError, subprocess.SubprocessError):
        return set()

    names = set()
    for line in out.splitlines():
        code, rel = line[:2], line[3:]
        # Geloeschtes listet artisan ohnehin nicht mehr auf.
        if "D" in code:
            continue
        # Umbenanntes steht als «alt -> neu»; gemeint ist der neue Pfad.
        if " -> " in rel:
            rel = rel.split(" -> ", 1)[1]
        f = source.repo / rel.strip('"')
        if not f.is_file():
            continue
        # Der Name steht am Anfang der Signatur, vor Argumenten und Optionen:
        #     protected $signature = 'anton:reencrypt-secrets
        #         {--dry-run}';
        m = re.search(r"protected\s+\$(?:signature|name)\s*=\s*['\"]([^\s'\"{]+)",
                      f.read_text(errors="replace"))
        if m:
            names.add(m.group(1))
    return names


def cell(text: str) -> str:
    """Ein Text als Tabellenzelle: eine Zeile, ohne senkrechte Striche."""
    return " ".join((text or "").strip().split()).replace("|", "\\|")


def build_table(commands: list[dict], source: Source, locale: str) -> str:
    """Eine Tabelle je Namespace: Befehl und Beschreibung (Anton)."""
    rows = []
    for c in commands:
        name = c["name"]
        if not source.includes(name) or name in source.skip:
            continue
        desc = cell(c.get("description") or "")
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
            # Ohne Doppelpunkt fuer Befehle, die keinen Namespace haben
            # (`matomo`) -- «matomo: (1)» las sich wie ein abgeschnittener Name.
            heading = f"{ns}: ({count})" if ":" in name else f"{ns} ({count})"
            lines += [f"\n### {heading}\n",
                      f"| {head_name} | {head_desc} |", "|---|---|"]
        lines.append(f"| `{name}` | {desc} |")
    lines.append(END)
    return "\n".join(lines) + "\n"


def _entries(definition: dict, key: str) -> list[dict]:
    """Argumente oder Optionen einer Befehlsdefinition; `artisan` liefert ein
    leeres Objekt als Liste."""
    value = definition.get(key) or {}
    return list(value.values()) if isinstance(value, dict) else list(value)


def _default(value) -> str:
    """Eine Vorgabe, wie sie in der Zelle steht; leer, wo es keine gibt."""
    if value is None or value is False or value == [] or value == "":
        return ""
    if value is True:
        return "`true`"
    if isinstance(value, list):
        return ", ".join(f"`{v}`" for v in value)
    return f"`{value}`"


def anchor(name: str) -> str:
    """Stabiler Anker eines Befehls, in jeder Sprache gleich: lotte:client:create
    -> lotte-client-create."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def build_detailed(commands: list[dict], source: Source, locale: str) -> str:
    """Je Befehl ein Abschnitt mit Beschreibung, Aufruf und einer Tabelle der
    Argumente und Optionen (Lotte: wenige Befehle, viele Optionen)."""
    head_arg, head_desc, head_default = DETAIL_HEADERS.get(locale, DETAIL_HEADERS["de"])
    lines = [BEGIN]
    for c in sorted(commands, key=lambda c: c["name"]):
        name = c["name"]
        if not source.includes(name) or name in source.skip:
            continue
        definition = c.get("definition") or {}
        rows = []
        for arg in _entries(definition, "arguments"):
            label = f"`<{arg['name']}>`" + ("" if arg.get("is_required") else " (optional)")
            rows.append((label, cell(arg.get("description") or ""), _default(arg.get("default"))))
        for opt in _entries(definition, "options"):
            bare = opt["name"].lstrip("-")
            if bare in GLOBAL_OPTIONS:
                continue
            label = f"`{opt['name']}`"
            if opt.get("accept_value"):
                label = f"`{opt['name']}=…`"
            rows.append((label, cell(opt.get("description") or ""), _default(opt.get("default"))))

        usage = (c.get("usage") or [name])[0]
        lines += [
            f"\n### `{name}` {{#{anchor(name)}}}\n",
            cell(c.get("description") or ""),
            "",
            "```bash",
            f"php artisan {usage}",
            "```",
        ]
        if rows:
            lines += ["", f"| {head_arg} | {head_desc} | {head_default} |", "|---|---|---|"]
            lines += [f"| {a} | {d} | {v} |" for a, d, v in rows]
    lines.append(END)
    return "\n".join(lines) + "\n"


def build_block(commands: list[dict], source: Source, locale: str = "de") -> str:
    if source.style == "detailed":
        return build_detailed(commands, source, locale)
    return build_table(commands, source, locale)


def structure_ok(text: str, source: Source) -> bool:
    """Prüft ohne das Repo, dass der generierte Block vorhanden, nicht leer und
    wohlgeformt ist. Fängt versehentliches Zerstören des Blocks ab."""
    m = re.search(re.escape(BEGIN) + r"(.*?)" + re.escape(END), text, flags=re.S)
    if not m:
        print(f"Marker {BEGIN} / {END} fehlen.", file=sys.stderr)
        return False
    body = m.group(1)
    if source.style == "detailed":
        entries = [ln for ln in body.splitlines() if ln.startswith("### `")]
    else:
        entries = [ln for ln in body.splitlines() if ln.startswith("| `")]
    if len(entries) < source.min_entries:
        print(f"Generierter Block wirkt beschädigt: nur {len(entries)} Befehle.",
              file=sys.stderr)
        return False
    return True


def run(source: Source, check: bool) -> int:
    """0: aktuell bzw. geschrieben; 1: Drift (nur --check); 2: Fehler oder das
    Repo ist nicht erreichbar (nur beim Schreiben)."""
    targets = pages(source)

    for path, _ in targets:
        if not path.is_file():
            print(f"{source.label}: Seite {path} fehlt.", file=sys.stderr)
            return 2
        text = path.read_text()
        if BEGIN not in text or END not in text:
            print(f"Marker {BEGIN} / {END} fehlen in {path}", file=sys.stderr)
            return 2

    commands = artisan_list(source)

    if commands is None:
        # Repo nicht erreichbar (CI): nur Strukturprüfung, aber über alle
        # Sprachfassungen — eine zerschossene Uebersetzung faellt sonst durch.
        if check:
            ok = all(structure_ok(p.read_text(), source) for p, _ in targets)
            print(f"{source.label}: Struktur ok in {len(targets)} Sprachfassung(en) "
                  f"({source.label} nicht erreichbar — volle Drift-Prüfung braucht DDEV)."
                  if ok else f"{source.label}: Struktur fehlerhaft.")
            return 0 if ok else 1
        print(f"{source.label} nicht erreichbar (DDEV?) — nichts zu tun.", file=sys.stderr)
        return 2

    pending = pending_command_names(source)
    if pending:
        # Nur melden, was ueberhaupt in der Referenz stuende — internes und
        # Uebersprungenes interessiert hier nicht.
        hidden = sorted(n for n in pending if source.includes(n) and n not in source.skip)
        commands = [c for c in commands if c["name"] not in pending]
        if hidden:
            print(f"Übergangen, in {source.label} noch nicht committet: " + ", ".join(hidden),
                  file=sys.stderr)

    stale, written = [], []
    for path, locale in targets:
        text = path.read_text()
        block = build_block(commands, source, locale)
        new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: block.rstrip("\n"),
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
            print(f"{source.label}: Referenz ist veraltet ({names}) — "
                  f"`python3 scripts/gen-command-reference.py --source {source.key}` ausführen.")
            return 1
        print(f"{source.label}: Referenz ist aktuell ({len(targets)} Sprachfassung(en)).")
        return 0

    if written:
        print(f"{source.label}: Referenz aktualisiert: " + ", ".join(str(p) for p in written))
    else:
        print(f"{source.label}: keine Änderung nötig.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Command reference from `php artisan list`.")
    parser.add_argument("--check", action="store_true", help="only check, exit 1 on drift")
    parser.add_argument("--source", action="append", choices=sorted(SOURCES),
                        help="only this source (repeatable); default: all")
    args = parser.parse_args()

    codes = [run(SOURCES[key], args.check) for key in (args.source or list(SOURCES))]
    if args.check:
        return max(codes)
    # Beim Schreiben ist ein nicht erreichbares Repo nur dann ein Fehler, wenn
    # gar keines erreichbar war.
    return 2 if all(code == 2 for code in codes) else (1 if 1 in codes else 0)


if __name__ == "__main__":
    sys.exit(main())
