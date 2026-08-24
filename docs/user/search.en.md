# Full-text search

The full-text search searches all relevant fields of the archival records at once: titles, reference codes, text fields, linked actors, places and keywords — and also the text recognised by OCR from PDFs and images.

## What is searched

For each archival object, the following are combined for the search:

- **Titles** of the object and of all superordinate units (fonds → series → file → document)
- **Reference codes** (current and former) as well as the internal ID
- **Designations** of the level of description, the object type and the location
- **Datings**
- **Linked keywords** in all available language variants
- **Linked places**
- **Linked actors** (only those publicly visible)
- **Text fields** that are visible in the external form
- **OCR text** from media (PDFs, images)

!!! note "Extended view for internal editors"
    For logged-in users from the `user_intern` role upwards, the following are searched in addition:

    - private actors
    - all text fields (including those visible internally only)
    - objects marked as private

## Search behaviour

### Word beginnings are recognised automatically

Wildcards (`*`) are not necessary — the search automatically finds all words that **begin** with the search term entered.

| Search | Finds |
|---|---|
| `alkohol` | «Alkohol», «Alkoholverbot», «alkoholisch» |
| `müller` | «Müller», «Müller-Weber», «Müllers» |

!!! warning "But not in the middle of a word"
    `kohol` does **not** find «Alkohol». The search only takes effect at the beginning of a word.

### Several words are combined with AND

| Search | Finds |
|---|---|
| `alkohol verbot` | Records in which **both** terms occur — they may be any distance apart |

### Quotation marks for exact phrases

| Search | Finds |
|---|---|
| `"rudolf leder"` | Only records in which this sequence of words occurs **exactly like this** |
| `#rudolf leder#` | Identical — `#` is an alternative notation for `"` |

With a phrase, word beginnings are **not** searched automatically — the phrase has to occur exactly.

!!! warning "Very short words are ignored in phrases too"
    Words of fewer than 3 characters and some English stop words (`the`, `for`, `and`) drop out of the comparison even within quotation marks. A phrase such as `"AG Reinach"` therefore effectively matches only «Reinach».

!!! note "Phrases in the document text"
    If the archive keeps the full text **condensed** (setting
    `optimize_fulltext`), the index holds only the first occurrence of each word
    — phrases are then only findable to a limited extent in the text of PDFs.
    Search for single words is unaffected. Whether this applies is known to the
    administration; see [search fields](../admin/searchfields.md).

### Terms with a hyphen

Terms with a hyphen (e.g. `Arp-Hagenbach`) are automatically treated like a phrase: the search looks for both parts directly next to each other.

## What does not work

- **Terms of fewer than 3 characters** are ignored (`ag`, `zb`).
- **Very frequent short words** such as «und», «der», «die» are excluded from the database's search index (so-called stop words).
- **Searching in the middle of a word** is not possible (see above).

## Distinction from the weighted search

The full-text search searches **archival objects**. The [weighted search](weighted-search.md) is a different function and concerns the list views of **actors, places and keywords** — there, hits are sorted by relevance.
