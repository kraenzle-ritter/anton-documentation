# Architecture — overview

This section describes Anton for developers: not class by class — the code is the
source of truth for that — but the **shape** of the system, its decisions and the
invariants one can rely on.

!!! note "Internal concept papers"
    In-depth design documents are located in the Anton repository under
    `documentation/concepts/` (OCFL storage, RiC, Notes v2, TEI configuration,
    Typesense, SSO and others) and are versioned with the code. These pages refer
    to them at the appropriate points; without repository access they are not
    retrievable.

## The stack in one sentence

Anton is a **multi-tenant Laravel application** (Laravel 12, Livewire,
Alpine.js, Bootstrap) for archival description according to **ISAD(G)**. Every
archive is its own database; the same code serves them all.

## The load-bearing ideas

Five decisions shape almost every part of the code. Knowing them makes it clear
why Anton is built the way it is.

**One tenant is one database.** No tenant discriminator in the tables, but
separate databases, selected via `--env={slug}` or the domain. This keeps the
individual installation simple and the separation hard.

**The hierarchy is a closure table.** The archival arrangement — collection,
fonds, series, file, item — does not live in a `parent_id` alone but in a
materialised ancestor-descendant table. That makes subtree queries cheap and
re-hanging expensive; both shape the concurrency model.

**The form is configured, not coded.** Which fields a unit of description has is
stored in data, not in Blade templates. An archive designs its own masks. See
[The form system](forms.md).

**Derived fields are materialised and maintained asynchronously.** Path, depth,
release year, full text, aggregated dating — all values that follow from other
data but are stored and recalculated via the queue. See
[Concurrency](events-jobs.md).

**Tenant-specific behaviour docks on instead of forking.** Custom reference code
generation, custom exporters, custom conversions — everywhere a class is named
via a setting, rather than the core being changed. See
[Extension points](extension-points.md).

## The subsystems

| Subsystem | Purpose | In depth |
|---|---|---|
| Domain model | Units of description, authority data, events, media | [Domain model](domain-model.md) |
| Form engine | Configurable fields and views | [Form system](forms.md) |
| Event/job layer | Consistency of the derived fields | [Concurrency](events-jobs.md) |
| Export layer | EAD, RDF, TEI, DIP, OCFL, native round trip | [Export matrix](../admin/export-matrix.md) |
| Media pipeline | Upload, format identification, conversions, cloud/DIMAG | [Long-term preservation](../admin/preservation.md) |
| Search | MySQL full text and Typesense | [Instant search](../admin/typesense.md) |

## Working on the code

Setup, the local environment and conventions are documented in the Anton
repository itself — `DEVELOPMENT.md` (DDEV, tests, tools) and `CLAUDE.md`
(patterns, conventions, verification). These public pages deliberately do not
repeat that; they supply the mental model that the code alone does not give.
