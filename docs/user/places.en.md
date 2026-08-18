# Places

Places are independent records for geographical information — towns, bodies of
water, buildings, regions. Like [actors](actors.md), they are created once and
then used by any number of units of description. They are found under
**Admin → Places**.

A place is attached to a unit of description in two ways: as a **keyword** (the
place occurs in the content) or via an [event](antonevents.md) (something was
produced, received or performed there). The distinction is the same as with
actors.

## Types

The types follow the feature classes of GeoNames: country/state/region, bodies
of water, parks and areas, city/village, road/railway line, building/farm,
mountain/hill, undersea, and forest/field. Further types can be added per
archive.

## Recording

The form contains type, name, other name forms, variants, abbreviations,
city/municipality, state/canton, country, address, description, sources, comment
and the coordinates.

Places can also be created directly from the object form via the **+** next to
the selection list.

## Geocoordinates

If a place has coordinates, the detail view shows a map. In the place list, an
overview map can also be displayed via **show map**; it is coupled to the list —
panning or zooming the map filters the list to the visible section.

### Via authority data — the easiest way

If a place is [linked](authorities.md) to **GeoNames** or **ortsnamen.ch** in the
edit view, Anton adopts the coordinates automatically.

### By hand

In the **coordinates (lat lng)** field of an **already saved** place, the values
can be entered directly.

!!! warning "Not yet when creating"
    Coordinates entered in the form for a **new** place are not saved. The place
    has to be created first and the coordinates added afterwards via **Edit** —
    or obtained from GeoNames right away.

Anton recognises the format automatically and converts to WGS84:

| Format | Example |
|---|---|
| WGS84 (decimal degrees) | `47.3769 8.5417` |
| Swiss national coordinates LV95 | `2683141 1247637` or `2'683'141 1'247'637` |
| Swiss national coordinates LV03 | `683141 247637` |

Signs, thousands separators (`'` or space), separation by space or comma and
decimal places are each optional.

If coordinates are present, an additional button for deleting them appears in
the edit view.

## Deleting

A place can only be deleted as long as it is **not in use**. Anton refuses
deletion in both of the following cases and reports which one applies:

- the place is involved in an **event**,
- or it is entered as a **descriptor** on a unit of description.

If the aim is to get rid of a duplicate, **merging** is the better route than
deletion: the links then move to the remaining record instead of being lost (see
below).

!!! note "Different up to v0.82.0"
    Until then, a place was deleted without any check, and its links to the
    units of description silently disappeared with it.

## Merging duplicates

Two records for the same place can be merged. Events, authority links and the
links to units of description move to the target record. The text fields
(description, sources, comment) and the name forms of the dissolved place are
adopted as well; its coordinates only move across if the target record does not
yet have any — existing ones are never overwritten. The old record is deleted
afterwards.

!!! note "Reserved for superusers"
    Merging is reserved for superusers; with Anton as a Service, k & r is
    responsible for it. A place cannot be merged with itself.
