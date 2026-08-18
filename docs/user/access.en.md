# Access and protection periods

Anton regulates access at three levels: via the person's role, via the setting
of whether the archive is public at all, and via protection periods on the
individual record.

## Is the archive public?

The **public_access** setting determines whether outsiders can see the
catalogue. If it is switched off, the database is only open to logged-in
persons. If it is switched on, the catalogue is public — what individual records
show is then governed by the protection periods.

What each role is allowed to do is set out in
[Getting started](index.md#roles).

## Protection periods

If a unit of description is still subject to a protection period, the record
remains visible, but the images and documents do not.

Anton calculates **one** release year for each record. Decisive is:

1. **The «protected until» field** (release year). This value takes precedence
   and **is inherited down the tree** by all subordinate units.
2. **Otherwise the protection period of the chosen type**, counted from the date
   of creation. Type protection periods apply **only to the record itself** and
   are not inherited.

The **conditions of access / closure period** field selects the type. Three are
provided by default:

| Type | Period |
|---|---|
| public | none — immediately free |
| standard protection period | 30 years |
| extended protection period | 70 years |

The periods are configurable per archive: types can be renamed, added and
changed in duration; «never release» is also possible. Maintenance is reserved
for superusers; with Anton as a Service, k & r is responsible for it.

!!! note "The release year displayed"
    What is displayed is the first year in which the unit is **free** — with
    creation in 1990 and a 30-year period, therefore 2021, not 2020.

## Blocking indefinitely

**Individual media** can be blocked indefinitely in the edit form.

**Whole records** are blocked by the **blocked** field. It affects the record,
all subordinate units and their media; they remain visible only to internal
users, editors and the administration.

## Releasing individual areas

A person with the user role can be granted access to particular branches. To do
so, the IDs of the records are entered in the user administration as a
comma-separated list. An ID always stands for the **entire branch** below it.

## Status of the description

The field is intended for fonds. If a fonds is set to **draft**, it is
accessible only to internal users, editors and the administration.
