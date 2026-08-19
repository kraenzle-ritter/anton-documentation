# Protection periods

The protection periods determine when the media of a unit of description become
public. How they take effect in cataloguing is described in
[Access and protection periods](../user/access.md) — this page deals with the
set-up.

## How Anton calculates

Anton determines **one** release year for each record and keeps it stored.
Catalogue, gallery and search all read the same value — there is no second
calculation elsewhere. Decisive is:

1. The **protected until** field on the record. It takes precedence and **is
   inherited downwards** by the entire subtree.
2. Otherwise the period of the type chosen in the **conditions of access /
   closure period** field, counted from the date of creation. Type periods apply
   **only to the record itself** and are not inherited.

!!! note "Unified since v0.78"
    Before version 0.78, several places calculated the period independently of
    one another, which could lead to discrepancies between catalogue, gallery
    and search. Since then there is exactly one source. After updating, the
    release year is recalculated once for the whole holdings.

## Records without a date of creation

A type period is counted from the **end** of the period of creation, that is,
from the **creation to** field. If this is missing, the release year cannot be
determined — the record then remains **blocked** until one of the two entries is
supplied:

* the **creation date to**, or
* a **protected until** directly on the record.

!!! important "Fill in both date fields"
    Anton expects **creation from** and **creation to** to be set. With a single
    date, both fields contain the same value. A filled-in «from» alone is not
    sufficient: what counts for the period is the end of the range, and Anton
    does not guess it from the start — an 80-year period from 1933 ends
    differently from one starting in 1965, and only the archive knows which of
    the two values is meant.

!!! warning "Changed: such records used to be displayed"
    Until then, Anton calculated from year 0 when the date was missing. A period
    of 80 years therefore expired in the year 81, that is, long ago — the record
    counted as free and was publicly visible even though a period was set. On
    updating, these records disappear from the public view.

    Only records for which someone actually chose a period are affected. Without
    a chosen closure period, a record remains free even without a date of
    creation.

    Which records in a given holding are affected can be evaluated on request —
    with Anton as a Service via k & r. It makes sense to supply the missing
    creation dates rather than leaving the entries blocked.

## Maintaining the types

Every entry of the value list carries:

| Item | Meaning |
|---|---|
| **Duration in years** | Period from the date of creation |
| **public** | no period — immediately free |
| **never release** | permanently blocked |

Three types are provided by default: **public** (0 years), **standard
protection period** (30 years) and **extended protection period** (70 years).
Types can be renamed, added and changed in duration.

!!! important "Reserved for superusers"
    The editor is located at `/admin/protection-periods` and is reserved for
    superusers — it cannot be reached with the `admin` role. With Anton as a
    Service, k & r is responsible for it.

For archives without permanent blocks, «never release» is optional; it does not
have to be configured.

## What the displayed year means

What is displayed is the first year in which the unit is **free**. With creation
in 1990 and a 30-year period, therefore 2021, not 2020.

## When changing a period

A changed duration affects **all** records of that type — including existing
ones. The release year is redetermined, and media can therefore become public or
disappear from one moment to the next. Changing the periods is accordingly not a
trifle and should be checked before it lands on a production archive.
