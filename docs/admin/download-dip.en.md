# DIP download

A **DIP** (Dissemination Information Package) is a ZIP that bundles an object
with its entire subtree — all subordinate records, their media files and
accompanying metadata. Intended for the classic handover of files to third
parties. For preservation-oriented delivery, see
[OCFL download](download-ocfl.md).

## Adding the button and making it visible

The DIP button belongs in the download module (`module_word_download`) of the
internal detail form — the same module as Word, OCFL and the RDF exports. It
appears **only** for levels of description that are listed in the setting:

| Setting | Meaning | Example |
|---|---|---|
| `level_of_description_ids_for_dip_download` | Level IDs with a DIP button | `[3, 4, 5, 6]` |
| `dip_creator_class` | Creator class (default `CreateDip`) | `CreateDip` |

Level-of-description IDs: `1` collection, `2` recordgroup, `3` fonds, `4` class,
`5` file (dossier), `6` item, `700` series.

Neither setting is editable via `/settings` — they are set by seeder or Tinker:

```php
\Ottosmops\Settings\Setting::setValue('level_of_description_ids_for_dip_download', [3,4,5,6]);
```

The button is suppressed automatically if the object lies in the accession area
(`accessions_archives_id` in its path).

## What is in the package (`CreateDip`, default)

The standard produces a **BagIt bag** (ZIP):

```
<full_id>.zip
└── <full_id>/
    ├── data/
    │   ├── content/<Title>/…        ← media files, folders = object titles
    │   └── meta/
    │       ├── <file>.xml           ← Dublin Core per medium
    │       └── <full_id>.docx       ← Word finding aid (cf. download-word)
    ├── manifest-md5.txt             ← MD5 checksums of all files
    ├── bagit.txt
    └── bag-info.txt                 ← repository details, external identifier
```

- Checksums: **MD5** (the BagIt default SHA-512 has deliberately been removed).
- `bag-info.txt` draws `repository_name`, `repository_address` and
  `repository_email` from the settings.
- Files are named after the reference code, folders after the object title.

## Simplified variant (`ZhCreateDip`)

If `dip_creator_class` is set to `ZhCreateDip`, a lean ZIP is produced
**without BagIt and without metadata**: only the folder structure from the
titles, with the media files under their **original file names**. Only leaf
objects (without children of their own) that carry media are included.

Custom variants: create a class under `app/Services/Exporter/Dip/` with
`create(AntonObject $object): string` and enter the class name in the setting.

## Batch export from the console

```bash
php artisan anton:export-dip --env=<slug> --ids=42,77,103 --target-dir=/path/to/target
```

`--target-dir` is optional (default: the transfer directory). The CLI export
always uses `CreateDip` and places the ZIPs in the target directory instead of
deleting them after delivery as the web download does.

!!! note "Visibility"
    The DIP download is only reachable for logged-in internal users. Like the
    rest of the internal view, a DIP also contains **records marked as
    private** — internal users are meant to see them.
