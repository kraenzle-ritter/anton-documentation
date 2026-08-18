#!/usr/bin/env python3
"""
Meldet Uebersetzungen, die ihrer deutschen Quelle hinterherhinken.

Deutsch ist die Quellsprache. Zu jeder Seite `docs/pfad/seite.md` kann es
Uebersetzungen `docs/pfad/seite.en.md`, `.fr.md`, `.it.md` geben. Wird die
deutsche Seite geaendert, ohne dass die Uebersetzung nachgezogen wird, driftet
sie — und veraltete Doku ist schlechter als gar keine.

Vergleichsmassstab ist der letzte Commit, der die jeweilige Datei angefasst hat.
Uncommittete Aenderungen im Working Tree werden mitgezaehlt, damit der Check
schon vor dem Commit anschlaegt.

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/check-translations.py            # Bericht, Exit 0
    python3 scripts/check-translations.py --strict   # Exit 1 bei Drift
    python3 scripts/check-translations.py --lang fr  # nur eine Sprache
"""
import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
LANGS = ("en", "fr", "it")


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
    args = ap.parse_args()
    langs = (args.lang,) if args.lang else LANGS

    stale: list[tuple[str, str]] = []
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
            tr_time = last_change(tr)
            if src_time is not None and tr_time is not None and tr_time < src_time:
                stale.append((tr.relative_to(DOCS).as_posix(),
                              src.relative_to(DOCS).as_posix()))

    for lang in langs:
        n = translated[lang]
        print(f"{lang}: {n}/{total} Seiten uebersetzt ({n * 100 // total}%)")

    if stale:
        print(f"\n{len(stale)} veraltete Uebersetzung(en):")
        for tr, src in stale:
            print(f"  {tr}  <-  {src} ist neuer")
        print("\nNachziehen und die Uebersetzung im selben oder einem "
              "Folge-Commit aktualisieren.")
        return 1 if args.strict else 0

    print("\nKeine veralteten Uebersetzungen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
