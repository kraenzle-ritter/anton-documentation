# Access, withholding and closure periods

Anton regulates access at three levels: via the person's role, via the setting
of whether the archive is public at all, and on the individual record via two
separate things — **withholding** the record and the **closure period**.

## Is the archive public?

The **public_access** setting determines whether outsiders can see the
catalogue. If it is switched off, the database is only open to logged-in
persons. If it is switched on, the catalogue is public — what individual records
show is then governed by withholding and closure periods.

What each role is allowed to do is set out in
[Getting started](index.md#roles).

## Withholding and closure periods

> The **closure period** protects the material; the record stays findable.
> **Withholding** hides the whole record, its description included.

| | Record withheld | Closure period |
|---|---|---|
| Description (title, dates, cataloguing) | hidden | visible and searchable |
| Images and documents | hidden | only from «Open from» |
| Subordinate units | always withheld too | type: no; «Open from» set by hand: yes |
| Limited in time | no | yes |

Both stay visible to internal users, editors and the administration. An archive
may have renamed the fields; since Anton 0.108 the standard names are the ones
used here.

## Record withheld

The **Record withheld** field hides the whole record from the public:
description, media and all subordinate units. It appears neither in the search
nor through interfaces (API, OAI, sitemap). Withholding is always inherited
downwards — below a withheld record there is no public one.

## Closure period

The closure period protects only the material and digital copies: if a unit of
description is still subject to a closure period, the record remains visible
and searchable, but the images and documents do not.

Anton calculates for each record **one** year from which it is open. Decisive
is:

1. **The «Open from» field.** This value takes precedence and **applies down
   the tree** to all subordinate units.
2. **Otherwise the closure period of the chosen type**, counted from the date
   of creation. Type closure periods apply **only to the record itself** and
   are not inherited.

The **Closure period** field selects the type. Three are provided by default:

| Type | Period |
|---|---|
| public | none — open at once |
| standard closure period | 30 years |
| extended closure period | 70 years |

The periods are configurable per archive: types can be renamed, added and
changed in duration; «closed permanently» is also possible. Maintenance is
reserved for superusers; with Anton as a Service, k & r is responsible for it.

!!! note "«Open from» is the first open year"
    With creation in 1990 and a 30-year period it reads 2021: from 2021 the
    material is open. Until 0.107 the field was called «Closure period until» —
    the value has always been the first open year.

## Single media: internal only

**Single media** can be set to **internal only** in the edit form. This holds
without a time limit and only for that medium; the record and its other media
stay as they are.

## Releasing individual areas

A person with the user role can be granted access to particular branches. To do
so, the IDs of the records are entered in the user administration as a
comma-separated list. An ID always stands for the **entire branch** below it.

## Status of the description

The field is intended for fonds. If a fonds is set to **draft**, it is
accessible only to internal users, editors and the administration.
