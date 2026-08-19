# agate SIP import

Since **v0.61.0**, [agate](https://github.com/kraenzle-ritter/agate) (the Anton
preparation tool for SIPs built from loose file collections) can send BagIt
packages directly to Anton via HTTP. Anton receives the ZIP, checks it, creates
a backup, imports the contents as units of description below the chosen fonds
and notifies agate when everything is finished.

The whole path runs **asynchronously** — agate can carry on working in parallel
or prepare other SIPs.

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

## Inbox (`/sip/inbox`)

Visible to the editor and admin roles under **Import / Export → SIP Inbox**.
Per row:

- SIP file name, upload date
- Preview (number of files, BagIt validity, NARA categories)
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

- Multipart form with a `file` field (`sip.zip` BagIt container)
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

## Accession archive

If the tenant has an **accession archive** configured
(`setting('accessions_archives_id')`), the SIP import is recorded there as a new
entry — with date, agate version information and a file name reference. The
import path is thereby auditable after the fact as well.

## Configuration checklist

For agate imports to work:

1. Set **`setting('enable_sip_anton_import')` to `true`** (default false for
   security reasons)
2. Generate an **API token** for agate (see
   [API authentication](../api/authentication.md))
3. Set **`accessions_archives_id`** to a suitable wrapper fonds, so that the
   entry is recorded
4. Create the **NARA mapping** (see above) — a default mapping exists, but
   tenant-specific values are likely to be necessary
5. The **queue worker** has to be running (Anton standard: Supervisor)

## Common stumbling blocks

- **Repeated uploads with the same file name** work since v0.61.0 — Anton now
  checks the original file name, not the UUID-suffixed path on disk.
- **A NARA category without a tenant type** no longer aborts the import (since
  v0.61.0). The `object_type` remains empty.
- **The wrapper record at the top of the SIP** is no longer forced to have an
  object type — the hard-coded "Agate SIP" has been removed.

## Related pages

- [SIP ingest](sip-ingest.md) — generic SIP import mechanics
- [Inge / DIMAG upload](inge.md) — DIMAG connection for ZH municipalities
- [API authentication](../api/authentication.md) — tokens for agate
