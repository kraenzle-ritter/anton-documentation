# Export matrix

An overview of which Anton data is output via which export format — and which can
only be reconstructed from the complete SQL dump.

What each artefact is good for is set out in
[Long-term preservation: overview](preservation.md). The short version: **the
native round trip and the SQL dump are backups, everything else is a publication
or exchange view.**

!!! info "Status"
    This matrix reflects the state of **16 August 2026** (Anton v0.87). It is
    maintained together with the exporters.

## Available formats

| Format | Standard | Scope | Entry point |
|---|---|---|---|
| EAD 2002 | apeEAD (`ead.xsd` + `apeEAD.xsd`) | Object tree from fonds level | Admin → Export |
| EAD3 | `ead3.rng` | Object tree (reduced) | Admin → Export |
| EAD holding guide | apeEAD `type=holdings_guide` | Holdings overview | Admin → Export |
| TEI – authority lists | TEI-P5 `standOff` | Actors / places / keywords (all) | `/api/tei/{actors,places,keywords}` |
| TEI – per object | TEI-P5 | one record | API with `?format=tei` |
| RDF «A+» | CIDOC CRM + RiC-O (dual) | Object tree, all entities | Admin → Export, `anton:export-rdf` |
| RDF RiC | pure RiC-O 1.1 (JSON-LD) | Object tree | Admin → Export |
| RDF Memobase | RiC-O subset (JSON-LD) | Object tree (lossy) | Admin → Export |
| RDF «A+» bundle | CIDOC CRM + RiC-O **+ media files** as a ZIP | Object tree, viewable offline without Anton; with `--include-protected --include-originals` a **migration package** (see below) | Admin → Export, `anton:export-rdf --profile=a-plus-bundle` |
| **Native round trip** | `anton-import-format` v0.4 (JSON) **+ master media** as a ZIP | Object tree, **losslessly re-importable** | `anton:export-native` / `anton:import-native` |
| Dublin Core | OAI-DC | per object (embedded only) | Building block in DIP / OCFL |
| DIP | BagIt | Package: media + metadata (subtree) | «DIP» button on the record |
| OCFL | Oxford Common File Layout | Package: media + metadata (object/subtree) | Button on the record |
| Excel (full) | XLSX | current result list, all fields | Result list → Export |
| Excel (update table) | XLSX | Result list, **only writable fields**, re-importable | Result list → Export → Update |
| Word / PDF | DOCX / PDF | Finding aid per object | Button on the record |
| Paper | HTML print view | Result list (max. 1000) | Result list |
| **SQL dump** | mysqldump (gzip) | **whole tenant database** | Admin → Export |

## Entity matrix

Key: ● full · ◐ partial / embedded · ○ not included

| Entity | EAD2002 | EAD3 | TEI | RDF A+ | RiC | Memobase | DC | DIP/OCFL | Excel full | Excel update | SQL dump |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Unit of description | ● | ◐ | ◐ | ● | ● | ● | ● | ● | ● | ◐ | ● |
| Hierarchy | ● | ● | ○ | ● | ● | ● | ◐ | ● | ◐ | ○ | ● |
| Media (metadata) | ◐ | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ○ | ○ | ● |
| Media (files) | ○ | ○ | ○ | ◐¹ | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| Full text / OCR | ○ | ○ | ○ | ●¹ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Actors (embedded) | ◐ | ◐ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Actors (authority file) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Places (embedded) | ◐ | ○ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Places (authority file) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Keywords | ◐ | ◐ | ● | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Events (graph) | ◐ | ◐ | ◐ | ● | ● | ○ | ○ | ○ | ◐ | ○ | ● |
| Text fields (ISAD fields) | ● | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ● | ● |
| Termselect values | ◐ | ○ | ○ | ● | ○ | ○ | ○ | ◐ | ○ | ○ | ● |
| Pages / editions | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Languages / display date | ● | ◐ | ○ | ● | ● | ○ | ○ | ○ | ◐ | ◐ | ● |
| Location (physical) | ○² | ○² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Protection period (structured) | ○² | ○² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Comments (internal) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ●³ |
| User accounts | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Settings / forms | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| AI cataloguing data | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| File provenance (PRONOM/NARA) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |

² **EAD** outputs conditions of access and location details only as free text —
`<accessrestrict>` and `<originalsloc>` are fed from the text fields of the same
name, not from the «conditions of access / closure period» field or the location
reference. A consumer therefore receives what someone wrote down, not the
evaluable period. `<physloc>` is not implemented.

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

## Well covered

**Units of description** are broadly supported. **EAD2002** is the most complete
format: title, reference code, dating, level, extent, languages and all ISAD(G)
text fields. **RDF A+** types the same thing twice (CIDOC CRM *and* RiC-O),
including multilingual titles.

**Authority data** has exactly one structured, standalone export: the **TEI
authority lists** with all name forms, life dates, coordinates, description,
sources and external links. Two restrictions: only **free** authority records not
bound to objects are output, and actors or places without a type are skipped.
Otherwise authority data appears only embedded in object exports.

## Only in the SQL dump

This data survives **no** format export:

- **User accounts and authentication** — which does not belong in an archival
  export anyway
- **Settings, form definitions, locations, orders, notifications**
- **File provenance** — PRONOM/NARA history and conversion events, that is, the
  entire preservation history of the files
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
| `--include-protected` | bypasses the data protection filter — blocked objects, private media and internal text fields come along. Takes effect with `a-plus`, `ric` and `a-plus-bundle`, **not** with `memobase` |
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
| EAD, TEI, RDF (standard), A+ bundle (standard), DIP, OCFL, Excel, Word/PDF | **yes** |
| A+ bundle with `--include-protected` / `--include-originals` | **no** — the UI and the API do not pass the switches through, CLI only |
| Native round trip (`anton:export-native` / `anton:import-native`) | **no** — a pure CLI command |

With *Anton as a Service*, k & r produces the CLI artefacts on request; *on
premises*, the commands are run by the operating institution.

## Format restrictions in detail

**EAD3** is considerably thinner than EAD2002: no text fields, no places, no
actor descriptors, no media, no language details — only reference code, title,
dating, creators and keywords.

**The EAD holding guide** delivers a flat holdings overview without text fields
per node.

**Memobase RDF** is deliberately lossy: no actors, places, keywords or events —
only institution, objects, instantiations and around eight text field types.

**TEI per object** knows no overall export, no hierarchy and hardly any media.

**DIP and OCFL** carry no PREMIS and no METS; the preservation metadata is
limited to the OCFL inventory. The ZH variant of the DIP contains only media
files, no metadata.

**The two Excel exports pursue opposite purposes.** The *full* export is an
evaluation view: it takes along everything that can be represented flatly and
**cannot** be loaded back in. The *update table* is the opposite — it
deliberately contains only what a data update is allowed to write, and leaves
out hierarchy (`parent`) and events, because these would be blocked on
re-import. The location has been included since v0.86: it is written on update,
and rearranging the stacks is one of the most frequent reasons for a bulk
update. Taking the narrower file therefore does not lose information by
accident; it deliberately limits the scope of effect, and the download dialogue
allows this to be narrowed further.

Since **v0.87**, the update table of a **multilingual** archive carries the title
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
`anton-import-format` v0.4 together with master media, which Anton reads back in.
Anchored via UUIDs (unknown → create new, known → skip, update with `--update`),
hierarchy via the UUID of the superordinate unit, all languages, events, text
fields of **all** carriers including private ones, termselect values, form set
and the reconnection of the media. Before every write operation the whole package
is validated; if it fails, it is rolled back.
