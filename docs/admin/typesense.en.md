# Instant search and gallery (Typesense)

Anton can optionally complement the classic full-text search with a
[Typesense](https://typesense.org) backend: a **fast instant search** at
`/search-v2` and a **Typesense-backed media gallery** (Gallery V2). Both can be
**enabled per archive** and run in parallel with the classic search and gallery.

!!! info "Pro feature"
    The Typesense search is a **Pro feature** and is currently reserved for Pro
    customers. It requires a dedicated Typesense server per customer.

!!! note "Optional and with a fallback"
    Without Typesense (the default), Anton runs with the unchanged MySQL search.
    If the Typesense server is unreachable, the application automatically falls
    back to the classic search or the legacy gallery.

## What the instant search offers

- Instant hits while typing, plus autocomplete in the navigation bar
- A mixed, ranked hit list of objects **and** PDF/OCR full text
- Facet sidebar: level of description, object type, media, actors / keywords /
  places, plus a period slider
- Sorting by relevance/date; the entire search state is contained in the URL
  (shareable and bookmarkable)
- Synonyms, «did you mean …?» suggestions and a local list of recent searches

Media gallery V2 offers a filter sidebar (fonds, keywords, media types, period)
with live hit counters, while the tile appearance remains unchanged.

## Prerequisites

- A **Typesense server** for the customer (a dedicated container or Typesense
  Cloud).
- The connection details in the archive's environment file (`.env`):

| Variable | Default | Purpose |
|---|---|---|
| `TYPESENSE_ENABLED` | `false` | Switch (can be overridden by a setting) |
| `TYPESENSE_HOST` | `localhost` | Host of the server |
| `TYPESENSE_PORT` | `8108` | Port |
| `TYPESENSE_PROTOCOL` | `http` | `http` / `https` |
| `TYPESENSE_API_KEY` | — | Master API key |
| `TYPESENSE_CONNECTION_TIMEOUT` | `2` | Timeout in seconds |
| `TYPESENSE_COLLECTION_PREFIX` | `anton_` | Prefix of the collection names |

Every archive gets its own separate search collections
(`{prefix}{slug}_objects`, `_media_texts`, `_gallery`) — no mixing across
tenants.

## Set-up per archive

All commands with `--env=<slug>` (or, in the container, `anenv <slug>`
beforehand):

```bash
php artisan typesense:setup --env=<slug>              # create collections + synonyms
php artisan typesense:index --env=<slug>              # index objects
php artisan typesense:index-media-texts --env=<slug>  # index PDF/OCR full text
php artisan typesense:gallery-index --env=<slug>      # index gallery (for Gallery V2)
php artisan typesense:status --env=<slug>             # check status
```

Then switch the feature on — via `TYPESENSE_ENABLED=true` in the `.env` **or**
via the setting `typesense_enabled` in the admin interface.

!!! tip "Several archives at once"
    `php artisan typesense:reindex-all-tenants` runs setup and indexing across
    all active archives (`--only=`, `--exclude=`, `--dry-run`).

!!! warning "After a schema update"
    If the search schema grows with an update, existing archives have to be set
    up once again: `typesense:setup --fresh --force` followed by the index
    commands.

The time-dependent closure period releases (which PDF contents are publicly
searchable) are recalculated automatically at the turn of the year — no manual
intervention needed.

## Settings: search

All settings are empty by default (= behaviour as delivered) and require **no**
reindexing. Editable in the admin settings interface.

| Setting | Effect |
|---|---|
| `typesense_enabled` | Feature on/off per archive |
| `search_facets` | Which facets appear in what order (`level_of_description`, `object_type`, `has_media`, `year`, `actor_ids`, `keyword_ids`, `place_ids`). Empty = sensible default; facets without values are hidden automatically. |
| `search_default_sort` | Default sorting: `relevance`, `date_desc`, `date_asc` |
| `search_browse_enabled` | Browse list on an empty search (default: on) |
| `search_per_page` | Hits per page (default: 25) |
| `search_weights` | Field weights of the search, e.g. `{"title":5,"full_text":3,"signature":4}` |
| `typesense_synonyms_extra` | Additional synonym groups (takes effect after `typesense:setup`) |

The **hit card** is designed via the form system (form types `search` and
`search_intern`) — with the same editor as list and detail views.

## Settings: Gallery V2

| Setting | Effect |
|---|---|
| `gallery_typesense_enabled` | Switch `/gallery` over to the Typesense gallery (requires `typesense_enabled`). Default: off → classic gallery. |
| `gallery_filter_fields` | Filter layout (fields + column widths) |
| `gallery_media_types` | Selectable media types |
| `gallery_fonds` / `gallery_fonds_extern` | Fonds for the internal and public gallery respectively |
| `gallery_tile_width` | Target tile width in px (optional, default 240) |

For the remaining `gallery_*` settings, see [media gallery](gallery.md).

!!! note "Two routes to the new gallery"
    `/gallery-v2` always renders the new gallery (for testing in parallel);
    `/gallery` only switches to V2 with `gallery_typesense_enabled`.

## Security and visibility

The access restrictions are built into the search: anonymous, logged-in and
internal users each see exactly what they are otherwise allowed to see. The
PDF/media full text respects the **closure period** — embargoed content never
appears in the public search, even if the metadata matches. The gallery
reproduces the visibility rules of the classic gallery exactly.
