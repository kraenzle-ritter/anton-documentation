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
    ├── manifest-sha512.txt          ← SHA-512 checksums of all files
    ├── manifest-md5.txt             ← MD5 checksums of all files
    ├── bagit.txt
    └── bag-info.txt                 ← repository details, external identifier
```

- Checksums: **SHA-512**, as BagIt recommends, and **MD5** beside it for recipients that only check that.
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
always uses `CreateDip` for the BagIt DIP and places the ZIPs in the target directory instead of
deleting them after delivery as the web download does.

!!! note "Visibility"
    The DIP download is only reachable for logged-in internal users. Like the
    rest of the internal view, a DIP also contains **records marked as
    private** — internal users are meant to see them.


## E-ARK DIP

Besides the BagIt DIP there is an **E-ARK DIP 2.2.0** following the European standard for dissemination packages (anton#697). It can be read without Anton: `METS.xml` describes the package, the representations lie below `representations/`, the description below `metadata/descriptive/`.

### Two scopes

| | Access (default) | Full (`--full`) |
|---|---|---|
| Where | «E-ARK DIP» button, console | console only |
| Records | what a guest sees: without locked records and drafts, with their subtree | all |
| Media | access copies (`web`) in `representations/access/`; without private media and without the media of records under a protection period (their description stays) | masters in `representations/master/`, kept originals in `representations/original/` |
| Description | EAD3 or EAD 2002, optionally RiC-O and CIDOC CRM | the same, plus the native format (`anton-native.json`) |
| PREMIS | each representation's function, each file's format and source — no events, no persons | plus PREMIS per record with all events (as in the BagIt DIP) |
| Word finding aid | no (it does not filter) | yes, under `documentation/` |
| Holdings log | «Export delivered» | «Master downloaded» |

The access scope is always built as the public view, whoever downloads it. A medium without an access copy is left out and counted; `media:conversions` computes it. What was left out is counted in `documentation/export.txt`, never with titles.

### Validation

Every package is validated against E-ARK after it is written (`kraenzle-ritter/eark-ip`). A package with errors is deleted and not delivered; the message names the failed requirements. Warnings do not stop it.

If you also check the packages with commons-ip, the Java validator of the E-ARK community, you get one warning on CSIP101. It is a false alarm of commons-ip: here the package follows the example of the specification and the DILCIS test corpus, and commons-ip reports the same for the corpus's own valid sample package (reported as keeps/commons-ip#390).

### Settings

| Setting | Meaning | Default |
|---|---|---|
| `level_of_description_ids_for_eark_dip_download` | level ids with an «E-ARK DIP» button | `[]` (no button) |
| `eark_dip_ead` | `ead3` or `ead` (EAD 2002) | `ead3` |
| `eark_dip_rdf` | further descriptions: `ric`, `cidoc` | empty |
| `eark_dip_sync_limit` | from how many media in the subtree the package is built in the background | `500` |

Above `eark_dip_sync_limit`, the package is built in the background and appears under **Data export → E-ARK DIP** (`/export/dip`), where internal users download or delete it.

### Console

```bash
php artisan anton:export-dip --env=<slug> --ids=42 --format=eark --target-dir=/path/to/target
php artisan anton:export-dip --env=<slug> --ids=42 --format=eark --full --target-dir=/path/to/target
```

Without `--format` the BagIt DIP is written as before; `--full` applies to `--format=eark` only. The full scope checks first whether there is enough free space (about twice the size of the masters).
