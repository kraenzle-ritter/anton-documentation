# Locations

A location is the physical storage place of the original — stack area, depot,
room, shelf. Locations are records in their own right and are maintained under
**Admin → Locations**.

!!! note "Not for the public"
    The location record itself is visible exclusively to internal users,
    editors and the administration, never to outsiders — where something is kept
    is none of the public's business.

    The **field** «location» on a unit of description is a separate matter: new
    installations are delivered with it removed from the public (external)
    forms, so that «Location: …» does not appear in the public catalogue.
    Existing installations remain unchanged — there the field has to be removed
    from the external forms via the [forms](../admin/forms.md) where required.

## Recording

The location is deliberately kept lean and has only four fields:

| Field | Purpose |
|---|---|
| ID | assigned automatically |
| Abbreviation | short form, e.g. `M2` |
| Name | plain text, e.g. «Stack area 2, shelf C» |
| Description | free text |

No types, no coordinates, no [authority data](authorities.md).

!!! note "Permission"
    Creating, changing and deleting locations requires the `editor` role.
    Internal users (`user_intern`) can view them — unlike actors, places and
    keywords, locations are not public at all.

## Assigning

A unit of description is assigned to a location in the **location** field. It is
in the «allied materials» section and is a selection list.

A unit of description has at most **one** location. Whether the field appears in
the form depends on the [form set](forms.md) — by default, file, series and item
carry it, but not collection and fonds.

!!! tip "Location or location detail?"
    Two fields with similar names should not be confused:

    - **Location** — the choice from the recorded locations, a genuine link. It
      can be evaluated.
    - **Location (detail)** — a text field for supplementary information,
      without a link.

## What is held at a location

The detail page of a location lists — as with actors and places — all units of
description assigned to it.

## Deleting

If units of description are still attached to a location, Anton refuses deletion
and reports this. The assignments have to be released first.

## Reference codes with location

In some archives, the abbreviation of the location forms part of the
[reference code](identifiers.md). Where this is set up, an additional
**location** selection field appears in the «Create new records» window.

!!! note "Archive-specific"
    This function requires a specially programmed way of forming reference
    codes. The standard scheme does not use the location — the selection field
    would have no effect there. With Anton as a Service, k & r knows whether a
    given installation comes with such a scheme.
