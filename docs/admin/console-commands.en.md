# Console commands

Anton's commands are [Laravel commands](https://laravel.com/docs/artisan) and are
called via `artisan`.

This page describes the commands most important in operation, with context. A
**complete, automatically generated list** of all commands is at the end under
[Complete reference](#vollstandige-referenz).

## Basics

Most commands expect an environment to be specified, that is, a customer slug:

```bash
php artisan anton:command --env=besenval
```

Anton commands only output something on `stdout` when the verbosity is
increased: `-v` shows `info` messages, `-vv` additionally `debug` messages.
Without a flag they run silently.

!!! warning "Back up before writing commands"
    Commands that write to the database — repairs, merges, reset — should never
    run unsecured on a production archive. First
    [`anton:backup`](#sicherung-und-wiederherstellung), then act.

## Installation and updating

| Command | Purpose |
|---|---|
| `anton:install --env=<slug>` | Set up a new installation from a `.env` file |
| `anton:customdir` | Create the customer directory including subfolders (see [installation](installation.md)) |
| `anton:update --env=<slug>` | Update to the latest stable version — runs migrations and seeders without overwriting labels |
| `anton:setting` / `anton:home` | Read or set a setting or a home page entry |

## Backup and restoration {#sicherung-und-wiederherstellung}

**`anton:backup`** creates a database dump. Without `--target-dir` it ends up in
the customer directory (`db_backup`). For rotating backups, `--hourly`,
`--weekly`, `--monthly`, `--yearly` prepare the file names (e.g.
`00_backup_besenval-daily-19.sql.gz`); `--file` specifies a name of your own.

```bash
php artisan anton:backup --env=besenval
```

!!! note "The database only"
    `anton:backup` does **not** back up media files. A complete backup concept is
    covered by [backup and restoration](restore.md); what each backup contains is
    shown by the [export matrix](export-matrix.md).

**`anton:restore`** restores the most recent backup by default.
**`anton:reset`** resets an installation (database and assets) to a defined
state — the basis of the test archive that is reset daily.

## Media and integrity

**`media:check`**{#mediacheck} checks the consistency between the Anton
database, the local file system, Inge and DIMAG. Six check levels, individually
or combined:

```bash
php artisan media:check --levels=1,5,6 --env=besenval -vv
```

```
    --levels=               Check levels (1-6), comma-separated
    --sip=                  Only media of a particular SIP (AntonObject ID)
    --fix-cloud-status      Repairs cloud_status in the DB (level 5)
    --delete-local-masters  Deletes local masters after cloud verification (level 5)
    --delete-from-system    Deletes file system entries without a DB counterpart (level 3)
    --delete-from-inge      Deletes orphans from Inge/DIMAG (level 6)
```

Level 4 verifies the **MD5 checksum** of every file against the database — the
actual fixity check. On DIMAG installations it is skipped (the masters are held
there). For details see [Inge and DIMAG](inge.md) and
[long-term preservation](preservation.md#integritat-prufen).

**`media:snapshot --verify --git`**{#mediasnapshot} writes a checksum snapshot
of all media and commits changes to a local Git repository — the basis of a
recurring integrity check. Anton does not run it by itself; it is set up per
installation as a cron job.

**`media:identify`**{#mediaidentify} determines the file format
(Siegfried/Fido → PRONOM ID) and derives the NARA risk assessment from it. With
new uploads this runs automatically; the command serves to supply the data
retrospectively for existing holdings. Without `--force`, only media without
identification data. For the evaluation see
[preservation planning](preservation-planning.md).

**`media:extract-av-metadata`**{#mediaextract-av-metadata} fills the `av_*`
columns (duration, codec, bitrate, resolution …) via `ffprobe` — likewise a
backfill command, since new uploads do this automatically. `--dry-run` only
shows what would change; `--force` also overwrites values that are already
filled.

**`media:add`** attaches a medium to a record from the command line — useful
when a file is too large for the browser upload:

```bash
php artisan media:add file.jpg --env=besenval --id=123
```

**`storage:audit`** checks local master files and SIP directories;
`--clean-sips` and `--clean-masters` tidy up.

## Search (Typesense)

The [instant search](typesense.md) maintains its own index. In case of problems
or after larger data changes, it is rebuilt:

| Command | Purpose |
|---|---|
| `typesense:status` | Show the state of the collections |
| `typesense:reindex` | Rebuild all collections of an archive (setup + objects + full text + gallery) |
| `typesense:reindex-all-tenants` | The same across all installations |
| `typesense:flush` | Remove all documents from the collection |

## Import and export

| Command | Purpose |
|---|---|
| `anton:import` | Excel import; the defaults are deliberately defensive (see [data import](../user/import.md)) |
| `anton:import-native` / `anton:export-native` | Lossless round trip of a subtree (backup, re-importable) |
| `anton:export` | EAD/EAD3 export |
| `anton:export-rdf` | RDF export in three profiles (see below) |
| `resources:sync` | [Authority data synchronisation](authorities.md) with GND, Wikidata, Metagrid |

**`anton:export-rdf`** exports a fonds — or the whole tenant if `--root=` is
missing — as RDF:

```bash
php artisan anton:export-rdf --env=kr --root=42 --profile=a-plus --format=turtle > fonds.ttl
```

- `--profile=a-plus` (default) — CIDOC CRM + RiC-O; `turtle`, `jsonld`,
  `rdfxml`, `ntriples`
- `--profile=ric` — pure RiC-O 1.1, default `jsonld`
- `--profile=memobase` — Memobase JSON-LD

Details under [RDF export](download-rdf.md). The output goes to `stdout`.

## Maintenance and repair

These commands restore the consistency of derived fields. Why they exist —
materialised fields in a closure table — is explained by
[concurrency](../developer/events-jobs.md).

| Command | Purpose |
|---|---|
| `anton:repair-closure-table` | Check and repair the consistency of the hierarchy table |
| `anton:reorder-positions` | Reorder the position field of siblings; `anton:restore-positions` undoes it from a snapshot |
| `anton:update-fulltext` | Rebuild the full-text index (necessary after language changes, for example) |
| `anton:update-dates` / `anton:update-all-dates` | Recalculate the aggregated dating |
| `anton:update-release-year` | Materialise the effective release year |
| `anton:merge <type> <target_id>` | Merge actors, places or keywords |
| `anton:repair-content-locale --from=<language>` | Move titles and text fields an import filed under the wrong language into the archive's content language |
| `anton:audit-orphans` | Report rows whose record no longer exists, and remove them on request |

`anton:repair-content-locale` concerns archives that imported **before 15 August
2026**: until then an import wrote the application's default language rather than
the archive's. A title filed under a language the archive does not keep shows on
the detail page but leaves an empty cell in every list.

Without `--write` the command only reports what it would move. `--from` is
required, `--to` defaults to the archive's first configured language. Records
that already carry the target language are listed rather than overwritten. A
`--from` that is one of the archive's own configured languages is refused unless
`--force` — content in a configured language is not misfiled.

`anton:audit-orphans` looks for rows pointing at a record that is no longer
there. Anton keeps text fields, external identifiers, comments, term values,
upload tokens and relations in polymorphic tables; when the owner goes, nothing
takes them with it. None of it is visible — nothing renders a row whose owner is
missing — which is exactly why it has to be looked for.

Without `--write` it only reports. `--only=` narrows it to one place, and every
finding comes with the first few ids so you can look before deciding. **Media is
reported and never removed**: a media row is the registration of a file on disk,
and dropping the row loses the trail to the file rather than the file.

## Diagnosis

**`anton:doctor`**{#antondoctor} checks an installation for consistency — the
same checks as the interface under [Anton Doctor](doctor.md), only scriptable:

```bash
php artisan anton:doctor --env=besenval --all -vv
```

```
    --all           check everything
    --binaries      external programs
    --closure       closure table (repair with --repair)
    --database      position collisions
    --disk          storage space
    --environment   environment variables, settings
    --jobs          is the supervisor running?
    --media         problematic media
```

Further diagnostic commands: **`anton:check-disk-space`** (identical to
`anton:doctor --disk`; warns from 80 % of the quota stored in
`maximum_storage`), **`anton:db-info`** (active driver and version),
**`sip:reconcile`** (SIP status across Anton, Inge and DIMAG),
**`inge:check-infrastructure`** (connection to Inge/DIMAG). The `anton:audit-*`
commands report duplicates in reference codes and positions without changing
anything.

## Notifications

**`notification:send`** creates a [system notification](notifications.md) in one
or all installations:

```bash
php artisan notification:send --title="Wartung" --body="Details." --env=besenval
php artisan notification:send --title="Update" --all --audience=editors
```

`--title` (mandatory) and `--body` accept a string or JSON for several
languages; `--audience` restricts to `editors` or `admins`.

## Complete reference {#vollstandige-referenz}

The following table lists **all** admin-relevant commands with the description
from their own `--help` output. It is generated from `php artisan list` and kept
up to date with every change to the commands.

!!! note "Automatically generated"
    This section is generated; the descriptions are in the language of the code
    (English). Not included are internal developer commands (`boost:`,
    `debugbar:`, `ide-helper:` …) and customer-specific namespaces (`gf:`,
    `gosteli:`, `ballyana:`).


<!-- BEGIN generated command reference -->

### anton: (58)

| Command | Description |
|---|---|
| `anton:add-user` | Add or Update a User. With --api-token option, an api token will be issued. |
| `anton:audit-identifiers` | Report duplicate values in objects.identifier. Empty/NULL identifiers (e.g. on Lod=class) are … |
| `anton:audit-note-name-collisions` | Detect (name, type) collisions that would block the unify-note migration on this tenant. |
| `anton:audit-orphans` | Report (and optionally remove) rows pointing at a record that no longer exists (#512). |
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
| `anton:export-antonfields` | Export per-formset field labels, form order and controlled-vocabulary labels as antonfields.js… |
| `anton:export-dip` | Export metadata to a XML-File (EAD or EAD3) |
| `anton:export-native` | Export an Anton subtree as a lossless native round-trip package (anton-import-format + media). |
| `anton:export-rdf` | Export Anton tenant data as RDF (CIDOC CRM + RiC-O A+ profile, Memobase, or a self-contained A… |
| `anton:home` | Get or set a home entry. If you set a value, you should also choose a locale |
| `anton:i18n-check` | Find user-visible strings that are missing a translation (JSON + PHP keys) |
| `anton:import` | Import an Excel File. The default options are as defensive as possible. |
| `anton:import-actors` | Import an Excel-File to actors-table |
| `anton:import-descriptors` | Import an Excel-File of descriptors |
| `anton:import-directory` | Scan a directory and list all contents in a flat array with parent information |
| `anton:import-native` | Restore an Anton subtree from a native round-trip package (anton-import-format + media). |
| `anton:import-pages` | Import an excel file with metadata for pages |
| `anton:install` | Install Anton for a .env file with --env |
| `anton:mail` | Send a circular (or a downtime notice) to this tenant's editors and admins |
| `anton:measure-disk-usage` | Measure and cache storage disk usage in the background (feeds anton:doctor CheckDiskSpace, #293) |
| `anton:merge` | Merge multiple records into one (actors, places, or keywords) |
| `anton:migrate-import-audit` | Move import sidecars from the archive into the import audit log. |
| `anton:move-objects` | Move objects into a parent |
| `anton:moveMediaToCloud` | Move media files to an cloud-storage (s3 or inge), but keep the conversions. |
| `anton:protection-baseline` | Snapshot or diff the current per-object protection-period release decision (read-only, #256). |
| `anton:prune-cache` | Delete expired rows from the database cache table (#389) |
| `anton:reencrypt-secrets` | Re-encrypt two-factor secrets and passkeys onto the current APP_KEY (#479). |
| `anton:reorder-positions` | Reorder AntonObjects position field (deterministic tie-break + automatic pre-snapshot for roll… |
| `anton:repair-closure-table` | Check and repair the object_closure table consistency |
| `anton:repair-content-locale` | Move objects.title and notes from a wrongly written language into the archive's own (#506). |
| `anton:repair-edit-metadata` | Restore updated_at/updated_by from the history column on records a mass run restamped (#421). |
| `anton:reset` | Reset a Anton Installation (DB and assets) |
| `anton:restore` | Restore Database from the last Backup (by default) |
| `anton:restore-positions` | Restore object positions from an anton:reorder-positions snapshot TSV. |
| `anton:save-searchqueries` | Exports and deletes data based on the given year and saves it to a file. |
| `anton:setting` | Get or set a setting. Admin users can edit "editable" settings, superusers can edit all settin… |
| `anton:setup-import-audit` | Migrate this tenant from accessions_archives_id (legacy) to import_audit_archives_id (new) — s… |
| `anton:shrink-to-public` | Create a public anton from a production anton. |
| `anton:sitemap` | Generate sitemap.xml for this tenant (#383) |
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

| Command | Description |
|---|---|
| `inge:check-infrastructure` | Check connectivity between Anton and Inge (and Dimag via Inge /status). On failure, reports a … |

### media: (12)

| Command | Description |
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

| Command | Description |
|---|---|
| `notification:send` | Create a system notification in one or all tenant databases. |

### resources: (2)

| Command | Description |
|---|---|
| `resources:sync` | Anton-specific resources (external links) management |
| `resources:test-resources` | Check that every configured resource provider still answers |

### sip: (5)

| Command | Description |
|---|---|
| `sip:check` | Some function for debugging the SIP-Ingest / import array. It checks the package (zip) and sho… |
| `sip:check-import` | Check the import of a SIP after it was done. Revert it if something failed downstream (INGE, D… |
| `sip:import-agate` | Run an agate-driven SIP import for an existing Importevent (issue #190). |
| `sip:load-xml` | Transform a metadata.xml to LoadXml which can be fed to Dimag |
| `sip:reconcile` | Reconcile SIP state across Anton DB, Inge and Dimag. Shows per-run media counts and flags disc… |

### storage: (3)

| Command | Description |
|---|---|
| `storage:audit` | Audit local storage: count master files on disk, list SIP archives vs. unpacked directories. |
| `storage:link` | Create the symbolic links configured for the application |
| `storage:unlink` | Delete existing symbolic links configured for the application |

### typesense: (9)

| Command | Description |
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
