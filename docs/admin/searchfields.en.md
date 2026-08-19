# Search fields

Which fields the **advanced search** offers is configurable per archive. This is
controlled via the settings `searchfields` (internal) and
`search_fields_extern` (public) — the separation makes it possible to give
outsiders fewer search options than the archive itself.

## The complete list

The settings contain a JSON object. Anyone who only wants to add or remove
individual fields is best off starting from the complete list. A given
installation outputs it at the following address:

```
https://<own-installation>/admin/searchfields
```

The desired excerpt can be taken from there. The
[test installation](https://kr.anton.ch/admin/searchfields) can also serve as a
reference.

!!! note "Empty means default"
    If the setting is empty, Anton uses the built-in default. A custom JSON
    replaces it **completely** — it is not a supplement. Anyone who only wants
    to add one field should therefore take the whole list and add it there.

## Relationship to the forms

The search fields are part of the form system: they sit in their own form sets
for the internal and the public search. The label of a search field follows the
same logic as with the [forms](forms.md) — it can be overridden, otherwise the
translation of the field name applies.

## Full text and instant search

The advanced search is only one of three routes. The
[full-text search](../user/search.md) searches a combined index across all
relevant fields and is not controlled via the search fields; the
[instant search](typesense.md) has its own configuration.
