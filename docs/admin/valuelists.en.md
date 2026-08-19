# Value lists

Value lists feed the selection fields of the forms — object type, level of
description, actor type, keyword type, conditions of access and others. They can
be consulted in the application under **Help → Value lists**; that is at the same
time the most reliable information about what applies in the **particular**
archive.

## Structure

Every value list is a taxonomy with entries. An entry has a technical **name**,
which stays fixed, and a **label** per language, which is free. When
cataloguing, the label is displayed; what is stored is the entry.

From this follows the most important point in dealing with value lists:

!!! tip "Renaming is harmless, deleting is not"
    The label of an entry can be changed at any time — existing records then
    simply show the new text. If an entry is removed, however, the records that
    use it lose their value.

## Extensible or fixed

Not every value list may be added to. The difference is deliberate:

| Value list | Extensible? |
|---|---|
| Keyword type, place type, object type | yes — each archive according to its own needs |
| Level of description | no — it follows ISAD(G), and Anton calculates with it |
| Actor type | no — person, family, corporate body, department, group, software are anchored in the code |

With the fixed lists, the **labels** are nevertheless freely translatable. An
archive can therefore call «corporate body» «organisation» — it just cannot
extend the list itself.

## Maintenance

Value lists are edited under **Admin → Value lists**. The levels of description
and other system-related lists are reserved for superusers; with Anton as a
Service, k & r is responsible for them.

Which value list feeds a selection field is determined by the
[form](forms.md) — the same field definition can point to different lists in
different forms.

## Protection periods

The conditions of access are a value list with a particularity: periods in years
are attached to their entries. They are therefore maintained separately — see
[protection periods](protection-periods.md).
