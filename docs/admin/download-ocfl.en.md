# OCFL download

In addition to DIP/BagIt, Anton can export holdings in the [Oxford Common File
Layout (OCFL) v1.1](https://ocfl.io/1.1/spec/). OCFL is a storage specification
for long-term preservation: versioned, checksum-secured, content-addressed,
self-describing. Several Swiss long-term archives — namely UB Basel and the
DLZA — expect OCFL for handover.

## Two modes

| Mode | Button in the detail view | Content |
|---|---|---|
| **Single object** | "OCFL" | One OCFL object root with the media of this record |
| **Subtree (fonds)** | "OCFL (fonds)" | One OCFL storage root (HashedNTupleStorageLayout) with one object per descendant |

Both modes deliver a ZIP for immediate download. Per OCFL version (v1), each
object contains:

- `data/content/<file>` — the original media files
- `metadata/ead.xml` — complete EAD description
- `metadata/dc/<file>.xml` — Dublin Core per medium
- `metadata/anton-import.json` — round-trip payload in the Anton import format

The object ID is `urn:anton:{tenant}-objects-{id}` (corresponding to the
`full_id` of the AntonObject, with a URN prefix).

## Configuring the visibility of the buttons

As with DIP/Word, the OCFL buttons belong in the module
`module_word_download` of the internal detail form. Visibility per level of
description is controlled by two settings:

| Setting | Default | Recommended |
|---|---|---|
| `level_of_description_ids_for_ocfl_download` | empty | `[3, 4, 5, 6]` (fonds, series, file, item) |
| `level_of_description_ids_for_ocfl_subtree_download` | empty | `[3]` (fonds only) |

The defaults are **deliberately empty** — OCFL only makes sense for archives
whose receiving body expects the format. Activate via `/settings` or Tinker.

## Address field in the OCFL inventory

Every OCFL version carries a `user.address` entry in the `inventory.json` for
provenance. Anton fills it with the tenant setting `repository_email` (as a
`mailto:` URI); the fallback is a stable URN `urn:anton:tenant:{slug}`. This
keeps personal email addresses out of the archival package while giving the
receiving archive a point of contact.

## Validation

Every export is run through the official OCFL validator of the
[`ottosmops/ocfl`](https://packagist.org/packages/ottosmops/ocfl) package and
validates all 55/12/13 OCFL fixtures of the spec.

External validation is possible via the CLI:

```bash
# validate an OCFL object
ddev exec vendor/bin/ocfl validate <path-in-container>

# list a storage root
ddev exec vendor/bin/ocfl list <path-in-container>

# show object content
ddev exec vendor/bin/ocfl info <path-in-container>
```

Exit codes: `0` valid, `1` invalid, `2` usage error, `3` runtime error.

## When OCFL, when DIP?

| Receiving body | Format |
|---|---|
| Classic final archive expecting a BagIt container | **DIP** |
| Long-term archive with an OCFL requirement (UB Basel §7, DLZA) | **OCFL** |
| Research repository that understands OCFL | **OCFL** |
| Local handover with a Word finding aid | **DIP** |

Both run alongside each other — DIP is fully retained.

## Routes

- `GET /objects/ocfl/{id}` — single object export (ZIP)
- `GET /objects/ocfl-subtree/{id}` — subtree export (ZIP)

Both behind the `admin` middleware. No web form, direct download.
