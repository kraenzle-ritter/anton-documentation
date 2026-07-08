# Data Tables (Livewire)

Data tables are rendered as Livewire components. Each entity (Places, Actors, Keywords, etc.) has its own DataTable class that extends `DataTableWithRequest`.

## Form definition

Column definitions come from the `list` form type. The form system resolves definitions in priority order: **DB form → Settings → PHP fallback**.

For example, `PlacesForms` defines the list columns:

```php
<?php

namespace Anton\Forms;

class PlacesForms extends AbstractForms
{
    protected static function modelShortName(): ?string
    {
        return 'Place';
    }

    public static function getDefinitions(string $type, mixed $model = null): array
    {
        $forms = [
            'list' => [
                ['name' => 'id', 'type' => 'display', 'label' => 'ID', 'sortField' => 'id'],
                ['name' => 'type_id', 'type' => 'select', 'valuelist' => 'place_type', 'label' => 'Type', 'sortField' => 'type_id'],
                ['name' => 'label', 'type' => 'module', 'label' => 'Name', 'sortField' => 'name'],
                ['name' => 'city', 'label' => 'City', 'sortField' => 'city'],
                ['name' => 'state', 'label' => 'State', 'sortField' => 'state'],
                ['name' => 'country_code_id', 'type' => 'select2', 'valuelist' => 'countries', 'label' => 'Country', 'sortField' => 'ct.label'],
                ['name' => 'buttons', 'sort' => false, 'with' => ['detail', 'edit', 'delete']],
            ],
            // ... detail, detail_intern, edit, create ...
        ];

        return $forms[$type] ?? [];
    }
}
```

Since `modelShortName()` returns `'Place'`, the DB form is checked first. If a `forms` record exists for `model=Place`, `type=list`, `scope=external` with attached antonfields, that takes priority over the PHP definition.

## DataTable class

```php
<?php

namespace Anton\Http\Livewire\Places;

use Livewire\WithPagination;
use Anton\Http\Livewire\DataTableWithRequest;
use Livewire\Attributes\Locked;

class DataTable extends DataTableWithRequest
{
    use WithPagination;

    #[Locked]
    public string $endpoint = '/places';

    #[Locked]
    public string $formtype = 'list';

    #[Locked]
    public string $model = 'Anton\Models\Place';

    #[Locked]
    public string $view = 'places.data-table';

    #[Locked]
    public bool $supportsWeightedSearch = true;
}
```

Key properties:

- `$endpoint` — URL prefix for links
- `$formtype` — key in the form definitions array (usually `list`)
- `$model` — fully qualified model class
- `$view` — Livewire view path
- `$supportsWeightedSearch` — enables weighted fulltext search

## Index view

```blade
@extends('master')

@section('content')
    <h2>{{ trans('messages.Places') }}</h2>
    @livewire('places.data-table')
@stop
```

## Livewire view

```blade
@include('includes._data-table')
```

## Model: `dtQuery` scope

The model needs a `scopeDtQuery()` method for search filtering and joins:

```php
public function scopeDtQuery($query, $params)
{
    $search = $params['search'] ?? '';
    $locale = App::getLocale();

    $query = $query->selectRaw('places.id as id, ...')
        ->leftJoin('terms as t', 'places.place_type_id', '=', 't.id')
        // ... joins for translated labels ...

    if ($search) {
        $query->where('places.name', 'like', '%'.$search.'%')
              ->orWhere(...);
    }

    return $query;
}
```

## Select fields in list columns

Select and select2 fields in list forms automatically resolve their `valuelist` to display translated labels instead of raw IDs. This is handled by `DataTableWithRequest` — no accessor needed for valuelist columns.

## Controller

The controller needs `$modelClass` and `$endpoint`:

```php
class PlacesController extends BaseController
{
    public $modelClass = '\Anton\Models\Place';
    public $endpoint = 'places';
}
```
