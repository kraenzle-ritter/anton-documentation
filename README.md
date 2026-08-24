# Anton Documentation

[![Software License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

Work in progress...

https://documentation.anton.ch

## Lokal bauen

CI und Arbeitsplatz ziehen aus derselben Liste, damit ein Build, der lokal
durchläuft, auch in der Pipeline durchläuft:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # Vorschau auf http://127.0.0.1:8000
mkdocs build --strict   # wie in der CI
```

Ohne `mkdocs-static-i18n` bricht der Build schon in der Konfigurationsphase ab
(«The "i18n" plugin is not installed») — die Mehrsprachigkeit hängt daran.

## Deployment of the github page:

https://www.mkdocs.org/user-guide/deploying-your-docs/

```bash
mkdocs gh-deploy
```

## Images

Images must be referenced with a __relative path__ from the document.

## Übersetzungen

Die Doku wird viersprachig geführt (de/en/fr/it, Deutsch ist Quellsprache).
Dateikonvention, Sprachumfang pro Bereich und das verbindliche Glossar stehen in
[TRANSLATING.md](TRANSLATING.md):

```bash
python3 scripts/check-translations.py           # Drift melden (Zeitstempel + Form)
python3 scripts/check-translations.py --strict  # Exit 1 bei Drift
python3 scripts/check-anchors.py                # Anker über Sprachgrenzen prüfen
```

Der Übersetzungs-Check läuft in der CI **nicht blockierend** (sonst bräuchte
jede deutsche Korrektur sofort drei Übersetzungen), der Anker-Check dagegen
**blockierend**: ein Link ins Leere ist kein Rückstand, sondern ein Fehler, und
MkDocs meldet ihn nur als INFO — auch unter `--strict`.

## Console-Command-Referenz

Die Tabelle am Ende von `docs/admin/console-commands.md` (zwischen den
`<!-- BEGIN/END generated command reference -->`-Markern) wird aus Antons
`php artisan list` erzeugt — nicht von Hand pflegen:

```bash
python3 scripts/gen-command-reference.py          # neu erzeugen
python3 scripts/gen-command-reference.py --check   # prüfen (Exit 1 bei Drift)
```

Der Generator liest aus dem Nachbar-Repo `../anton.test` (DDEV muss laufen).
Ein **Pre-Push-Hook** prüft das automatisch; einmal pro Klon aktivieren:

```bash
git config core.hooksPath .githooks
```

Ohne laufendes DDEV fällt die Prüfung auf eine Strukturkontrolle zurück und
blockiert nicht. Auch die CI führt `--check` aus (dort ebenfalls nur
strukturell, da Anton privat und nicht ausgecheckt ist).
