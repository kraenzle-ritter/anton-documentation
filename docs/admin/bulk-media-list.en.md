# Media files — list and bulk management

Under **Admin → Media → List / Bulk** (`/admin/media/list`), administrators find
a paginated list of all media files of the archive with a filter bar, per-row
switches and bulk actions.

The page addresses the original request from the Gosteli archive: setting
several hundred digitised items to "not in gallery" without opening each record
individually in its administration.

## What the list shows

For each media file you see:

- **ID**
- **File name** (`media.file_name`)
- **Mime type** (e.g. `application/pdf`, `image/jpeg`)
- **Collection** (`image`, `application`, `video`, …)
- **Record** — the record the file is attached to (clickable)
- **In gallery** — switch (on/off) for `media.dont_show_in_gallery`
- **Private** — switch (on/off) for `media.private_media`

Sortable by ID, file name, mime, collection, bytes, creation date (click the
column headers).

## Filters

A filter bar above the table:

| Filter | Meaning |
|---|---|
| **File name contains** | Substring search (LIKE), case-insensitive. Suitable for filtering by fonds reference codes in the file name, for example. |
| **Mime type** | All / images / documents / video / audio |
| **Collection** | All / dynamic list from the values actually occurring in the archive |
| **only hidden from gallery** | Shows only records with `dont_show_in_gallery = 1` |
| **only private** | Shows only records with `private_media = 1` |

URL parameters are persisted (bookmarking is possible):
`?search=…&mime=image&col=image`.

## Selection and bulk actions

In the table header row:

- A **checkbox** selects/deselects the *current page*
- An **icon button** next to it (`bi-check2-all`) selects *all records affected
  by the filter* (cap 5000)

As soon as something is selected, a light blue action bar appears at the top:

- **Hide from gallery** — sets `dont_show_in_gallery = 1` for all selected
- **Show in gallery** — sets `dont_show_in_gallery = 0`
- **Set private** — sets `private_media = 1`
- **Set public** — sets `private_media = 0`
- **Clear selection** — empties the selection

Selection works across several pages: you can select page 1, page on, select
again on page 3 and finally apply an action to all of them.

## Per-row switches (optimistic update)

Clicking one of the two switches per row saves immediately (no explicit "save"
button). Cache invalidation for the gallery runs automatically via the
`Media::updated` hook — the gallery facets update by themselves the next time
they are called.

## Permission

Behind the `admin` middleware. Editors do not see the page. More granular
permissions (per fonds, for example) are not provided for — a `MediaPolicy`
could be added later if needed.

## Routes

- `GET /admin/media/list` → Livewire component `Anton\Http\Livewire\Admin\MediaList`

The list is integrated as an additional tab in `/admin/media` ("List / Bulk"
tab, next to Overview, Duplicates, PDF pages).
