# Anton Documentation

[![Software License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

Work in progress...

https://documentation.anton.ch

## Deployment of the github page:

https://www.mkdocs.org/user-guide/deploying-your-docs/

```bash
mkdocs gh-deploy
```

## Images

Images must be referenced with a __relative path__ from the document.

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
