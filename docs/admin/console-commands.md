# Console Commands

Antons Kommandos sind [Laravel-Kommandos](https://laravel.com/docs/artisan) und
werden über `artisan` aufgerufen.

Diese Seite beschreibt die im Betrieb wichtigsten Befehle mit Kontext. Eine
**vollständige, automatisch erzeugte Liste** aller Befehle steht am Ende unter
[Vollständige Referenz](#vollstandige-referenz).

## Grundsätzliches

Die meisten Befehle erwarten die Angabe einer Umgebung, also eines
Kunden-Slugs:

```bash
php artisan anton:command --env=besenval
```

Anton-Befehle geben auf `stdout` nur etwas aus, wenn die Ausführlichkeit erhöht
wird: `-v` zeigt `info`-Meldungen, `-vv` zusätzlich `debug`-Meldungen. Ohne
Flag laufen sie still.

!!! warning "Vor schreibenden Befehlen sichern"
    Befehle, die in die Datenbank schreiben — Reparaturen, Merges, Reset —
    sollten nie ungesichert auf einem produktiven Archiv laufen. Erst
    [`anton:backup`](#sicherung-und-wiederherstellung), dann handeln.

## Installation und Aktualisierung

| Befehl | Zweck |
|---|---|
| `anton:install --env=<slug>` | Eine neue Installation aus einer `.env`-Datei aufsetzen |
| `anton:customdir` | Das Kundenverzeichnis samt Unterordnern anlegen (siehe [Installation](installation.md)) |
| `anton:update --env=<slug>` | Auf die letzte stabile Version aktualisieren — führt Migrationen und Seeder aus, ohne Beschriftungen zu überschreiben |
| `anton:setting` / `anton:home` | Eine Einstellung bzw. einen Startseiten-Eintrag lesen oder setzen |

## Sicherung und Wiederherstellung

**`anton:backup`** erstellt einen Datenbank-Dump. Ohne `--target-dir` landet er
im Kundenverzeichnis (`db_backup`). Für rotierende Sicherungen bereiten
`--hourly`, `--weekly`, `--monthly`, `--yearly` die Dateinamen vor (z.B.
`00_backup_besenval-daily-19.sql.gz`); `--file` gibt einen eigenen Namen vor.

```bash
php artisan anton:backup --env=besenval
```

!!! note "Nur die Datenbank"
    `anton:backup` sichert **keine** Mediendateien. Ein vollständiges
    Backup-Konzept behandelt [Sicherung und Wiederherstellung](restore.md);
    was welche Sicherung enthält, zeigt die [Export-Matrix](export-matrix.md).

**`anton:restore`** spielt standardmässig die letzte Sicherung zurück.
**`anton:reset`** setzt eine Installation (Datenbank und Assets) auf einen
definierten Stand zurück — die Grundlage des täglich zurückgesetzten
Testarchivs.

## Medien und Integrität

**`media:check`** prüft die Konsistenz zwischen Anton-Datenbank, lokalem
Dateisystem, Inge und DIMAG. Sechs Prüfebenen, einzeln oder kombiniert:

```bash
php artisan media:check --levels=1,5,6 --env=besenval -vv
```

```
    --levels=               Prüfebenen (1-6), kommasepariert
    --sip=                  Nur Medien eines bestimmten SIP (AntonObject-ID)
    --fix-cloud-status      Repariert cloud_status in der DB (Ebene 5)
    --delete-local-masters  Löscht lokale Master nach Cloud-Verifikation (Ebene 5)
    --delete-from-system    Löscht Dateisystem-Einträge ohne DB-Pendant (Ebene 3)
    --delete-from-inge      Löscht Waisen aus Inge/DIMAG (Ebene 6)
```

Ebene 4 verifiziert die **MD5-Prüfsumme** jeder Datei gegen die Datenbank — die
eigentliche Fixity-Prüfung. Auf DIMAG-Installationen wird sie übersprungen
(die Master liegen dort). Details siehe [Inge und DIMAG](inge.md) und
[Langzeitarchivierung](preservation.md#integritat-prufen).

**`media:snapshot --verify --git`** schreibt einen Prüfsummen-Schnappschuss
aller Medien und committet Änderungen in ein lokales Git-Repository — die
Grundlage einer wiederkehrenden Integritätsprüfung. Anton führt ihn nicht von
selbst aus; er wird pro Installation als Cronjob eingerichtet.

**`media:identify`** bestimmt das Dateiformat (Siegfried/Fido → PRONOM-ID) und
leitet daraus die NARA-Risikobewertung ab. Bei neuen Uploads läuft das
automatisch; der Befehl dient dem Nachtragen bei Altbeständen. Ohne `--force`
nur Medien ohne Erkennungsdaten. Auswertung siehe
[Preservation Planning](preservation-planning.md).

**`media:extract-av-metadata`** füllt die `av_*`-Spalten (Dauer, Codec, Bitrate,
Auflösung …) via `ffprobe` — ebenfalls ein Backfill-Befehl, da neue Uploads das
automatisch tun. `--dry-run` zeigt nur, was sich ändern würde; `--force` auch
über bereits gefüllte Werte.

**`media:add`** hängt ein Medium über die Kommandozeile an einen Datensatz —
nützlich, wenn eine Datei zu gross für den Browser-Upload ist:

```bash
php artisan media:add file.jpg --env=besenval --id=123
```

**`storage:audit`** prüft lokale Masterdateien und SIP-Verzeichnisse;
`--clean-sips` und `--clean-masters` räumen auf.

## Suche (Typesense)

Die [schnelle Suche](typesense.md) hält einen eigenen Index. Bei Störungen oder
nach grösseren Datenänderungen wird er neu aufgebaut:

| Befehl | Zweck |
|---|---|
| `typesense:status` | Zustand der Collections anzeigen |
| `typesense:reindex` | Alle Collections eines Archivs neu aufbauen (Setup + Objekte + Volltext + Galerie) |
| `typesense:reindex-all-tenants` | Dasselbe über alle Installationen |
| `typesense:flush` | Alle Dokumente aus der Collection entfernen |

## Import und Export

| Befehl | Zweck |
|---|---|
| `anton:import` | Excel-Import; die Vorgaben sind bewusst defensiv (siehe [Datenimport](../user/import.md)) |
| `anton:import-native` / `anton:export-native` | Verlustfreier Round-Trip eines Teilbaums (Sicherung, wieder einlesbar) |
| `anton:export` | EAD/EAD3-Export |
| `anton:export-rdf` | RDF-Export in drei Profilen (siehe unten) |
| `resources:sync` | [Normdaten-Abgleich](authorities.md) mit GND, Wikidata, Metagrid |

**`anton:export-rdf`** exportiert einen Bestand — oder den ganzen Mandanten,
wenn `--root=` fehlt — als RDF:

```bash
php artisan anton:export-rdf --env=kr --root=42 --profile=a-plus --format=turtle > fonds.ttl
```

- `--profile=a-plus` (Vorgabe) — CIDOC CRM + RiC-O; `turtle`, `jsonld`, `rdfxml`, `ntriples`
- `--profile=ric` — reines RiC-O 1.1, Vorgabe `jsonld`
- `--profile=memobase` — Memobase-JSON-LD

Details unter [RDF-Export](download-rdf.md). Die Ausgabe geht auf `stdout`.

## Wartung und Reparatur

Diese Befehle stellen die Konsistenz abgeleiteter Felder wieder her. Warum es sie
gibt — materialisierte Felder in einer Closure Table — erklärt
[Nebenläufigkeit](../developer/events-jobs.md).

| Befehl | Zweck |
|---|---|
| `anton:repair-closure-table` | Konsistenz der Hierarchie-Tabelle prüfen und reparieren |
| `anton:reorder-positions` | Positionsfeld der Geschwister neu ordnen; `anton:restore-positions` macht es aus einem Snapshot rückgängig |
| `anton:update-fulltext` | Volltextindex neu aufbauen (nötig z.B. nach Sprachänderungen) |
| `anton:update-dates` / `anton:update-all-dates` | Aggregierte Datierung neu berechnen |
| `anton:update-release-year` | Das effektive Freigabejahr materialisieren |
| `anton:merge <type> <target_id>` | Akteur:innen, Orte oder Schlagwörter zusammenführen |

## Diagnose

**`anton:doctor`** prüft eine Installation auf Konsistenz — dieselben Prüfungen
wie die Oberfläche unter [Anton Doctor](doctor.md), nur skriptfähig:

```bash
php artisan anton:doctor --env=besenval --all -vv
```

```
    --all           alles prüfen
    --binaries      externe Programme
    --closure       Closure-Table (mit --repair reparieren)
    --database      Positionskollisionen
    --disk          Speicherplatz
    --environment   Umgebungsvariablen, Einstellungen
    --jobs          läuft der Supervisor?
    --media         problematische Medien
```

Weitere Diagnosebefehle: **`anton:check-disk-space`** (identisch mit
`anton:doctor --disk`; warnt ab 80 % des in `maximum_storage` hinterlegten
Kontingents), **`anton:db-info`** (aktiver Treiber und Version),
**`sip:reconcile`** (SIP-Status über Anton, Inge und DIMAG),
**`inge:check-infrastructure`** (Verbindung zu Inge/DIMAG). Die
`anton:audit-*`-Befehle melden Dubletten bei Signaturen und Positionen, ohne zu
ändern.

## Nachrichten

**`notification:send`** legt eine [System-Nachricht](notifications.md) in einer
oder allen Installationen an:

```bash
php artisan notification:send --title="Wartung" --body="Details." --env=besenval
php artisan notification:send --title="Update" --all --audience=editors
```

`--title` (Pflicht) und `--body` akzeptieren einen String oder JSON für
mehrere Sprachen; `--audience` schränkt auf `editors` oder `admins` ein.

## Vollständige Referenz

Die folgende Tabelle listet **alle** admin-relevanten Befehle mit der
Beschreibung aus ihrer eigenen `--help`-Ausgabe. Sie wird aus `php artisan list`
erzeugt und mit jeder Änderung an den Befehlen nachgeführt.

!!! note "Automatisch erzeugt"
    Dieser Abschnitt wird generiert; die Beschreibungen stehen in der Sprache
    des Codes (Englisch). Nicht enthalten sind interne Entwickler-Befehle
    (`boost:`, `debugbar:`, `ide-helper:` …) und kundenspezifische Namespaces
    (`gf:`, `gosteli:`, `ballyana:`).

<!-- BEGIN generated command reference -->

### anton: (50)

| Befehl | Beschreibung |
|---|---|
| `anton:add-user` | Add or Update a User. With --api-token option, an api token will be issued. |
| `anton:audit-identifiers` | Report duplicate values in objects.identifier. Empty/NULL identifiers (e.g. on Lod=class) are … |
| `anton:audit-note-name-collisions` | Detect (name, type) collisions that would block the unify-note migration on this tenant. |
| `anton:audit-positions` | Report position collisions: records sharing the same (parent_id, position) value. |
| `anton:backup` | Create a Database dump and save it to local storage. |
| `anton:check-customer-fields` | Check the current database for legacy antonfields with id > 4999 |
| `anton:check-terms` | Check Term. |
| `anton:condense-history` | Reduce the entries in object.history field |
| `anton:count` | Count rows in a db-table. |
| `anton:create-accession-archive` | Create a AntonObject for accessions (eg SIP) |
| `anton:customdir` | Manage customers directory. |
| `anton:db-info` | Print the active database driver, version, and resolved geo-axis order. |
| `anton:doctor` | Check an installation. You have to use the --env=slug option. What is checked: 1) check slug 2… |
| `anton:export` | Export metadata to a XML-File (EAD or EAD3) |
| `anton:export-antonfields` | Export per-formset field labels and form order as antonfields.json for static catalogues (issu… |
| `anton:export-dip` | Export metadata to a XML-File (EAD or EAD3) |
| `anton:export-native` | Export an Anton subtree as a lossless native round-trip package (anton-import-format + media). |
| `anton:export-rdf` | Export Anton tenant data as RDF (CIDOC CRM + RiC-O A+ profile, Memobase, or a self-contained A… |
| `anton:home` | Get or set a home entry. If you set a value, you should also choose a locale |
| `anton:import` | Import an Excel File. The default options are as defensive as possible. |
| `anton:import-actors` | Import an Excel-File to actors-table |
| `anton:import-descriptors` | Import an Excel-File of descriptors |
| `anton:import-directory` | Scan a directory and list all contents in a flat array with parent information |
| `anton:import-native` | Restore an Anton subtree from a native round-trip package (anton-import-format + media). |
| `anton:import-pages` | Import an excel file with metadata for pages |
| `anton:install` | Install Anton for a .env file with --env |
| `anton:mail` | Inform users about a downtime of Anton |
| `anton:measure-disk-usage` | Measure and cache storage disk usage in the background (feeds anton:doctor CheckDiskSpace, #293) |
| `anton:merge` | Merge multiple records into one (actors, places, or keywords) |
| `anton:move-objects` | Move objects into a parent |
| `anton:moveMediaToCloud` | Move media files to an cloud-storage (s3 or inge), but keep the conversions. |
| `anton:protection-baseline` | Snapshot or diff the current per-object protection-period release decision (read-only, #256). |
| `anton:reorder-positions` | Reorder AntonObjects position field (deterministic tie-break + automatic pre-snapshot for roll… |
| `anton:repair-closure-table` | Check and repair the object_closure table consistency |
| `anton:reset` | Reset a Anton Installation (DB and assets) |
| `anton:restore` | Restore Database from the last Backup (by default) |
| `anton:restore-positions` | Restore object positions from an anton:reorder-positions snapshot TSV. |
| `anton:save-searchqueries` | Exports and deletes data based on the given year and saves it to a file. |
| `anton:setting` | Get or set a setting. Admin users can edit "editable" settings, superusers can edit all settin… |
| `anton:setup-import-audit` | Migrate this tenant from accessions_archives_id (legacy) to import_audit_archives_id (new) — s… |
| `anton:shrink-to-public` | Create a public anton from a production anton. |
| `anton:update` | Update Anton to the last stable Version. |
| `anton:update-all-dates` | Fast update all dates in the objects table. |
| `anton:update-dates` | Update the dates in the objects table. |
| `anton:update-fulltext` | Refresh or update the full_text column in the objects table. |
| `anton:update-has_children` | Update has_children attribute in objects table. |
| `anton:update-loans` | Refresh or update the loans (users_objects table) for descendants |
| `anton:update-path` | Fill path attribute of objects.table |
| `anton:update-release-year` | Materialize release_year_calculated (the single effective release year) for all objects (#256). |
| `anton:upwd` | Update password for specified user (by default resets admin password). |

### inge: (1)

| Befehl | Beschreibung |
|---|---|
| `inge:check-infrastructure` | Check connectivity between Anton and Inge (and Dimag via Inge /status). On failure, reports a … |

### media: (12)

| Befehl | Beschreibung |
|---|---|
| `media:add` | Add a media file to an AntonObject |
| `media:check` | Check Media. level 1: Mediacount. Count media in Database and Filesystem. level 2: Media from … |
| `media:conversions` | Create media conversions. The select options are exclusive. If you do not specify a conversion… |
| `media:count-pdf-pages` | Count PDF pages per fonds using pdfinfo. Shows page count statistics grouped by fonds (Bestand). |
| `media:delete-master` | Delete Masterfiles from local media directory (eg. if the masters are in a repository) |
| `media:extract-av-metadata` | Backfill AV technical metadata (av_duration_seconds, av_codec, av_bitrate, av_resolution, av_s… |
| `media:identify` | Process media files for format identification and NARA risk assessment |
| `media:rename` | Rename media to original name or vice versa |
| `media:set-to-private` | Set media to private |
| `media:size` | Get the size of media and save it into the media table. |
| `media:snapshot` | Creates a Snapshot of media files with integrity-check and a git-commit if something has changed |
| `media:validate-pdfs` | Validate PDF media (master + web conversion). Records results in media.custom_properties.event… |

### notification: (1)

| Befehl | Beschreibung |
|---|---|
| `notification:send` | Create a system notification in one or all tenant databases. |

### resources: (2)

| Befehl | Beschreibung |
|---|---|
| `resources:sync` | Anton-specific resources (external links) management |
| `resources:test-resources` | Test resources providers functionality |

### sip: (5)

| Befehl | Beschreibung |
|---|---|
| `sip:check` | Some function for debugging the SIP-Ingest / import array. It checks the package (zip) and sho… |
| `sip:check-import` | Check the Import of a SIP after the import was done. Revert a SipImport if it failed somewhere… |
| `sip:import-agate` | Run an agate-driven SIP import for an existing Importevent (issue #190). |
| `sip:load-xml` | Transform a metadata.xml to LoadXml which can be fed to Dimag |
| `sip:reconcile` | Reconcile SIP state across Anton DB, Inge and Dimag. Shows per-SIP media counts and flags disc… |

### storage: (3)

| Befehl | Beschreibung |
|---|---|
| `storage:audit` | Audit local storage: count master files on disk, list SIP archives vs. unpacked directories. |
| `storage:link` | Create the symbolic links configured for the application |
| `storage:unlink` | Delete existing symbolic links configured for the application |

### typesense: (9)

| Befehl | Beschreibung |
|---|---|
| `typesense:flush` | Delete all documents from the active tenant's Typesense collection (keeps the collection schem… |
| `typesense:gallery-index` | Index gallery media into the active tenant's Typesense gallery collection. |
| `typesense:index` | Index AntonObjects into the active tenant's Typesense collection. |
| `typesense:index-media-texts` | Index MediaText (PDF/OCR) content into the active tenant's Typesense media-texts collection. |
| `typesense:reindex` | Reindex all Typesense collections (setup + objects + media-texts + gallery) for the active ten… |
| `typesense:reindex-all-tenants` | Run setup + index + index-media-texts + gallery-index across every active tenant. |
| `typesense:setup` | Create or update the Typesense collection for the active tenant. |
| `typesense:status` | Show the Typesense collections status for the active tenant. |
| `typesense:update-release` | Recompute time-dependent release flags (is_released, is_publicly_searchable) on every media-te… |
<!-- END generated command reference -->
