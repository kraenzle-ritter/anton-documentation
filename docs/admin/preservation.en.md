# Long-term preservation: overview

Anton covers parts of digital preservation and deliberately leaves others to the
infrastructure or to a connected long-term archive. This page sets out what
happens where and refers to the detail pages. Above all it answers the question
of which artefact is a **backup** and which is a **publication view**.

## The chain

### Transfer

During [SIP ingest](sip-ingest.md) according to eCH-0160, Anton verifies the
checksum declared in the `metadata.xml` for **every file in the package**: the
hash is recalculated over the actual file and compared. If it deviates,
validation fails. The algorithm comes from the package itself, so it is not
fixed to MD5. In addition, Anton remembers the checksum of the SIP ZIP and
rejects packages that have already been loaded.

### Storage

For every media file, Anton calculates an **MD5 checksum** on upload and stores
it in the database. The **master remains unchanged**; the derivatives (`web`,
`thumb`) are access copies.

### Format identification and risk

On upload, Anton identifies the format via **Siegfried** or **Fido** and records
the **PRONOM ID**; from this it derives the risk assessment according to the
**NARA Digital Preservation Framework**. For existing holdings this can be
supplied retrospectively with
[`media:identify`](console-commands.md#mediaidentify). It is evaluated in
[preservation planning](preservation-planning.md).

!!! note "Depends on the server"
    Identification requires Siegfried or Fido to be installed on the server. If
    both are missing, the PRONOM ID remains empty — and without it there is no
    risk assessment either. The «unidentified media» tab shows how complete the
    identification is.

### Delivery

See [Backup or publication?](#sicherung-oder-publikation) further down.

## Checking integrity {#integritat-prufen}

Anton brings the tools with it but does not run them of its own accord:

| Command | What it does |
|---|---|
| [`media:check --levels=4`](console-commands.md#mediacheck) | Reads every file afresh, calculates the MD5 anew and compares it with the database. With `--log-integrity-check`, every check is logged as an event — producing a demonstrable history. |
| [`media:snapshot --verify --git`](console-commands.md#mediasnapshot) | Writes a checksum snapshot of all media, compares it against the database and commits changes to a local Git repository. This makes it traceable what has changed between two runs. |

!!! important "To be set up, not built in"
    Anton does **not** carry out a recurring integrity check by itself — there is
    no built-in schedule. The check is set up per installation as a cron job.

    **With Anton as a Service** this is currently set up for the large archives;
    for further installations on our servers, k & r is responsible. **On
    premises**, the operating institution sets up the job itself — the commands
    are available for it, but an automatic run does not arise from that on its
    own.

To be distinguished from this is [`anton:doctor`](console-commands.md): it
checks the **consistency of the database** — hierarchy, reference codes, derived
fields — and whether the files are present. It does not compare checksums.

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

Which data each format takes with it in detail, which is only in the SQL dump
and who can trigger which artefact is shown by the
[export matrix](export-matrix.md). In short: the SQL dump and the standard
exports go via the interface, the native round trip and the migration package
only via the CLI.

For the [static publication](statische-publikation.md) of a fonds as a
standalone website there is a dedicated bundle.

## What Anton does not do

So that no false expectations arise:

- **No format migration.** Anton produces access copies but does not normalise
  into archival formats — no TIFF to JPEG2000, no PDF/A, no video
  normalisation. Preservation planning **points out the need for action but does
  not act**.
- **No PREMIS, no METS.**
- **No storage redundancy.** Redundant storage is provided by the operating
  infrastructure, not by the application. Anton itself sees a local store and
  optionally a cloud store and can neither display nor monitor the redundancy.
  With **Anton as a Service**, the data is held in
  [three copies at three locations](../faq/longterm_archives.md) (sixfold
  redundancy in total); **on premises**, the operating institution is
  responsible for this itself.

## With a connected long-term archive

In installations with a [DIMAG connection](inge.md), Anton hands over every
media file to DIMAG on upload via the Inge middleware and keeps a record of
whether the handover is verified — see [upload status](dimag-uploads.md). After
that, the bitstream preservation of the master lies with DIMAG.

!!! note "Anton then no longer checks itself"
    On these installations, `media:check` skips the integrity check of the
    masters with a note that the files are held in DIMAG. Fixity is the
    responsibility of the long-term archive there. On request, Anton deletes the
    local copy after a verified handover.
