## Summary
It is possible to import data and the associated files (media) into Anton. The descriptive data (Excel file) is recorded in a (prescribed) Excel sheet and uploaded to the server together with the files. The data is then validated and, if validation was successful, the import/ingest can take place (descriptive data and media). See also the documentation in Anton at `/import/documentation`.

## Import hub `/import`

All import paths are brought together at one address: `/import` (in the menu under **Import / Export → Import**). The page has four tabs:

| Tab | Content |
|---|---|
| **Inbox** (default) | Waiting agate SIPs that still need a parent fonds. When something is waiting, a counter badge appears next to it in the admin menu. |
| **SIP** | Direct SIP upload (BagIt packages) with validation and ingest. See [SIP ingest](../admin/sip-ingest.md) and [agate SIP](../admin/agate-sip.md). |
| **Excel** | Excel imports (the main subject of this page, see below). |
| **Directory** | Import of a directory structure (ZIP/GZ). |

The old URLs (`/sip/validation`, `/sip/ingest`, `/import/validation`, `/import/ingest`, `/sip/inbox`) redirect transparently to the appropriate tab — bookmarks and external links remain valid.

### Detail view in the inbox

For each waiting SIP in the inbox there is a **details** link. Behind it is an inspection page that reads only the `metadata.json` from the BagIt (without unpacking the media) and shows:

- BagIt validity (manifest, checksums)
- number of records in the SIP
- NARA object type categories — with a note if the tenant does not know a suitable type for a category
- title of the topmost record

This makes it possible to see before the import whether the SIP makes sense, whether the tenant vocabulary fits, and to discard the SIP if necessary before anything ends up in the database.

### Live progress

All imports run **asynchronously in the background**. After clicking "import", you land on a progress page that updates the current status every few seconds: phase (preparation / creating records / reading media), rows completed, and at the end a link to the **run in the import log**.

This applies to all paths — Excel, SIP, directory and finalising the inbox.

### A reference code for every import

Every import (regardless of the path) gets a reference code `IMPORT-{yyyy}-{NNN}` and an entry in the import log. The entry records:

- the original file name
- the MD5 checksum
- the time of import
- the import path (Excel / SIP / directory / agate)
- the **settings used** (see below)
- the outcome, and the message if it failed

<!-- v0.88.0: receipts in the accession archive retired, existing ones migrated into the log -->
!!! info "No receipt in the accession archive"
    An import does not create an archival record as a receipt. The accession archive stays reserved for real accessions — physically arrived, not yet catalogued — and its reference codes are not used up by imports.

The reference code is assigned at the start. A failed run therefore keeps it and stays in the log with its error — a failed delivery has to stay distinguishable from one that never happened.

### Import log {#import-protokoll}

Under **`/import/audit`** is the list of all import runs: reference code, source file, time, number of records created and the content language used. It is an ordinary Anton table — sortable, with a configurable page length, and the columns can be adapted under *Admin → Forms* like those of any other list.

Successful runs are shown by default; a filter reveals failed and aborted ones. Nothing is ever deleted.

The **details** link leads to the run: source file, checksum, settings used together with their origin, who triggered it, and the records it created.

The imported file is kept. After a successful run it moves to `metadata_imported/` — so it stops appearing in the picker — and the entry says where it went.

The settings are recorded in plain text, one line per setting with its value and origin. They remain there permanently — even a year later it is thus possible to trace the assumptions under which a delivery came in.

## Procedure (Excel import)
First, an Excel file has to be created according to the specifications below. This is uploaded under "Upload Metadata", and the associated media files are uploaded under "Upload Media". Finally, the Excel file can be checked under "Validation". The validation displays errors and issues warnings. The data can only be imported once the validation is free of errors. The import is triggered under "Ingest" and can take several minutes depending on the volume.

## Content language of the import

Translatable fields — titles, text fields, newly created keywords, actors, places and locations — need a language. This is a deliberate decision that is visible before the run.

<!-- v0.87.0: content language made explicit; before that the import followed the interface language -->
!!! note "The interface language plays no role"
    Whichever language the interface is currently showing has no influence on the import. What counts is solely the content language of the run.

The content language is determined in this order — the first value that is set wins:

1. the choice for this run (`--locale` on the command line)
2. the archive setting `import_options.locale`
3. the first language from `locales` — the main language of the archive

Before the start, the inspection page names the language that applies **and where it comes from** («chosen for this run», «archive setting», «default»). After the run, the same information is in the log entry (see [Import log](#import-protokoll)).

A column with a language code (`title_fr`) trumps this choice for its own field — see [titel](#titel-title).

### Why the language matters for searching too

The content language determines not only where data is written, but also **what Anton searches in when looking for existing actors and places**. If a language is chosen in which the holdings are not recorded, the matching finds nothing — and, where creation is switched on, creates a new record for every name.

Anton therefore searches in two rounds: first in the language of the run, then in the main language of the archive. A hit from the second round is noted in the log. And the preview (see below) shows the number of new records before anything is written — if the language does not fit the holdings, almost all actors appear as «new» there at a glance.

### Where the settings are

The import settings are a matter for the archive (`import_options`) and are viewed where they take effect: on the inspection page of the uploaded file, each with the **value that applies**, its origin and an explanation. Displayed are the content language and the switches determining whether unknown actors, places, keywords, locations and object types are newly created.

There is deliberately **no** second place to store them in the user profile: a value that is only needed when importing belongs in one place — and that place names it together with its origin, instead of merely saying «default».

## Preview: what the import would create

Before the start, the inspection page shows how many **distinct** authority entries the run would newly create: actors, places, keywords, locations, object types. Along with the names themselves.

The number counts distinct entries, not rows: an unknown actor occurring in 500 rows is **one** new record.

The names are more important than the number. A wrong separator shows up in the fact that «Muster, Hans; Beispiel, Anna» stands as *one* name in the list — in a mere number that would be invisible.

If creation is switched off for one kind, the same entries appear as **not assignable**, with a note that these links will be dropped in the run without replacement. That, too, is a result one wants to know beforehand.

If the number of new records of one kind exceeds half the number of rows, a **warning** appears. That more often indicates a separator, language or column problem than genuine growth. The warning blocks nothing — the run can be started.

!!! note "The preview writes nothing"
    It only reads. No record is created, not even one that would have to be removed again afterwards.

## Columns
The file may contain additional columns; these are, however, not imported. For simplicity, columns may be deleted. The final file must contain at least the following columns:

    parent
    verzeichnungsstufe

## Explanation and rules for the individual columns/fields

### parent

The `parent` field specifies where the record to be imported is attached. The field must not be empty. It may contain at most 100 characters. It must contain a reference code that already exists in the database.

Since Anton can contain units of description without a reference code (classes, recordgroups, for example), it is also possible to specify the `parent` via the `id`. If the `parent` contains an integer, the importer assumes that the `parent_id` is meant. The `id` of a unit of description can be seen from the `permalink`.

### Verzeichnungsstufe (level_of_description)

The field must not be empty. It must contain an existing level of description:

    Archiv
    Bestandsgruppe
    Bestand
    Klasse
    Serie
    Dossier
    Einzelstück

### signatur (identifier)

The field may contain at most 100 characters. Each reference code may occur only once. If no reference code is given, a new, unique reference code is generated by Anton.

### altsignatur (identifier_old)

The field may contain at most 100 characters.

### titel (title)

The field may contain free text.

The title is a **translatable field**. Which language it is written in is decided by the [content language of the import](#content-language-of-the-import) — or, more precisely, by the column designation itself:

| Column | writes to |
|---|---|
| `titel` or `title` | the content language of the run |
| `title_de`, `title_fr`, `title_it`, `title_en` | exactly the language named |

Multilingual titles can therefore be imported: one column per language. Both forms may stand side by side; the column with a language code is the more precise specification and wins, and the inspection page points this out.

The same applies to the **text fields**: `scopecontent` writes into the content language, `scopecontent_fr` specifically into French, without touching the other languages of the same text field.

!!! note "Only configured languages"
    A language code is only recognised if it is present in the archive's `locales` setting (see [language configuration](languages.md)). `title_es` in an archive without Spanish is not a language specification but an unknown column — and the inspection reports it as such.

### Antonevents
Antonevents link the units of description to the actors and the places. They consist of the following fields: `actors, place, date_start, date_start_ca, date_end, date_end_ca, date_event_details`. To import an Antonevent, the EventType now has to be placed before the field name in the column designation, for example for the creation (date range):  `creation_actors, creation_place, creation_date_start, creation_date_start_ca, creation_date_end, creation_date_end_ca, creation_date_event_details`.

There are numerous Antonevents: `creation`, `acquisition`, `accumulation`, `destruction`, `validation`, `migration`, `reproduction`, `publication`, `digitisation`, `ingest`, `reception`, `performance`, `provenance`, `loaned`, `preservation`, `engravation`, `writing`, `coloring`, `edition`, `production`, `other`, `text_author`. 

#### Actors (e.g. creation_actors)

The field may contain at most 500 characters. Giving the period of existence (dates of life) in brackets is not obligatory but is possible. Round brackets must not, however, be used for other purposes. Several actors should be separated with `::`.

Example for two actors: 

```
Müller, Martina (1934-1977) :: Rechtsabteilung
```

The format is not validated in advance! Actors are newly created if they are not found in Anton (the search is by name).

Import setting `create-actors`: actors are newly created if they are not found in Anton.

If an actor is already recorded in Anton, they can also be referenced via their ID (integer).

If an actor was recorded with a GND or another resource, they can also be recognised by that resource, by giving the entry a prefix (in lower case and with a colon, without a space): "gnd:118519522" (the resource does, however, have to be unique within Anton). If the actor does not yet exist, they are newly created from the GND data.

#### Places
The field can contain a place or a places id (integer). Import setting `create-places`: places are newly created if they are not found in Anton. If a place is already recorded in Anton, it can also be referenced via its ID (integer).

Places can contain the following elements:  
- name (separated by "/")  
- city/municipality  
- canton/state (placed in brackets after the municipality)

### Columns with value lists

Several columns only accept values that are defined in the archive:
`verzeichnungsstufe`, `objekttyp`, `schutzfrist`, `status_of_description`,
`detail_of_description` and `vacat`.

They all accept **three forms**, equivalently:

| Form | Example |
|---|---|
| Designation | `Bestand` |
| Internal name | `fonds` |
| ID | `3` |

The ID is the most stable form — it survives a renaming. Where a designation
happens to look like a number, the designation wins.

!!! tip "The permitted values are in the error message"
    If a value is not recognised, the check names not only the problem but
    also the solution:

    > «Schachtel» is not in the value list. Permitted are: Archiv
    > (collection), Bestandsgruppe (recordgroup), Bestand (fonds), Klasse
    > (class), Dossier (file), Einzelstück (item), Serie (series)

    The designation comes first, the internal name in brackets. The lists
    therefore do not have to be looked up beforehand.

#### Looking up all value lists

There is an overview of all value lists under
**Table import → Value lists** (`/valuelists`): for each entry the
designation, internal name and ID, plus the import column to which the list
belongs. A search field filters across all lists at once.

The page is read-only and open to everyone who is allowed to import. The
editable lists under *Admin → Value lists*, by contrast, require the right to
**change** a list — outside the system administration only few people have
that, and only for two of the seventeen lists. Anyone who merely wanted to
look something up previously faced a locked door.

Also on the page: the **location IDs** for the `location_id` column of the
update table.

Keywords, actors and places are *not* there — those are authority records with
their own searchable pages, not lists to be read through.

### objekttyp (object_type)

The field must contain an already existing object type:

```
Akte
Bild
Band
Film
...
```

The list of permitted values depends on the object types that the respective archive has defined.

### umfang_zahl (object_count)

The field must contain an integer. The figure refers to the object type.

### sprache (languages)

The field can contain several languages. The languages must either correspond to the [ISO 639-2/B language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) ("ger" not "deu", "fre" not "fra") or be written exactly as in the existing list. Several languages can be separated with the following characters (comma and semicolon are not possible):

```
    ::
```

### standort (location)

The field must contain a location that is already in use. If a new location is to be used, add it under Admin locations first.

There are two columns, and the name says in each case what belongs in it: **`location_id`** takes only the ID, **`location`** (also: `standort`) takes an ID *or* a designation. If both are present, `location_id` wins.

### formularsatz (formset)

Determines which form set is used for the record — that is, which fields appear in what order. The field is **optional**: if it remains empty, Anton resolves the form set via the level of description. It is only necessary if a record deliberately deviates from that, for example the form set `letter` on items.

As with the location, two columns: **`formset`** (also: `formularsatz`) takes the name *or* the ID, **`formset_id`** only the ID. The names of the available form sets are listed under *Administration → Form sets* — in a standard installation, for example, `fonds`, `class`, `series`, `file`, `item`, `collection`, `recordgroup`, `default`.

The downloaded update table carries the `formset` column and writes the **name**. An empty cell leaves the form set unchanged.

### vacat

Specifies whether the unit of description is a placeholder (a gap in the
numbering for which there are no records).

Internally the column carries term IDs. Accepted are the designation
(`vacat`), the ID (`56` for vacat, `57` for not vacat) and — from older
tables — `1` and `0`.

What is **exported** is the designation: `vacat` for a placeholder,
otherwise an empty cell. Older tables with `56`/`57` can continue to be used
unchanged.


### bilder (media)

The field may contain at most 500 characters. Several file names (assets) can be separated with the following characters:

```
, ; ::
```


Example:

```
erstes_bild.tif::zweites_bild.tif
```

### schutzfrist (period_of_protection)

The field must contain an existing protection period:

```
public
standard
prolonged
```

### private

The field may only contain 0 (no) or 1 (yes). If private contains no value, 0 is set.


### status_of_description

The field may only contain names from the corresponding value list:

```
draft
final
```

### detail_of_description

The field may only contain names from the corresponding value list::

```
minimal
partial
full
```

### Further fields

The further fields are free text fields::

    Neuzugänge (note.accruals)
    Bewertung und Kassation (note.appraisal)
    Informationen des Bearbeiters (note.archivists_notes)
    Ordnung und Klassifikation (note.arrangement)
    Verwaltungsgeschichte / Biographie (note.bioghist)
    Zugangsbedingungen (note.condition_of_access)
    Reproduktionsbestimmungen (note.condition_of_reproduction)
    Bestandsgeschichte (note.custod_hist)
    Kommentar zur Datierung (note.date_comment)
    Umfang (Beschreibung) (note.extent_text)
    Findmittel (note.finding_aids)
    Allgemeine Anmerkungen (note.general_note)
    Archivinterne Bemerkungen (note.internal_note)
    Sprache/Schrift (note.language_script)
    Standort (Detail) (note.location_details)
    Physische Beschaffenheit und technische Anforderungen (note.physical_description)
    Provenienz (note.provenance)
    Publikationen (note.publications)
    Verwandte Verzeichnungseinheiten (note.related_units)
    Kopien/Reproduktionen (note.reproductions)
    Verzeichnungsgrundsätze (note.rules_note)
    Form und Inhalt (note.scopecontent)

## Updating existing records (update via the browser)

!!! warning "Experimental feature"
    The data update is marked as **experimental** (badge in the tab and on the upload page). It changes existing records directly. Anton therefore **automatically creates a backup of the database before every update** (see below); nevertheless, check the result on a sample basis.

Besides creating new records, existing units of description can also be updated directly via the browser. There is a dedicated **«Update»** tab under **Table import** for this (after *Metadata* and *Media*). Upload the table there — update files have their own list, separate from the normal import — and open it with **«Details»**. The file is checked directly in update mode, and the button **«Load as update»** appears.

Because the *Update* tab checks the file exclusively as an update, a pure update table (only `id` plus the columns to be changed, without `parent`) needs no detours: the `parent` column required when creating new records is not demanded here. The regular *Metadata* tab remains unchanged for creating new records.

An update overwrites the fields of the existing records «in place» — **no new records are created** in the process. So that an update remains safe and predictable, three preconditions apply. If one of them is violated, the file is blocked and the reason is displayed on the inspection page:

1. **Every row needs a numeric `id`.** The record to be updated is found via this `id`. The `id` of a unit of description can be seen from the `permalink`.
2. **No `parent` (or `parent_id`) column.** An update must not move records. To change the hierarchy, re-hang the records in Anton in the regular way.
3. **No event columns (Antonevents).** Columns such as `creation_actors`, `creation_date_start` and so on are not permitted in an update, so that no duplicate events arise. Maintain actor and place links in Anton.

What an update writes:

- **Only filled fields are overwritten.** Empty cells leave the existing value untouched — it is therefore possible to update only particular columns (e.g. only `titel` or only `schutzfrist`).
- **Keywords, actors, places, languages and text fields are replaced.** A filled cell is the *complete new list*: anyone who deletes an entry from the cell thereby also dissolves the link on the record. An empty cell changes nothing. (In the normal import — that is, when creating new records — keywords continue to be merely added.)
- **Media** continue to be added.

The same file may be loaded as an update several times; the duplicate block that otherwise applies (same file = same MD5 checksum) does not take effect for updates, since an update is repeatable.

After the start, the progress page shows the update as a **«data update»** (not as an import) and reports at the end how many records were *updated*.

**Automatic backup.** Before an update writes even a single row, Anton creates a dump of the database (the same backup as `anton:backup`, stored under `db_backup/`). The step appears in the progress display as the *backup* phase; the dump's file name is recorded on the run. If the backup cannot be created, **the update is aborted** and nothing is changed. The backup is also enforced when `no-backup` is otherwise set for the tenant — that option is intended for fast bulk *creation*, where a way back is trivial.

Every update run is in the import log — like an import — but with its **own reference code series `UPDATE-{yyyy}-{NNN}`** instead of `IMPORT-{yyyy}-{NNN}`. An update is not an accession — nothing new comes into the archive — and the separate series makes it visible at a glance which entries are updates. The counter runs independently of the import series and is reset for each calendar year.

### Downloading a suitable table

So that an update does not have to be compiled by hand, the current **result list can be downloaded directly as an update table**: in the object list, top right, the Excel symbol next to the print view. The download adopts exactly the filters currently displayed.

The file contains exclusively columns that an update is also allowed to write — `id`, the field columns, languages, the location (`location_id`), keywords/actors/places (as IDs) and the text field columns `note.*`. Deliberately **not** included are `parent` and the event columns, which would block the update. The `identifier` column serves only for orientation: the update finds the records via the `id`, and changes to the reference code have no effect.

!!! tip "Multilingual archives: one title column per language"
    If the archive maintains several content languages, the update table contains one column `title_de`, `title_fr` and so on instead of `titel`. Only in this way is the route out and back in lossless: with a single title column, the language of the run would have to decide where the value goes back to when loading — and a French title would end up in the German field.

    Monolingual archives keep the familiar `titel` column; there is nothing to distinguish there. Older tables with `titel` remain loadable in any case.

!!! tip "Changing locations"
    For the location there are **two columns**, and the name says in each case what belongs in it:

    | Column | Content |
    |---|---|
    | `location_id` | **only the ID** of the location (found under *Admin → Locations*) |
    | `location` | ID **or** designation |

    The downloaded update table uses `location_id`. Anyone who prefers to work with designations renames the column to `location`; there both forms are accepted. A designation has to be written exactly as in the location administration, including capitalisation — the ID is therefore the safe route.

    An **empty cell leaves the location unchanged** — for rearranging, therefore change only the rows that actually move. A location that does not yet exist has to be created under *Admin → Locations* beforehand; otherwise the inspection reports it as unknown and the update does not run.

On clicking, a dialogue opens in which the **columns can be selected**. That is more than convenience: what is not in the file cannot be written by an update either. Anyone who only wants to correct a single title selects `id` and `titel` — then nothing else can come to harm when loading. `id` is always included and cannot be deselected.

!!! warning "The table is a snapshot"
    As little time as possible should pass between download and update. The file contains the state at the time of the download. If it is only loaded days later, its old values overwrite everything that has been changed on those records in the meantime — including changes that other people made deliberately and that are meant to remain. Do not keep a downloaded table and reuse it later, but export it anew for each round of corrections. The fewer columns are selected, the smaller the risk.

    **Anton checks this too.** On export, the time is written into the file (into the document properties, not into a column — it also survives renaming). The inspection page compares it with the modification date of the records concerned and reports concretely which have been edited since: *«3 records have been edited since the table was exported (20.07.2026 08:30) — the update would overwrite these changes: SIG-1, SIG-7, …»*. This does not block the update; there can be good reasons for loading it nonetheless. If no time can be determined (with a table created by hand, for example), the page says that too — a missing notice therefore never automatically means «everything is in order».

The button is reserved for administrators and can be hidden in one's own profile under *Settings*. Next to it is the **complete Excel export** (all fields including `parent` and the event columns) — that one is intended for evaluations and *cannot* be loaded back in as an update.

### Why events are not carried along in an update

Event columns (`creation_actors`, `creation_date_start`, `acquisition_place` …) are **blocked** in an update. The reason lies in the structure: in Anton an event is a tuple of *actor, place, period and type* — one row per actor. Per object and event type, a table can represent only **one combination** of these: one place, one period, one detail text, shared by any number of actors.

Three things follow from this that a table cannot deliver:

- **Several events of the same type.** If an object was worked on in Zurich in 1920 *and* in Bern in 1925, that cannot be expressed in one set of columns. In the complete Excel export, the columns of this type are therefore left out. **An empty event cell therefore means two things:** either no event is recorded — or there are more than this table form can carry. The download dialogue points this out. The update table contains no event columns at all and is not affected by this.
- **Deleting events.** The import only creates events or updates them; there is no way to remove one via the table.
- **Shifting a date.** The matching runs via *type + object + actor + start date*. If the date is changed in the table, a **second** event arises and the existing one remains.

The last two points in particular make events unusable in an update: it would only be possible to add, never to correct — and repeated loading would multiply events. Events are therefore maintained in Anton itself, not via the table.

Also not represented are the free-text dating field (`datierung_text`, in neither direction) and the place address (`<type>_place_address`, only on import and only if the `import_addresses` setting is set).

!!! note "Only via the internal `id`"
    The update in the browser always finds the records via the internal `id`, never via the reference code. An update via the reference code is only possible from the command line (`--update --default-excel-column=identifier`, see below).

## Import from the command line


### Simple import

For the customer (slug) "besenval" and the Excel file "test.xlsx", the import command is:

```bash
php artisan anton:import --env=besenval --file="test.xlsx" --import
```

It is assumed that `test.xlsx` is located in the folder `customers/besenval/metadata_to_import/`. Files to be imported with it (media) must be located in the folder `customers/besenval/assets_to_import/`.

Without the `--import` option, the file is only validated.

### Options

The `anton:import` command offers a number of options that can be useful in specific situations.

| Option|Description|
|:---   | :----------|
|--no-backup | dont backup the database before import |
|--import                  |really start import|
|--locale=                 |content language of the run (e.g. `de`, `fr`). Without a specification, the archive setting applies, otherwise the main language of the archive — see [content language of the import](#content-language-of-the-import)|
|--update                  |update existing records instead of creating new ones; matching by default via the `id`|
|--default-excel-column=   |`id` (default) or `identifier` — determines, with `--update`, what the records are found by|
|--dont-validate           |do not validate the file|
|--skip-parent-validation  |to build hierarchies with one excel file|
|--create-actors           |create new actors if they dont exist|
|--create-keywords         |create new keywords if they dont exist|
|--create-places           |create new places if they dont exist|
|--create-locations        |create new locations if they dont exist|
|--create-object-types     |create new object_type terms if they dont exist|
|--show-rules              |show rules for this file|
|--show-columns            |show the original columns of this file|
|--show-column-mapping     |show columns with mapping|
|--show-possible-columns   |show all possible column names|
|--show-mapping            |show mapping for this file|
|--show-separators         |show separators|
|--from-ead                |import file is a xml-ead file (also use --parent and --dont-validate)|
|--parent=                  |if import file is an ead you need a parent|

Example
```bash
php artisan anton:import customers/kr/ead/test_2-ead.xml --from-ead --dont-validate --create-actors --create-places --create-keywords --parent=1 --env=kr -vv --import --no-backup
```
