## Summary
The table import brings records and their files (media) into Anton from an Excel, ODS or CSV table. The table is uploaded, checked and then imported; the media are uploaded beforehand in the «Media» tab. The help in Anton (Table import → tab «Documentation», `/import/excel/documentation`) shows the same column list as this page, with the values and separators of your own archive.

## Data import `/import`

Every import path starts under **Admin → Import / Export → Data import** (`/import`). The page shows a tile per path:

| Tile | Content |
|---|---|
| **Table import** | Excel, ODS or CSV table with records and media (the subject of this page). Tabs: Metadata, Media, Update, Documentation, Value lists. |
| **SIP eCH-0160** | Submission packages according to eCH-0160, see [SIP ingest](../admin/sip-ingest.md). |
| **Directory import** | Import of a directory structure (ZIP/GZ). |
| **Agate Sipline import** | only where set up: packages from agate, see [agate SIP](../admin/agate-sip.md). |
| **Review list for suggestions**, **Imports**, **DIMAG status** | depending on permission and setup: review suggestions, the [import log](#import-protokoll), the state of the hand-over to DIMAG. |

Old addresses such as `/import/validation`, `/import/ingest`, `/import/documentation` or `/sip/validation` lead to the table import or to this overview.

### Detail view in the inbox

For each waiting SIP in the inbox there is a **details** link. Behind it is an inspection page that reads only the `metadata.json` from the package (without unpacking the media) and shows:

- package check: BagIt (manifest, checksums) or E-ARK (E-ARK validation)
- number of records in the SIP
- NARA object type categories — with a note if the tenant does not know a suitable type for a category
- title of the topmost record

This makes it possible to see before the import whether the SIP makes sense, whether the tenant vocabulary fits, and to discard the SIP if necessary before anything ends up in the database.

### Live progress

All imports run **asynchronously in the background**. After clicking "import", you land on a progress page that updates the current status every few seconds: step (database backup, reading, checking, creating records, taking over media files, done), rows completed, and at the end a link to the **run in the import log**.

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

## Procedure (table import)

1. **Get the template.** The «Documentation» tab offers an empty template and an example table with valid rows from your own archive. Only the first sheet is read; the check names further sheets as not read.
2. **Upload the media.** If the table names files (column `media`), upload them first in the «Media» tab. A missing file is an error in the check.
3. **Upload the table** in the «Metadata» tab (`.xlsx`, `.ods` or `.csv`; Anton cannot read old `.xls` files).
4. **Check.** The eye icon in the list opens the check: recognised and ignored columns, errors, warnings, what would be created and under which settings (see [preview](#preview-what-the-import-would-create)).
5. **Import.** Once the check has passed, «Import» starts the run in the background.

Only the «Update» tab changes existing records (see [below](#updating-existing-records-update-via-the-browser)), never a new import: the check refuses a row with an existing `id`.

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

A column with a language code (`title_fr`) trumps this choice for its own field — see [multilingual columns](#multilingual-columns).

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

Required are `parent` and `level_of_description` for a new record, `id` or `uuid` for an update. The order of the columns does not matter, nor does the case of the header row. A column Anton does not know is not imported; the check names it and suggests a similar name. A text longer than the database holds stops the import with a message instead of being cut silently.

The table is generated from Anton (`anton:import-columns`), from the same rules the import checks by. The separators are the defaults of a new installation; every archive can change them, and the help in Anton shows its own.

<!-- BEGIN generated import columns -->

| Column | Content | Kind | New | Update | Also read as |
|---|---|---|---|---|---|
| `id` | Internal id of the record. Key of an update table; a new import refuses rows with an existing id. | key | – | id or uuid |  |
| `uuid` | Lasting identifier (UUID) of the record, a key of the update table like id. | key | – | id or uuid |  |
| `parent` | The record above: its reference code or its id. It must be in the holdings or further up in the same table; a number alone counts as an id. | reference code or id | required | – |  |
| `identifier` | Reference code, at most 100 characters, unique in the holdings. Left empty, Anton derives it from the record above, except for record groups and classes. | text, unique | yes | yes | `signatur` |
| `identifier_old` | Former reference code, free text. | text | yes | yes | `altsignatur` |
| `title` | Title in the language of the import. | text | yes | yes | `titel` |
| `title_<lang>` | Title in another language of the archive, e.g. title_fr. | text | yes | yes |  |
| `level_of_description` | Level of description from the value list: label, name or id. | value list | required | yes | `verzeichnungsstufe` |
| `object_type` | Object type from the value list. An unknown one is created only with the import setting create-object-types on. | value list | yes | yes | `objekttyp` |
| `object_count` | Number of units. | whole number | yes | yes | `umfang_zahl` |
| `extent_cm` | Extent in running metres, e.g. 2.5 or 2,5; Anton stores it in centimetres. The name misleads: the column takes metres. | number | yes | yes | `extent_lfm`, `extent_rm` |
| `creation_date_start` | Start of creation: year, month or day (1900, 1900-03, 1900-03-12, also 12.03.1900); «ca.» in front counts as 1 in creation_date_start_ca. Empty means no date. Format the cell as text. | date | yes | – | `datum_von` |
| `creation_date_start_ca` | 1 if the start is approximate (ca.); otherwise 0 or empty. | 0 or 1 | yes | – | `datum_von_ca` |
| `creation_date_end` | End of creation, date as in creation_date_start; not before the start (a year counts as the whole year). For a point in time set start and end alike. | date | yes | – | `datum_bis` |
| `creation_date_end_ca` | 1 if the end is approximate (ca.); otherwise 0 or empty. | 0 or 1 | yes | – | `datum_bis_ca` |
| `creation_actors` | Actors of the creation: name, id or authority identifier (gnd:…). Unknown ones are created with the import setting create-actors on, otherwise the check reports them as errors. | actors (separated by `::` `;`) | yes | – | `provenienz_autor` |
| `creation_place` | Places of the creation: name, «name / town», id or geonames:…. Unknown ones are created with create-places on. | places (separated by `::` `;`) | yes | – |  |
| `creation_event_details` | Details of the creation event, free text. | text | yes | – |  |
| `<event>_actors` | Actors of another event; <event> is one of the event types (list in the documentation). | actors (separated by `::` `;`) | yes | – |  |
| `<event>_place` | Places of another event. | places (separated by `::` `;`) | yes | – |  |
| `<event>_date_start` | Start of another event, date as above; with <event>_date_start_ca. | date | yes | – |  |
| `<event>_date_end` | End of another event, date as above; with <event>_date_end_ca. | date | yes | – |  |
| `<event>_event_details` | Details of another event, free text. | text | yes | – |  |
| `note.<name>` | Text field of the form by its name, e.g. note.scopecontent or scopecontent; with a language suffix (_fr) for further languages. | text | yes | yes |  |
| `languages` | Languages of the content as codes of the languages set up in the archive. | language codes (separated by `::`) | yes | yes | `sprache`, `sprachen` |
| `keywords_terms` | Subject keywords: name or id. Unknown ones are created with create-keywords on. | keywords (separated by `::` `,` `;`) | yes | yes | `keywords`, `sachschlagworte`, `schlagworte` |
| `keywords_actors` | Actors as keywords, like creation_actors. | actors (separated by `::` `;`) | yes | yes | `schlagworte_akteure`, `schlagworte_names` |
| `keywords_places` | Places as keywords, like creation_place. | places (separated by `::` `;`) | yes | yes | `schlagworte_orte`, `schlagworte_places` |
| `digitisation_actors` | Who digitised, actors like creation_actors. | actors (separated by `::` `;`) | yes | yes | `digitalisiert_von` |
| `location` | Location: label or id. An unknown one is created only with create-locations on. | location | yes | yes | `standort` |
| `location_id` | Location as id only. | whole number | yes | yes |  |
| `formset` | Form set: name or id. | form set | yes | yes | `formularsatz` |
| `formset_id` | Form set as id only. | whole number | yes | yes |  |
| `period_of_protection` | Protection period from the value list: label, name or id; empty means none. | value list | yes | yes | `schutzfrist` |
| `status_of_description` | Status of description from the value list: label, name or id. | value list | yes | yes | `status_beschreibung` |
| `detail_of_description` | Level of detail from the value list: label, name or id. | value list | yes | yes | `detail_beschreibung` |
| `vacat` | Vacat from the value list: label or id; 0 and 1 from older tables are still understood. | value list | yes | yes | `fehlt` |
| `private` | 1 locks the record and everything below it for the public; 0 or empty does not. | 0 or 1 | yes | yes | `privat` |
| `media` | File names of the media, exactly as uploaded in the «Media» tab. A missing file is an error in the check. | file names (separated by `::` `,` `;`) | yes | yes | `bilder` |
| `private_media` | Like media, but the media are visible only to signed-in accounts with permission. | file names (separated by `::` `,` `;`) | yes | yes | `private_bilder` |
| `loan` | Borrower: «surname, first name» or user id. | user | yes | yes |  |

<!-- END generated import columns -->

### Multilingual columns
The title is a **translatable field**. Which language it is written in is decided by the [content language of the import](#content-language-of-the-import) — or, more precisely, by the column designation itself:

| Column | writes to |
|---|---|
| `titel` or `title` | the content language of the run |
| `title_de`, `title_fr`, `title_it`, `title_en` | exactly the language named |

Multilingual titles can therefore be imported: one column per language. Both forms may stand side by side; the column with a language code is the more precise specification and wins, and the inspection page points this out.

The same applies to the **text fields**: `scopecontent` writes into the content language, `scopecontent_fr` specifically into French, without touching the other languages of the same text field.

!!! note "Only configured languages"
    A language code is only recognised if it is present in the archive's `locales` setting (see [language configuration](languages.md)). `title_es` in an archive without Spanish is not a language specification but an unknown column — and the inspection reports it as such.

### Events

Events link a record with actors, places and a time span. A group of columns belongs to an event type: the type stands in front of the field names `actors`, `place`, `date_start`, `date_start_ca`, `date_end`, `date_end_ca`, `event_details`, for creation thus `creation_actors`, `creation_place`, `creation_date_start`, `creation_date_start_ca`, `creation_date_end`, `creation_date_end_ca`, `creation_event_details`.

Event types: `creation`, `acquisition`, `reproduction`, `digitisation`, `ingest`, `reception`, `performance`, `provenance`, `loaned`, `preservation`, `engravation`, `writing`, `coloring`, `edition`, `production`, `other`, `text_author`. The help in Anton shows the current list.

The date columns take a year, a month or a day: `1900`, `1900-03`, `1900-03-12`, also `12.03.1900`. «ca.» in front of the date (`ca. 1900`) sets the ca. flag like a 1 in the `…_ca` column. The check reports a date it cannot read and an end date before the start date; a year counts as the whole year, so `1923` does not end before `1923-05-15`. An empty field means: no date.

#### Actors (e.g. creation_actors)

An actor is found by name, id or an authority identifier with a prefix, in lower case with a colon and no space: `gnd:118519522`. Life dates in brackets are possible but not needed; round brackets must not be used for anything else. Several actors are separated by the archive's separator (default `::` or `;`):

```
Müller, Martina (1934-1977) :: Legal department
```

Whether an unknown actor is created depends on the import setting `create-actors`: on (the default in the browser), it is created, with a GND identifier from the GND's data; off, the check reports it as an error. From the command line it is created only with `--create-actors`.

#### Places (e.g. creation_place)

A place is found by its name, its id or an identifier like `geonames:2954172`. Whether an unknown place is created depends on the import setting `create-places`.
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

### vacat

Specifies whether the unit of description is a placeholder (a gap in the
numbering for which there are no records).

Internally the column carries term IDs. Accepted are the designation
(`vacat`), the ID (`56` for vacat, `57` for not vacat) and — from older
tables — `1` and `0`.

What is **exported** is the designation: `vacat` for a placeholder,
otherwise an empty cell. Older tables with `56`/`57` can continue to be used
unchanged.

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

Besides creating new records, existing units of description can also be updated directly via the browser. There is a dedicated **«Update»** tab under **Table import** for this (after *Metadata* and *Media*). Upload the table there — update files have their own list, separate from the normal import — and open it with the eye icon. The file is checked directly in update mode, and the button **«Load as update»** appears.

Because the *Update* tab checks the file exclusively as an update, a pure update table (only `id` plus the columns to be changed, without `parent`) needs no detours: the `parent` column required when creating new records is not demanded here. The regular *Metadata* tab remains unchanged for creating new records.

An update overwrites the fields of the existing records «in place» — **no new records are created** in the process. So that an update remains safe and predictable, three preconditions apply. If one of them is violated, the file is blocked and the reason is displayed on the inspection page:

1. **Every row names its record by `id` or `uuid`.** The `id` of a unit of description can be seen from the `permalink`; the update table from the results list carries both.
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

The file contains exclusively columns that an update is also allowed to write — `id`, the field columns, languages, the location (`location_id`), keywords/actors/places (as IDs) and the text field columns `note.*`. Deliberately **not** included are `parent` and the event columns, which would block the update. The `identifier` column is for orientation only: the update finds the records via the `id`, never writes the reference code and leaves a changed one alone. For records without a reference code (classes, record groups) the cell stays empty.

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

!!! note "Via the `id` or the `uuid`"
    The update in the browser finds the records via the internal `id` or, if the table has no `id` column, via the `uuid`, never via the reference code. A row with an unknown `id` or `uuid`, or with two values naming different records, is refused; an update creates nothing. Files the record already carries are not attached again, so the same table can be run again. An update via the reference code is only possible from the command line (`--update --default-excel-column=identifier`, see below).

## Import from the command line


### Simple import

For the customer (slug) "besenval" and the Excel file "test.xlsx", the import command is:

```bash
php artisan anton:import test.xlsx --env=besenval --import
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
|--default-excel-column=   |`id` (default), `uuid` or `identifier` — determines, with `--update`, what the records are found by|
|--no-validation           |do not validate the file|
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
|--from-ead                |import file is an EAD 2002 or EAD3 file (use with --parent)|
|--parent=                  |the record the fonds goes under (id, UUID or signature)|
|--no-ead-validation        |do not check the EAD file against its schema before the import|
|--show-ead                 |show the rows the EAD file makes|
|--no-ead-import            |check and show only, import nothing|

Example
```bash
php artisan anton:import test_2-ead.xml --from-ead --create-actors --create-places --create-keywords --parent=1 --env=kr --import
```

The file lies in `metadata_to_import`, like an Excel table. What Anton's EAD 2002
and EAD3 exports write is read: every ISAD(G) note (as Markdown), access points
as keywords, actors and places, languages, dates, extent, titles in other
languages. An actor already in the archive under the same GND number is taken
rather than created again. The file is checked against its schema before the
import; an invalid file imports nothing. `anton:import-ead <file>` checks a file
and shows its rows without importing.

## Comparing signatures {#signaturenabgleich}

Under **Admin → Import / Export → Signature check** a list of signatures can be compared with the holdings: paste it or upload a table (CSV, Excel, ODS, the first column is read), at most 50,000 signatures. The result is on the page or comes as a CSV to download. What you may not see counts as not found.
