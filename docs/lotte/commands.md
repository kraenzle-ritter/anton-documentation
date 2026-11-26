# Lotte: Befehlsreferenz

Lottes Befehle sind [Laravel-Kommandos](https://laravel.com/docs/artisan) und werden im Verzeichnis der Anwendung über `artisan` aufgerufen. Anders als bei Anton wird der Mandant nicht mit `--env` gewählt, sondern als erstes Argument genannt: `<tenant>` ist sein Slug aus der Mandanten-Datei.

```bash
php artisan lotte:show beispiel 01944a8e-…
```

Jede Operation der [API](api.md) gibt es auch als Befehl. Objekte werden mit ihrer UUID genannt; wo ein Befehl mehrere Objekte nimmt, geht auch die OCFL-ID `urn:uuid:…`. Wie die Befehle im Betrieb zusammenspielen, steht unter [Betrieb](operation.md).

## Nach Aufgabe {#nach-aufgabe}

| Aufgabe | Befehle |
|---|---|
| Mandanten | [`lotte:tenant:init`](#lotte-tenant-init), [`lotte:migrate`](#lotte-migrate) |
| Clients und Schlüssel | [`lotte:client:create`](#lotte-client-create), [`lotte:client:revoke`](#lotte-client-revoke) |
| Übernahme | [`lotte:ingest`](#lotte-ingest), [`lotte:commit`](#lotte-commit), [`lotte:discard`](#lotte-discard), [`lotte:prune-packages`](#lotte-prune-packages) |
| Objekte | [`lotte:show`](#lotte-show), [`lotte:get`](#lotte-get), [`lotte:metadata`](#lotte-metadata) |
| Ableitungen und Text | [`lotte:derive`](#lotte-derive), [`lotte:derivatives`](#lotte-derivatives), [`lotte:ocr`](#lotte-ocr) |
| Prüfung und Migration | [`lotte:verify`](#lotte-verify), [`lotte:migrate-format`](#lotte-migrate-format) |
| Änderungsfeed | [`lotte:changes`](#lotte-changes) |
| Zurückziehen und Löschen | [`lotte:withdraw`](#lotte-withdraw), [`lotte:purge`](#lotte-purge) |
| Betrieb | [`lotte:work`](#lotte-work), [`lotte:health`](#lotte-health), [`lotte:rebuild-index`](#lotte-rebuild-index) |

`lotte:migrate` migriert die Datenbanken der Mandanten, nicht Formate; eine Formatmigration ist `lotte:migrate-format`. `lotte:ocr`, `lotte:verify` und `lotte:migrate-format` legen dieselben Aufträge an wie `POST /t/<slug>/jobs` und führen sie gleich aus, mit `--queue` in der Warteschlange des Mandanten.

!!! warning "Schreibende Befehle"
    `lotte:migrate-format` ohne `--probe`, `lotte:metadata` und `lotte:withdraw` legen eine neue Version an; `lotte:purge --confirm` entfernt den Inhalt eines Objekts endgültig. Vorher ohne `--confirm` bzw. mit `--probe` ansehen, was geschähe.

## Vollständige Referenz {#vollstandige-referenz}

Die folgenden Abschnitte listen **alle** Befehle `lotte:*` mit Aufruf, Argumenten und Optionen, wie sie in ihrer eigenen `--help`-Ausgabe stehen.

!!! note "Automatisch erzeugt"
    Dieser Abschnitt wird aus `php artisan list lotte` erzeugt (`scripts/gen-command-reference.py`); die Beschreibungen stehen in der Sprache des Codes (Englisch). Nicht aufgeführt sind die Optionen, die jeder Laravel-Befehl hat (`--help`, `--quiet`, `--verbose` …).

<!-- BEGIN generated command reference -->

### `lotte:changes` {#lotte-changes}

List a customer's change feed after a sequence

```bash
php artisan lotte:changes [--since [SINCE]] [--limit [LIMIT]] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--since=…` | the entries after this sequence | `0` |
| `--limit=…` | at most this many (1 to 1000) | `100` |

### `lotte:client:create` {#lotte-client-create}

Create a client with a key for one customer

```bash
php artisan lotte:client:create [--abilities [ABILITIES]] [--description [DESCRIPTION]] [--] <tenant> <name>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<name>` |  |  |
| `--abilities=…` | comma-separated: read, ingest, jobs, withdraw, metadata | `read` |
| `--description=…` |  |  |

### `lotte:client:revoke` {#lotte-client-revoke}

Revoke all keys of a client of one customer

```bash
php artisan lotte:client:revoke <tenant> <name>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<name>` |  |  |

### `lotte:commit` {#lotte-commit}

Commit a checked package of a customer into OCFL objects

```bash
php artisan lotte:commit <tenant> <package>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<package>` |  |  |

### `lotte:derivatives` {#lotte-derivatives}

Keep a customer's derivative rows true to the store and make up missing or failed derivatives

```bash
php artisan lotte:derivatives [--reconcile] [--backfill] [--object [OBJECT]] [--limit [LIMIT]] [--dry-run] [--given-up] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--reconcile` | align the derivative rows with the derivative and text store |  |
| `--backfill` | queue missing derivatives, failed ones with fewer than three attempts, and claims older than a day |  |
| `--object=…` | with --reconcile, only these objects |  |
| `--limit=…` | with --backfill, at most this many per run | `500` |
| `--dry-run` | with --backfill, count only |  |
| `--given-up` | list the derivatives failed three times, which the backfill no longer tries |  |

### `lotte:derive` {#lotte-derive}

Queue (or with --sync make) a customer's missing derivatives and text

```bash
php artisan lotte:derive [--object [OBJECT]] [--conversion [CONVERSION]] [--retry-failed] [--sync] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--object=…` | only these objects (UUID or urn:uuid:…) |  |
| `--conversion=…` | only this conversion (web, thumb, poster, text …) |  |
| `--retry-failed` | also what failed fewer than three times |  |
| `--sync` | make them in this process instead of queueing |  |

### `lotte:discard` {#lotte-discard}

Discard a package of a customer

```bash
php artisan lotte:discard <tenant> <package>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<package>` |  |  |

### `lotte:get` {#lotte-get}

Copy a file of an OCFL object of a customer

```bash
php artisan lotte:get [--at [AT]] [--to [TO]] [--] <tenant> <object> <path>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<object>` | the object's UUID |  |
| `<path>` | logical path, e.g. data/scan.tif |  |
| `--at=…` | version v1, v2, …; the head by default |  |
| `--to=…` | target file |  |

### `lotte:health` {#lotte-health}

Check the storage base and, per customer, database, folder and queue; Nagios output and exit code

```bash
php artisan lotte:health
```

### `lotte:ingest` {#lotte-ingest}

Ingest the files of a folder as one package and check it

```bash
php artisan lotte:ingest [--reference-prefix [REFERENCE-PREFIX]] [--route [ROUTE]] [--] <tenant> <folder>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<folder>` |  |  |
| `--reference-prefix=…` | reference = prefix + file name |  |
| `--route=…` | the route the files came by; the format policy decides by it | `upload` |

### `lotte:metadata` {#lotte-metadata}

Give an object of a customer a new metadata copy (a new version)

```bash
php artisan lotte:metadata <tenant> <object> <file>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<object>` | the object's UUID |  |
| `<file>` | a JSON file with the new metadata copy |  |

### `lotte:migrate` {#lotte-migrate}

Migrate the customers' databases

```bash
php artisan lotte:migrate [--tenant [TENANT]] [--all]
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `--tenant=…` | only these customers |  |
| `--all` | every customer in the tenants file |  |

### `lotte:migrate-format` {#lotte-migrate-format}

Migrate objects of a customer by a format policy rule (with --probe: only report)

```bash
php artisan lotte:migrate-format [--rule [RULE]] [--object [OBJECT]] [--package [PACKAGE]] [--probe] [--queue] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--rule=…` | the format policy rule to apply, e.g. tiff_zip |  |
| `--object=…` | these objects (UUID or urn:uuid:…) |  |
| `--package=…` | the committed objects of this package |  |
| `--probe` | run the rule on copies and report per object; changes nothing |  |
| `--queue` | hand the job to the customer's queue instead of running it here |  |

### `lotte:ocr` {#lotte-ocr}

Run an OCR job over objects or a package of a customer

```bash
php artisan lotte:ocr [--object [OBJECT]] [--package [PACKAGE]] [--queue] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--object=…` | these objects (UUID or urn:uuid:…) |  |
| `--package=…` | the committed objects of this package |  |
| `--queue` | hand the job to the customer's queue instead of running it here |  |

### `lotte:prune-packages` {#lotte-prune-packages}

Discard forgotten packages

```bash
php artisan lotte:prune-packages [--tenant [TENANT]] [--all]
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `--tenant=…` | only these customers |  |
| `--all` | every customer |  |

### `lotte:purge` {#lotte-purge}

Purge a withdrawn object's content for good (operator only; the rule when this is allowed is not decided yet)

```bash
php artisan lotte:purge [--reason [REASON]] [--operator [OPERATOR]] [--confirm] [--] <tenant> <object>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<object>` | the object's UUID |  |
| `--reason=…` | why the content is purged (required) |  |
| `--operator=…` | who purges it (required) |  |
| `--confirm` | remove for real; without it only say what would be removed |  |

### `lotte:rebuild-index` {#lotte-rebuild-index}

Rebuild a customer's object index from its OCFL storage root

```bash
php artisan lotte:rebuild-index [--prune] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--prune` | remove index rows whose object is not in the storage root |  |

### `lotte:show` {#lotte-show}

Show an OCFL object of a customer

```bash
php artisan lotte:show <tenant> <object>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<object>` | the object's UUID |  |

### `lotte:tenant:init` {#lotte-tenant-init}

Create a customer's folder and database and migrate it

```bash
php artisan lotte:tenant:init <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` | slug from the tenants file |  |

### `lotte:verify` {#lotte-verify}

Validate a customer's OCFL objects (fixity), with --ocfl also with ocfl-py

```bash
php artisan lotte:verify [--ocfl] [--object [OBJECT]] [--package [PACKAGE]] [--queue] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--ocfl` | also validate each object with ocfl-py |  |
| `--object=…` | only these objects (UUID or urn:uuid:…) |  |
| `--package=…` | only the committed objects of this package |  |
| `--queue` | hand the job to the customer's queue instead of running it here |  |

### `lotte:withdraw` {#lotte-withdraw}

Withdraw an object of a customer: nothing served any more, derivatives and text removed, the content kept

```bash
php artisan lotte:withdraw [--reason [REASON]] [--] <tenant> <object>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `<object>` | the object's UUID |  |
| `--reason=…` | why it is withdrawn (required) |  |

### `lotte:work` {#lotte-work}

Work the queue of one customer

```bash
php artisan lotte:work [--once] [--stop-when-empty] [--] <tenant>
```

| Argument / Option | Beschreibung | Vorgabe |
|---|---|---|
| `<tenant>` |  |  |
| `--once` |  |  |
| `--stop-when-empty` |  |  |
<!-- END generated command reference -->
