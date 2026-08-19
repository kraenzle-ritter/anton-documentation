# Forms and form sets

Anton does not prescribe a fixed field schema. Which fields a unit of
description has, what they are called and in what order they appear is
determined by each archive itself. This is maintained under
**Admin → Forms** and **Admin → Form types**.

How this plays out in cataloguing is described in
[Forms and fields](../user/forms.md) in the user section.

## The three levels

| Level | What it is |
|---|---|
| **Antonfield** | A field *definition* — name, type, base label. Exists once and is used by any number of forms. |
| **Form** | An ordered selection of fields for **one** view. Determines position and label per field. |
| **Form set** | Bundles five forms into one unit — the five views of the same record type. |

A field therefore does not appear «in the form» but is **linked** to it — and
the link carries the details.

## The form set and its five views

| Slot | Purpose |
|---|---|
| Internal — Edit | The cataloguing form |
| Internal — Detail | Detail view for logged-in users |
| Internal — List | Result list for logged-in users |
| External — Detail | Detail view for the public |
| External — List | Result list for the public |

There is no external edit form. The internal/external separation is the lever
that controls what outsiders see: **a field only appears if it is part of the
respective form.**

!!! warning "No substitute for protection periods"
    Removing a field from the external form hides it in the display — it is not
    access control. For anything requiring protection,
    [protection periods](protection-periods.md) and the «blocked» marker are the
    right means.

!!! note "Location not public by default"
    New installations are delivered with the **location** field removed from the
    external forms (External — Detail/List), so that the physical storage place
    does not appear in the public catalogue. Existing installations remain
    unchanged; there the field can be removed from the external forms here.

Form sets exist not only for units of description, but also for actors, places,
keywords and locations.

## Which form set applies?

Anton decides in this order:

1. If the **form set** field is set on the record, that one applies.
2. Otherwise the form set whose name corresponds to the **level of
   description** — `fonds`, `file`, `item` and so on.
3. Otherwise the default set.

For most archives it is therefore sufficient to maintain one set per level of
description. Separate sets are worthwhile when a type of holding needs
different fields — photographs, plans, films.

## What can be overridden per form

The same field definition can appear differently in each form. Among the things
that can be overridden are:

- **Label** — the same field can be called something different in the edit form
  than in the detail view
- **Position** — the order
- **Value list** — which [value list](valuelists.md) feeds a selection field
- **Default value**
- **Type** — in exceptional cases

The value list is resolved in three stages: the override in the form, otherwise
the default of the field definition, otherwise a hard-coded fallback.

## Sections

Fields of type *section* are not input fields but grey intermediate headings. A
section without a visible field is omitted entirely — empty sections therefore
do not have to be removed by hand.

## Field types

Which fields are available at all and what type they have is shown by the
**Anton Fields** help page in the application. For every field it lists the
label, the type, the help text and the forms in which it occurs — and is
therefore the most reliable information about the **particular** archive.

!!! note "Do not rename standard fields — in the technical sense"
    The name and type of Anton's standard fields are fixed; code and import rely
    on them. The **label**, by contrast, is free and is preserved across
    updates.

## Result lists

The list views are only configurable to a limited extent, because there modules
pull several items into one column. For an additional preview image column
there is the setting `form-objects-list`.

## Configurable embedded tables {#konfigurierbare-eingebettete-tabellen}

The detail pages of actors, places, keywords and locations show an embedded
object list — the units of description that use the record as a descriptor. By
default this list follows a hard-coded specification.

Under **Admin → Forms** it can be adapted per archive: the section
**Configurable embedded tables** offers a **Configure** action, which converts
the built-in specification into an editable form and hands it over to the normal
column editor. From then on, columns and labels can be changed as in any other
form. Merely looking changes nothing — only **Configure** creates the editable
form.
