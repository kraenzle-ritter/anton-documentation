# Export matrix

An overview of which Anton data is output via which export format — and which can
only be reconstructed from the complete SQL dump.

What each artefact is good for is set out in
[Long-term preservation: overview](preservation.md). The short version: **the
native round trip and the SQL dump are backups, everything else is a publication
or exchange view.**

!!! info "Status"
    This matrix reflects the state of **29 October 2026**. It is
    maintained together with the exporters.

## Available formats

| Format | Standard | Scope | Entry point |
|---|---|---|---|
| EAD 2002 | apeEAD (`ead.xsd` + `apeEAD.xsd`) | Object tree from fonds level | Admin → Export |
| EAD3 | `ead3.rng` | Object tree from the fonds | Admin → Export |
| EAD holding guide | apeEAD `type=holdings_guide` | Holdings overview | Admin → Export |
| TEI – authority lists | TEI-P5 `standOff` | Actors / places / keywords (all) | `/api/tei/{actors,places,keywords}` |
| TEI – per object | TEI-P5 | one record | API with `?format=tei` |
| RDF «A+» | CIDOC CRM + RiC-O (dual) | Object tree, all entities | Admin → Export, `anton:export-rdf` |
| RDF RiC | pure RiC-O 1.1 (JSON-LD) | Object tree | Admin → Export |
| RDF Memobase | RiC-O subset (JSON-LD) | Object tree (lossy) | Admin → Export |
| RDF «A+» bundle | CIDOC CRM + RiC-O **+ media files** as a ZIP | Object tree, viewable offline without Anton; with `--include-protected --include-originals` a **migration package** (see below) | Admin → Export, `anton:export-rdf --profile=a-plus-bundle` |
| **Native round trip** | `anton-import-format` v0.5 (JSON) **+ master media** as a ZIP | Object tree, **losslessly re-importable** | `anton:export-native` / `anton:import-native` |
| Dublin Core | OAI-DC | per object (embedded only) | Building block in DIP / OCFL |
| DIP | BagIt | Package: media + metadata (subtree) | «DIP» button on the record |
| E-ARK DIP | E-ARK DIP 2.2.0 (CSIP) | Package of a record and its subtree: *access* = public view with access copies, *full* = everything with masters and originals | «E-ARK DIP» button on the record (access), `anton:export-dip --format=eark [--full]` |
| OCFL | Oxford Common File Layout | Package: media + metadata (object/subtree) | Button on the record |
| Excel (full) | XLSX | current result list, all fields | Result list → Export |
| Excel (update table) | XLSX | Result list, **only writable fields**, re-importable | Result list → Export → Update |
| Word / PDF | DOCX / PDF | Finding aid per object | Button on the record |
| Paper | HTML print view | Result list (max. 1000) | Result list |
| **SQL dump** | mysqldump (gzip) | **whole tenant database** — without sessions, job queues and caches, API and upload tokens empty | Admin → Export |

## Entity matrix

Key: ● full · ◐ partial / embedded · ○ not included

| Entity | EAD2002 | EAD3 | TEI | RDF A+ | RiC | Memobase | DC | DIP/OCFL | Excel full | Excel update | SQL dump |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Unit of description | ● | ● | ◐ | ● | ● | ● | ● | ● | ● | ◐ | ● |
| Hierarchy | ● | ● | ○ | ● | ● | ● | ◐ | ● | ◐ | ○ | ● |
| Media (metadata) | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ○ | ○ | ● |
| Media (files) | ○ | ○ | ○ | ◐¹ | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| Full text / OCR | ○ | ○ | ○ | ●¹ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Actors (embedded) | ● | ● | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Actors (authority file) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Places (embedded) | ◐ | ◐ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Places (authority file) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Keywords | ● | ● | ● | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Events (graph) | ◐ | ◐ | ◐ | ● | ● | ○ | ○ | ○ | ◐ | ○ | ● |
| Text fields (ISAD fields) | ● | ● | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ● | ● |
| Termselect values | ◐ | ○ | ○ | ● | ○ | ○ | ○ | ◐ | ○ | ○ | ● |
| Pages / editions | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Languages / display date | ● | ● | ○ | ● | ● | ○ | ○ | ○ | ◐ | ◐ | ● |
| Location (physical) | ◐² | ◐² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Protection period (structured) | ◐² | ◐² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Comments (internal) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ●³ |
| User accounts | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Settings / forms | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| AI cataloguing data | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| File provenance (PRONOM/NARA) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ◐⁴ | ○ | ○ | ● |

² **EAD 2002 and EAD3** write the closure period as a sentence in `<accessrestrict>`,
with the year from which the material is open, next to the text field
«Conditions of access». apeEAD allows no element of its own that could be
evaluated. The text field «Location (detail)» goes out as `<physloc>`, the
location reference does not.

³ **Comments** are internal working notes and deliberately appear in no
publication format — not even in the native round trip. They are held
exclusively in the SQL dump. This is not a state of implementation but a
decision: they are kept in a separate table that no exporter knows about, so
that they cannot accidentally end up in a publication either. See
[comments](comments.md).

¹ Only in the **A+ bundle**: the pure A+ export delivers bundle-relative media
references, image dimensions, AV duration and OCR full text in the graph; the ZIP
additionally places the derivatives (`thumb`/`web`) alongside — in the standard
case **not the masters**. With `--include-originals` the master files are added,
see [migration export](#migrations-export-das-bundle-als-weg-hinaus).

⁴ **PREMIS 3** per record with media (anton#661): formats (PRONOM), checksums,
kept originals and every event on the media with tool and version. The NARA
risk assessment is not included. Applies to the native round trip too, not to
the ZH variant of the DIP.

## Well covered

**Units of description** are broadly supported. **EAD2002** is the most complete
format: title also in the other languages, reference code, dating with its
comment, level, extent, languages and script, closure period and the ISAD(G)
text fields that the record's form shows to the public. Access points are
written by type (`persname`, `corpname`, `famname`, `subject`, `geogname`) with
the GND number where one is linked. Digital objects go out as the web view and
thumbnail, never as the master. Every file is checked against `ead.xsd` and
`apeEAD.xsd` as it is written, also in the nightly run; a finding is in the log
and in the output of `anton:export`.
Multilingual text fields are not possible: apeEAD allows each text field only
once and has no language attribute on it. The version in the archive's main
language goes out. **RDF A+** types the same thing twice (CIDOC CRM *and* RiC-O),
including multilingual titles.

**Authority data** has exactly one structured, standalone export: the **TEI
authority lists** with all name forms, life dates, coordinates, description,
sources and external links. Two restrictions: only **free** authority records not
bound to objects are output, and actors or places without a type are skipped.
Otherwise authority data appears only embedded in object exports.

**Dates** of actors go out as precisely as they were recorded: a year as a year,
a month as a month. TEI carries a circa date as `cert="medium"`, CIDOC CRM through
the inner bounds (P81), RiC-O in the readable `expressedDate`. The native round
trip and the actors spreadsheet keep it. CIDOC CRM gives the formation and
dissolution of corporate bodies (from Anton v0.103.0).

## Only in the SQL dump

This data survives **no** format export:

- **User accounts and authentication** — which does not belong in an archival
  export anyway
- **Settings, form definitions, locations, orders, notifications**
- **NARA risk assessment** of the files — the rest of the file provenance
  (formats, checksums, events) travels as PREMIS in the DIP, OCFL and native
  round trip since anton#661
- **AI cataloguing data** — profiles, consumption, budgets, audit samples
- **Editions** and **correspondences**
- **The full-text index**
- **The event graph as a relation** — events appear only flattened (Excel) or
  implicitly (EAD, RDF)

## Migration export: the bundle as a way out {#migrations-export-das-bundle-als-weg-hinaus}

The matrix above describes the **standard case**. The RDF export knows two
switches that lift it out of the publication corner:

| Switch | Effect |
|---|---|
| `--include-protected` | bypasses the data protection filter — withheld records, internal-only media and internal text fields come along. Takes effect with `a-plus`, `ric` and `a-plus-bundle`, **not** with `memobase` |
| `--include-originals` | `a-plus-bundle` only: packs the **original masters** into the ZIP, not just `web`/`thumb` |

```bash
php artisan anton:export-rdf --env=<slug> --root=<id> \
    --profile=a-plus-bundle --include-protected --include-originals
```

The result is a standards-compliant package of CIDOC CRM/RiC-O graph, blocked
data and original files — suitable for transferring a fonds into **another
system**. For the way back into Anton there is no ready-made tool — the native
round trip remains responsible for that. And it contains personal data: do not
host it publicly.

## Who can trigger which artefact

| Artefact | Self-service in the interface |
|---|---|
| SQL dump | **yes** — Admin → Export |
| EAD, TEI, RDF (standard), A+ bundle (standard), DIP, E-ARK DIP (access), OCFL, Excel, Word/PDF | **yes** |
| E-ARK DIP full (`--full`) | **no** — CLI only |
| A+ bundle with `--include-protected` / `--include-originals` | **no** — the UI and the API do not pass the switches through, CLI only |
| Native round trip (`anton:export-native` / `anton:import-native`) | **no** — a pure CLI command |

With *Anton as a Service*, k & r produces the CLI artefacts on request; *on
premises*, the commands are run by the operating institution.

## Format restrictions in detail

**EAD3** contains the same as EAD2002, written in EAD3 and checked against
`ead3.rng` as it is written: extent and dating structured, names with
`@identifier` and `@source` of the authority record, titles in the other
languages with `@lang`. Text fields go out in the main language, as in EAD2002.
The validation page checks EAD3 files too.

**The EAD holding guide** delivers a flat holdings overview without text fields
per node.

**Memobase RDF** is deliberately lossy: no actors, places, keywords or events —
only institution, objects, instantiations and around eight text field types.

**TEI per object** knows no overall export, no hierarchy and hardly any media.

**E-ARK DIP** (anton#697) comes in two scopes. *Access* is a publication view: what a guest may see, whoever exports — locked records and drafts are left out with their subtree, records under a protection period keep their description but not their media, private media are left out. The media are access copies (`web`) in representation `access`, described in EAD3 or EAD 2002 (setting `eark_dip_ead`), optionally also RiC-O and CIDOC CRM as Turtle (`eark_dip_rdf`). PREMIS names each representation's function and each file's source, without events and without persons. *Full* (`--full`, CLI only) is a hand-over like DIP and OCFL: every record, masters in `master`, kept originals in `original`, plus the native format (`anton-native`), PREMIS per record and the Word finding aid. Every package is validated before it is delivered; an invalid one is not delivered. See [DIP download](download-dip.md#e-ark-dip).

**DIP, OCFL and native round trip** carry a **PREMIS 3 file** per record with media since anton#661 (DIP: `data/meta/<record>.premis.xml`, OCFL: `metadata/premis.xml`, native: `premis/<record>.xml`). It lists the files and kept originals with MD5/SHA-512, size and PRONOM format, every event on the media (virus check, integrity and format checks, format identification, format rules, transfer to the cloud, ingest with the person who acted) and the tools involved with their version. A format rule at ingest is a *normalization* and names as implementer whoever added the medium; `media:migrate` is a *migration* and names the account that started the run, as `<account>@cli`. A file a format rule replaced without keeping it is an object of its own without a file, with the checksums, size and format the rule recorded before converting; the medium refers to it as its source (anton#751). There is no METS. The ZH variant of the DIP contains only media files, no metadata and no PREMIS.

**The two Excel exports pursue opposite purposes.** The *full* export is an
evaluation view: it takes along everything that can be represented flatly and
**cannot** be loaded back in. The *update table* is the opposite — it
deliberately contains only what a data update is allowed to write, and leaves
out hierarchy (`parent`) and events, because these would be blocked on
re-import. The location is included: it is written on update,
and rearranging the stacks is one of the most frequent reasons for a bulk
update. Taking the narrower file therefore does not lose information by
accident; it deliberately limits the scope of effect, and the download dialogue
allows this to be narrowed further.

The update table of a **multilingual** archive carries the title
in one column per content language (`title_de`, `title_fr` …) instead of a single
one. This makes the round trip lossless in the multilingual case too: with one
column, the language of the run would have to decide on re-import where the value
belongs, and a French title would end up in the German field. Monolingual
archives keep the bare `titel` column. The *full* export continues to output the
title monolingually — it is a reading view, not a way back.

Neither is a **backup**: even the full Excel export carries neither media nor
authority files nor forms. For a way back, the native round trip or the SQL dump
serve (see below).

## RDF A+ and the native round trip are two products

The **A+ graph is a discovery view, not a backup.** An Anton tenant cannot be
reconstructed from the bundle alone: the UUIDs, the form set, the raw values and
the protection periods are missing.

For the lossless route there is the **native round trip**
(`anton:export-native` → `anton:import-native`): a package in the
`anton-import-format` v0.5 together with master media, which Anton reads back in.
Anchored via UUIDs (unknown → create new, known → skip, update with `--update`),
hierarchy via the UUID of the superordinate unit, all languages, events, text
fields of **all** carriers including private ones, termselect values, form set
and the reconnection of the media. Before every write operation the whole package
is validated; if it fails, it is rolled back.

Actors, places and keywords carry a portable UUID too — a re-import anchors them
to it instead of merging authority records that happen to share a name.

!!! warning "Comments are lost in the round trip"
    «Lossless» refers to the description. Internal
    [comments](comments.md) are excluded: they are kept in a table of their own
    that no exporter knows — not even the native one — so that they cannot end
    up in a publication by accident. An export-import cycle leaves them behind.

    Anyone who has to take them along needs the **SQL dump**. That is the backup
    which really does contain everything.

Not included, and therefore still the SQL dump: user accounts, settings, form
definitions and the AI data.

## Privacy filter

RDF, TEI and EAD filter out withheld records and actors, internal-only media as
well as internal text field types (internal archival remarks, cataloguer's information, comment).

**EAD** always shows the public view, whoever generates the file: no locked
descriptions or drafts, with everything below them, and no locked actors, not
even as creators. Anton serves the file of a public fonds to anybody through
OAI-PMH. Up to v0.100.0 it contained what the person generating it could see,
and always the locked creators (anton#616).

!!! warning "Plain flag logic"
    The filter evaluates the `private` flag — it is **not a role check**. Apart
    from the file name, downloading a generated RDF file checks no further
    permissions.

## The essence

**Descriptive metadata** is excellently covered by open standards and can be
packaged. **Authority data** has exactly one export of its own (TEI). **File provenance**
travels as PREMIS in the DIP, OCFL and native round trip. **The event graph,
users, configuration and AI data** have no standards-based export and can only
be secured through the complete SQL dump.
