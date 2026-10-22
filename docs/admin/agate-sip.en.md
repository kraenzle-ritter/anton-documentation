# agate SIP import

[agate](https://github.com/kraenzle-ritter/agate) (the Anton preparation tool
for SIPs built from loose file collections) can send SIPs (BagIt or E-ARK) directly to
Anton via HTTP. Anton receives the ZIP, checks it, creates
a backup, imports the contents as units of description below the chosen fonds
and notifies agate when everything is finished.

The whole path runs **asynchronously** — agate can carry on working in parallel
or prepare other SIPs.

## BagIt or E-ARK

agate delivers a SIP as a BagIt bag or as an E-ARK SIP 2.2.0, depending on its settings. Both carry the same `metadata.json`. Anton recognises the layout from the content of the ZIP (`bagit.txt` or `METS.xml`); the file name stays `sip-agate-<fonds_id>.zip`, and both take the same ways in: direct import, inbox, upload on `/import/sip-anton` and `anton:import --from-sip`.

| | BagIt | E-ARK |
|---|---|---|
| `metadata.json` | `data/meta/metadata.json` | dmdSec with `OTHERMDTYPE="anton-import-format"`, usually `metadata/descriptive/metadata.json` |
| Files | `data/content/` | `representations/rep1/data/` |
| Check before the import | the bag's manifests | the checksums in the METS, for `metadata.json` and every file it names |
| Validation report | — | E-ARK validation (eark-ip), kept as a validation event with the run |

A missing or altered file stops the import before anything is written. The E-ARK report does not stop the import: whether the files are unchanged is decided by the checksums. E-ARK packages from other tools are accepted too, see below.

## E-ARK packages from other tools

An E-ARK package without `anton-import-format` (for example from RODA-in, commons-ip or ESSArch) is recognised by its content as well, on every way in and under any file name. Without a target in its name (`…-agate-<holding_id>.zip`) the package waits in the inbox.

- **Description:** from the first EAD in the package (EAD3 or EAD 2002, read as the EAD import reads it), else from Dublin Core as one record, else one record named after the package (METS `LABEL` or `OBJID`).
- **Files:** the files of the master representation hang below the description as folders and records. When an EAD `<dao>` names a file of the package, that file becomes the medium of its unit of description.
- **Representations:** the inbox shows each representation with its number of files and a proposal (from PREMIS, from the name, otherwise the first as master and the others «unknown»). For each one chooses master, original (version), access copy or separate entries; exactly one must be the master, at most one the access copy. A file of a version or access copy hangs on the medium of the master file with the same folder and name without extension; files without a pair and separate entries go below a folder named after their representation. Without a choice in the inbox (import with a target in the file name, console) the proposal applies, «unknown» as separate entries.
- **Check:** every file of every representation is checked against its checksum in the METS before the import.

## Workflow

```
┌──────────┐    HTTP POST     ┌──────────┐
│  agate   │ ───────────────▶ │  Anton   │
│          │   sip.zip        │          │
└──────────┘                  └──────────┘
                                    │
                                    ▼ async job
                              ┌──────────┐
                              │  Import  │
                              │  BagIt   │
                              │  validate│
                              │  + apply │
                              └──────────┘
```

### Two paths

1. **Direct import** — if the file name follows the convention
   `sip-agate-<fonds_id>.zip`, the import starts immediately below the fonds
   specified.

2. **Inbox** — otherwise the SIP ends up in the **inbox** at `/sip/inbox`.
   Editors see all waiting uploads and either assign a fonds manually per entry
   or discard the SIP.

The inbox prevents unassigned SIPs from silently eating up storage space —
editors actively see what is waiting.

The same holds for the manual upload in the tab **Manual upload** of **SIP import (anton-import-format)**: a SIP named `sip-agate-<fonds_id>.zip` appears in the list and is started with **Import**; any other goes to the inbox. A SIP whose content is already imported, or being imported, is not accepted.

## Inbox (`/sip/inbox`)

Visible to the editor and admin roles under **Import / Export → SIP Inbox**.
Per row:

- SIP file name, upload date
- Preview (number of files, package check BagIt or E-ARK, NARA categories)
- Actions: **assign fonds** (opens a selection) or **discard**

## Vocabulary mapping: NARA → tenant object type

Internally, agate speaks in NARA standard categories (StillImage, Audio,
Textual, Video, Geospatial …). On import, Anton translates these into the
tenant-specific value list "object type" (image, file, photograph, plan,
collection …).

The mapping is **configurable per tenant**. The advantage: agate does not have
to know the specific vocabulary of the archive.

Configuration:

```php
Setting::setValue('nara_to_objecttype_map', [
    'StillImage' => 'Bild',
    'Textual'    => 'Akte',
    'Audio'      => 'Tonaufnahme',
    // ...
]);
```

If no suitable tenant type exists for a NARA category, the `object_type` field
remains empty (instead of aborting the import) and can be assigned by hand
later.

## HTTP API

Endpoint: `POST /api/sip/upload`

Request:

- Multipart form with a `file` field (`sip.zip`, BagIt or E-ARK)
- Header `Authorization: Bearer <api_token>` (Sanctum token, see
  [API authentication](../api/authentication.md))

Response: `202 Accepted` with JSON containing the job ID:

```json
{
  "job_id": "01J5XYZ...",
  "status": "queued",
  "callback_url": "https://your-anton.ch/api/sip/status/01J5XYZ..."
}
```

agate then polls `callback_url` until `status: completed` (or `failed`).

## Import log

Every agate SIP import is a run in the import log — with reference code
`IMPORT-{yyyy}-{NNN}`, file name, checksum, time, outcome and the records it
created. The import path is thereby auditable after the fact as well; no
accession archive is needed for it.

## Format conversion in agate

Anton applies no format rule to a SIP: its checksums prove that the delivered
files arrived unchanged. agate therefore applies the archive's format rules
itself before it closes a SIP; it reads the switches from Anton through the
API.

What agate did to a file is recorded in `metadata.json` on the file entry
(`format_normalization`). For each rule Anton records a `format-normalization`
event on the medium, as for a conversion in Anton itself. The event names the
rule, the tool versions and the checksums before and after the conversion, so
the checksum of the file as agate received it stays on record.

## Original and access copy

From anton-import-format 0.6 on, a SIP may deliver more than the master for a file: the file before a conversion (`versions`, role `original`) and an access copy (`access_copy`). The master stays the medium.

- **Original:** Anton keeps it behind the medium (version «original», with its own checksums and events, in DIMAG through `media:versions-to-cloud`), never as a medium of its own. If agate converted the file and kept the original, the `format-normalization` event points to that version.
- **Access copy:** the setting `import_access_copy` decides. `derive` (default): Anton computes the web version itself and does not store the delivered copy. `adopt`: Anton takes it as the web version when it fits the master (image → JPEG, PDF → PDF, video → MP4, audio → MP3) and its checksum matches; otherwise it computes its own. The decision is recorded as an «access copy» event on the medium. `media:conversions` replaces an adopted web version only with `--replace-supplied`. Anton always computes the thumbnail itself.
- **Checks:** original and access copy are checked before the import like the master: virus check, checksum, and for E-ARK against the METS of their representation (`representations/<source>/data/`). A failure stops the import before anything is written.
- **Format version:** agate asks Anton through `GET /api/import-format` which version of the format its import reads, and writes original and access copy only when Anton reports 0.6 or later. Anton refuses a `metadata.json` in a newer version than it reads.

## Configuration checklist

For agate imports to work:

1. Set **`setting('enable_sip_anton_import')` to `true`** (default false for
   security reasons)
2. Generate an **API token** for agate (see
   [API authentication](../api/authentication.md))
3. Create the **NARA mapping** (see above) — a default mapping exists, but
   tenant-specific values are likely to be necessary
4. The **queue worker** has to be running (Anton standard: Supervisor)

## Common stumbling blocks

- **Repeated uploads with the same file name** work — Anton checks the
  original file name, not the UUID-suffixed path on disk.
- **A NARA category without a tenant type** does not abort the import. The
  `object_type` remains empty.
- **The wrapper record at the top of the SIP** is no longer forced to have an
  object type — the hard-coded "Agate SIP" has been removed.

## Related pages

- [SIP ingest](sip-ingest.md) — generic SIP import mechanics
- [Inge / DIMAG upload](inge.md) — DIMAG connection for ZH municipalities
- [API authentication](../api/authentication.md) — tokens for agate
