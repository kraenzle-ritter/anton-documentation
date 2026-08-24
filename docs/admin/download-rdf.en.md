# RDF export (CIDOC CRM, RiC-O, Memobase)

Anton exports holdings as RDF in **three profiles** — Anton is the only archival
database system in Switzerland that delivers all three in a standards-compliant
way:

- **A+ profile** — CIDOC CRM 7.1.x as the leading model, RiC-O 1.1 selectively
  annotated alongside (for the broad linked data world, Wikidata, Europeana etc.)
- **Pure RiC-O profile** — pure RiC-O 1.1, standards-compliant, without CRM (for
  RiC-O-only consumers such as SPA / Swiss Archival Portal, future ICA portals)
- **Memobase profile** — JSON-LD form according to
  `https://api.memobase.ch/context/*` (for delivery to Memobase via Memoriav
  convention §9)

## The three profiles at a glance

| Profile | Leading model | Format | Purpose |
|---|---|---|---|
| **A+** (standard) | CIDOC CRM 7.1.x + RiC-O 1.1 selectively | Turtle (default), JSON-LD, RDF/XML, N-Triples | LOD publication, broad consumers (Wikidata, Europeana, GND aggregators) |
| **RiC-O (pure)** | Pure RiC-O 1.1, standard namespace | JSON-LD (default), Turtle, RDF/XML, N-Triples | RiC-O-only consumers (SPA, ICA portals, RDA-compliant archives) |
| **Memobase** | RiC-O 1.1 with Memobase `@context` | JSON-LD (default), Turtle (debug) | Delivery to Memobase / Memoriav |

All three profiles speak about the same Anton data and the same holdings
hierarchy; they differ only in the choice of RDF properties, in the IRI scheme
and in the JSON-LD context.

## Access

### 1. UI — `/export/rdf`

In the menu under **Data export → RDF**. Three columns side by side (reduced
responsively to one column below the `md` breakpoint):

- **A+ (CIDOC CRM + RiC-O)** — dropdown with the root object (collection /
  recordgroup / fonds); the `Create RDF` button asynchronously produces a Turtle
  file in `storage/rdf/<identifier>-cidoc.ttl`.
- **RiC-O (pure)** — same dropdown; the `Create RiC-O RDF` button produces
  JSON-LD in `storage/rdf/<identifier>-ric.jsonld`.
- **Memobase** — same dropdown; the `Create Memobase RDF` button produces JSON-LD
  in `storage/rdf/<identifier>-memobase.jsonld`.

The generated files appear in the file table below and can be downloaded or
deleted directly.

### 2. API — `/api/v1/objects/{id}?format=…`

On demand, without file caching. Authentication via api_token as with all other
Anton API calls.

```bash
# A+ (default Turtle)
curl "https://archiv.example/api/objects/42?api_token=TOKEN&format=cidoc-crm"

# A+ as JSON-LD
curl "https://archiv.example/api/objects/42?api_token=TOKEN&format=cidoc-crm&serialization=jsonld"

# A+ as RDF/XML or N-Triples
curl "...&format=cidoc-crm&serialization=rdfxml"
curl "...&format=cidoc-crm&serialization=ntriples"

# Memobase (default JSON-LD)
curl "...&format=memobase"

# Memobase as Turtle (debug)
curl "...&format=memobase&serialization=turtle"

# Pure RiC-O (default JSON-LD)
curl "...&format=ric"

# Pure RiC-O as Turtle / RDF-XML / N-Triples
curl "...&format=ric&serialization=turtle"
curl "...&format=ric&serialization=rdfxml"
curl "...&format=ric&serialization=ntriples"
```

Accepted `format` values for the A+ profile: `cidoc-crm`, `cidoc`, `rdf`
(aliases). For the RiC-O profile: `ric`, `rico` (aliases). Accepted
`serialization` values per profile:

| Profile | turtle | jsonld | rdfxml | ntriples |
|---|---|---|---|---|
| `cidoc-crm` | ✓ (default) | ✓ | ✓ | ✓ |
| `ric` | ✓ | ✓ (default) | ✓ | ✓ |
| `memobase` | ✓ (debug) | ✓ (default) | ✗ HTTP 400 | ✗ HTTP 400 |

### 3. CLI — `anton:export-rdf`

```bash
# whole tenant, A+, Turtle, to stdout
php artisan anton:export-rdf --env=kr > kr.ttl

# one subtree (e.g. fonds with id 42)
php artisan anton:export-rdf --env=kr --root=42 > fonds_42.ttl

# Memobase profile
php artisan anton:export-rdf --env=gf --root=1 --profile=memobase --format=jsonld > gf.jsonld

# pure RiC-O
php artisan anton:export-rdf --env=kr --root=1 --profile=ric --format=jsonld > kr-ric.jsonld

# JSON-LD from the A+ profile
php artisan anton:export-rdf --env=kr --format=jsonld > kr.jsonld
```

Options:

| Option | Default | Meaning |
|---|---|---|
| `--root=<id>` | empty | Restricts the export to the closure table subtree below the AntonObject with this ID. Without `--root=`, all root objects are exported. |
| `--format=<value>` | `turtle` (a-plus), `jsonld` (memobase + ric + bundle) | Serialisation |
| `--profile=<value>` | `a-plus` | `a-plus`, `memobase`, `ric` (alias `rico`) or `a-plus-bundle` |
| `--include-protected` | off | Bypasses the data protection filter: blocked objects, private media and internal text fields come along. **For migration and backup, not for publication.** Takes effect with `a-plus`, `ric` and `a-plus-bundle` — **not** with `memobase` |
| `--include-originals` | off | `a-plus-bundle` only: in addition to the `web`/`thumb` derivatives, packs the **original masters** into the ZIP |
| `--media-layout=<value>` | `flat` | `a-plus-bundle` only: `flat` (anton-static) or `native` (mirrors the media storage, with a conversion subfolder per medium) |

### Migration export {#migrations-export}

Together, the two switches turn the bundle into a **complete migration package**
instead of a publication view:

```bash
php artisan anton:export-rdf --env=<slug> --root=<id> \
    --profile=a-plus-bundle --include-protected --include-originals
```

The ZIP then contains the CIDOC CRM/RiC-O graph **including the blocked
records** and the **original files**. This allows a fonds to be transferred to
another system in a standards-compliant way.

!!! warning "Three limitations"
    - There is **no ready-made tool that reads the package back into Anton**. A
      way back would be feasible with some effort, but it has not been built —
      for backup and restoration, the
      [native round trip](statische-publikation.md#nativer-round-trip-anton-import-format)
      is the intended route.
    - Protection periods are in the graph and can be evaluated automatically,
      but **they have to be enforced in the target system**.
    - A package produced this way contains personal and blocked data and must
      **not be hosted publicly**.

!!! info "CLI only"
    The UI (`/export/rdf`) and the API do **not** pass `--include-protected` and
    `--include-originals` through — there, the filtered publication variant with
    derivatives is always produced. With *Anton as a Service*, k & r produces the
    migration package on request; *on premises*, the operating institution runs
    the command itself.

## What is in the A+ profile

CRM carries the full detail, RiC-O the most important classes plus a skeleton.
In outline:

- **AntonObject** → `crm:E73_Information_Object` (`E22` for physical objects,
  `E33`/`E36`/`E31` depending on `object_type`) + `rico:RecordSet`/`Record`
  depending on the level of description.
- **Hierarchy** → `crm:P46`/`P46i` + `rico:isOrWasIncludedIn`.
- **AntonEvent** → 17 verified event types (creation, acquisition, reception,
  digitisation, …) onto the corresponding CRM classes (`E12_Production`,
  `E8_Acquisition`, `E10_Transfer_of_Custody`, …) plus the Anton term
  redundantly as `crm:P2_has_type`.
- **Notes** typed as `crm:E33_Linguistic_Object` AND additionally as matching
  `rico:scopeAndContent`/`rico:history`/`rico:conditionsOfAccess` etc. on the
  entity (the A+ «loss #2 fix»).
- **Authority links** (GND/VIAF/Wikidata/GeoNames) → `owl:sameAs` /
  `skos:exactMatch` to the external URI.
- **Location** → `crm:P55_has_current_location` +
  `rico:hasOrHadPhysicalLocation` on a dedicated `<location/…>` node
  (`crm:E53_Place` / `rico:PhysicalLocation`). The `locations` table is not the
  same as `places`, hence its own IRI space.
- **Protection period** → `crm:P104_is_subject_to` + `rico:isOrWasRegulatedBy`
  on a `crm:E30_Right` / `rico:Rule` node with the period type
  (`crm:P2_has_type` / `rico:hasOrHadRuleType`), duration as
  `crm:E54_Dimension` and release year as `crm:E52_Time-Span`. In addition, a
  plain-text statement in `rico:conditionsOfAccess` («Closed until 2099»), so
  that the status is readable without calculation. If the date of creation is
  missing, the period is stated without a year — see
  [protection periods](protection-periods.md).
- **Private material is filtered**: `objects.private`, `media.private_media`,
  `actors.private` plus private note types (`internal_note`,
  `archivists_notes`, `comment`).

!!! warning "The export represents periods but does not apply them"
    With `--include-protected` (migration/backup), the package also contains
    blocked records. The periods are then in the graph and can be evaluated
    automatically, but they have to be enforced in the target system.

Full spec: <https://github.com/kraenzle-ritter/anton-cidoc>.

## What is in the RiC-O (pure) profile

Pure RiC-O 1.1, no CIDOC CRM, no Memobase aliases. Standard `rico:` namespace,
multilingual literals as `@language`-tagged values (de/fr/it/en/rm — all locales
are retained).

- **AntonObject** → `rico:Record` (items) or `rico:RecordSet` (all other
  levels).
- **Title** as its own node via `rico:hasOrHadTitle` → `rico:Title` with
  `rico:title` (multilingual).
- **Identifier** as its own node via `rico:hasOrHadIdentifier` →
  `rico:Identifier` (two nodes if `identifier_old` is set).
- **Hierarchy** via `rico:isOrWasIncludedIn`.
- **AntonEvent** → a standalone `rico:Activity` node with
  `rico:hasActivityType` (term URI), `rico:hasParticipant` (record),
  `rico:hasOrHadAgent` (person), `rico:hasOrHadLocation` (place),
  `rico:hasBeginningDate`/`hasEndDate` → separate `rico:Date` nodes with
  `rico:expressedDate` (text) + `rico:normalizedDateValue` (typed
  `xsd:date`/`gYear`).
- **Actor** → `rico:Person`/`Family`/`CorporateBody` with `rico:hasOrHadName` →
  separate `rico:Name` nodes for the main name plus variants and alternative
  names.
- **Place** → `rico:Place` with `rico:hasOrHadName` and `rico:hasOrHadLocation`
  → blank node with `geo:asWKT` (lon/lat corrected).
- **Keywords** as `rico:Concept` + `skos:Concept`, referenced via
  `rico:hasOrHadSubject`.
- **Media** as `rico:Instantiation` with `ebucore:hasMimeType`/`hasHash`/`size`
  always, plus AV EBUcore properties when the `av_*` columns are filled.
- **IRI scheme**: `https://<tenant>.anton.ch/id/<entity-type>/<tenant-slug>-<id>`
  (overridable via `setting('ric_base_iri')` per tenant or
  `config('exporter_rdf.ric.base_iri')` globally).
- **Authority links** as `schema:sameAs` to GND/VIAF/Wikidata/GeoNames.

The main difference from the A+ profile: A+ writes the «RiC-O skeleton»
relations (`isOrWasIncludedIn`, `hasCreator`) alongside the CRM detail; pure
RiC-O delivers genuine `rico:Activity` nodes with all roles — a RiC-O-only
consumer thus sees the events in full.

## What is in the Memobase profile

Leaner and Memobase-specific:

- The class trio **Institution / RecordSet / Record** (Anton tenant ↦
  institution, Anton object level `item` ↦ record, everything else ↦ record
  set).
- IRI scheme
  `https://memobase.ch/(institution|recordSet|record|digital)/<inst-slug>-<id>`
  (configurable via the `memobase_slug` setting; the fallback is the tenant
  slug).
- **Language-suffixed property aliases** instead of `@language` tags:
  `titleDe`/`titleFr`/`titleIt`, `scopeAndContentDe`, `conditionsOfAccessFr`
  etc. **German/French/Italian only** — English and Romansh are dropped
  (English-only values end up as a fallback under the bare alias name).
- A **Memoriav sponsoring notice** `rdau:P60451 → https://www.memoriav.ch/` on
  every record set and record, as soon as
  `setting('memobase_sponsoring_memoriav')` is set to `1` (Memoriav convention
  §9).
- **EBUcore for AV material**: `ebucore:hasMimeType`, `ebucore:hasHash`,
  `ebucore:size` always. When the `av_*` columns in the `media` table are filled
  (see below), additionally `ebucore:duration`, `ebucore:hasCodec`,
  `ebucore:bitRate`, `ebucore:videoTrack`, `ebucore:samplingRate`,
  `ebucore:aspectRatio`.

The JSON-LD context is frozen as a snapshot — Memobase could change it on the
server side; we notice that through a targeted audit, not automatically at
export runtime.

## Per-tenant settings for Memobase

| Setting | Mandatory? | Meaning |
|---|---|---|
| `repository_name` | ✓ | Institution name (becomes `nameDe`) |
| `repository_isil` | recommended | ISIL code (`wdt:P791` on the institution node) |
| `repository_email` | recommended | Contact email (`wdt:P968`) |
| `repository_url` | recommended | Official website (`wdt:P856`) |
| `memobase_slug` | optional | Memobase slug in the IRI (default: tenant slug) |
| `memobase_sponsoring_memoriav` | for Memoriav customers | `1` activates the sponsor notice on every record |

All settings are maintained via `/settings` or by Tinker
(`setting('key', 'value')`).

## AV metadata

Anton carries six AV columns in `media`: `av_duration_seconds`, `av_codec`,
`av_bitrate`, `av_resolution`, `av_sample_rate`, `av_aspect_ratio`.

They are filled automatically:

- **On a new upload**: the listener `MediumIdentifyAndConvert` calls
  `media:extract-av-metadata` for the individual new medium directly after
  PRONOM identification. Inline, ~50 ms, blocks nothing; on an ffprobe error
  only a warning log.
- **For existing holdings**: a one-off backfill run via
  `php artisan media:extract-av-metadata --env=<slug>` (see
  [console commands](console-commands.md#mediaextract-av-metadata)).

For images (`image/*`), only `av_resolution` is filled from width × height — no
codec, no duration. That is enough for the Memobase export to emit the
`ebucore:videoTrack` element with `width`/`height` for every photograph.

In the frontend (object detail view, media tab), a small line with the available
values appears per medium — `1:08`, `1246x1020 (623:510)`, `h264`, `903 kbps`, …
— provided they are filled.

## Per-object buttons in the detail view

In addition to the `/export/rdf` tab (job-based, asynchronous), every object can
be made synchronously downloadable in the detail view via the **download
module** (Antonfield id 1105, formerly `word_download`). The
module renders up to **eight buttons** in the internal detail view — which ones
appear is controlled per format by its own setting:

| Button | Setting | Content |
|---|---|---|
| WORD | `level_of_description_ids_for_word_download` | Word finding aid via `WordController` |
| DIP | `level_of_description_ids_for_dip_download` | OAIS DIP package (BagIt ZIP) |
| OCFL | `level_of_description_ids_for_ocfl_download` | OCFL object (ZIP) |
| OCFL (fonds) | `level_of_description_ids_for_ocfl_subtree_download` | OCFL storage root |
| **EAD** | `level_of_description_ids_for_ead_download` | EAD XML for this object |
| **CIDOC CRM** | `level_of_description_ids_for_cidoc_download` | A+ Turtle for this subtree |
| **RiC-O** | `level_of_description_ids_for_ric_download` | Pure RiC-O JSON-LD |
| **Memobase** | `level_of_description_ids_for_memobase_download` | Memobase JSON-LD |

Every setting is a list of `level_of_description_id` values. The default is `[]`
everywhere — in a fresh installation, the user sees **no** new button until an
admin enters the LoDs via `/settings` (or Tinker).

Example: activating all four new buttons on fonds/series/file/item:

```bash
ddev artisan tinker --env=<slug> --execute='
use Ottosmops\Settings\Setting;
foreach (["ead", "cidoc", "ric", "memobase"] as $k) {
    Setting::setValue("level_of_description_ids_for_".$k."_download", [3, 4, 5, 6]);
}
'
```

The buttons all hang off synchronous inline download routes
(`/objects/{id}/download/{format}` with format `ead|cidoc-crm|ric|memobase`) and
respect the `mayBeShown()` privacy logic of the existing detail view (private
objects are accessible to admins only).

> **Note on the rename:** a backwards-compatibility class
> `WordDownload extends Download` remains in place, so that customer-specific
> form configurations still referring to `word_download` continue to render.
> The alias will be removed eventually — tenants with customer-specific forms
> should switch to `download`.

## What does not end up in the export

Applies to the **standard case** — that is, without `--include-protected`:

- Full text (`objects.full_text`) — not part of the ISAD fields
- Internal text fields (note types `internal_note`, `archivists_notes`,
  `comment`) — filtered identically in the A+ and the Memobase profile
- Private records (`private = 1`) — subtree children are exported, but the
  hierarchy connection to the private parent object is missing

With `--include-protected`, the last two points no longer apply: blocked
records, private media and the internal text fields are then included. The full
text stays out in every case.

## Points of reference

- Spec repo CIDOC CRM + RiC-O: <https://github.com/kraenzle-ritter/anton-cidoc>
- Memobase API: <https://api.memobase.ch> (LOD), <https://memobase.ch>
  (frontend)
- Memoriav convention §9 on the obligation to deliver descriptions — available
  via the institution's respective Memoriav project contract
