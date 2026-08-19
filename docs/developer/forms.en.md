# The form system

The core idea: **which fields a unit of description has is stored in data, not
in code.** An archive designs its own cataloguing masks — and two installations
can look completely different on the same code base. That explains a large part
of the effort in and around the forms.

From the administration's point of view, the same thing is described under
[Forms and form sets](../admin/forms.md); this page addresses the why and the
extension seam.

## Three levels

| Level | Model | Table | What it is |
|---|---|---|---|
| **Antonfield** | `Antonfield` | `antonfields` | A field definition: name, type, base label |
| **Form** | `Objectform` | `forms` | An ordered field selection for **one** view |
| **Form set** | `Objectformtype` | `formsets` | Bundles the five views of the same record type |

A field does not appear «in the form» but is **linked** via the pivot table
`antonfields_forms` — and the link carries the per-form details: position, label,
value list, default value and, if need be, the type.

!!! note "Historical table names"
    The model class is called `Objectformtype`, but the table was renamed to
    `formsets`; `forms` used to be called `objectforms`. Searching for the old
    name leads down the wrong track.

## Why three levels

The separation solves three requirements at once:

- **Reuse** — the same field definition appears in many forms; a change to the
  field takes effect everywhere.
- **Context** — the same field may be named differently and sit in a different
  place per view. That is the reason for the pivot overrides.
- **Visibility** — the five slots of a form set (internal list/detail/edit,
  external list/detail) control what outsiders see. A field only appears if it
  is part of the respective form. There is no external edit form.

!!! warning "Visibility is not access control"
    Leaving a field out of the external form hides it in the display — it
    protects nothing. Access is governed by protection periods and the `private`
    marker.

## Resolution

Which form set applies to a record is decided in this order: the `formset_id`
field on the record, otherwise the set with the name of the level of description
(`fonds`, `file` …), otherwise the default.

Field values are resolved in three stages — the override in the form, otherwise
the default of the field definition, otherwise a hard-coded fallback. This
applies equally to label, value list, default value and type.

## The V2 rendering engine

A field is not rendered directly as a Blade template but passes through
`AntonForms\V2\AntonFormsElement`, which determines a *display mode* from type
and view (`discoverDisplayMode()`) and resolves the component from it. Two
consequences are important:

- **One field covers editing and detail.** Simple input types (`text`, `select`,
  `radio` …) automatically switch to `display` in detail and list views. No
  duplicate definition is needed.
- **Modules resolve via the name.** Complex fields have the type `module`; the
  component follows from the field name (`module_actors` → the Actors module).
  This is how title, events, descriptors, media, location and others make it
  into the mask.

Which field types and modules actually exist is **data-driven** and is shown in
the application under **Help → Anton Fields** — always current per installation.
A fixed list at this point would only go stale.

## Field definitions and ID ranges

Antonfields with **ID < 5000** are core fields: name and type are fixed, because
code and the enums `Eventtype`/`Notetype` refer to them. The **label** is free
and is deliberately not overwritten by `anton:update` — so tenant-specific
adaptations survive every update.

Fields with **ID ≥ 5000** stem from old customer-specific configurations and
should no longer exist after `anton:update`; `anton:check-customer-fields`
checks this.

## Database override with a PHP fallback

Not every form is in the database. If the `Objectform` row is missing or empty,
`AbstractForms::get()` returns the versioned PHP default, provided the subclass
declares one via `phpFallback()` — otherwise `FormNotFoundException` is still
thrown. This keeps the built-in defaults the source of truth until an archive
deliberately overrides them; existing database forms behave unchanged.

The embedded «used as descriptor» object list (shared by the actor, place,
keyword and location detail pages) renders from the PHP default in this way,
without a seeder being necessary. Under **Admin → Forms**, the «Configure»
action materialises this default into an editable `Objectform` row (idempotent,
reserved ID range ≥ 5000) and hands over to the normal column editor — see
[Configurable embedded tables](../admin/forms.md#konfigurierbare-eingebettete-tabellen)
in the admin section.

## How an archive changes its forms

Via the interface under **Admin → Forms** / **Form types**, or — reproducibly
for deployments — via seeders. Seeders deliberately do not overwrite existing
forms (`if ($form->antonfields()->count() > 0) return;`), so that they do not
destroy delivered configurations.
