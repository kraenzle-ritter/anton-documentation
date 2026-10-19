# Preservation planning

Anton offers a dashboard for digital preservation — an overview of file formats, risks and recommended actions per
tenant.

Under **Admin → Preservation Planning** there are these areas.

## MIME type distribution

Interactive charts (donut / bars) show how the media holdings are distributed
across MIME types:

- number of files per MIME type
- total size per MIME type
- clicking a slice opens the list of the records concerned

Helps with questions such as: «How many PDFs do we have?» / «Have our TIFFs
already been migrated?» / «How large is the audio share?».

## NARA categories

Classification according to the standards of the **US National Archives** (NARA
risk/action matrix). Every file is assigned to a category (StillImage, Audio,
Textual, Video, Geospatial, …) and receives a **risk level** plus a
**recommended action** from the NARA list.

Implemented via the Anton open source package
[`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk).

Risk levels:

| Level | Meaning | Examples |
|---|---|---|
| **Low** | Standards-compliant format, well documented | PDF/A, TIFF, WAV |
| **Moderate** | Widespread format with risks | JPEG, MP3 |
| **High** | Proprietary or poorly documented | DOC, RAW image formats |
| **Unknown** | Format not identified | unknown |

Recommended actions: **retain**, **transform** (DOC → PDF/A, for example),
**replace** (RAW → DNG, for example), **monitor**.

## PRONOM IDs

PRONOM is the UK National Archives database for file format identification.
Every file in Anton is given a PUID (PRONOM Unique IDentifier) via **Siegfried**
(or the internal `kraenzle-ritter/puidentify` library).

The dashboard lists:

- top PUIDs by frequency
- file examples per PUID (clickable, opens the record)
- a note when a PUID is on a NARA warning list

## Risk assessment

Consolidated view: NARA risk × PUID confidence × count. Shows in prioritised
form where measures make sense. Example:

> *«127 files are WordPerfect 5.x (PUID fmt/192) — NARA recommends migration to
> PDF/A. 89 of them are under `Akzession 2018/3`.»*

Clicking the row opens the list with bulk actions (trigger migration, move into
a collection, etc.).

## Format validation {#formatpruefung}

Where the holdings stand in the [format validation](preservation.md), each
master by its latest check: per format group (PDF, TIFF, other images, audio
and video) invalid, valid with warnings, valid, not validated, never checked.
Also how far the nightly run has come (latest check thorough, at ingest only,
never), PDF risks and PDF/A claims, contradictions between extension, format
and PRONOM ID, and the list of media invalid in their latest check, with a link
to the record. What was checked when is under **Administration → Logs →
Format validation**.

## Virus check {#virenpruefung}

For each master the result of its latest virus check, at ingest or with
[`media:virus-scan`](console-commands.md#mediavirus-scan): malware found, not
checkable, clean, never checked. Also the scanner and signatures of the latest
check and the list of masters with a finding or not checkable. Files refused at
ingest never became media; they are in the security log.

## Batch processing with Siegfried

For new media, Anton carries out format identification asynchronously as a queue
job (`ProcessMediaIdentification`). For **surveying existing holdings** (after a
migration step or a data import, for example) there is a batch command:

```bash
ddev exec php artisan media:identify --env=<tenant>
```

Options:

- `--limit=1000` — only N files
- `--collection=image` — only files of one collection
- `--force` — also re-identify files that already have a PUID

The command uses **Siegfried** if it is available on the server (`which sf`);
otherwise it falls back to the pure PHP implementation of `puidentify` (slower
but with no external dependency).

## Open source packages of this pipeline

Three packages from the Anton ecosystem form the basis of preservation planning:

| Package | Purpose |
|---|---|
| [`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk) | NARA risk/action mapping |
| [`kraenzle-ritter/puidentify`](https://github.com/kraenzle-ritter/puidentify) | PRONOM PUID lookup |
| [`ottosmops/office2text`](https://github.com/ottosmops/office2text) | Full-text extraction from Office files (for the search, not preservation directly) |

## When does what run?

| Event | Trigger |
|---|---|
| New file uploaded | Async queue: PRONOM identification + NARA mapping |
| File replaced | Async queue: same pipeline again |
| Manual audit | `media:identify` CLI command |
| Daily statistics | Cache is recalculated overnight (see `app/Console/Kernel.php`) |

## Related topics

- [Console commands](console-commands.md) — `media:identify`,
  `media:validate-pdfs`, `media:check`
- [SIP ingest](sip-ingest.md) — with a SIP import, PRONOM identification runs
  automatically
