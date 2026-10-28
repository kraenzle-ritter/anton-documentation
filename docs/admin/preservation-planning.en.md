# Preservation planning

Under **Admin → Preservation Planning**, Anton shows which file formats the archive holds, how NARA rates their risk and where format validation and virus check stand. The figures are computed from the database each time the page is opened. The page is a view: it reports nothing by itself and triggers no measures; a migration runs through [`media:migrate`](console-commands.md#mediamigrate), today as lossless repacking within the same format (see [format decisions](preservation.md#formatentscheide)).

## MIME types

Number and share of media per MIME type, as a table and as a pie chart.

## NARA categories

Classification according to the standards of the **US National Archives** (NARA risk/action matrix). Every file is assigned to a category (StillImage, Audio, Textual, Video, Geospatial, …) and receives a **risk level** plus a **recommended action** from the NARA list.

Implemented via the Anton open source package [`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk).

Risk levels:

| Level | Meaning | Examples |
|---|---|---|
| **Low** | Standards-compliant format, well documented | PDF/A, TIFF, WAV |
| **Moderate** | Widespread format with risks | JPEG, MP3 |
| **High** | Proprietary or poorly documented | DOC, RAW image formats |
| **Unknown** | Format not identified | unknown |

Recommended actions as NARA assigns them: **Retain**, **Retain for Future Assessment**, **Transform** (convert to another format), **Identify** (determine format or version more precisely). The view counts media without identification under **Identify**.

## PRONOM IDs

PRONOM is the UK National Archives database for file format identification. Anton gives every file a PUID (PRONOM Unique IDentifier); identification is done by **Siegfried** or **Fido** through the `kraenzle-ritter/puidentify` library.

The table lists the PUIDs by frequency, with format name, share and the most frequent NARA risk level and action. «View» opens the media list filtered on that PUID; a row of its own counts the unidentified media.

## Risk assessment

A cross table counts the media by NARA risk and recommended action; two pie charts show the distribution of risk levels and of actions. Below are up to 50 media that need action: unidentified ones first, then all others except **Retain**, ordered by risk.

## Format validation {#formatpruefung}

Where the holdings stand in the [format validation](preservation.md), each master by its latest check: per format group (PDF, TIFF, other images, audio and video) invalid, valid with warnings, valid, not validated, never checked. Also how far the nightly run has come (latest check thorough, at ingest only, never), PDF risks and PDF/A claims, contradictions between extension, format and PRONOM ID, and the list of media invalid in their latest check, with a link to the record. What was checked when is under **Administration → Logs → Format validation**.

## Virus check {#virenpruefung}

For each master the result of its latest virus check, at ingest or with [`media:virus-scan`](console-commands.md#mediavirus-scan): malware found, not checkable, clean scanned in parts (files over 2 GB), clean, never checked. Also the scanner and signatures of the latest check and the list of masters with a finding or not checkable. Files refused at ingest never became media; they are in the security log.

## Format list {#formatliste}

Which formats the archive prefers and accepts, by PUID, and the media whose format is not on it. Here an admin saves an own list or returns to the default; see [Format list](formatliste.md).

## Media files

All media with search and filters by PUID, NARA risk, NARA action and MIME type, each with a link to the record and to the master download.

## Batch processing with Siegfried

For new media, Anton carries out format identification asynchronously as a queue job (`ProcessMediaIdentification`). For **surveying existing holdings** (after a migration step or a data import, for example) there is a batch command:

```bash
ddev exec php artisan media:identify --env=<tenant>
```

Options:

- `--limit=1000` — only N files
- `--collection=image` — only files of one collection
- `--force` — also re-identify files that already have a PUID
- `--oldest=N` — the N media identified longest ago, those without an identification event first (implies `--force`)

The command uses **Siegfried** or **Fido**, whichever is installed on the server. If neither is, identification stays empty; there is no fallback without an external program. Every identification is an event on the medium, with tool, version and signature file; a new identification also reassesses the NARA risk.

## Open source packages of this pipeline

Three packages from the Anton ecosystem form the basis of preservation planning:

| Package | Purpose |
|---|---|
| [`kraenzle-ritter/nara-risk`](https://github.com/kraenzle-ritter/nara-risk) | NARA risk/action mapping |
| [`kraenzle-ritter/puidentify`](https://github.com/kraenzle-ritter/puidentify) | PRONOM PUID lookup via Siegfried or Fido |
| [`ottosmops/office2text`](https://github.com/ottosmops/office2text) | Full-text extraction from Office files (for the search, not preservation directly) |

## When does what run?

| Event | Trigger |
|---|---|
| New file uploaded | Async queue: PRONOM identification + NARA mapping |
| File replaced | Async queue: same pipeline again |
| Manual audit | `media:identify` CLI command |
| Dashboard opened | Figures are computed from the database when the page is opened; there is no schedule for it |

## Related topics

- [Console commands](console-commands.md) — `media:identify`, `media:validate-pdfs`, `media:check`
- [SIP ingest](sip-ingest.md) — with a SIP import, PRONOM identification runs automatically
