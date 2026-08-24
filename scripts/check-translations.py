#!/usr/bin/env python3
"""
Meldet Uebersetzungen, die ihrer deutschen Quelle hinterherhinken.

Deutsch ist die Quellsprache. Zu jeder Seite `docs/pfad/seite.md` kann es
Uebersetzungen `docs/pfad/seite.en.md`, `.fr.md`, `.it.md` geben. Wird die
deutsche Seite geaendert, ohne dass die Uebersetzung nachgezogen wird, driftet
sie — und veraltete Doku ist schlechter als gar keine.

Der Check hat zwei Teile, weil eine Uebersetzung auf zwei Arten driftet:

*Zeitstempel* — die deutsche Seite ist neuer als ihre Uebersetzung.
Vergleichsmassstab ist der letzte Commit, der die jeweilige Datei angefasst hat;
uncommittete Aenderungen im Working Tree zaehlen mit, damit der Check schon vor
dem Commit anschlaegt.

*Struktur* — beide wurden angefasst, aber die Uebersetzung hat einen Abschnitt
weniger, eine Tabelle mehr oder einen anderen expliziten Anker. Das faengt den
Fall, den der Zeitstempel nicht sieht: eine Uebersetzung, die im selben Commit
nur halb nachgezogen wurde. Verglichen wird die *Form*, nie der Text — die
Ueberschrift heisst uebersetzt ja anders. Gezaehlt wird ausserhalb von
Code-Bloecken, sonst zaehlt ein `# Kommentar` in einem Shell-Beispiel als
Ueberschrift.

Explizite Anker (`{#import-protokoll}`) muessen in allen Sprachen gleich lauten.
Sie sind das Mittel gegen brechende Links, wenn eine nur deutsch/englisch
gepflegte Seite (Admin) in den viersprachigen User-Bereich verlinkt: der
fallback_to_default-Build zieht die deutsche Seite nach /fr/ und /it/, wo der
automatische Anker anders heisst. Siehe scripts/check-anchors.py.

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/check-translations.py             # Bericht, Exit 0
    python3 scripts/check-translations.py --strict    # Exit 1 bei Drift
    python3 scripts/check-translations.py --lang fr   # nur eine Sprache
    python3 scripts/check-translations.py --no-structure   # nur Zeitstempel
"""
import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
LANGS = ("en", "fr", "it")

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+\S")
ADMONITION = re.compile(r"^\s*(!!!|\?\?\?)\s+\w")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
EXPLICIT_ANCHOR = re.compile(r"\{#([A-Za-z0-9_-]+)\}")


def last_change(path: Path) -> int | None:
    """Unix-Zeit der letzten Aenderung: Working Tree schlaegt Commit."""
    rel = path.relative_to(REPO).as_posix()
    dirty = subprocess.run(
        ["git", "status", "--porcelain", "--", rel],
        cwd=REPO, capture_output=True, text=True,
    ).stdout.strip()
    if dirty:
        # Noch nicht committet — gilt als "gerade eben geaendert".
        return int(path.stat().st_mtime)
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", rel],
        cwd=REPO, capture_output=True, text=True,
    ).stdout.strip()
    return int(out) if out else None


def slugify(text: str) -> str:
    """Der Anker, den Python-Markdown aus einer Ueberschrift bildet.

    Nachgebaut aus markdown.extensions.toc.slugify (ohne unicode_slugs):
    nach ASCII falten (»Integritaet« wird zu `integritat`, nicht `integritaet`),
    Satzzeichen weg, klein, Leerraum zu Bindestrichen.
    """
    text = re.sub(r"`([^`]*)`", r"\1", text)          # Code-Auszeichnung
    text = re.sub(r"\*\*?([^*]*)\*\*?", r"\1", text)  # fett / kursiv
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # Links
    text = EXPLICIT_ANCHOR.sub("", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def anchors_of(path: Path) -> set[str]:
    """Alle Anker einer Seite: explizit gesetzte und automatisch gebildete."""
    found: set[str] = set()
    in_fence = False
    for line in path.read_text(encoding="utf-8").split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        found.update(EXPLICIT_ANCHOR.findall(line))
        if m := HEADING.match(line):
            rest = line[len(m.group(1)):]
            if not EXPLICIT_ANCHOR.search(rest):
                found.add(slugify(rest))
    return found


def shape(path: Path) -> dict:
    """Die Form einer Seite: was sich sprachunabhaengig vergleichen laesst.

    Ueberschriften als Folge ihrer Ebenen (`[1, 2, 2, 3]`) — der Text ist
    uebersetzt und taugt nicht zum Vergleich, die Gliederung dagegen schon.
    Code-Bloecke, Admonitions und Tabellenzeilen als Zahl. Explizite Anker als
    Menge, denn die muessen woertlich uebereinstimmen.
    """
    levels: list[int] = []
    fences = admonitions = table_rows = 0
    anchors: set[str] = set()
    in_fence = False

    for line in path.read_text(encoding="utf-8").split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
            fences += 1
            continue
        if in_fence:
            continue
        anchors.update(EXPLICIT_ANCHOR.findall(line))
        if m := HEADING.match(line):
            levels.append(len(m.group(1)))
        elif ADMONITION.match(line):
            admonitions += 1
        elif TABLE_ROW.match(line):
            table_rows += 1

    return {
        "headings": levels,
        "code_blocks": fences // 2,
        "admonitions": admonitions,
        "table_rows": table_rows,
        "anchors": anchors,
    }


def compare_shape(src: Path, tr: Path) -> list[str]:
    """Nennt die Formunterschiede zwischen Quelle und Uebersetzung."""
    a, b = shape(src), shape(tr)
    diffs: list[str] = []

    if a["headings"] != b["headings"]:
        diffs.append(
            f"Gliederung: {len(a['headings'])} Ueberschriften in der Quelle, "
            f"{len(b['headings'])} in der Uebersetzung"
            if len(a["headings"]) != len(b["headings"])
            else "Gliederung: gleiche Zahl an Ueberschriften, andere Ebenen"
        )

    for key, label in (("code_blocks", "Code-Bloecke"),
                       ("admonitions", "Admonitions"),
                       ("table_rows", "Tabellenzeilen")):
        if a[key] != b[key]:
            diffs.append(f"{label}: {a[key]} vs. {b[key]}")

    # Ein expliziter Anker der Quelle muss die Uebersetzung erreichen, sonst
    # bricht ein sprachuebergreifender Link im Fallback-Build.
    if missing := a["anchors"] - anchors_of(tr):
        diffs.append("fehlende Anker: " + ", ".join(f"{{#{x}}}" for x in sorted(missing)))

    # Umgekehrt ist ein expliziter Anker in der Uebersetzung erwuenscht, solange
    # er einen Anker der deutschen Quelle nachbildet — genau so haelt man den
    # deutschen Anker ueber alle Sprachen stabil. Nur ein Anker, den es auf der
    # Quellseite gar nicht gibt, ist ein Fehler: er zeigt ins Leere.
    if stray := b["anchors"] - anchors_of(src):
        diffs.append("Anker ohne Entsprechung in der Quelle: "
                     + ", ".join(f"{{#{x}}}" for x in sorted(stray)))

    return diffs


def sources() -> list[Path]:
    """Alle deutschen Quellseiten (ohne die Sprach-Suffix-Dateien selbst)."""
    return sorted(
        p for p in DOCS.rglob("*.md")
        if len(p.suffixes) < 2 or p.suffixes[-2].lstrip(".") not in LANGS
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="Exit 1, wenn Uebersetzungen veraltet sind")
    ap.add_argument("--lang", choices=LANGS, help="nur diese Sprache pruefen")
    ap.add_argument("--no-structure", action="store_true",
                    help="nur den Zeitstempel vergleichen, nicht die Form")
    args = ap.parse_args()
    langs = (args.lang,) if args.lang else LANGS

    stale: list[tuple[str, str]] = []
    drifted: list[tuple[str, str, list[str]]] = []
    translated = {lang: 0 for lang in langs}
    total = 0

    for src in sources():
        total += 1
        src_time = last_change(src)
        for lang in langs:
            tr = src.with_suffix(f".{lang}.md")
            if not tr.exists():
                continue
            translated[lang] += 1
            tr_rel = tr.relative_to(DOCS).as_posix()
            src_rel = src.relative_to(DOCS).as_posix()

            tr_time = last_change(tr)
            if src_time is not None and tr_time is not None and tr_time < src_time:
                stale.append((tr_rel, src_rel))

            if not args.no_structure and (diffs := compare_shape(src, tr)):
                drifted.append((tr_rel, src_rel, diffs))

    for lang in langs:
        n = translated[lang]
        print(f"{lang}: {n}/{total} Seiten uebersetzt ({n * 100 // total}%)")

    if stale:
        print(f"\n{len(stale)} veraltete Uebersetzung(en) (Zeitstempel):")
        for tr, src in stale:
            print(f"  {tr}  <-  {src} ist neuer")

    if drifted:
        print(f"\n{len(drifted)} Uebersetzung(en) mit abweichender Form:")
        for tr, src, diffs in drifted:
            print(f"  {tr}  <-  {src}")
            for d in diffs:
                print(f"      {d}")

    if stale or drifted:
        print("\nNachziehen und die Uebersetzung im selben oder einem "
              "Folge-Commit aktualisieren.")
        return 1 if args.strict else 0

    print("\nKeine veralteten Uebersetzungen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
