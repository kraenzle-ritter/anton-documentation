#!/usr/bin/env python3
"""
Faengt Links, die im Fallback-Build einer anderen Sprache ins Leere zeigen.

Der Admin- und der Developer-Bereich werden nur auf Deutsch und Englisch
gepflegt, der User-Bereich viersprachig. `fallback_to_default: true` zieht eine
nicht uebersetzte Seite trotzdem nach /fr/ und /it/ — mit deutschem Inhalt. Ein
Link von dort in den User-Bereich landet dann auf `import.fr.md`, wo die
Ueberschrift franzoesisch heisst und der automatische Anker entsprechend anders:

    docs/admin/sip-ingest.md:  [Import](../user/import.md#import-protokoll)
    docs/user/import.fr.md:    ### Journal des imports   ->  #journal-des-imports

Der Link bricht still. mkdocs meldet das als INFO, und `--strict` laesst es
durch — die Meldung kommt vom i18n-Plugin, nicht vom Link-Validator von mkdocs,
den `validation.anchors` scharf stellt. Dieses Skript liest den Build-Output
und macht daraus einen Fehler.

Das Gegenmittel im Text ist ein *expliziter* Anker, in allen Sprachfassungen
gleich lautend, damit er die Uebersetzung ueberlebt:

    ### Import-Protokoll {#import-protokoll}
    ### Journal des imports {#import-protokoll}

`scripts/check-translations.py` prueft, dass explizite Anker der deutschen
Quelle in den Uebersetzungen ankommen. Dieses Skript hier prueft das Ergebnis am
gebauten Site-Baum — es faengt also auch, was beim Verlinken schiefging.

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/check-anchors.py           # Exit 1 bei gebrochenen Ankern
    python3 scripts/check-anchors.py --quiet    # nur die Fundstellen
"""
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# INFO -  Doc file 'admin/sip-ingest.md' contains a link '../user/import.md#x',
#         but the doc 'user/import.fr.md' does not contain an anchor '#x'.
BROKEN = re.compile(
    r"Doc file '(?P<src>[^']+)' contains a link '(?P<link>[^']+)', "
    r"but the doc '(?P<target>[^']+)' does not contain an anchor '(?P<anchor>[^']+)'"
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true",
                    help="nur die Fundstellen ausgeben, keine Erklaerung")
    args = ap.parse_args()

    # In ein Wegwerf-Verzeichnis bauen, damit ein site/ aus einem frueheren
    # Lauf unangetastet bleibt und der Check nebenwirkungsfrei ist.
    with tempfile.TemporaryDirectory() as tmp:
        proc = subprocess.run(
            ["mkdocs", "build", "--site-dir", tmp],
            cwd=REPO, capture_output=True, text=True,
        )

    if proc.returncode != 0:
        print("Der Build selbst ist fehlgeschlagen — erst den beheben:\n")
        print(proc.stderr.strip() or proc.stdout.strip())
        return proc.returncode

    findings = []
    for line in (proc.stdout + proc.stderr).split("\n"):
        if m := BROKEN.search(line):
            findings.append(m.groupdict())

    if not findings:
        print("Keine gebrochenen Anker.")
        return 0

    # Dieselbe Quelle bricht typischerweise in mehreren Sprachen gleich; nach
    # Quelle gruppiert liest sich das als ein Problem, nicht als drei.
    by_source: dict[tuple[str, str], list[str]] = {}
    for f in findings:
        by_source.setdefault((f["src"], f["link"]), []).append(f["target"])

    print(f"{len(by_source)} gebrochene(r) Anker:\n")
    for (src, link), targets in sorted(by_source.items()):
        print(f"  {src}")
        print(f"      Link:  {link}")
        print(f"      fehlt in:  {', '.join(sorted(targets))}")

    if not args.quiet:
        print("\nBeheben: der Zielueberschrift in *allen* Sprachfassungen "
              "denselben expliziten Anker geben, z.B.")
        print("    ### Import-Protokoll {#import-protokoll}")
        print("    ### Journal des imports {#import-protokoll}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
