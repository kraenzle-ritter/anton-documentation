# Antonfields

An **Antonfield** is a single field definition — it defines the name, type, and label of one piece of data that can appear in a form. Fields are reusable across multiple forms via the `antonfields_forms` pivot table.

See [Forms & Formsets](forms.md) for the complete system documentation including field types, pivot overrides, and how to modify forms.

---

## Standard Anton fields (id 1–4999)

These are maintained by the Anton core. Their `name` and `type` must not be changed — they are referenced by code and by the `Eventtype`/`Notetype` enums. Their `label` may be customised per installation (labels are not overwritten during `anton:update`).

## Customer-specific fields (id ≥ 5000)

Fields with id ≥ 5000 were created by old customer-specific configurations. After running `anton:update` they should no longer exist. Use the maintenance command to audit:

```bash
php artisan anton:check-customer-fields --env=be
```

## Add a new custom field

```php
use Anton\Models\Antonfield;
use Anton\Models\Objectform;

$af = Antonfield::firstOrCreate(
    ['name' => 'my_field', 'type' => 'text'],
    ['label' => ['de' => 'Mein Feld', 'en' => 'My Field', 'fr' => 'Mon champ', 'it' => 'Il mio campo']]
);

// Attach to a form
$form = Objectform::where('model', 'Actor')
    ->where('type', 'edit')
    ->where('scope', 'internal')
    ->first();

$form->antonfields()->attach($af->id, ['position' => 20]);
```

## Edit labels

Labels are translatable JSON. To change a label without overwriting it during updates, edit directly in the database or via the `/antonfields` admin UI. Labels are intentionally skipped by seeders so customer customisations are preserved.
