# Media gallery

The gallery is an Anton module offering facet-based access to selected media
(images, PDFs, audio, video) — with a PDF.js viewer, video chapters and a
configurable filter layout.

Reachable at `/gallery`.

## Content and title

- `gallery_title` (in the `Home` table, multilingual): custom title of the
  gallery page

## Fonds

- `gallery_fonds`: array of fonds IDs whose media are visible to internal users
- `gallery_fonds_extern`: array of fonds IDs whose media are publicly visible
- `gallery_show_fonds_select`: shows/hides the fonds dropdown

## Filters

- `gallery_show_keywords_select`: shows/hides the keyword dropdown
- `gallery_show_media_type_filter`: shows/hides the media type dropdown
- `gallery_media_types`: which media types can be selected, e.g.
  ```json
  {"image/": "Bilder", "application/pdf": "Dokumente"}
  ```
  This restriction applies even when the dropdown is hidden.
- **Period filter (from / to)** with flexible date entry — configured via
  `gallery_filter_fields` (see the next section).
- **Full-text search** searches object titles and the full text of the media
  files (PDF text layer via `media_texts`, see
  [weighted search](weighted-search.md)). The gallery full-text search works
  with **prefix matching**: a search term such as `alkohol` also
  finds `Alkoholkonsum`, `alkoholisch` and so on. Parts of words in the middle
  are not found (`alkohol` does **not** find `Methylalkohol`). Several terms are
  combined with AND.
- **The PDF viewer adopts the search term**: clicking a PDF hit opens PDF.js
  directly with the current search term prefilled.

### Configurable filter layout

The filter bar layout is configurable per tenant via the setting
`gallery_filter_fields`. This allows the order, width and visibility of the
filters to be controlled. Example:

```php
Setting::setValue('gallery_filter_fields', [
    ['name' => 'search',     'width' => 4, 'visible' => true],
    ['name' => 'fonds',      'width' => 3, 'visible' => true],
    ['name' => 'media_type', 'width' => 2, 'visible' => true],
    ['name' => 'date_from',  'width' => 2, 'visible' => true],
    ['name' => 'date_to',    'width' => 2, 'visible' => true],
    ['name' => 'keywords',   'width' => 3, 'visible' => false],
]);
```

Widths are Bootstrap columns (1–12). The reset button is always visible.

## Modal views

Clicking a medium opens a modal detail view. Per media type:

| Type | Display |
|---|---|
| **Image** | Lightbox with zoom |
| **PDF** | PDF.js viewer with **integrated full-text search** (adopts the current gallery search term as a prefill) |
| **Video** | HTML5 player with **chapter overview** (provided chapter data is stored in `media.custom_properties`) |
| **Audio** | HTML5 player with **audio overlay**: title always visible, icons only on hover |

Tooltips for the media icons are translated into four languages (de/en/fr/it).

## Presentation

- `list_limit_gallery`: number of media per page (default 25)
- `gallery_image_width`: image width in pixels (default 215)
- `gallery_full_images`: which image version the modal links to: `web` (default)
  or `master`

A **masonry layout** ensures optimal image arrangement; images are not cropped.

## Visibility per tenant

- The **internal gallery** (`/gallery`) is visible to logged-in users
- The **public gallery** (`/gallery?extern=1` or directly
  `gallery_fonds_extern`) shows only fonds from `gallery_fonds_extern`. It is
  typically made available to external visitors via a separate domain or a menu
  item.

If a medium carries the flag `dont_show_in_gallery = 1`, it does not appear in
the gallery — even if the corresponding record is public. This flag is
conveniently managed per filter in the
[bulk media list](bulk-media-list.md).

## Performance

- The redundant field `objects.fonds_id` allows fast gallery
  queries without a closure table join
- Gallery facets are held in a **per-tenant cache**
  (`{slug}.gallery.facets.intern` / `…extern`) and invalidated via the
  `Media::updated` hook when `private_media` or `dont_show_in_gallery` changes

## Related topics

- [Bulk media list](bulk-media-list.md) — switching `dont_show_in_gallery` and
  `private_media` on and off per filter
- [Weighted search](weighted-search.md) — full-text indexing
