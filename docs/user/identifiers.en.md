# Reference codes

Anton creates reference codes automatically. The standard scheme is described
here; how reference codes are formed can be changed per archive via the
`identifier_generator` setting:

| Value | Behaviour |
|---|---|
| `standard` | The scheme described below |
| `recordgroup_as_base` | Like standard, but with the recordgroup instead of the collection as the base |
| `id_identifier` | Consecutive number |
| `manual_identifiers` | No automatic assignment — the reference code is entered by hand |

Beyond this, an archive-specific way of forming reference codes can be
programmed. The setting is chosen during set-up and cannot be changed in the
admin area.

## Levels of description

|Level of description|Example reference code|Description|May contain|
|:-------------------|:---------------------|:----------|:----------|
| Collection | KRA | Comprehensive unit of an institution. Has no parent unit of description. | Recordgroup, Fonds |
| Recordgroup | not relevant to the reference code | Allows fonds to be ordered logically. | Recordgroup, Fonds |
| Fonds | KRA 3 | Unit of one provenance or one transfer. Fonds are numbered consecutively per collection. | Series, Class, File, Item |
| Class | not relevant to the reference code | Allows files to be ordered logically. | Series, Class, File, Item |
| Series | KRA 3/22 | Behaves like a file as far as reference codes are concerned | Series, File, Item |
| File | KRA 3/22 | Standard unit of description. Records, official registers and the like are described at file level. Files are numbered consecutively per fonds. | File, Item |
| Item | KRA 3/22.1 | Lowest level of description, for photographs or individual documents, for example. | Item |

Recordgroups, classes, series, files and items may contain units of their own
kind (sub-files, for example). Fonds within fonds, by contrast, are not
permitted.

For **collection, recordgroup and class**, Anton assigns no reference code —
these levels are not relevant to the reference code and are labelled by hand
where desired.

## Reference code scheme
The reference code is composed of the collection abbreviation, the fonds number
and the file and item numbers.

```
CollectionAbbreviation FondsNumber/FileNumber.ItemNumber
```

The file number and item number can be nested further. Each additional level is
separated by a full stop.

### Examples
> KRA, 22/1.5     (collection KRA;  fonds 22; series or file 1; sub-file or item 5)

> Test, 1/1       (collection Test; fonds  1; series, file or item 1)

> HDR, 25/4.7.5   (collection HDR;  fonds 25; series or file 4; series or (sub-)file 7; sub-file or item 5)

## Changing reference codes by hand

The automatically assigned reference code can be overwritten — the **reference
code** field is an ordinary input field.

!!! warning "Reference codes are not unique"
    Anton does not enforce unique reference codes. If a reference code that has
    already been assigned is entered, a notice appears on saving with a
    reference to the affected records — but the record is saved nonetheless. The
    notice is deliberately non-blocking, because duplicates do occur in practice.

When a record is [moved](hierarchy.md), the reference code remains unchanged. It
has to be adjusted manually afterwards where necessary.

## Former reference code

A separate **former reference code** field is available for superseded
reference codes and file numbers. It is included in the
[full-text search](search.md).
