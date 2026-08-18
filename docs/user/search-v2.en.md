# Instant search

The instant search (`/search-v2`) is an as-you-type search: hits appear while
typing, can be filtered via a sidebar and are presented as a mixed list of
objects **and** PDF full text, sorted by relevance.

!!! info "Pro feature"
    The instant search is available to Pro customers and runs in parallel with
    the classic [full-text search](search.md). What is searched and how the
    search behaves in principle (word beginnings, AND combination, internal
    view) is described there and applies here as well.

## Searching

Enter the search term at the top — the hit list updates immediately. Every hit
shows:

- a type marker (**object** with object type, or **PDF** for a full-text hit in
  a document),
- the level of description and the path (fonds → series → …),
- a highlighted text excerpt of the passage found,
- a preview image, if available.

If the input is empty, a browse list of the most recent records is shown (where
activated), so that the page is never empty.

## Filtering (sidebar)

The sidebar offers facets with hit counts. Depending on the archive, available
are:

- **level of description**, **object type**, **media** (with/without)
- **actors**, **keywords**, **places** — with a search field for quick narrowing
  where there are many values
- **period** — a slider with two handles (from/to); the values can also be typed
  in directly

Several values within one facet act as «or», different facets as «and».
**Reset filters** clears the selection.

!!! note "Only visible facets"
    Facets for which an archive holds no values (no places, for example) are
    hidden automatically.

## Sorting

Via the sort menu: **relevance** (default), **date (newest first)** or **date
(oldest first)**.

## Sharing and linking

The complete search state is in the address bar — search term, filters, period
and sorting. The URL can be **saved or shared** and restores the search
including its filters.

## Further aids

- **Autocomplete** in the navigation bar suggests hits while typing.
- **«Did you mean …?»** offers a corrected spelling when there are few or no
  hits.
- The **recent searches** are offered locally in the browser.

## Visibility

As in the classic search, you only see what you are allowed to see. Blocked
(embargoed) PDF contents do not appear in the public search, even if the
descriptive data matches the search term.
