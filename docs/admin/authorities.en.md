# Authority data synchronisation (`resources:sync`)

Anton keeps the links to external authority data (GND, Wikidata, Metagrid …) as
a **local copy** in the `resources` table. For newly available links to arrive
there, a synchronisation has to be run regularly. The user-side view of the
topic is described in [Authority data](../user/authorities.md).

## Command

```bash
php artisan resources:sync --env={slug}
```

One run carries out three steps in sequence:

1. **Normalise provider names** – outdated provider designations are brought
   into their canonical form (see [normalisation](#normalisierung)).
2. **Check for duplicates** – resources with an identical URL are reported (and
   removed on request, see `--delete-duplicates`).
3. **Synchronise entities** – all actors, places and keywords that already have
   a resource from one of the sync providers are queried again at the
   respective provider and supplemented with newly available links.

At the end, a summary is output (entities processed/updated, new resources,
errors, duplicates cleaned up).

### Options

| Option | Effect |
|---|---|
| `--env={slug}` | Target installation (environment slug), as with all `--env` commands. |
| `--dry-run` | Write nothing, only simulate and report. |
| `--limit={n}` | Process only the first *n* entities per model (for testing). |
| `--delete-duplicates` | Actually delete URL duplicates found (without the flag, only report them). |
| `--mail={address}` | Send the summary by email (several addresses comma-separated). |

## Configuration

### Which providers

When **linking interactively** in the edit form, the full list of providers
defined in `config/resources.php` (key `providers`) is available – among them
GND, Wikidata, Metagrid, GeoNames, ortsnamen.ch, Idiotikon, various Wikipedia
languages as well as numerous reference works and partner archives. Each
provider definition determines the `api-type`, `base_url`, the `target_url` of
the stored link and – where applicable – the `wikidata_property`; Anton-based
partner archives (Georg Fischer, Gosteli, KBA, for example) additionally
require an `api_token` from the `.env`.

The **periodic synchronisation** `resources:sync`, however, only queries the
three providers again for which live updating makes sense – in this order:

1. `metagrid`
2. `gnd`
3. `wikidata`

The models **Actor**, **Place** and **Keyword** are synchronised. An entity is
only touched if it already has at least one resource from one of these
providers – the synchronisation supplements existing links, it does not create
entirely new ones.

!!! note "Adding new providers"
    Additional providers (or changed base URLs/tokens) are a matter of code and
    configuration in `config/resources.php` and are rolled out with a deploy,
    not via `/settings`. Whether a provider is also included in the periodic
    synchronisation is determined in the command itself.

### Filter

When updating, the synchronisation passes the value of the setting
`resources_filter` to the provider (empty if not set). This allows hits to be
restricted installation-wide.

### Normalisation {#normalisierung}

The `rename` section in `config/resources.php` maps outdated or inconsistent
provider slugs to the canonical form (`loc` → `lcnaf`, `wikipedia` →
`wikipedia-de`, `sudoc` → `idref`, for example). Every sync run applies this
mapping first, so that the holdings remain consistent.

## Setting up a cron job

On the production servers, the Laravel scheduler (`schedule:run`) is **not**
installed. Instead, the synchronisation is set up **per installation as its own
crontab entry** – provisioned on the k & r servers via **anton-ansible**, not in
`app/Console/Kernel.php`.

An entry calls the command directly with the environment slug, for example for
a nightly run:

```cron
# Authority data synchronisation for the installation "besenval", daily 02:30
30 2 * * *  cd /var/www/anton && php artisan resources:sync --env=besenval --delete-duplicates --mail=admin@example.org >> storage/logs/resources-sync.log 2>&1
```

- **One entry per environment** – the slug determines the target installation.
- The **frequency** can be chosen freely per installation (usually nightly);
  because of the rate limits of the external APIs, large holdings do not run
  through in a matter of seconds.
- `--delete-duplicates` and `--mail=` are optional, but usual in scheduled
  operation, in order to keep the holdings clean and to be informed about the
  result.

!!! note "Metagrid partnership"
    For an institution's **own** actors to appear in Metagrid, it has to be
    registered as a partner with [Metagrid](https://metagrid.ch/). The
    synchronisation only concerns the local holdings – it does not replace the
    partnership. For details see [Authority data](../user/authorities.md).
