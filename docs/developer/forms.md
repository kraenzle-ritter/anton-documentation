# Forms — Antonfields, Forms & Formsets

Anton uses a three-layer system to define which fields appear in which view. This page documents the database structure, field types, components, and how to modify forms.

---

## Overview

Three building blocks work together:

| Concept | DB table | Model class | What it represents |
|---------|----------|-------------|-------------------|
| **Antonfield** | `antonfields` | `Antonfield` | A single field definition (name, type, label) |
| **Form** | `forms` | `Objectform` | A list of ordered fields for one view of one entity |
| **Formset** | `objectformtypes` | `Objectformtype` | Assigns forms to an level of description (e.g. Fonds, Dossier) |

```
Formset "fonds" (AntonObject)
  ├── form_external_detail_id → Form "AntonObject/detail/external"
  ├── form_internal_detail_id → Form "AntonObject/detail/internal"
  ├── form_internal_edit_id   → Form "AntonObject/edit/internal"
  └── form_external_list_id   → Form "AntonObject/list/external"
         └── antonfields_forms (pivot)
               ├── Antonfield "name"    position=1
               ├── Antonfield "type_id" position=2
               └── ...
```

---

## Database Structure

### `antonfields` — Field definitions

| Column | Type | Description |
|--------|------|-------------|
| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Primary key (see ID ranges below) |
| `name` | varchar | Field identifier (unique together with `type`) |
| `type` | varchar | Field type (see [Field Types](#field-types) below) |
| `label` | json | Translatable label in all 4 locales: `{"de": "Name", "en": "Name", "fr": "Nom", "it": "Nome"}` |
| `help` | json | Optional help text per locale |
| `default_config` | json | Default search configuration (operators, url, endpoint, multiple). Used as fallback when pivot.config has no operators. |

**ID ranges:**

| Range | Purpose | Examples |
|-------|---------|---------|
| 1–109 | ISAD(G) standard + note fields | `object.identifier` (3), `note.scopecontent` (18) |
| 110–199 | Reserved | |
| 200–229 | Search fields | `fulltext` (200), `creation_actor` (208) |
| 250–269 | Module fields (canonical) | `actors` (250), `places` (251), `keywords` (252) |
| 300–355 | Entity form + list fields | `label` (300), `type_id` (301), `identifier` (350) |
| 1000–1015 | Antonevent fields | `creation` (1000), `provenance` (1001) |
| ≥ 5000 | Customer-specific fields | |

UNIQUE constraint on `(name, type)`. Labels are resolved in the **current application locale** by `AbstractForms::get()` and returned as plain strings.

### `forms` — Form definitions (DB table name: `forms`, was `objectforms`)

| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Primary key |
| `model` | varchar | Short model name: `Actor`, `Place`, `Keyword`, `Location`, `AntonObject` |
| `type` | varchar | View type: `detail`, `edit`, `list` |
| `scope` | varchar | `external` (public) or `internal` (admin) |
| `name` | varchar | Human-readable name (e.g. `default`) |
| `label` | json | Translatable form label |
| `help` | json | Optional help text |

### `antonfields_forms` — Pivot (fields ↔ forms)

| Column | Type | Description |
|--------|------|-------------|
| `antonfield_id` | int | FK → `antonfields.id` |
| `form_id` | int | FK → `forms.id` |
| `position` | int | Sort order within the form |
| `valuelist` | varchar | Override the field's value list (e.g. `authority_type`) |
| `default_value` | varchar | Override default value |
| `type` | varchar | Override the antonfield's render type for this form (e.g. force `display`) |
| `label` | json | **Label override** for this form: `{"de": "Sonderbezeichnung", "en": "Special name"}` |
| `config` | json | Per-form metadata and render options (see [config reference](#pivot-config-reference)) |
| `help` | json | Override help text per locale for this form |

#### `label` in the pivot

`pivot.label` is a locale-JSON map that overrides `antonfields.label` for this specific form only. Use it when the same antonfield should appear with a different label in one particular form without changing the global label.

```json
{"de": "Abkürzungen (intern)", "en": "Abbreviations (internal)", "fr": "...", "it": "..."}
```

If `pivot.label` is null, `AbstractForms::get()` falls back to `antonfields.label` in the current locale (with `de` as secondary fallback, then the field name).

#### `pivot.config` reference

The `config` column is a JSON object that can contain any combination of the following keys:

| Key | Type | Used in | Description |
|-----|------|---------|-------------|
| `sortField` | string | `list` forms | DB column to ORDER BY when sorting this column (e.g. `"type_id"`, `"ct.label"`) |
| `sort` | bool | `list` forms | `false` disables the sort arrow for this column |
| `with` | array | `list` forms, `buttons` fields | Action buttons to render: `["detail", "edit", "delete"]` |
| `use_field` | bool | all forms | Internal: use `field` key instead of `name` for component rendering |
| `class` | string | `edit` forms | Additional CSS class on the input element (e.g. `"form-control-sm"`) |
| `position` | string | `buttons` | Button placement: `"right"` (default) or `"left"` |

Example for a sortable list column:

```json
{"sortField": "type_id", "sort": true}
```

Example for a buttons column:

```json
{"sort": false, "with": ["detail", "edit", "delete"]}
```

Example for a list column that cannot be sorted:

```json
{"sort": false}
```

### `objectformtypes` — Formsets

Assigns a set of forms to a named entity configuration (level of descriptions):

| Column | Description |
|--------|-------------|
| `model` | `AntonObject`, `Actor`, `Place`, `Keyword`, `Location` |
| `name` | Identifier, e.g. `fonds`, `series`, `default` |
| `form_external_list_id` | → `forms.id` |
| `form_external_detail_id` | → `forms.id` |
| `form_internal_list_id` | → `forms.id` |
| `form_internal_detail_id` | → `forms.id` |
| `form_internal_edit_id` | → `forms.id` |

---

## Field Types

The `type` column on `antonfields` (overridable per form via `antonfields_forms.type`) determines how a field is rendered.

### Simple field types

| Type | Blade component | Edit mode | Detail/List mode |
|------|----------------|-----------|-----------------|
| `text` | `forms.fields.text` | `<input type="text">` | auto → `display` |
| `textarea` | `forms.fields.textarea` | `<textarea>` | auto → `display` |
| `select` | `forms.fields.select` | Dropdown (Choices.js) | auto → `display` |
| `select2` | `forms.fields.select2` | Select with AJAX search | auto → `display` |
| `radio` | `forms.fields.radio` | Radio buttons | auto → `display` |
| `checkbox` | `forms.fields.checkbox` | Checkbox | auto → `display` |
| `number` | `forms.fields.text` | `<input type="number">` | auto → `display` |
| `email` | `forms.fields.text` | `<input type="email">` | auto → `display` |
| `display` | `forms.fields.display` | Read-only (no input) | Read-only |
| `section` | `forms.fields.section` | Visual grouping header | Visual grouping header |
| `password` | `forms.fields.modules.password` | Password input | — |
| `buttons` | *(in list template)* | — | Action buttons (detail/edit/delete) |

**Auto-switch to display:** In `detail` and `list` forms, `text`, `textarea`, `select`, `select2`, and `radio` automatically render as `display`. This means one antonfield covers both edit and detail views — no duplicate needed.

### Module types

Modules are complex components with their own PHP class in `app/View/Components/Forms/Fields/Modules/`.

#### `note`

Renders a translatable, poly-morphic notes field. The field is linked via `note_type_id = antonfield.id`.

- **Used on:** Actor, Place, Keyword, Location, AntonObject
- **Forms:** `detail`, `detail_intern`, `edit`, `create`
- **Common names:** `description`, `sources`, `custod_hist`, `scope_content`, `appraisal`

```php
['name' => 'description', 'type' => 'note']
```

#### `antonevent`

Renders Anton events of one subtype (creation, provenance, acquisition, …). Each event has an actor, a place, and a date.

- **Used on:** AntonObject only
- **Forms:** `detail`, `edit`
- **Resolved by:** `event_type_id = antonfield.id` (IDs 1000–1015 from `Eventtype` enum)
- **Common names:** `creation`, `provenance`, `acquisition`, `reproduction`, `coloring`, `digitisation`, `edition`, `engravation`, `ingest`, `other`, `performance`, `preservation`, `production`, `reception`, `text_author`, `writing`

```php
['name' => 'creation', 'type' => 'antonevent']
```

#### `userevent`

Renders user events (loan, moved, maintenance). The field is linked via `event_type_id`.

- **Used on:** AntonObject
- **Forms:** `detail_intern`, `edit`
- **Common names:** `loan`, `moved`, `maintenance`

#### `module` (generic)

The component is resolved from the field's `name`: `forms.fields.modules.{name}`.

- **Used on:** depends on the specific module (see table below)
- **Forms:** `detail`, `detail_intern`, `edit`

| Field name | Component | Used on | Description |
|-----------|-----------|---------|-------------|
| `actors` | `modules.actors.table` | AntonObject | Actor descriptors |
| `places` | `modules.places.table` | AntonObject | Place descriptors |
| `keywords` | `modules.keyword` | AntonObject | Keyword descriptors |
| `media` / `images` | `modules.images` | AntonObject | Media attachments |
| `language` | `modules.language` | AntonObject | Language assignments |
| `relations` | `modules.relations` | AntonObject | Related objects |
| `access` | `modules.access` | AntonObject | Access restrictions / protection periods |
| `updates` | `modules.updates` | Actor, Place, Keyword, Location, AntonObject | Created/updated metadata |
| `permalink` | `modules.permalink` | Actor, Place, Keyword, Location, AntonObject | Permanent link display |
| `anton_date_interval` | `modules.anton-date-interval` | Actor | Date range editor |
| `extent` | `modules.extent` | AntonObject | Extent of material |
| `vacat` | `modules.vacat` | AntonObject | Vacat flag |
| `title` | `modules.title` | AntonObject | Translatable title field |

```php
['name' => 'updates', 'type' => 'module']
['name' => 'permalink', 'type' => 'module', 'label' => 'Permalink']
['name' => 'actors', 'type' => 'module']
```

### Search field type

Antonfields with type `search` represent logical search fields that don't map directly to a DB column (e.g. `fulltext`, `creation_actor`, `city`). They are used in `AntonObject/search/external` and `AntonObject/search/internal` forms.

The `pivot.config` stores search metadata:

```json
{"operators": "searchoperators_text"}
{"operators": "searchoperators_in_not_in", "url": "/api/actors?format=select2", "endpoint": "/api/actors", "multiple": true}
```

The `antonfields.default_config` column stores the standard search configuration. When a search field is added to a form, `pivot.config` overrides `default_config`.

---

## Form resolution

`AbstractForms::get($type)` resolves form definitions as follows:

- **DB-managed entities** (Actor, Place, Keyword, Location, AntonObject list/search): The DB is the **single source of truth**. If no `forms` record exists for `model` + `type` + `scope`, a `FormNotFoundException` is thrown.
- **Admin entities** (User, Settings, Cart, etc.): No `modelShortName()` → PHP `getDefinitions()` is used directly.
- **AntonObject detail/edit**: Uses the Formset path (`Objectformtype` assigns forms per level of description).
- **AntonObject list/search**: Uses DB lookup like entity forms.

There is no settings fallback — all form definitions live in the `forms` + `antonfields_forms` tables.

---

## Label resolution

`AbstractForms::get()` always returns `col->label` as a **plain string in the current application locale**. Templates output it directly — no further `trans()` call is needed for DB-path forms.

### Resolution order (DB path)

1. `pivot.label[currentLocale]` — per-form locale override
2. `pivot.label['de']` — German fallback within pivot override
3. `antonfields.label[currentLocale]` — global field label in current locale
4. `antonfields.label['de']` — German fallback
5. `antonfield.name` — last resort

### Customer customisation

Labels come directly from the DB. Customer-specific label changes can be made by editing `antonfields.label` or attaching a `pivot.label` override — no code deployment required.

---

## How to modify forms

### Via the admin UI

- `/formsets` — manage formsets and their form assignments
- `/antonfields` — browse and edit field labels and help texts
- `/objectformtypes/{id}/edit` — add/remove fields, change field order and pivot settings

### Via seeders (recommended for deployments)

Each entity has a seeder in `database/seeders/`:

- `InitActorForms.php` (IDs 100–103)
- `InitPlaceForms.php` (IDs 110–113)
- `InitKeywordForms.php` (IDs 120–123)
- `InitLocationForms.php` (IDs 130–133)
- `InitObjectListForms.php` (IDs 3–4)
- `InitSearchForms.php` (IDs 14–15)
- `InitEntityFormsets.php`
- `SeedEntityFormLabels.php`

```bash
php artisan db:seed --class=InitActorForms --env=kr
```

Init seeders only create forms that don't have fields yet — they never overwrite existing customer customisations.

### Adding a new custom field

```php
use Anton\Models\Antonfield;
use Anton\Models\Objectform;

// 1. Create the antonfield
$af = Antonfield::firstOrCreate(
    ['name' => 'my_field', 'type' => 'text'],
    ['label' => ['de' => 'Mein Feld', 'en' => 'My Field', 'fr' => 'Mon champ', 'it' => 'Il mio campo']]
);

// 2. Attach to a form
$form = Objectform::where('model', 'Actor')
    ->where('type', 'edit')
    ->where('scope', 'internal')
    ->first();

$form->antonfields()->attach($af->id, [
    'position' => 20,
]);
```

### Overriding the type for one form

Use `pivot.type` to change how a field renders in a specific form without changing its global type:

```php
// Show textarea as read-only in detail form
$form->antonfields()->attach($af->id, [
    'position' => 5,
    'type'     => 'display',
]);
```

### Overriding the label for one form

Use `pivot.label` to give a field a different label in one specific form:

```php
$form->antonfields()->attach($af->id, [
    'position' => 3,
    'label'    => json_encode(['de' => 'Interner Titel', 'en' => 'Internal title']),
]);
```

### Configuring a list column

Use `pivot.config` for sort metadata and button configuration:

```php
// Sortable column with custom DB sort column
$form->antonfields()->attach($af->id, [
    'position' => 2,
    'config'   => json_encode(['sortField' => 'type_id']),
]);

// Buttons column
$form->antonfields()->attach($af->id, [
    'position' => 99,
    'config'   => json_encode(['sort' => false, 'with' => ['detail', 'edit', 'delete']]),
]);
```

---

## PHP form definitions (admin entities)

For admin entities (`User`, `Setting`, `Media`, `Cart`, etc.) that don't have DB-managed forms, PHP classes in `app/Forms/` define the field lists. For DB-managed entities (Actor, Place, Keyword, Location, AntonObject), the PHP classes serve only as data source for the Init seeders — they are never used at runtime.

```
app/Forms/
  AbstractForms.php          ← Base class with get() priority logic
  ActorsForms.php
  PlacesForms.php
  KeywordsForms.php
  LocationsForms.php
  ObjectsForms.php           ← AntonObject: loads from DB (Objectformtype)
  UsersForms.php
  ObjectformsForms.php
  ObjectformtypesForms.php
```

### Field definition structure

```php
// Simple text field
['name' => 'city', 'type' => 'text', 'label' => 'City']

// Select with value list
['name' => 'type_id', 'type' => 'select', 'valuelist' => 'authority_type', 'label' => 'Type']

// Note module
['name' => 'description', 'type' => 'note']

// Generic module (component resolved from name)
['name' => 'actors', 'type' => 'module']
['name' => 'updates', 'type' => 'module']

// List column with sort
['name' => 'name', 'label' => 'Name', 'sortField' => 'name']

// Buttons column (no label)
['name' => 'buttons', 'type' => 'buttons', 'sort' => false, 'with' => ['detail', 'edit', 'delete']]
```

All available definition keys:

| Key | Description |
|-----|-------------|
| `name` | Model attribute name |
| `field` | Full field path alternative (e.g. `note.description`) |
| `type` | Field type |
| `label` | Display label — translation key string for PHP-path forms (e.g. `'Name'`); locale-resolved string for DB-path forms |
| `valuelist` | Key for select/radio options |
| `default_value` | Default value |
| `sortField` | DB column for sorting (list forms; stored in `pivot.config`) |
| `sort` | `false` disables sorting (stored in `pivot.config`) |
| `with` | Button list for `buttons` columns (stored in `pivot.config`) |
| `help` | Help text (stored in `pivot.help`) |
| `placeholder` | Input placeholder text |
| `class` | Additional CSS classes on the input (stored in `pivot.config`) |

---

## Rendering pipeline

```
Controller
  └── passes $model to View
       └── <x-forms.render :model="$model" type="detail|edit|create" />
            └── AbstractForms::get($type)     ← DB → Settings → PHP
                 └── array of stdClass columns
            └── AntonFormsElement[] created per column
            └── components.forms.templates.table
                 └── foreach $form_definition as $element
                      └── <x-dynamic-component :component="$element->resolved_component_name" />
```

### `<x-forms.render>` parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model` | `null` | Eloquent model passed to field components |
| `type` | `'edit'` | Form type: `detail`, `edit`, `create`, `detail_intern` |
| `definition` | `null` | Explicit field array (overrides automatic lookup) |
| `url` | `null` | `action` attribute of the `<form>` tag |
| `method` | `'get'` | HTTP method: `get`, `post`, `put`, `patch`, `delete` |
| `id` | auto | HTML id of the form (`frm-{table}-{type}`) |
| `template` | `'table'` | Render template (currently only `table`) |

---

## Maintenance commands

```bash
# Check a customer database for legacy fields (id >= 5000)
php artisan anton:check-customer-fields --env=be

# Remove orphaned legacy fields (no name, no pivot references)
php artisan anton:check-customer-fields --env=be --delete-orphaned
```

Exit code is `1` if any in-use fields (id ≥ 5000) are found, `0` otherwise.
