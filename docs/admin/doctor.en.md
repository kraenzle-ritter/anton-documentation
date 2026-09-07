# Anton Doctor

Anton Doctor checks an installation for consistency and reports what is not
right. It is the first tool to reach for when Anton behaves oddly — records in
the wrong place, missing preview images, a stalled import.

Reachable from the admin page; the `admin` role is sufficient. The tabs are not
translated and appear in English.

!!! important "Doctor checks metadata, not files"
    It checks the database and whether files are **present** — it does **not**
    compare checksums. Whether a file is unchanged is answered by
    [`media:check --levels=4`](console-commands.md#mediacheck); see
    [long-term preservation](preservation.md#integritat-prufen).

## The tabs

**Overview** summarises and is the entry point.

**Supervisor** shows whether background processing is running and how many jobs
are in the queue. Failed jobs can be restarted here individually or as a group.
This is the first thing to look at when uploads are not being processed or
conversions fail to appear: if the supervisor is down, everything piles up.

**Derived Fields** concerns the derived fields — path, depth, «has children»,
release year, creation dates, full text and the archival arrangement. They are
calculated from other data and can become stale after an import or a bulk
change. The tab shows the result of the **last** run from the cache;
recalculation has to be triggered explicitly.

**Data Integrity** checks on invocation: fonds within fonds, position
collisions among siblings, duplicate reference codes.

**Environment** checks environment variables, settings and whether the customer
directories are readable and writable.

**Binaries** checks whether the external programs Anton depends on are present —
ImageMagick, Ghostscript, ffmpeg and others. If one is missing, the
corresponding conversions fail silently. When format identification is missing,
this is the first place to look.

**Disk** shows the disk usage.

## On the command line

The same checks run via [`anton:doctor`](console-commands.md#antondoctor), in a
recurring job for example. The archival arrangement can also be **repaired**
with it — the check reports, the repair run intervenes:

```bash
php artisan anton:doctor --closure --env=<slug>
php artisan anton:doctor --closure --repair --env=<slug>
```

!!! warning "Back up before repairing"
    A repair run writes to the database. Create a [backup](restore.md)
    beforehand.

### The OAI endpoint

`--oai` compares the `oai_enabled` setting with what the endpoint actually
does, and reports both directions: switched on but silent — and switched off
but answering all the same.

```bash
php artisan anton:doctor --oai --env=<slug>
```

The check exists because this failure does not announce itself. If the endpoint
stays silent while the setting says otherwise, the harvester simply stops
receiving: no error, no log entry. The archive hears about it from the portal
weeks later. An archive that is harvested therefore adds the call to its
recurring job.

The check asks the route through the application itself rather than over the
network — the route and its middleware are what is in question, and a machine
cannot always reach its own public name. A proxy in front of Anton can still
refuse a harvester that this check calls healthy, which is why the message
names the public address to try from outside.

## No automatism

Anton does **not** run the checks of its own accord; there is no built-in
schedule. Where they are meant to run recurrently, they are set up per
installation as a cron job.
