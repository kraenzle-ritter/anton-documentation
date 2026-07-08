# Fields

All fields must have a `name` (or `field` for edit/create forms).

## Attributes

### `name`

Rules: `string`

The model attribute name or accessor that returns the value to display/edit.

### `type`

Rules: `nullable|string`

Default: `display`

Determines how the field is rendered. See [Forms — Field Types](forms.md#field-types) for the full list including `text`, `textarea`, `select`, `select2`, `radio`, `checkbox`, `number`, `email`, `display`, `section`, `note`, `antonevent`, `module`, `buttons`, and more.

**Auto-switch to display:** In `detail` and `list` forms, input types (`text`, `textarea`, `select`, `select2`, `radio`) automatically render as `display`. One field definition covers both edit and detail views.

### `label`

Rules: `nullable|string`

- **DB-path forms:** Resolved from `antonfields.label` (translatable JSON) or overridden via `pivot.label`. Always returned as a plain string in the current locale — no `trans()` needed.
- **PHP-path forms:** A translation key string (e.g. `'Name'`). Templates apply `trans('messages.{label}')` with fallback to the raw string.

### `valuelist`

Rules: `nullable|string`

Key for select/radio options (e.g. `authority_type`, `countries`, `place_type`).

### `sortField`

Rules: `nullable|string`

DB column to ORDER BY when sorting this column in list forms. Stored in `pivot.config` for DB forms.

### `help`

Rules: `nullable|string|json`

Help text displayed below the field. DB forms use translatable JSON; PHP forms use plain strings.

## Module types

Modules are complex components rendered via `type: 'module'`. The component is resolved from the field's `name`:

| Field name | Component | Used on |
|-----------|-----------|---------|
| `actors` | `modules.actors.table` | AntonObject |
| `places` | `modules.places.table` | AntonObject |
| `keywords` | `modules.keyword` | AntonObject |
| `media` / `images` | `modules.images` | AntonObject |
| `language` | `modules.language` | AntonObject |
| `relations` | `modules.relations` | AntonObject |
| `access` | `modules.access` | AntonObject |
| `updates` | `modules.updates` | All entities |
| `permalink` | `modules.permalink` | All entities |
| `anton_date_interval` | `modules.anton-date-interval` | Actor |
| `extent` | `modules.extent` | AntonObject |
| `vacat` | `modules.vacat` | AntonObject |
| `title` | `modules.title` | AntonObject |
| `label` | `modules.label` | Actor, Place, Keyword |

See [Forms](forms.md) for the complete documentation.
