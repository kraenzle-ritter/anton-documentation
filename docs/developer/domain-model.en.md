# Domain model

The domain changes slowly — it is the most durable part of the system. Knowing
it means reading the code with the right mental model.

## The entities

**AntonObject** — the unit of description, the central record. It sits in the
archival arrangement and carries title, reference code, dating, text fields,
media and links. Everything else is grouped around it.

**Actor, Place, Keyword** — the authority data. Independent records that are
created once and used by many units of description. They are of equal rank among
themselves; there is no hierarchy and no thesaurus.

**AntonEvent** — the link between an actor (or a place) and a unit of
description, **with role and date**. This is the most important distinction in
the whole model (see below).

**Note** — a polymorphic text field. Attached to AntonObject, but also to Actor,
Place, Keyword and Location. One record per language. In the documentation these
fields are called «text fields».

**Media** — the digital objects, via `spatie/laravel-medialibrary` with
conversions (`web`, `thumb`). The master remains unchanged.

## The hierarchy is a closure table

The archival arrangement does not live in a `parent_id` but in a closure table
(`franzose/closure-table`): a table that holds one row for **every**
ancestor-descendant pair, together with the depth.

The consequences shape the rest of the system:

- **Subtree queries are cheap** — «all descendants of X» is a join, not a
  recursive traversal. Inheritance of protection periods, aggregation of datings
  and visibility rules are based on this.
- **Re-hanging is expensive** — it rewrites many rows. That is why maintenance
  of the derived fields runs asynchronously after a move; see
  [Concurrency](events-jobs.md).
- **Denormalised fields accompany the structure** — `path`, `real_depth`,
  `has_children`, `fonds_id`. They are materialised and have to be kept
  consistent; that is the job of the job layer.

Fonds within fonds are not permitted — the allowed level transitions are in
`config/constants.php`.

## The one distinction one has to understand

Actors can be attached to a unit of description in **two fundamentally different
ways** — and the two are constantly confused, in operation as in the code:

| As a **descriptor** | As an **event participant** |
|---|---|
| Keyword indexing: actors *occur* | Actors *did something* |
| `actors_descriptors` (belongsToMany) | `AntonEvent.actor_id` |
| no role, no date | role = event type, plus place and date |
| «keywords (actors)» in the form | «creation date», «engraver» … |

The same separation applies to places. Anyone recording the creator wants the
event; anyone noting that someone is mentioned wants the descriptor.

## Invariants

Things one can rely on — and that one should not violate:

- **Reference codes are not unique.** There is no unique constraint; duplicates
  are permitted and are reported only as a non-blocking warning.
- **Event type and note type are Antonfields.** `antonevents.event_type_id` and
  `notes.note_type_id` refer to `antonfields.id`. The enums `Eventtype` and
  `Notetype` map the types referenced in the code — not necessarily all those a
  tenant has configured.
- **Authority data carries a portable UUID** — the basis for the
  lossless re-import, which does not merge records of the same name.
- **Deletion cascades.** The `deleting` hook on AntonObject removes every child
  recursively; there is no recycle bin (no `deleted_at`).

## Standards

Anton implements four archival standards: **ISAD(G)** the units of description,
**ISAAR(CPF)** the actors, **ISDIAH** the institution, and **RiC-O / CIDOC CRM**
the output as linked data. The first three are not a mapping in the code but
reference texts in the in-app help under «Standards».
