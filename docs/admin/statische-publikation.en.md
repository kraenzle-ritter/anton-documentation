# Static publication and round trip

Anton knows two **self-contained** export packages that pack an entire
(sub-)fonds including media into *one* ZIP file — without a running Anton
instance being needed for display or restoration:

- **A+ static bundle** — the CIDOC CRM/RiC-O graph plus media derivatives,
  **safe for public use** and hostable offline. Intended as a *publication*.
- **Native round trip** — Anton's own format plus master media, **lossless and
  re-importable**. Intended as *backup / migration*.

Guiding idea: **Anton is the editor, the package is the delivery.** Small
archives can maintain their holdings with it and publish the result free of
charge as a static website (GitHub Pages, for example) — without a server,
without a database, without running costs.

!!! info "In brief: which package for what?"
    - **Show publicly / deliver to portals** → **A+ static bundle** (private
      material is filtered out, standards-compliant).
    - **Back up / migrate to another Anton instance** → **native round trip**
      (lossless, but contains private data → do *not* host publicly).

---

## A+ static bundle (CIDOC CRM + RiC-O)

A ZIP with the serialised A+ graph as `data.jsonld` at the root, the copied
media derivatives (`thumb`/`web`) under `media/{id}/…` and a `manifest.json`
with a transparency overview. The media references in the graph are
**bundle-relative paths** (`media/123/web.jpg`), so that the package renders
anywhere — from a hard disk, from GitHub Pages, from a subdirectory.

```
bundle.zip
├── data.jsonld          ← CIDOC/RiC-O graph (JSON-LD)
├── manifest.json        ← format, media count, transparency summary
└── media/{id}/…         ← thumb/web derivatives
```

**Producing it:**

```bash
# CLI — writes <identifier>-bundle.zip to storage/rdf/
php artisan anton:export-rdf --env=<slug> --root=<id> --profile=a-plus-bundle
```

Or in the UI under **Data export → RDF**, column *«A+ bundle (static)»*. The
finished ZIP appears in the file list for download.

**Safe for public use:** the same data protection filter applies as with the RDF
export — private objects, `private_media` and private note types
(`internal_note`, `archivists_notes`, `comment`) are left out. The
`manifest.json` transparently counts how much was filtered and which conversions
were missing, so that the package can be checked before publication.

!!! warning "Unless the filter is switched off"
    With `--include-protected` the blocked records come along; with
    `--include-originals` the master files as well. Both are intended for
    **migration**, not for publication — a package produced that way does not
    belong on GitHub Pages. See
    [migration export](download-rdf.md#migrations-export). The UI does not pass
    the switches through; via the interface, the publicly safe variant is always
    produced.

For details on the A+ graph itself, see [RDF export](download-rdf.md).

---

## Native round trip (anton-import-format) {#nativer-round-trip-anton-import-format}

A ZIP with the holdings as an **`anton-import-format` document**
(`metadata.json`) plus the **master media files**. It is the lossless
counterpart to the (deliberately lossy) CIDOC package: what Anton exports here,
Anton can **read back in**.

```
package.zip
├── metadata.json        ← anton-import-format v0.4 (JSON)
└── media/{id}/…         ← master files (originals)
```

**Producing and restoring:**

```bash
# export a subtree
php artisan anton:export-native --env=<slug> --root=<id> --out=/path/package.zip

# read it back in (into the same or a different Anton instance)
php artisan anton:import-native /path/package.zip --env=<targetslug>

# overwrite existing records instead of skipping them
php artisan anton:import-native /path/package.zip --env=<targetslug> --update
```

**What it carries losslessly:** objects (including `uuid`, `formset_id`, all
language variants of title/label), hierarchy (via the parent `uuid`), events,
descriptors, **notes of all records** (including private ones, biographies),
termselect values and the media identity. It applies **no data protection
filter** — it is a backup, not a publication.

**Identity via `uuid` (portable).** Objects *and* authority data
(Actor/Place/Keyword) carry a stable, instance-independent `uuid`. On re-import
they are re-anchored via it:

- unknown `uuid` → new record,
- known `uuid` → skipped (updated with `--update`),
- the same `uuid` in two holdings → *one* record (no duplicates).

This makes the round trip work **between different Anton instances** as well: a
fonds from instance A ends up in instance B under its original `uuid`s; a later
repeat import updates the same records instead of duplicating them.

!!! warning "Contains private data"
    The native export is a backup and deliberately carries **private objects,
    private media and internal notes** as well. It is **not** intended for public
    hosting — the A+ static bundle exists for that.

The underlying format is maintained as a separate, versioned package:
[`kraenzle-ritter/anton-import-format`](https://github.com/kraenzle-ritter/anton-import-format).
The Excel import and the agate SIP pipeline consume the same format.

---

## Concrete comparison: anton format ↔ CIDOC

Both packages describe the same holdings and pack the same media — but with
opposite purposes. One is **standards interop** (broadly consumable,
semantically rich, lossy), the other is **Anton-native fidelity** (lossless,
re-importable, simple).

| | **anton format** (native round trip) | **CIDOC A+ bundle** |
|---|---|---|
| **Purpose** | Backup · restore · migration between Anton instances | Publication · interop · static display |
| **Basis** | `anton-import-format` v0.4 (JSON) | CIDOC CRM 7.1 + RiC-O 1.1 (JSON-LD) |
| **Standardised** | No (Anton's own schema) | Yes (international ontologies) |
| **Lossless** | **Yes** — `uuid`, `formset_id`, all locales, all notes, termselect, raw values | No — discovery view; no `formset_id`, no raw values |
| **Re-importable** | **Yes** (`anton:import-native`, uuid-anchored) | No |
| **Privacy** | Contains private material (it is a backup!) → **do not host publicly** | Private material filtered → **intended for public hosting**; no longer so with `--include-protected` |
| **Structure** | Flat and close to Anton: `entries[]` with `title`/`identifier`/`events`/`notes`/`files` | Graph of CRM/RiC nodes and properties |
| **Rendering in a JS viewer** | **Simple** (directly readable/mappable) | **More laborious** (ontology traversal needed) |
| **Media** | Master files (originals) | `thumb`/`web` derivatives; with `--include-originals` the masters as well |
| **Portability** | `uuid` identity, also cross-tenant | bundle-relative locators, offline |
| **Target group** | Anton operators | Aggregators (Europeana, Memobase) · a custom static viewer |
| **Command** | `anton:export-native` / `anton:import-native` | `anton:export-rdf --profile=a-plus-bundle` |

**The core message:** CIDOC is the *standardised, publicly safe* view — ideal
for handing data to portals or putting it online in a standards-compliant way,
but its JSON-LD is more laborious to process for a home-built viewer. The anton
format is *simple to render and lossless*, but carries private data and is not a
recognised standard.

---

## Vision: publishing small archives statically and free of charge

The actual purpose of these packages: **small projects should be able to use
Anton as an editor and publish their holdings as a static website** — without a
server, without a database, virtually free of charge (GitHub Pages, Netlify, a
USB stick).

The planned next step is a **small, standalone static viewer application** (a
separate project): a pure browser client that loads an exported package and
presents the holdings as a navigable website — tree, detail pages, media,
full-text search on the client side.

**Which format should this viewer consume?** The two packages above mark the
ends of a spectrum:

- **A+ bundle (CIDOC)** — publicly safe and standards-compliant, but the graph is
  unwieldy to render.
- **anton format** — trivial to render, but it contains private data and is not a
  standard.

For a *public* viewer, one wants both at once: **simple to render *and* filtered
for data protection**. That suggests a third, lean **publication export** for the
viewer project — flat, readable JSON like the anton format, but with the same
data protection filter as the A+ bundle and only display derivatives
(`thumb`/`web`). It would combine the simplicity of the native builder with the
privacy filter of the publication.

Until this dedicated publication export exists, the **A+ static bundle is the
right public basis** — it is already hostable offline and privacy-safe; the
viewer would «only» have to read the JSON-LD graph.

!!! note "Status"
    The A+ static bundle and the native round trip are implemented and tested.
    The dedicated, lean publication export and the static viewer application are
    envisaged as a **separate follow-up project**.
