# Lotte: overview

Lotte is the digital archive behind Anton: a service of its own that keeps each media file as an OCFL object and takes over everything that has to do with the bytes. Anton keeps the description and decides who may see what. In short: content in Anton, technique in Lotte. Lotte is a Laravel application of its own, with a database per tenant, its own queue and its own command line; it goes on running, checking and migrating while Anton is under maintenance, or after Anton has been replaced.

!!! note "Under construction"
    Lotte has been developed but is not yet connected to Anton and not yet in production use (anton#857). Until then, Anton ingests files itself as before, see [Digital archive: overview](../admin/preservation.md). The interface may still change until Anton is connected; these pages describe the state of the service.

The pages of this section:

- [Operation](operation.md): installation, tenants, clients and keys, workers, recurring tasks, backup, monitoring and recovery;
- [Command reference](commands.md): every `lotte:*` command;
- [API reference](api.md): every route, generated from the OpenAPI description.

## Division of tasks {#aufgabenteilung}

| Lotte | Anton |
|---|---|
| the files: masters, kept versions, OCFL objects | description, authority data, relations |
| checksums, integrity, virus check | who may see what: rights, protection periods, locks |
| format identification, format validation, format policy, migration | search, gallery, user interface |
| derivatives, OCR, text from files | users, roles, capabilities |
| preservation events (PREMIS), jobs | |

Lotte never calls Anton, neither for a check nor for a status or metadata. What Lotte needs arrives with the request. Anton is a client with a key and fetches changes itself, from the [change feed](#aenderungsfeed). If one side is down for maintenance, nothing gets stuck. Nothing in Lotte is public: every route with content requires a key; whether something is shown publicly is Anton's decision.

## One service per server {#ein-dienst-je-server}

Lotte runs once per server, with tenants of its own: once on the server that carries the Anton installations of Anton as a Service, and once on the server of an institution that wants to keep its files on its own premises. There is no central service for all installations; an archive's files do not leave its infrastructure, and an outage affects only the archives of that server. Each Anton tenant talks to exactly one Lotte tenant on its own server.

## One database and one folder per tenant {#mandanten}

A tenant is a customer of the service, named by its slug in the server's tenants file. Each tenant has a database and a folder of its own, and nothing of it lies anywhere else:

- the database `<slug>_archiv`, on the same MySQL instance as the tenant's Anton database, with a database user of Lotte's own: Anton's user has no rights on it, and Lotte's none on Anton's database;
- the folder `<base>/<slug>/` with four areas:

| Area | Content |
|---|---|
| `ocfl/` | the archive: the OCFL storage root (OCFL 1.1) |
| `derivatives/` | access copies, thumbnails, posters; can be made again at any time |
| `text/` | text from OCR and text extraction; can be made again at any time |
| `work/` | packages before commit, working copies |

A tenant can thus be restored, handed over, moved to another server or deleted on its own, by its database dump and its folder, without touching another tenant. The folder is the archive; the database is an index over it plus the running business (clients, open packages, jobs, change feed). [`lotte:rebuild-index`](commands.md#lotte-rebuild-index) rebuilds the object index and the state of the derivatives from the folder alone.

## One OCFL object per medium {#ocfl-objekt}

Each media file becomes one OCFL object, with SHA-512 as its digest. Lotte assigns the ID itself, `urn:uuid:<uuid>` (time-ordered); the client's reference (for Anton: tenant and medium number) is recorded and unique per tenant, but not part of the ID. One object per medium, because a record can be renumbered and moved and a delivery split, while a medium stays what it is. An object contains:

| Path in the object | Content |
|---|---|
| `data/<file>` | the master, as delivered or migrated |
| `metadata/description.json` | the copy of the metadata the client sends along (for Anton: reference code, title, path in the archival arrangement, delivery, rights) |
| `metadata/events.json` | the preservation events (PREMIS): checks at ingest, fixity, migration, withdrawal |
| `metadata/object.json` | the client's reference and the state (active or withdrawn) |
| `metadata/characteristics.json` | technical characteristics of PDF, text, audio and video |

Each change is a new version: a migration, a new metadata copy, a fixity finding, the withdrawal. What was there before stays in the earlier version, bit for bit; a delivered file kept by a format rule is the first version, the result the second. Writes to one object happen one after another, into a new version directory that is moved into place only when complete. Because everything is in the object, it can be read, checked and restored without Lotte's database. Besides the OCFL library that writes, a second implementation (`ocfl-py`) checks every object: in the tests and, on request, across the holdings ([`lotte:verify --ocfl`](commands.md#lotte-verify)).

## Ingest in two steps {#uebernahme}

An ingest happens in two steps: Lotte accepts the files checked but provisionally; only the commit turns them into OCFL objects. In between, the client creates its own records, and if that fails, it discards the package.

1. **Describe and upload a package.** The client describes a package: per file its name, reference, optionally the delivered checksum, the metadata copy and the size. Then it uploads the files, in parts if need be; an interrupted upload continues where it stopped.
2. **Check.** Lotte checks each file as a job on the tenant's queue: viruses (ClamAV), delivered checksum, format policy (preingest and normalisation by the tenant's rules and the route the files came by), format identification (Siegfried), format validation, consistency of extension, content and PRONOM ID, technical characteristics. The package is then **provisional**, with a result per file: accepted, or refused with a reason.
3. **Commit or discard.** With `commit`, Lotte writes one OCFL object per accepted file, with the events of the checks and an ingestion event, and queues derivatives and text. With `discard`, the client drops the package; nothing remains. A package neither committed nor discarded is discarded by [`lotte:prune-packages`](commands.md#lotte-prune-packages) after the retention time (default 7 days).

Each step can be repeated without creating anything twice: a package with the same `Idempotency-Key` is not created twice, and a committed package answers a second `commit` as it did the first. The checks are the same as in Anton's own ingest ([Checks at every ingest](../admin/preservation.md#prufungen-bei-jeder-ubernahme)); Lotte has taken them over. Operators ingest a folder with [`lotte:ingest`](commands.md#lotte-ingest).

## Derivatives and text {#ableitungen}

Derivatives (access copy `web`, thumbnail `thumb`, poster `poster` for video) and text never go into the OCFL object. Lotte makes them from the master of the newest version and puts them into `derivatives/` and `text/`, to be thrown away at will: whatever is there can be made again at any time. Which derivatives an object has depends on its MIME type; tools and settings are the same as in Anton. Text comes from the text layer of a PDF, from office documents and text files, and where the tenant has OCR on, also from images and PDFs without a text layer (ocrmypdf); it stays as written, without the preparation for Anton's search.

Per object and derivative, Lotte keeps a state: missing, queued, ready, failed, with the number of attempts. After three failures Lotte gives up; [`lotte:health`](commands.md#lotte-health) reports such derivatives as a warning. The API serves a finished derivative; one that is not there yet is queued and answered with 202. For a browser without a key there are short-lived signed URLs (default 15 minutes).

## Jobs {#auftraege}

Four kinds of jobs run over objects or over the objects of a committed package, on the tenant's queue, in slices, with progress and a result per object:

| Job | What it does |
|---|---|
| `derive` | makes missing derivatives and text, on request only one derivative or also what failed |
| `ocr` | makes text by OCR, even where the tenant does not have OCR on |
| `verify` | checks each file against the inventory (fixity), on request also the whole object with `ocfl-py`. A check adds no version; when and with what outcome an object was checked is kept in the index and in the job's result. Only a finding goes into the object, as a failed fixity event in a new version. |
| `migrate` | applies one format policy rule to a working copy of the master and writes a new version only if the result passes the rule's verification, format validation and format identification; the earlier file stays in the version before. As a probe, the job only reports. |

A job with the same `Idempotency-Key` is not created twice, and a job that is over never runs again. Every job skips withdrawn objects, with the reason as their result. Operators create the same jobs with [`lotte:ocr`](commands.md#lotte-ocr), [`lotte:verify`](commands.md#lotte-verify) and [`lotte:migrate-format`](commands.md#lotte-migrate-format); [`lotte:derive`](commands.md#lotte-derive) makes derivatives directly.

## Change feed {#aenderungsfeed}

What happens to objects, packages and jobs, Lotte writes into a change feed per tenant, in a running sequence. A client fetches the entries after its position with `GET /t/<slug>/changes?since=<sequence>` and keeps the last one itself; Lotte sends nothing of its own accord. There are entries for:

| Kind | When |
|---|---|
| `object.created` | an object was created from a package |
| `object.version_added` | a new version by migration, normalisation or a fixity finding |
| `object.metadata_updated` | a new metadata copy |
| `object.withdrawn` | the object was withdrawn |
| `object.purged` | an operator purged the content |
| `derivative.ready` / `text.ready` | a derivative or the text is ready |
| `derivative.failed` | every failure, with the number of attempts and whether Lotte gives up |
| `package.discarded` | a package was discarded, by the client, by an operator or after the retention time |
| `job.finished` | a job is over |

An entry is written in the same database transaction as the index change it reports: both are there or neither. The OCFL version is written before; if the transaction fails, the object is ahead of its index until `lotte:rebuild-index` brings the index up to date. Entries become visible in the order of their sequence number, so a client never skips one, and no entry is ever changed or deleted. `lotte:rebuild-index` writes no entries; where it changed the index it says so, and the clients resync those objects.

## Withdrawal and purge {#zurueckziehen-und-loeschen}

A client deletes nothing in Lotte; it withdraws. A **withdrawn** object gets a new version in which `metadata/object.json` records the state with reason, time and client, and an event records the withdrawal; its derivatives and text are removed. Afterwards the object, its files, derivatives, text and signed URLs answer 410 with the reason, and jobs skip it. The content stays in the archive, and `lotte:rebuild-index` restores the state from the folder.

Only an operator may **purge** the content (data protection, a court order), on the command line with [`lotte:purge`](commands.md#lotte-purge): only a withdrawn object, with a reason and the operator's name, and without `--confirm` as a dry run that says what would go. The command removes the object's directory and its rows in the index, and records who purged it, when and why, in the database and as `object.purged` in the change feed; a purged object thus leaves a trace although its content is gone.

!!! warning "The rule for purging is not decided yet"
    When purging a withdrawn object is allowed (time limits, approvals, who decides) is still open. `lotte:purge` currently checks only that the object is withdrawn.
