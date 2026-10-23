# Preservation Planning

Unter **Admin → Preservation Planning** zeigt Anton, welche Dateiformate im Archiv liegen, wie NARA ihr Risiko bewertet und wo Format- und Virenprüfung stehen. Die Zahlen werden bei jedem Aufruf aus der Datenbank berechnet. Die Seite ist eine Ansicht: Sie meldet nichts von sich aus und löst keine Massnahmen aus; eine Migration läuft über [`media:migrate`](console-commands.md#mediamigrate).

## MIME-Typen

Anzahl und Anteil der Medien je MIME-Typ, als Tabelle und als Kreisdiagramm.

## NARA-Kategorien

Klassifizierung nach den Standards der **US National Archives** (NARA Risk/Action Matrix). Jede Datei wird einer Kategorie zugeordnet (StillImage, Audio, Textual, Video, Geospatial, …) und erhält eine **Risiko-Stufe** plus eine **empfohlene Aktion** aus der NARA-Liste.

Implementiert über das Anton-Open-Source-Package [`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk).

Risiko-Stufen:

| Stufe | Bedeutung | Beispiele |
|---|---|---|
| **Low** | Standard-konformes Format, gut dokumentiert | PDF/A, TIFF, WAV |
| **Moderate** | Verbreitetes Format mit Risiken | JPEG, MP3 |
| **High** | Proprietär oder schlecht dokumentiert | DOC, RAW-Bildformate |
| **Unknown** | Format nicht identifiziert | unbekannt |

Empfohlene Aktionen, wie NARA sie vergibt: **Retain** (behalten), **Retain for Future Assessment** (behalten, später neu bewerten), **Transform** (in ein anderes Format überführen), **Identify** (Format oder Version genauer bestimmen). Medien ohne Erkennung zählt die Ansicht unter **Identify**.

## PRONOM-IDs

PRONOM ist die UK-National-Archives-Datenbank für Dateiformat-Identifikation. Anton versieht jede Datei mit einer PUID (PRONOM Unique IDentifier); die Erkennung leistet **Siegfried** oder **Fido** über die Library `kraenzle-ritter/puidentify`.

Die Tabelle listet die PUIDs nach Häufigkeit, mit Formatname, Anteil und der häufigsten NARA-Risiko-Stufe und -Aktion. «Ansicht» öffnet die Medienliste, gefiltert auf diese PUID; eine eigene Zeile zählt die nicht identifizierten Medien.

## Risikobewertung

Eine Kreuztabelle zählt die Medien nach NARA-Risiko und empfohlener Aktion, zwei Kreisdiagramme zeigen die Verteilung der Risiko-Stufen und der Aktionen. Darunter stehen bis zu 50 Medien mit Handlungsbedarf: nicht identifizierte zuerst, dann die übrigen ausser **Retain**, nach Risiko geordnet.

## Formatprüfung {#formatpruefung}

Wo der Bestand in der [Formatprüfung](preservation.md) steht, je Master nach seiner letzten Prüfung: je Formatgruppe (PDF, TIFF, andere Bilder, Ton und Video) ungültig, gültig mit Warnungen, gültig, nicht geprüft, noch nie geprüft. Dazu, wie weit der Nachtlauf ist (zuletzt gründlich, nur bei der Übernahme, nie), die PDF-Risiken und der PDF/A-Anspruch, Widersprüche zwischen Endung, Format und PRONOM-ID, und die Liste der Medien, die zuletzt ungültig waren, mit Link zum Datensatz. Was wann geprüft wurde, steht unter **Administration → Protokolle → Formatprüfung**.

## Virenprüfung {#virenpruefung}

Je Master das Ergebnis seiner letzten Virenprüfung, bei der Übernahme oder mit [`media:virus-scan`](console-commands.md#mediavirus-scan): Schadsoftware gefunden, nicht prüfbar, ohne Befund in Teilen geprüft (Dateien über 2 GB), ohne Befund, noch nie geprüft. Dazu Scanner und Signaturen der letzten Prüfung und die Liste der Master mit Befund oder nicht prüfbar. Dateien, die schon bei der Übernahme abgewiesen wurden, sind nie Medien geworden; sie stehen im Sicherheitsprotokoll.

## Mediendateien

Alle Medien mit Suche und Filtern nach PUID, NARA-Risiko, NARA-Aktion und MIME-Typ, je mit Link zum Datensatz und zum Download des Masters.

## Batch-Verarbeitung mit Siegfried

Bei neuen Medien führt Anton die Format-Identifikation asynchron als Queue-Job aus (`ProcessMediaIdentification`). Für **Bestands-Sichtung** (z. B. nach einem Migrations-Schritt oder Datenimport) gibt es einen Batch-Befehl:

```bash
ddev exec php artisan media:identify --env=<tenant>
```

Optionen:

- `--limit=1000` — nur N Dateien
- `--collection=image` — nur Dateien einer Collection
- `--force` — auch Dateien neu identifizieren, die schon eine PUID haben
- `--oldest=N` — die N Medien, deren Erkennung am längsten zurückliegt, solche ohne Erkennungsereignis zuerst (schliesst `--force` ein)

Der Befehl nutzt **Siegfried** oder **Fido**, je nachdem, was auf dem Server installiert ist. Fehlen beide, bleibt die Erkennung leer; einen Ersatz ohne externes Programm gibt es nicht. Jede Erkennung steht als Ereignis am Medium, mit Werkzeug, Version und Signaturdatei; eine neue Erkennung bewertet auch das NARA-Risiko neu.

## Open-Source-Pakete dieser Pipeline

Drei Pakete aus dem Anton-Umfeld bilden die Preservation-Planning-Grundlage:

| Package | Zweck |
|---|---|
| [`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk) | NARA-Risk-/Action-Mapping |
| [`kraenzle-ritter/puidentify`](https://github.com/kraenzle-ritter/puidentify) | PRONOM-PUID-Lookup über Siegfried oder Fido |
| [`ottosmops/office2text`](https://github.com/ottosmops/office2text) | Volltext-Extraktion aus Office-Dateien (für die Suche, nicht direkt Preservation) |

## Wann läuft was?

| Ereignis | Trigger |
|---|---|
| Neue Datei hochgeladen | Async-Queue: PRONOM-Identifikation + NARA-Mapping |
| Datei ersetzt | Async-Queue: gleiche Pipeline neu |
| Manueller Audit | `media:identify` CLI-Befehl |
| Dashboard aufgerufen | Zahlen werden beim Aufruf aus der Datenbank berechnet; einen Zeitplan dafür gibt es nicht |

## Verwandte Themen

- [Console Commands](console-commands.md) — `media:identify`, `media:validate-pdfs`, `media:check`
- [SIP Ingest](sip-ingest.md) — bei SIP-Import läuft die PRONOM-Identifikation automatisch
