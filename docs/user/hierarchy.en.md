# Archival arrangement and moving records

All units of description hang in a tree structure, the archival arrangement.
Every unit has exactly one parent unit — with the exception of the collections
at the topmost level.

## Levels of description

The levels follow ISAD(G) and determine what may be created below a unit:

| Level | Permitted subordinate units |
|---|---|
| Collection | Recordgroup, Fonds |
| Recordgroup | Recordgroup, Fonds |
| Fonds | Series, Class, File, Item |
| Class | Series, Class, File, Item |
| Series | Series, File, Item |
| File | File, Item |
| Item | Item |

Fonds within fonds are not permitted and are rejected by Anton.

## Navigating the tree

Anton does not present the arrangement as an expandable tree, but in two parts:

- Above every record stands the **path** — the chain of parent units, indented
  in steps and hyperlinked.
- Below the detail view stands the **contents** section with the list of
  subordinate units.

## Moving records

Moving is done in two steps: first the record is earmarked, then the target is
navigated to.

1. On the record to be moved, click the **Move** button. A yellow band appears
   with the note «Record to be moved» together with the reference code and
   title. The ✕ in the band cancels the operation.
2. Navigate to the target record. The band remains visible throughout.
3. In the band, choose the desired position: **before**, **in** or **after**
   this record.

!!! tip "No link visible in the band?"
    The links only appear if the level of description is permitted at the target
    position. A file cannot be moved «in» an item — there the band offers no
    choice. A glance at the table above shows whether the desired position is
    possible at all.

Several records can be moved together; their order is preserved at the target.
Collections at the topmost level cannot be moved. Nor can a record be moved into
its own subtree — Anton rejects this and skips the record concerned.

Moving does **not** change the reference code. It has to be adjusted manually
afterwards where necessary.
