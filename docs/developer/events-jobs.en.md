# Concurrency: events, listeners, jobs

A unit of description carries fields that **follow** from other data: its path in
the archival arrangement, its depth, the release year, the full-text index, the
dating aggregated across the subtree. These values are **materialised** — they
sit in columns instead of being recalculated on every query.

Materialisation buys fast queries at the price of having to keep the values
consistent. That is exactly what the event and job layer does. Understanding it
means understanding why a seemingly simple change to an object triggers a chain
of background jobs.

## The pattern

Anton couples domain operations and follow-up maintenance loosely via Laravel
events:

```
Operation on the AntonObject  →  domain event  →  listener  →  job (queue)
```

The core lies in the model hooks of `AntonObject` (`booted()`) and in
`EventServiceProvider`. The follow-up maintenance runs via the queue, because it
can touch entire subtrees — with a closure table that is potentially expensive.

## Why asynchronous and idempotent

Two design decisions explain almost everything:

**Subtree work belongs in the queue.** A move rewrites the paths and depths of
all descendants; a title change can affect the full text of the entire subtree.
Doing such work synchronously in the request would blow it up — hence jobs with
generous timeouts and retries.

**The jobs are repeatable.** Each recalculates the target state from the source
data instead of carrying deltas forward. That makes them idempotent: a second
run does no harm, a lost run can be made up. The ability to repair rests on
exactly this — `anton:doctor` and `RepairAllDerivedAttributes` can restore the
consistent state at any time.

## Domain events are suppressed in bulk operations

An important detail: when creating many records (`create_bulk`) and during a
move, the code sets `$suppressDomainEvents = true` and triggers the follow-up
maintenance **once at the end** instead of per object. Otherwise a bulk
operation would generate hundreds of redundant jobs. Anyone writing a new bulk
operation has to know this pattern and take care themselves that paths, dates
and full text are updated once afterwards.

## The derived fields

| Field | Recalculated on | Job |
|---|---|---|
| `path`, `real_depth` | Creation, move | `UpdatePaths` |
| aggregated dating | Date change in the subtree | `UpdateDates` |
| `full_text`, `full_text_intern` | Title/content change, new media | `RefreshFulltext` |
| `release_year_calculated` | Protection period/date change | via descendant maintenance |
| `private`, `status_of_description_id` | Change on an ancestor | inheritance to all descendants |

`RefreshFulltext` illustrates a general precaution of the layer: with few IDs it
runs in-process, with many or with the whole database in a **separate PHP
process** — for memory isolation, so that a large rebuild does not blow up the
worker.

## Prerequisite: the supervisor is running

The whole layer presupposes that the queue is being worked off. If the
supervisor is down, jobs pile up without an error message and the derived fields
go stale silently. The **Supervisor** tab in
[Anton Doctor](../admin/doctor.md) shows the state — the first port of call for
«changes are not coming through».

## No scheduler on the servers

The Laravel scheduler (`schedule:run`) does not run on the production servers
(cf. the comment in `app/Console/Kernel.php`). Recurring tasks — integrity
checks, disk measurement, authority data synchronisation — are therefore set up
per installation as cron jobs, not via the scheduler. Anyone needing a periodic
task schedules it as a cron job.
