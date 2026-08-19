# Settings

Anton is configured via settings — around 180 of them, each a key-value pair.
They are maintained on the admin page under **Settings**.

## Structure

Besides key and value, every setting has:

| Item | Meaning |
|---|---|
| **Type** | `boolean`, `string`, `integer` or `array` (JSON) — determines how the value is entered |
| **Scope** | The thematic assignment: `theme`, `export`, `search`, `gallery`, `import`, `inge` and others |
| **Editable** | Whether the value can be changed via the interface |
| **Description** | What the setting is for |

The description in the interface is the most reliable information about the
**particular** installation — it sits on the setting itself.

## Who may change what

| Setting | Changed by |
|---|---|
| editable | role `admin` |
| not editable | superusers only |

Non-editable settings are those that are determined when the installation is
set up and that fundamentally shape operation — the formation of reference
codes, the connection to a long-term archive or the order basket, for example.
They appear in the list, but the edit form remains locked. With Anton as a
Service, k & r is responsible for changing them.

## Empty means default

If a setting is empty, the built-in default applies — that is not the same as
«switched off». With settings of type `array`, a custom value also replaces the
default **completely**; it does not supplement it.

## Subscription and storage space

| Setting | Value |
|---|---|
| `abo` | `basic`, `standard` or `pro` |
| `maximum_storage` | Agreed storage space in GB |

`maximum_storage` is evaluated by `anton:check-disk-space` and appears in the
statistics under «Overview».

## Where the individual topics are described

Most settings belong to a topic and are described there:

- [Forms and form sets](forms.md) — including the list layout
  (`form-objects-list`)
- [Value lists](valuelists.md) and [protection periods](protection-periods.md)
- [Search fields](searchfields.md), [instant search](typesense.md),
  [weighted search](weighted-search.md)
- [Media gallery](gallery.md), [watermarks](watermarks.md),
  [documents](documents.md)
- [Home page and navigation](home.md), [logo and favicons](logo.md)
- [Authority data synchronisation](authorities.md), [Inge and DIMAG](inge.md),
  [AI-assisted cataloguing](ai-cataloging.md)

## The .env file

Part of the configuration is not in the settings but in the installation's
environment file — database access, mail dispatch, server paths and switches
such as the release of AI-assisted cataloguing. It cannot be reached via the
interface and is set during [installation](installation.md).
