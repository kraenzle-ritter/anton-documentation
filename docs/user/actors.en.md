# Actors

Actors are persons, families and organisations — independent records that are
created once and then used by any number of units of description. They are found
under **Admin → Actors**.

## Two ways to a unit of description

Actors can be attached to a unit of description in two ways:

- **As a keyword** — in the «keywords (actors)» field. This says: this person
  *occurs in the content*. Without a role, without a date.
- **Via an [event](antonevents.md)** — with role, place, date and comment. This
  says: this person *did something* — they wrote the document, engraved the
  print, transferred the fonds.

Anyone recording the creator wants the event. Anyone noting that someone is
mentioned in the text wants the keyword.

On an actor's detail page, both uses appear separately: «is involved in» lists
the events, «appears in» the units of description in which the actor is a
keyword.

## Types

Six types are permanently available: **person**, **family**, **corporate body**,
**department**, **group** and **software**. The labels can be translated per
archive, but the types themselves cannot be extended.

## Recording

By default, the form contains type, name, other name forms, variants,
abbreviations, the dates of life or activity, description, sources and comment.
Which fields appear depends on the [form set](forms.md).

For the **dates**, «ca.» can be ticked for each date and day, month or year can
be left open individually — incomplete datings are therefore possible.

Actors can also be created **directly from the object form**: next to the
selection list there is a **+** which opens a window with the same form. After
creation the new entry is selected — the unit of description itself still has to
be saved afterwards.

Linking to [authority data](authorities.md) such as GND or Wikidata is done in
the right-hand column of the edit view.

## Gender {#geschlecht}

Persons have the field **Gender**. Its values come from the [value list](../admin/valuelists.md) «Gender»: female, male, diverse, unknown. The archive can rename them and add its own. Types other than persons have no gender; the form refuses a value there.

Whether and where the field appears is the archive's decision. Anton puts it on no existing form; it is added to the edit form and the internal detail form in the [form editor](forms.md). It is visible in public only if the archive also puts it on the public detail form. The API names it only to people signed in internally.

For every value Anton records where it came from: set by hand, from a comment «Geschlecht: …», from the stored GND or Wikidata data, guessed from a first name or salutation, or imported. Changing the value in the form sets it by hand. Empty fields can be filled from these hints with [`anton:fill-gender`](../admin/console-commands.md#maintenance-and-repair).

## Blocked actors

The **blocked** field hides an actor completely from everyone who is not logged
in internally — in lists, in the detail view, in the linked units of description
and in the full-text search. It is intended for living persons and information
requiring protection.

## Deleting

Actors can only be deleted as long as they are **not in use**. Anton refuses
deletion in both of the following cases and reports which one applies:

- the actor is involved in an **event**,
- or the actor is entered as a **descriptor** on a unit of description
  (see [Two ways to a unit of description](#two-ways-to-a-unit-of-description)).

To get rid of an actor, the links have to be cleaned up first — the events on
the units of description concerned, the descriptors in the «is used as
descriptor» register on the detail page.
