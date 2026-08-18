# Forms and fields

Anton does not prescribe a fixed field schema. Which fields a unit of
description has, in what order they appear and what they are called is
determined by each archive itself. That explains why the forms look different
from archive to archive — and why the examples in this documentation may deviate
from a given installation.

## Form sets

A **form set** bundles five forms for one and the same thing:

| Form | Purpose |
|---|---|
| Internal — Edit | The cataloguing form |
| Internal — Detail | The detail view for logged-in users |
| Internal — List | The result list for logged-in users |
| External — Detail | The detail view for the public |
| External — List | The result list for the public |

The internal/external separation is the reason why outsiders see less than the
archive itself: a field only appears if it is part of the respective form. There
is no edit form for the public.

Form sets exist not only for units of description, but also for
[actors](actors.md), [places](places.md), [keywords](keywords.md) and locations.

## Which form set applies?

Anton decides in this order:

1. If the **form set** field is filled in on the record, that one applies.
2. Otherwise the form set with the same name as the
   [level of description](hierarchy.md) applies — for a file, therefore, «file».
3. Otherwise the default set applies.

The **form set** field is at the very top of the cataloguing form and generally
remains empty. It is the way out for special cases: if a fonds contains
photographs that need different fields from the rest, a separate form set can be
created for them and assigned specifically.

## Fields

A field only appears if it is part of the form **and** has a value — empty
fields are hidden in the detail view rather than shown as an empty line. In the
edit form, by contrast, they are always visible.

The same field behaves differently depending on the view: what is an input field
or a selection list when editing appears as plain text in the detail view.

**Sections** with a grey background structure the form. They are not fields
themselves; a section without visible fields is omitted entirely.

## Help texts for fields

A help text can be stored for a field — the archive's own cataloguing rule for
that field. If one is stored, it appears in the edit form as a small note
directly below the input field.

This inline display can be switched on and off by each person in their own
profile; by default it is **off**. Independently of this, all help texts can be
consulted collectively on the **Anton Fields** help page in the application.

## Changing

Form sets and forms are maintained under **Admin → Forms** and
**Admin → Form types**. There, fields can be added, removed, reordered and
renamed per form — the label of a field can therefore read differently in the
edit form than in the detail view. Which fields are available at all is shown by
the **Anton Fields** help page in the application.
