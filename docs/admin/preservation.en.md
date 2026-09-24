# Long-term preservation: overview

Anton ingests digital records with verification, keeps the masters unchanged,
identifies their formats and records how well they can be preserved. Storage
itself and its redundancy are provided by the operating infrastructure; in
installations with a connected long-term archive, that archive takes over
bitstream preservation. This page shows how the tasks are divided and refers to
the detail pages. It also answers the question of which artefact is a
**backup** and which is a **publication view**.

## Division of tasks {#aufgabenteilung}

Digital preservation consists of several layers. Anton covers the archival
ones, operations cover storage:

| Task | Anton | Operations | Connected long-term archive |
|---|---|---|---|
| Checksums on transfer | verifies every file of a SIP against the package | | |
| Checksum per file | calculates MD5 and SHA-512 on upload and stores them | | |
| Format identification and risk | PRONOM ID, NARA assessment, [preservation planning](preservation-planning.md) | provides Siegfried or Fido | |
| Master and access copies | keeps the master unchanged, produces `web` and `thumb` | | |
| Integrity check | provides `media:check`, `media:snapshot` and `media:repair`, logs the checks | sets the schedule as a cron job, sets up the backup for `media:repair` | takes over fixity of the masters |
| Redundant storage | | copies at several locations | bitstream preservation |
| Format decisions | shows formats that need action | | |

**With Anton as a Service**, k & r provides operations. **On premises**, it is
the operating institution.

## The chain {#die-kette}

### Transfer {#ubernahme}

During [SIP ingest](sip-ingest.md) according to eCH-0160, Anton verifies the
checksum declared in the `metadata.xml` for **every file in the package**: the
hash is recalculated over the actual file and compared. If it deviates,
validation fails. The algorithm comes from the package itself, so it is not
fixed to MD5. In addition, Anton remembers the checksum of the SIP ZIP and
rejects packages that have already been loaded.

### Storage {#speicherung}

For every media file, Anton calculates an **MD5** and a **SHA-512 checksum** in
a single read on upload and stores both in the database. SHA-512 is the
reference for the integrity check, as OCFL and BagIt recommend; MD5 stays for
the DIMAG connection and for recognising duplicate imports. For media from
before version 0.98, [`media:checksum`](console-commands.md#mediachecksum)
computes SHA-512 afterwards — checking every file against its MD5 as it goes.
The **master remains unchanged**; the derivatives (`web`, `thumb`) are access
copies.

### Format identification and risk {#formaterkennung-und-risiko}

On upload, Anton identifies the format via **Siegfried** or **Fido** and records
the **PRONOM ID**; from this it derives the risk assessment according to the
**NARA Digital Preservation Framework**. For existing holdings this can be
supplied retrospectively with
[`media:identify`](console-commands.md#mediaidentify). It is evaluated in
[preservation planning](preservation-planning.md).

!!! note "Siegfried or Fido on the server"
    Identification uses Siegfried or Fido installed on the server. If the
    program is missing, uploads still succeed, only identification stays empty;
    [`anton:doctor`](doctor.md) therefore reports a missing `sf` as an error.
    The «unidentified media» tab shows how complete the identification of the
    holdings is.

### Format decisions {#formatentscheide}

Anton does not migrate masters into archival formats. Whether a file is
converted into another format is decided by the archive. Preservation planning
provides the basis for this: it shows which formats are in the holdings, which
risk NARA assigns to them and which action NARA recommends.

### Delivery {#abgabe}

See [Backup or publication?](#sicherung-oder-publikation) further down.

## Checking integrity {#integritat-prufen}

Two commands check the holdings against the stored checksums:

| Command | What it does |
|---|---|
| [`media:check --levels=4`](console-commands.md#mediacheck) | Reads every file afresh, calculates the checksum anew (SHA-512 where available, MD5 otherwise) and compares it with the database. With `--log-integrity-check`, every check is logged as an event — producing a demonstrable history. A missing file is a finding; the check carries on. |
| [`media:snapshot --oldest=N --git`](console-commands.md#mediasnapshot) | Writes the reference checksums of all media into lists (SHA-512 and MD5) and commits them to a local Git repository — traceable when a reference changed. In the same pass it checks the N files checked longest ago (or all with `--verify`) and logs every check. |

!!! note "Operations set the schedule"
    How often the check runs is determined by a cron job per installation. This
    allows the schedule to match the size of the holdings: a full run reads
    every file, and with several terabytes that needs planning.

    **With Anton as a Service**, k & r sets up the check (as of September 2026
    for the large archives). **On premises**, the operating institution sets up
    the job itself; the commands are available for it.

To be distinguished from this is [`anton:doctor`](console-commands.md): it
checks the **consistency of the database** — hierarchy, reference codes, derived
fields — and whether the files are present. Checksums are compared by the two
commands above.

### If the check reports a deviation {#wenn-die-prufung-anschlagt}

If a file deviates from its checksum, [`media:repair`](console-commands.md#mediarepair)
brings it back from the **local backup**: it goes through the versions from the
newest to the oldest (daily, monthly, yearly) and takes the first whose checksum
matches the stored reference. The damaged version is not deleted but copied to a
quarantine; every step is recorded as an event in the file's history.

Anton only replaces a file with one whose content provably equals the original.
And the application itself does not reach the backup: only root reads it,
`media:repair` runs as root and refuses to repair if the backup is open to
others. With many deviations at once it
repairs nothing and raises an alarm, because the cause then lies elsewhere
(disk, mount, malware).

If no local version matches — for instance because the file is newer than the
backup — with **Anton as a Service** we restore it manually from one of the
external backup servers; the report of `media:repair` names everything needed.
Tenants with DIMAG are excluded: there the master lies in the long-term archive.

!!! note "Set up by operations"
    `media:repair` needs a local backup that contains the media files, is
    reachable for root only and is configured (see
    [Installation](installation.md#selbstreparatur-aus-der-lokalen-sicherung)).
    Where that is not set up, the command says so and does nothing.

## Redundant storage {#redundante-speicherung}

Redundant storage is a matter for the infrastructure: Anton writes to a local
store and optionally to a cloud store, and operations create the copies
underneath. With **Anton as a Service**, the data is held in
[three copies at three locations](../faq/longterm_archives.md) (sixfold
redundancy in total); **on premises**, the operating institution is
responsible for this.

## Backup or publication? {#sicherung-oder-publikation}

The most important distinction, and the one most easily confused:

| Artefact | Purpose |
|---|---|
| **Native export** (`anton:export-native`) | **Backup.** Lossless and re-importable: metadata in all languages, events, text fields — including private ones —, authority references via UUID and the **master media**. |
| **SQL dump** | **Backup.** The only artefact with users, settings, forms and file provenance (PRONOM/NARA history). Contains no media files. |
| [**DIP**](download-dip.md) (BagIt) and [**OCFL**](download-ocfl.md) | **Delivery packages.** Media and metadata bundled, with checksums in the manifest. |
| [**RDF/CIDOC**](download-rdf.md), **EAD**, **TEI**, **Memobase** | **Publication views.** Filtered and lossy — Anton cannot be restored from them. |
| [**A+ bundle with `--include-protected --include-originals`**](download-rdf.md#migrations-export) | **Migration package.** Graph including blocked data plus original files — for the route into a *different* system. Not a restore tool for Anton, and not to be hosted publicly because of the personal data it contains. |

!!! danger "An RDF or EAD export is not a backup"
    These formats are built for research and exchange. Among other things they
    lack the UUIDs and the raw values; in the standard case, private content is
    filtered out. A backup requires the native export **and** the SQL dump.

    This also applies when exporting with `--include-protected
    --include-originals`: that package is intended as a **migration route
    outwards**. A way back could be constructed with effort, but there is no
    tool for it.

Anton keeps the provenance of a file (format identification, NARA assessment,
integrity checks) in the database; it therefore travels with the SQL dump. DIP
and OCFL secure the files through the checksums in the manifest and do not
output this provenance as PREMIS or METS.

Which data each format takes with it in detail, which is only in the SQL dump
and who can trigger which artefact is shown by the
[export matrix](export-matrix.md). In short: the SQL dump and the standard
exports go via the interface, the native round trip and the migration package
only via the CLI.

For the [static publication](statische-publikation.md) of a fonds as a
standalone website there is a dedicated bundle.

## With a connected long-term archive {#mit-angebundenem-langzeitarchiv}

In installations with a [DIMAG connection](inge.md), Anton hands over every
media file to DIMAG on upload via the Inge middleware and keeps a record of
whether the handover is verified — see [upload status](dimag-uploads.md). After
that, the bitstream preservation of the master lies with DIMAG.

!!! note "Fixity then lies with DIMAG"
    On these installations, the long-term archive checks the masters.
    `media:check` therefore skips them with a note that the files are held in
    DIMAG. On request, Anton deletes the local copy after a verified handover.
