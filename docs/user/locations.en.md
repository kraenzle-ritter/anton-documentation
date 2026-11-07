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

No coordinates, no [authority data](authorities.md). Where a location stands in the magazine, its level, the place above it and its capacity, is kept in the [Magazine](#magazin) box on its page.

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

## Magazine {#magazin}

Locations can be arranged into a magazine: room, shelf, segment, compartment and box, or however the archive divides its magazine. An archive that does not arrange its locations notices nothing; a flat list stays a flat list.

**Defining levels.** Under **Admin → Magazine levels** the administration defines the levels, from the top down, with a name per language. A level can be marked as a **container**, such as the box: a container takes its whole capacity on the place it stands on, full or empty. A level assigned to places cannot be deleted.

**Adding places.** The page of a location carries the **Magazine** box with the path, level, occupancy and the places below. **Add a place below** creates a new location under it; Anton suggests the next level. **Edit magazine details** changes the level, the place above («Located in»), the capacity in running centimetres and the order. A place cannot lie in itself or in one of its own places below.

**Path.** Wherever a location is named, its path is shown, such as «Room 1 › Shelf 3 › Compartment 4 › Box 17»: on the record, in the select of the mask and of bulk editing, in the order mail and in the full Excel export.

**Occupancy.** What counts is the extent of the records assigned to a place itself, over all levels below it: their own extent or, where none is recorded, the extent below them, as the detail page shows it. A fonds whose files stand in boxes counts through the boxes, not twice. A container with a capacity counts on its compartment with its whole capacity. Without a capacity Anton only shows how much is used.

**Magazine overview.** Under **Admin → Magazine overview** the magazine is shown as a tree with occupancy and the number of records per place. The tab **Free places** lists the places with a capacity that still have room, the emptiest first, optionally of one level only and with a minimum.

**Assigning in bulk.** Records reach their place through bulk editing or the Excel table. The column `standort` takes the ID, the name or the path, with `›`, `>` or `/` between the levels. A name several places carry, such as «Compartment 4», is refused as ambiguous instead of guessed; a path that does not exist is not created as a new location.

## What is held at a location

The detail page of a location lists the records assigned to it or to a place below it: a shelf also shows what lies in its boxes.

## Deleting

If records are still attached to a location, Anton refuses to delete it and says so. The assignments must be removed first. Likewise a location with places below it stays; they must be deleted or moved first.

## Reference codes with location

In some archives, the abbreviation of the location forms part of the
[reference code](identifiers.md). Where this is set up, an additional
**location** selection field appears in the «Create new records» window.

!!! note "Archive-specific"
    This function requires a specially programmed way of forming reference
    codes. The standard scheme does not use the location — the selection field
    would have no effect there. With Anton as a Service, k & r knows whether a
    given installation comes with such a scheme.
