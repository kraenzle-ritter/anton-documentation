# Lotte: Betrieb

Diese Seite beschreibt, was es braucht, um Lotte auf einem Server zu betreiben: Installation, Mandanten, Clients und Schlüssel, die Worker, die wiederkehrenden Aufgaben, Sicherung, Überwachung und Wiederherstellung. Was Lotte ist und wie die Daten liegen, steht im [Überblick](index.md); alle Befehle mit ihren Optionen stehen in der [Befehlsreferenz](commands.md).

**Bei Anton as a Service** betreibt k & r Lotte. **On Premises** richtet die betreibende Institution den Dienst nach dieser Seite ein.

## Voraussetzungen {#voraussetzungen}

- PHP 8.3 mit den üblichen Erweiterungen einer Laravel-Anwendung, Composer;
- MySQL 8, dieselbe Instanz wie die Anton-Datenbanken der Mandanten, mit einem eigenen Datenbankbenutzer für Lotte, der die Datenbanken `<slug>_archiv` anlegen darf und auf Antons Datenbanken keine Rechte hat;
- ein Webserver mit eigenem Hostnamen für Lotte, mit TLS;
- ein Speicherort für die Ordner der Mandanten, gross genug für die Master und ihre Fassungen;
- die Werkzeuge der Prüfungen und Ableitungen, wie Anton sie braucht: ClamAV (`clamd`), Siegfried (`sf`), veraPDF, ImageMagick, Ghostscript, poppler-utils, qpdf, MuPDF, libtiff-tools, ExifTool, `file`, FFmpeg, LibreOffice (ohne Oberfläche), Tesseract mit den Sprachen des Bestands, ocrmypdf und img2pdf;
- für die zweite Prüfung der OCFL-Objekte `ocfl-py` (Python), mit dem Befehl `ocfl-validate.py` im Pfad.

Lotte braucht keine Verbindung zu Anton und baut keine Verbindung nach aussen auf; die Werkzeuge laufen als Programme auf dem Server.

## Installation {#installation}

Lotte ist eine Laravel-Anwendung und wird installiert wie eine:

```bash
composer install --no-dev --optimize-autoloader
cp .env.example .env
php artisan key:generate
```

In der `.env` stehen die Verbindung zur Datenbank (Lottes eigener Benutzer; die Datenbank wählt Lotte je Mandant selbst), die Adresse des Dienstes und die Einstellungen von Lotte:

| Variable | Bedeutung | Vorgabe |
|---|---|---|
| `APP_URL` | die Adresse des Dienstes; signierte Adressen zeigen auf sie | |
| `DB_CONNECTION` | bleibt `tenant`: die Datenbank folgt dem Mandanten | `tenant` |
| `DB_HOST`, `DB_PORT`, `DB_USERNAME`, `DB_PASSWORD` | die MySQL-Instanz und Lottes Datenbankbenutzer | |
| `QUEUE_CONNECTION` | bleibt `database`: die Warteschlange liegt in der Datenbank des Mandanten | `database` |
| `LOTTE_BASE_PATH` | wo die Ordner der Mandanten liegen: `<basis>/<slug>/` | `storage/app/tenants` |
| `LOTTE_TENANTS_FILE` | die Mandanten-Datei | `tenants.php` |
| `LOTTE_VIRUS_CHECK` | `required` weist eine Datei ab, die ClamAV nicht prüfen konnte; `optional` übernimmt sie mit einer Warnung (nur für Entwicklung) | `required` |
| `LOTTE_CLAMD_SOCKET` | der Socket von `clamd` | |
| `LOTTE_IDENTIFICATION` | `required` weist eine Datei ab, wenn Siegfried fehlt; ein unbekanntes Format wird nie abgewiesen | `required` |
| `LOTTE_FORMAT_VALIDATION_INVALID` | `warn` übernimmt eine ungültige Datei und vermerkt es, `reject` weist sie ab | `warn` |
| `LOTTE_VERAPDF_BINARY`, `LOTTE_MUTOOL_BINARY` | veraPDF und MuPDF, wo sie nicht im Pfad liegen | |
| `LOTTE_PACKAGE_RETENTION_DAYS` | nach wie vielen Tagen ein vergessenes Paket verworfen wird | `7` |
| `LOTTE_OCR_LANGUAGES` | die Sprachen von Tesseract für OCR | `deu+eng+fra+ita` |
| `LOTTE_SIGNED_URL_MINUTES` | wie lange eine signierte Adresse gilt | `15` |
| `LOTTE_DERIVATIVE_RETRY_AFTER` | nach wie vielen Sekunden ein Client nach einer Ableitung wieder fragen soll | `30` |
| `LOTTE_HEALTH_QUEUE_WARNING_MINUTES` | ab wie vielen Minuten Wartezeit eines Auftrags die Überwachung warnt | `15` |

Der Webserver zeigt auf `public/`. Lotte braucht keine Sitzungen und kein Login; alles ausser `/health` und den signierten Adressen verlangt einen Schlüssel.

## Mandanten {#mandanten}

Die Mandanten eines Servers stehen in der Mandanten-Datei (`tenants.php`, nicht im Repository; Vorlage `tenants.example.php`). Je Mandant: die Datenbank (Vorgabe `<slug>_archiv`), die Regeln der Format Policy, die bei der Übernahme gelten, und ob Bilder und PDF ohne Textebene ihren Text mit OCR bekommen:

```php
return [
    'beispiel' => [
        'database' => 'beispiel_archiv',
        'format_policy' => ['tiff_zip' => true],
        'ocr' => false,
    ],
];
```

Ein neuer Mandant bekommt seinen Ordner und seine Datenbank mit [`lotte:tenant:init`](commands.md#lotte-tenant-init); der Befehl legt `ocfl/`, `derivatives/`, `text/` und `work/` an, erstellt die Datenbank und migriert sie. Nach einer Aktualisierung von Lotte migriert [`lotte:migrate --all`](commands.md#lotte-migrate) die Datenbanken aller Mandanten.

```bash
php artisan lotte:tenant:init beispiel
php artisan lotte:migrate --all
```

## Clients und Schlüssel {#clients}

Ein Client ist ein System, das Lotte über die API nutzt, für Anton ein Client je Mandant. Er bekommt einen Schlüssel, der nur für seinen Mandanten gilt, und Befugnisse:

| Befugnis | erlaubt |
|---|---|
| `read` | Objekte, Dateien, Ableitungen, Text und das Änderungsfeed lesen, Aufträge ansehen |
| `ingest` | Pakete beschreiben, hochladen, prüfen, abschliessen und verwerfen |
| `jobs` | Aufträge anlegen und ansehen |
| `metadata` | einem Objekt eine neue Metadaten-Kopie geben |
| `withdraw` | ein Objekt zurückziehen |

[`lotte:client:create`](commands.md#lotte-client-create) legt den Client an und zeigt den Schlüssel einmal; Lotte speichert ihn nur als Hash. [`lotte:client:revoke`](commands.md#lotte-client-revoke) widerruft alle Schlüssel eines Clients. Ob ein Schlüssel funktioniert, zeigt `GET /t/<slug>/whoami`.

```bash
php artisan lotte:client:create beispiel anton --abilities=read,ingest,jobs,metadata,withdraw
curl -H "Authorization: Bearer <schlüssel>" https://<lotte>/t/beispiel/whoami
php artisan lotte:client:revoke beispiel anton
```

Purge und die Verwaltung von Mandanten und Clients gibt es nur auf der Kommandozeile, für Operatoren mit Zugang zum Server.

## Ein Worker je Mandant {#worker}

Prüfungen, Ableitungen, Text und Aufträge laufen in der Warteschlange, und die liegt in der Datenbank des Mandanten. Jeder Mandant braucht darum einen eigenen Worker, [`lotte:work <slug>`](commands.md#lotte-work), als Dienst, der nach einem Absturz neu startet (etwa mit systemd oder Supervisor). Nach einer Aktualisierung von Lotte werden die Worker neu gestartet, damit sie den neuen Code laden. Ein Auftrag darf lange laufen; eine Umwandlung von Stunden wird nicht zweimal vergeben.

```bash
php artisan lotte:work beispiel
```

## Wiederkehrende Aufgaben {#wiederkehrende-aufgaben}

Lotte bringt keinen eigenen Zeitplan mit; die wiederkehrenden Aufgaben richtet der Betrieb als Cronjobs ein, je Mandant, wo der Befehl einen Mandanten verlangt. Empfohlen:

| Befehl | Rhythmus | Zweck |
|---|---|---|
| [`lotte:prune-packages --all`](commands.md#lotte-prune-packages) | täglich | Pakete verwerfen, die nach der Aufbewahrungsfrist weder abgeschlossen noch verworfen sind |
| [`lotte:derivatives <slug> --backfill`](commands.md#lotte-derivatives) | nachts | fehlende Ableitungen, solche mit weniger als drei Fehlschlägen und liegengebliebene in die Warteschlange stellen |
| [`lotte:derivatives <slug> --reconcile`](commands.md#lotte-derivatives) | gelegentlich | den Stand der Ableitungen mit den Dateien in `derivatives/` und `text/` abgleichen |
| [`lotte:verify <slug> --ocfl --queue`](commands.md#lotte-verify) | nach Grösse des Bestands, etwa monatlich | jede Datei gegen ihre Prüfsumme und jedes Objekt mit `ocfl-py` prüfen |
| [`lotte:health`](commands.md#lotte-health) | alle paar Minuten, aus der Überwachung | Zustand des Dienstes und jedes Mandanten |

Eine vollständige Prüfung liest jede Datei; bei mehreren Terabyte will der Rhythmus geplant sein, wie bei [Antons Integritätsprüfung](../admin/preservation.md#integritat-prufen).

## Sicherung {#sicherung}

Ein Mandant ist gesichert, wenn zwei Dinge gesichert sind:

- seine Datenbank `<slug>_archiv`, als Dump im selben nächtlichen Lauf wie die Anton-Datenbank des Mandanten;
- sein Ordner `<basis>/<slug>/`, als Snapshot wie die Mediendateien, auf ein anderes System und an einen anderen Standort.

Unersetzlich ist `ocfl/`: Dort liegen die Master, ihre früheren Fassungen, die Metadaten-Kopien und die Erhaltungsereignisse. OCFL beschreibt sich selbst; ein gesicherter Ordner lässt sich ohne Lottes Datenbank prüfen und lesen. `derivatives/` und `text/` lassen sich neu erzeugen, `work/` enthält nur, was noch nicht abgeschlossen ist. Die Datenbank enthält neben dem Index, was im Ordner nicht steht: Clients und Schlüssel, offene Pakete, Aufträge und das Änderungsfeed.

## Überwachung {#ueberwachung}

Zwei Wege zeigen denselben Zustand, beide ohne Anton zu fragen:

- **`GET /health`** antwortet ohne Schlüssel mit JSON: Gesamtzustand (`ok`, `warning`, `critical`), der Speicherort und je Mandant Datenbank, Ordner und Warteschlange. Der HTTP-Status ist 200, solange nichts kritisch ist, sonst 503.
- **[`lotte:health`](commands.md#lotte-health)** gibt eine Zeile für Nagios aus (`LOTTE OK - …`) und endet mit 0 (OK), 1 (WARNING) oder 2 (CRITICAL).

Kritisch ist: der Speicherort oder ein Bereich eines Mandanten ist nicht beschreibbar, eine Datenbank nicht erreichbar. Eine Warnung gibt es, wenn ein Auftrag länger als die eingestellte Zeit wartet (dann nimmt kein Worker Aufträge an) und wenn Ableitungen nach drei Fehlschlägen aufgegeben sind.

## Wiederherstellung {#wiederherstellung}

Ein Mandant wird aus seinem Ordner und seinem Datenbank-Dump wiederhergestellt. Weil Dump und Snapshot selten im selben Augenblick entstehen, kann der Ordner neuer sein als der Index in der Datenbank, oder die Datenbank fehlt ganz. Dann baut [`lotte:rebuild-index <slug>`](commands.md#lotte-rebuild-index) den Index aus dem Ordner wieder auf: Referenz und Zustand aus `metadata/object.json`, PRONOM-ID und MIME-Typ aus der Formaterkennung in `metadata/events.json`, und den Stand der Ableitungen aus den Dateien in `derivatives/` und `text/`. Mit `--prune` entfernt er Zeilen, deren Objekt nicht mehr im Ordner liegt. Ableitungen, die fehlen, erzeugt danach `lotte:derive` oder der nächtliche `lotte:derivatives --backfill`.

```bash
php artisan lotte:rebuild-index beispiel
php artisan lotte:derive beispiel
```

`lotte:rebuild-index` schreibt keine Einträge ins Änderungsfeed. Wo er den Index geändert hat, sagt er es; die Clients gleichen diese Objekte dann neu ab. Clients, Schlüssel, offene Pakete, Aufträge und das Änderungsfeed stehen nur in der Datenbank. Fehlt sie ganz, legt `lotte:tenant:init` sie leer an, bevor `lotte:rebuild-index` läuft. Die Clients bekommen dann neue Schlüssel, setzen ihren Stand im Änderungsfeed auf 0 zurück und gleichen alle Objekte neu ab, denn das neue Feed beginnt leer.
