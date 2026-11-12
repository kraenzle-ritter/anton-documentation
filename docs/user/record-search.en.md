# Search above the list

The search above the list replaces the page of the advanced search: a click on the magnifier opens every search criterion in one place above the record table. The table below shows the hits and keeps its own filters. The archive switches the search on (`record_search`); without this setting the previous page of the advanced search stays.

## Filters above every list

Above every list of records there are two filters:

| Filter | Effect |
|---|---|
| **Filter list** | Text that must occur in the list |
| **Time range** (from, to) | Records whose period of creation touches this period; records without a date drop out |

Both filters narrow only the list below them, not the rest of the page. How many rows a list shows is no longer chosen above the list but in the [profile](profile.md) under «Items per page».

## Searching

The magnifier opens the search above the table. It has:

- **Search full text:** the search field; it understands the same notation as the [full-text search](search.md) (quotes for phrases, minus to exclude)
- **Archive tree:** narrows the search to part of the archive and covers everything below it; **Whole archive tree** removes the restriction
- **Filters:** the archive's facets, such as level of description, object type or keywords, with the number of hits
- **Time range:** as above the list
- **Advanced search:** single conditions on particular fields; **Add condition** adds another, **Apply** searches

All criteria work together. **Hide search** closes the area; the chosen criteria stay as chips above the table and can be removed there one by one. **New search** resets everything.

Paging on the detail page, the way back to the list and the exports refer to the hits the table shows.

## Full text from the search index

Archives with [Typesense](../admin/typesense.md) can take the full text of this search from the search index (`record_search_index`). The search index tolerates typos and finds hits in the text of media, such as PDFs. Archive tree, filters, period, sort order and pages still come from the database; table, number of hits and exports therefore show the same records.

If the search index finds more than 5000 hits or does not answer, the database searches. Internal accounts (from the role `user_intern`) see beside the search field which one answered: «Full text from the search index» or «Full text from the database».

## Settings

| Setting | Effect | Default |
|---|---|---|
| `record_search` | Search above the list instead of the page of the advanced search | off |
| `record_search_index` | Full text of this search from the search index (requires Typesense) | off |
| `list_filters` | Filters above the lists for staff, in order: `search` (text), `period`; empty = none | both |
| `list_filters_extern` | the same for the public | both |
| `search_facets_extern` | Filters of the search for the public, keys as in `search_facets` | as `search_facets` |

Archives whose search is switched over to Typesense entirely (`search_typesense_enabled`) also take the full text from the search index.
