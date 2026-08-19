"""Stellt jeder Seite zwei Angaben fuer den Kopf bereit.

* `page_locales` — in welchen Sprachen es diese Seite *wirklich* gibt.
  Nicht alle vier: eine Admin-Seite, die nur auf Deutsch und Englisch
  vorliegt, soll auch nur «de | en» anzeigen. Die Fallback-Fassungen unter
  /fr/ und /it/ zeigen deutschen Text und sind keine Uebersetzung.
* `page_updated` — Datum des letzten Commits, der die Quelldatei angefasst
  hat. Das ist genauer als das Build-Datum: eine Seite, die seit einem Jahr
  unveraendert ist, soll das auch sagen.

Das Datum kommt aus *einem* `git log`-Lauf beim Start, nicht aus einem
Subprozess je Seite — bei 106 Seiten mal vier Sprachen waere das spuerbar.
"""
import subprocess
from pathlib import Path

# Deutsch ist Quellsprache und existiert immer.
SOURCE_LOCALE = "de"
TRANSLATED_LOCALES = ("en", "fr", "it")

# Beschriftung des Datums. Bewusst in allen Sprachen englisch: «Last updated»
# ist auch ausserhalb des Englischen gelaeufig, und die Zeile bleibt damit in
# jeder Sprachfassung gleich lang und gleich erkennbar.
UPDATED_LABEL = "Last updated"

# Beschriftung der Sprachwahl — ohne sie liest sich die Zeile wie eine
# Datenangabe und nicht wie etwas, das man anklicken kann.
LANGUAGE_LABEL = {
    "de": "Sprache",
    "en": "Language",
    "fr": "Langue",
    "it": "Lingua",
}

# Ausgeschriebene Namen statt Kürzel: «Français» versteht auch jemand, der
# nicht weiss, wofür «fr» steht.
LOCALE_NAMES = {
    "de": "Deutsch",
    "en": "English",
    "fr": "Français",
    "it": "Italiano",
}

_commit_dates: dict[str, str] = {}


def on_config(config):
    """Datum des letzten Commits je Datei unter docs/ einlesen."""
    _commit_dates.clear()
    repo = Path(config["docs_dir"]).parent
    try:
        out = subprocess.run(
            ["git", "log", "--pretty=format:%x00%cs", "--name-only", "--", "docs"],
            cwd=repo, capture_output=True, text=True, check=True, timeout=60,
        ).stdout
    except (subprocess.SubprocessError, OSError):
        # Ohne Git-Historie (z.B. flacher Klon) bleibt das Datum einfach weg.
        return config
    date = None
    for line in out.splitlines():
        if line.startswith("\x00"):
            date = line[1:].strip()
        elif line.strip() and date:
            # Der erste Treffer ist der neueste Commit — spaetere ignorieren.
            _commit_dates.setdefault(line.strip(), date)
    return config


def _source_uri(src_uri: str) -> str:
    """`user/objects.fr.md` -> `user/objects.md`."""
    parts = src_uri.split(".")
    if len(parts) > 2 and parts[-2] in TRANSLATED_LOCALES:
        return ".".join(parts[:-2] + parts[-1:])
    return src_uri


def _translation_uri(source_uri: str, locale: str) -> str:
    """`user/objects.md` -> `user/objects.fr.md`."""
    stem, _, ext = source_uri.rpartition(".")
    return f"{stem}.{locale}.{ext}"


def on_page_context(context, page, config, nav):
    docs = Path(config["docs_dir"])
    source_uri = _source_uri(page.file.src_uri)

    available = [SOURCE_LOCALE] + [
        loc for loc in TRANSLATED_LOCALES
        if (docs / _translation_uri(source_uri, loc)).exists()
    ]

    # Massgeblich ist die Sprache der gerade gebauten Site, nicht die der
    # Datei: eine deutsche Fallback-Seite unter /fr/ wird von jemandem
    # gelesen, der auf der franzoesischen Site ist — die Sprachwahl gehoert
    # dort franzoesisch beschriftet. Das i18n-Plugin setzt die Theme-Sprache
    # je Durchlauf. Auf einer Fallback-Seite ist die aktuelle Sprache dann in
    # `available` gar nicht enthalten, es wird also keine als aktiv markiert.
    current = config["theme"]["language"]

    # `page.url` traegt in den Nicht-Default-Builds bereits das Sprachpraefix
    # (`fr/user/objects/`). Fuer die Links brauchen wir den Pfad ohne, damit
    # nicht `/en/fr/user/objects/` daraus wird.
    path = page.url
    for locale in TRANSLATED_LOCALES:
        if path == locale or path.startswith(f"{locale}/"):
            path = path[len(locale):].lstrip("/")
            break

    # Absolute Pfade: die Site laeuft auf der Domain-Wurzel.
    def href(locale: str) -> str:
        prefix = "" if locale == SOURCE_LOCALE else f"/{locale}"
        return f"{prefix}/{path}"

    # Nur anzeigen, wenn es ueberhaupt etwas zu waehlen gibt.
    context["page_locales"] = [
        {
            "code": loc,
            "name": LOCALE_NAMES.get(loc, loc),
            "url": href(loc),
            "current": loc == current,
        }
        for loc in available
    ] if len(available) > 1 else []

    context["page_locales_label"] = LANGUAGE_LABEL.get(current, LANGUAGE_LABEL["de"])
    context["page_updated"] = _commit_dates.get(f"docs/{page.file.src_uri}")
    context["page_updated_label"] = UPDATED_LABEL
    return context
