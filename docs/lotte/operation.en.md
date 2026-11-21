# Lotte: operation

This page describes what it takes to run Lotte on a server: installation, tenants, clients and keys, the workers, the recurring tasks, backup, monitoring and recovery. What Lotte is and how the data is laid out is in the [overview](index.md); every command with its options is in the [command reference](commands.md).

**With Anton as a Service**, k & r runs Lotte. **On premises**, the operating institution sets up the service following this page.

## Requirements {#voraussetzungen}

- PHP 8.3 with the usual extensions of a Laravel application, Composer;
- MySQL 8, the same instance as the tenants' Anton databases, with a database user of Lotte's own that may create the databases `<slug>_archiv` and has no rights on Anton's databases;
- a web server with a host name of its own for Lotte, with TLS;
- a storage location for the tenants' folders, large enough for the masters and their versions;
- the tools of the checks and derivatives, as Anton needs them: ClamAV (`clamd`), Siegfried (`sf`), veraPDF, ImageMagick, Ghostscript, poppler-utils, qpdf, MuPDF, libtiff-tools, ExifTool, `file`, FFmpeg, LibreOffice (headless), Tesseract with the languages of the holdings, ocrmypdf and img2pdf;
- for the second check of the OCFL objects, `ocfl-py` (Python), with the command `ocfl-validate.py` on the path.

Lotte needs no connection to Anton and opens no connection to the outside; the tools run as programs on the server.

## Installation {#installation}

Lotte is a Laravel application and is installed like one:

```bash
composer install --no-dev --optimize-autoloader
cp .env.example .env
php artisan key:generate
```

The `.env` holds the database connection (Lotte's own user; Lotte chooses the database per tenant itself), the address of the service and Lotte's settings:

| Variable | Meaning | Default |
|---|---|---|
| `APP_URL` | the address of the service; signed URLs point to it | |
| `DB_CONNECTION` | stays `tenant`: the database follows the tenant | `tenant` |
| `DB_HOST`, `DB_PORT`, `DB_USERNAME`, `DB_PASSWORD` | the MySQL instance and Lotte's database user | |
| `QUEUE_CONNECTION` | stays `database`: the queue lives in the tenant's database | `database` |
| `LOTTE_BASE_PATH` | where the tenants' folders lie: `<base>/<slug>/` | `storage/app/tenants` |
| `LOTTE_TENANTS_FILE` | the tenants file | `tenants.php` |
| `LOTTE_VIRUS_CHECK` | `required` refuses a file ClamAV could not check; `optional` accepts it with a warning (development only) | `required` |
| `LOTTE_CLAMD_SOCKET` | the socket of `clamd` | |
| `LOTTE_IDENTIFICATION` | `required` refuses a file when Siegfried is missing; an unknown format is never refused | `required` |
| `LOTTE_FORMAT_VALIDATION_INVALID` | `warn` accepts an invalid file and records it, `reject` refuses it | `warn` |
| `LOTTE_VERAPDF_BINARY`, `LOTTE_MUTOOL_BINARY` | veraPDF and MuPDF, where they are not on the path | |
| `LOTTE_PACKAGE_RETENTION_DAYS` | after how many days a forgotten package is discarded | `7` |
| `LOTTE_OCR_LANGUAGES` | Tesseract's languages for OCR | `deu+eng+fra+ita` |
| `LOTTE_SIGNED_URL_MINUTES` | how long a signed URL is valid | `15` |
| `LOTTE_DERIVATIVE_RETRY_AFTER` | after how many seconds a client should ask for a derivative again | `30` |
| `LOTTE_HEALTH_QUEUE_WARNING_MINUTES` | after how many minutes of a job waiting monitoring warns | `15` |

The web server points to `public/`. Lotte needs no sessions and no login; everything except `/health` and the signed URLs requires a key.

## Tenants {#mandanten}

A server's tenants are listed in the tenants file (`tenants.php`, not in the repository; template `tenants.example.php`). Per tenant: the database (default `<slug>_archiv`), the format policy rules that apply at ingest, and whether images and PDFs without a text layer get their text by OCR:

```php
return [
    'beispiel' => [
        'database' => 'beispiel_archiv',
        'format_policy' => ['tiff_zip' => true],
        'ocr' => false,
    ],
];
```

A new tenant gets its folder and its database with [`lotte:tenant:init`](commands.md#lotte-tenant-init); the command creates `ocfl/`, `derivatives/`, `text/` and `work/`, creates the database and migrates it. After an update of Lotte, [`lotte:migrate --all`](commands.md#lotte-migrate) migrates the databases of all tenants.

```bash
php artisan lotte:tenant:init beispiel
php artisan lotte:migrate --all
```

## Clients and keys {#clients}

A client is a system that uses Lotte through the API; for Anton, one client per tenant. It gets a key valid for its own tenant only, and abilities:

| Ability | allows |
|---|---|
| `read` | reading objects, files, derivatives, text and the change feed, viewing jobs |
| `ingest` | describing, uploading, checking, committing and discarding packages |
| `jobs` | creating and viewing jobs |
| `metadata` | giving an object a new metadata copy |
| `withdraw` | withdrawing an object |

[`lotte:client:create`](commands.md#lotte-client-create) creates the client and shows the key once; Lotte stores only its hash. [`lotte:client:revoke`](commands.md#lotte-client-revoke) revokes all keys of a client. `GET /t/<slug>/whoami` shows whether a key works.

```bash
php artisan lotte:client:create beispiel anton --abilities=read,ingest,jobs,metadata,withdraw
curl -H "Authorization: Bearer <key>" https://<lotte>/t/beispiel/whoami
php artisan lotte:client:revoke beispiel anton
```

Purging and the administration of tenants and clients exist on the command line only, for operators with access to the server.

## One worker per tenant {#worker}

Checks, derivatives, text and jobs run on the queue, and the queue lives in the tenant's database. Each tenant therefore needs a worker of its own, [`lotte:work <slug>`](commands.md#lotte-work), as a service that restarts after a crash (with systemd or Supervisor, for instance). After an update of Lotte the workers are restarted so that they load the new code. A job may run for a long time; a conversion taking hours is not handed out twice.

```bash
php artisan lotte:work beispiel
```

## Recurring tasks {#wiederkehrende-aufgaben}

Lotte brings no schedule of its own; operations set up the recurring tasks as cron jobs, per tenant where the command requires a tenant. Recommended:

| Command | Interval | Purpose |
|---|---|---|
| [`lotte:prune-packages --all`](commands.md#lotte-prune-packages) | daily | discard packages that are neither committed nor discarded after the retention time |
| [`lotte:derivatives <slug> --backfill`](commands.md#lotte-derivatives) | nightly | queue missing derivatives, those with fewer than three failures, and stale ones |
| [`lotte:derivatives <slug> --reconcile`](commands.md#lotte-derivatives) | occasionally | align the state of the derivatives with the files in `derivatives/` and `text/` |
| [`lotte:verify <slug> --ocfl --queue`](commands.md#lotte-verify) | by the size of the holdings, e.g. monthly | check every file against its digest and every object with `ocfl-py` |
| [`lotte:health`](commands.md#lotte-health) | every few minutes, from monitoring | state of the service and of each tenant |

A full check reads every file; with several terabytes, the interval wants planning, as with [Anton's integrity check](../admin/preservation.md#integritat-prufen).

## Backup {#sicherung}

A tenant is backed up when two things are backed up:

- its database `<slug>_archiv`, as a dump in the same nightly run as the tenant's Anton database;
- its folder `<base>/<slug>/`, as a snapshot like the media files, to another system and another location.

`ocfl/` is irreplaceable: it holds the masters, their earlier versions, the metadata copies and the preservation events. OCFL is self-describing; a backed-up folder can be checked and read without Lotte's database. `derivatives/` and `text/` can be made again, `work/` holds only what has not been committed yet. Besides the index, the database holds what is not in the folder: clients and keys, open packages, jobs and the change feed.

## Monitoring {#ueberwachung}

Two ways show the same state, neither asks Anton:

- **`GET /health`** answers without a key with JSON: the overall state (`ok`, `warning`, `critical`), the storage location, and per tenant database, folder and queue. The HTTP status is 200 while nothing is critical, otherwise 503.
- **[`lotte:health`](commands.md#lotte-health)** prints one line for Nagios (`LOTTE OK - …`) and exits with 0 (OK), 1 (WARNING) or 2 (CRITICAL).

Critical: the storage location or an area of a tenant is not writable, a database is not reachable. A warning is given when a job has waited longer than the set time (then no worker is taking jobs) and when derivatives have been given up after three failures.

## Recovery {#wiederherstellung}

A tenant is restored from its folder and its database dump. As dump and snapshot are rarely taken at the same moment, the folder may be newer than the index in the database, or the database may be missing altogether. Then [`lotte:rebuild-index <slug>`](commands.md#lotte-rebuild-index) rebuilds the index from the folder: reference and state from `metadata/object.json`, PRONOM ID and MIME type from the format identification in `metadata/events.json`, and the state of the derivatives from the files in `derivatives/` and `text/`. With `--prune` it removes rows whose object is no longer in the folder. Missing derivatives are then made by `lotte:derive` or by the nightly `lotte:derivatives --backfill`.

```bash
php artisan lotte:rebuild-index beispiel
php artisan lotte:derive beispiel
```

`lotte:rebuild-index` writes no entries into the change feed. Where it changed the index it says so; the clients then resync those objects. Clients, keys, open packages, jobs and the change feed exist only in the database. If it is missing altogether, `lotte:tenant:init` creates it empty before `lotte:rebuild-index` runs. The clients then get new keys, reset their position in the change feed to 0 and resync all objects, because the new feed starts empty.
