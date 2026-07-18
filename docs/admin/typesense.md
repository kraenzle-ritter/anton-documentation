# Schnelle Suche & Galerie (Typesense)

Anton kann die klassische Volltextsuche optional durch ein
[Typesense](https://typesense.org)-Backend ergänzen: eine **schnelle
Sofortsuche** unter `/search-v2` und eine **Typesense-gestützte
Mediengalerie** (Gallery V2). Beide sind **pro Archiv zuschaltbar** und
laufen parallel zur klassischen Suche bzw. Galerie.

!!! info "Pro-Feature"
    Die Typesense-Suche ist ein **Pro-Feature** und derzeit den
    Pro-Kund:innen vorbehalten. Sie setzt einen eigenen Typesense-Server pro
    Kund:in voraus.

!!! note "Optional und mit Fallback"
    Ohne Typesense (Standard) läuft Anton mit der unveränderten
    MySQL-Suche. Ist der Typesense-Server nicht erreichbar, fällt die
    Anwendung automatisch auf die klassische Suche bzw. die Legacy-Galerie
    zurück.

## Was die schnelle Suche bietet

- Sofort-Treffer beim Tippen, plus Autocomplete in der Navigationsleiste
- Eine gemischte, gerankte Trefferliste aus Objekten **und** PDF-/OCR-Volltext
- Facetten-Sidebar: Erschliessungsstufe, Objekttyp, Medien, Akteur:innen /
  Schlagwörter / Orte sowie ein Zeitraum-Schieber
- Sortierung nach Relevanz/Datum; der gesamte Suchzustand steckt in der
  URL (teil- und bookmarkbar)
- Synonyme, „Meinten Sie …?"-Vorschläge und eine lokale Liste der letzten Suchen

Die Mediengalerie V2 bietet eine Filter-Sidebar (Bestände, Schlagwörter,
Medientypen, Zeitraum) mit Live-Trefferzählern bei unveränderter
Kachel-Optik.

## Voraussetzungen

- Ein **Typesense-Server** für die Kund:in (eigener Container oder
  Typesense Cloud).
- Die Verbindungsdaten in der Umgebungsdatei des Archivs (`.env`):

| Variable | Default | Zweck |
|---|---|---|
| `TYPESENSE_ENABLED` | `false` | Schalter (per Einstellung übersteuerbar) |
| `TYPESENSE_HOST` | `localhost` | Host des Servers |
| `TYPESENSE_PORT` | `8108` | Port |
| `TYPESENSE_PROTOCOL` | `http` | `http` / `https` |
| `TYPESENSE_API_KEY` | — | Master-API-Key |
| `TYPESENSE_CONNECTION_TIMEOUT` | `2` | Timeout in Sekunden |
| `TYPESENSE_COLLECTION_PREFIX` | `anton_` | Präfix der Collection-Namen |

Jedes Archiv bekommt eigene, getrennte Such-Sammlungen
(`{prefix}{slug}_objects`, `_media_texts`, `_gallery`) — keine
Vermischung über Mandanten hinweg.

## Einrichtung pro Archiv

Alle Befehle mit `--env=<slug>` (oder im Container vorab `anenv <slug>`):

```bash
php artisan typesense:setup --env=<slug>              # Sammlungen + Synonyme anlegen
php artisan typesense:index --env=<slug>              # Objekte indexieren
php artisan typesense:index-media-texts --env=<slug>  # PDF-/OCR-Volltext indexieren
php artisan typesense:gallery-index --env=<slug>      # Galerie indexieren (für Gallery V2)
php artisan typesense:status --env=<slug>             # Status prüfen
```

Danach das Feature einschalten — über `TYPESENSE_ENABLED=true` in der
`.env` **oder** über die Einstellung `typesense_enabled` in der
Admin-Oberfläche.

!!! tip "Mehrere Archive auf einmal"
    `php artisan typesense:reindex-all-tenants` führt Setup + Indexierung
    über alle aktiven Archive aus (`--only=`, `--exclude=`, `--dry-run`).

!!! warning "Nach einem Schema-Update"
    Wächst das Suchschema mit einem Update, müssen bestehende Archive
    einmalig neu aufgesetzt werden:
    `typesense:setup --fresh --force` gefolgt von den Index-Befehlen.

Die zeitabhängigen Sperrfrist-Freigaben (welche PDF-Inhalte öffentlich
durchsuchbar sind) werden automatisch zum Jahreswechsel neu berechnet —
kein manueller Eingriff nötig.

## Einstellungen: Suche

Alle Einstellungen sind standardmässig leer (= Verhalten wie
ausgeliefert) und benötigen **keine** Neu-Indexierung. Bearbeitbar in der
Admin-Settings-Oberfläche.

| Einstellung | Wirkung |
|---|---|
| `typesense_enabled` | Feature pro Archiv ein/aus |
| `search_facets` | Welche Facetten in welcher Reihenfolge erscheinen (`level_of_description`, `object_type`, `has_media`, `year`, `actor_ids`, `keyword_ids`, `place_ids`). Leer = sinnvoller Default, Facetten ohne Werte werden automatisch ausgeblendet. |
| `search_default_sort` | Standard-Sortierung: `relevance`, `date_desc`, `date_asc` |
| `search_browse_enabled` | Browse-Liste bei leerer Suche (Default: an) |
| `search_per_page` | Treffer pro Seite (Default: 25) |
| `search_weights` | Feldgewichte der Suche, z. B. `{"title":5,"full_text":3,"signature":4}` |
| `typesense_synonyms_extra` | Zusätzliche Synonymgruppen (wirkt nach `typesense:setup`) |

Die **Trefferkarte** wird über das Formular-System (Formtypes `search`
und `search_intern`) gestaltet — mit demselben Editor wie Listen- und
Detailansichten.

## Einstellungen: Galerie V2

| Einstellung | Wirkung |
|---|---|
| `gallery_typesense_enabled` | `/gallery` auf die Typesense-Galerie umstellen (setzt `typesense_enabled` voraus). Default: aus → klassische Galerie. |
| `gallery_filter_fields` | Filter-Layout (Felder + Spaltenbreiten) |
| `gallery_media_types` | Wählbare Medientypen |
| `gallery_fonds` / `gallery_fonds_extern` | Bestände für interne bzw. öffentliche Galerie |
| `gallery_tile_width` | Kachel-Zielbreite in px (optional, Default 240) |

Die übrigen `gallery_*`-Einstellungen siehe [Mediengalerie](gallery.md).

!!! note "Zwei Wege zur neuen Galerie"
    `/gallery-v2` rendert immer die neue Galerie (zum Parallel-Testen);
    `/gallery` wechselt erst mit `gallery_typesense_enabled` auf V2.

## Sicherheit & Sichtbarkeit

Die Zugriffsbeschränkungen sind in die Suche eingebaut: anonyme,
angemeldete und interne Nutzer:innen sehen jeweils genau das, was sie
auch sonst sehen dürfen. Der PDF-/Medien-Volltext respektiert die
**Sperrfrist** — embargierte Inhalte erscheinen nie in der öffentlichen
Suche, auch wenn die Metadaten treffen. Die Galerie reproduziert exakt
die Sichtbarkeitsregeln der klassischen Galerie.
