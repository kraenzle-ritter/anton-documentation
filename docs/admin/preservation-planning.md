# Preservation Planning

Anton bietet seit der **v0.40er-Serie** ein Dashboard für die digitale
Langzeitarchivierung — eine Übersicht über Dateiformate, Risiken und
empfohlene Handlungen pro Tenant.

Unter **Admin → Preservation Planning** stehen vier Analyse-Bereiche.

## MIME-Type-Verteilung

Interaktive Charts (Donut / Balken) zeigen, wie sich die Medienbestände
auf MIME-Typen verteilen:

- Anzahl Dateien pro MIME-Typ
- Gesamtgrösse pro MIME-Typ
- Klick auf einen Slice öffnet die Liste der betroffenen Datensätze

Hilft bei Fragen wie: „Wie viele PDFs haben wir?" / „Sind unsere TIFFs
schon migriert?" / „Wie gross ist der Audio-Anteil?".

## NARA-Kategorien

Klassifizierung nach den Standards der **US National Archives**
(NARA Risk/Action Matrix). Jede Datei wird einer Kategorie zugeordnet
(StillImage, Audio, Textual, Video, Geospatial, …) und erhält eine
**Risiko-Stufe** plus eine **empfohlene Aktion** aus der NARA-Liste.

Implementiert über das Anton-Open-Source-Package
[`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk).

Risiko-Stufen:

| Stufe | Bedeutung | Beispiele |
|---|---|---|
| **Low** | Standard-konformes Format, gut dokumentiert | PDF/A, TIFF, WAV |
| **Moderate** | Verbreitetes Format mit Risiken | JPEG, MP3 |
| **High** | Proprietär oder schlecht dokumentiert | DOC, RAW-Bildformate |
| **Unknown** | Format nicht identifiziert | unbekannt |

Empfohlene Aktionen: **retain**, **transform** (z. B. DOC → PDF/A),
**replace** (z. B. RAW → DNG), **monitor**.

## PRONOM-IDs

PRONOM ist die UK-National-Archives-Datenbank für Dateiformat-
Identifikation. Jede Datei in Anton wird über
**Siegfried** (oder die interne `kraenzle-ritter/puidentify`-Library)
mit einer PUID (PRONOM Unique IDentifier) versehen.

Das Dashboard listet:

- Top PUIDs nach Häufigkeit
- Datei-Beispiele pro PUID (klickbar, öffnet den Datensatz)
- Hinweis, wenn eine PUID auf einer NARA-Warn-Liste steht

## Risikobewertung

Konsolidierte Sicht: NARA-Risiko × PUID-Vertrauen × Anzahl. Zeigt
priorisiert, wo Massnahmen sinnvoll sind. Beispiel:

> *„127 Dateien sind WordPerfect 5.x (PUID fmt/192) — NARA empfiehlt
> Migration auf PDF/A. 89 davon sind unter `Akzession 2018/3`."*

Klick auf die Zeile öffnet die Liste mit Bulk-Aktionen (Migration
anstossen, in Sammlung verschieben, etc.).

## Batch-Verarbeitung mit Siegfried

Bei neuen Medien führt Anton die Format-Identifikation asynchron als
Queue-Job aus (`ProcessMediaIdentification`). Für **Bestands-Sichtung**
(z. B. nach einem Migrations-Schritt oder Datenimport) gibt es einen
Batch-Befehl:

```bash
ddev exec php artisan media:identify --env=<tenant>
```

Optionen:

- `--limit=1000` — nur N Dateien
- `--collection=image` — nur Dateien einer Collection
- `--force` — auch Dateien neu identifizieren, die schon eine PUID haben

Der Befehl nutzt **Siegfried** wenn auf dem Server verfügbar
(`which sf`), sonst fällt auf die Pure-PHP-Implementierung von
`puidentify` zurück (langsamer aber hat keine externe Dependency).

## Open-Source-Pakete dieser Pipeline

Drei Pakete aus dem Anton-Umfeld bilden die Preservation-Planning-
Grundlage:

| Package | Zweck |
|---|---|
| [`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk) | NARA-Risk-/Action-Mapping |
| [`kraenzle-ritter/puidentify`](https://github.com/kraenzle-ritter/puidentify) | PRONOM-PUID-Lookup |
| [`ottosmops/office2text`](https://github.com/ottosmops/office2text) | Volltext-Extraktion aus Office-Dateien (für die Suche, nicht direkt Preservation) |

## Wann läuft was?

| Ereignis | Trigger |
|---|---|
| Neue Datei hochgeladen | Async-Queue: PRONOM-Identifikation + NARA-Mapping |
| Datei ersetzt | Async-Queue: gleiche Pipeline neu |
| Manueller Audit | `media:identify` CLI-Befehl |
| Daily Statistics | Cache wird über Nacht neu berechnet (siehe `app/Console/Kernel.php`) |

## Verwandte Themen

- [Console Commands](console-commands.md) — `media:identify`,
  `media:validate-pdfs`, `media:check`
- [SIP Ingest](sip-ingest.md) — bei SIP-Import läuft die
  PRONOM-Identifikation automatisch
