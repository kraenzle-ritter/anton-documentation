# Closure periods

The closure periods determine when the material and media of a unit of
description become public; the description stays visible. Only the **Record
withheld** field hides the whole record. How both take effect in cataloguing is
described in [Access, withholding and closure periods](../user/access.md) — this
page deals with the set-up.

## How Anton calculates

Anton determines **one** «Open from» year for each record and keeps it stored.
Catalogue, gallery and search all read the same value — there is no second
calculation elsewhere. Decisive is:

1. The **Open from** field on the record. It takes precedence and **applies
   downwards** to the entire subtree.
2. Otherwise the period of the type chosen in the **Closure period** field,
   counted from the date of creation. Type periods apply
   **only to the record itself** and are not inherited.

!!! note "One source for the period"
    Catalogue, gallery and search calculate the period in exactly one place —
    so they cannot drift apart.

## Records without a date of creation

A type period is counted from the **end** of the period of creation, that is,
from the **creation to** field. If this is missing, the «Open from» year cannot
be determined — the material then stays **closed** until one of the two entries
is supplied (the description stays visible):

* the **creation date to**, or
* an **Open from** directly on the record.

!!! important "Fill in both date fields"
    Anton expects **creation from** and **creation to** to be set. With a single
    date, both fields contain the same value. A filled-in «from» alone is not
    sufficient: what counts for the period is the end of the range, and Anton
    does not guess it from the start — an 80-year period from 1933 ends
    differently from one starting in 1965, and only the archive knows which of
    the two values is meant.

!!! note "Whom this affects"
    Only records for which someone actually chose a period are affected. Without
    a chosen closure period, a record remains free even without a date of
    creation.

    Which records in a given holding are affected can be evaluated on request —
    with Anton as a Service via k & r. It makes sense to supply the missing
    creation dates rather than leaving the material closed.

## Maintaining the types

Every entry of the value list carries:

| Item | Meaning |
|---|---|
| **Duration in years** | Period from the date of creation |
| **public** | no period — immediately free |
| **closed permanently** | material never open, description visible |

Three types are provided by default: **public** (0 years), **standard
closure period** (30 years) and **extended closure period** (70 years).
Types can be renamed, added and changed in duration.

!!! important "Reserved for superusers"
    The editor is located at `/admin/protection-periods` and is reserved for
    superusers — it cannot be reached with the `admin` role. With Anton as a
    Service, k & r is responsible for it.

For archives without permanent closure, «closed permanently» is optional; it
does not have to be configured.

## What the displayed year means

«Open from» is the first year in which the unit is **open**. With creation in
1990 and a 30-year period, therefore 2021, not 2020. Until 0.107 the field was
called «Closure period until»; the value was the first open year even then.

## Field labels

Since 0.108 the standard labels of the fields are **Record withheld**,
**Closure period** and **Open from**, with help texts that state the
difference. If an archive has set its own labels or help texts, the update
leaves them in place. `anton:access-labels` lists them next to the standard;
`anton:access-labels --adopt` takes over the standard if the archive wants it.

## When changing a period

A changed duration affects **all** records of that type — including existing
ones. The «Open from» year is redetermined, and media can therefore become public or
disappear from one moment to the next. Changing the periods is accordingly not a
trifle and should be checked before it lands on a production archive.
