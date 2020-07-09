# Data Tables (Livewire)

Example: places

## Form Class

Create a `PlacesForm` Class in `app/Forms/`. The array should contain a 'list' entry with the column definitions:

```php

<?php

namespace Anton\Forms;

use Anton\Forms\AbstractForms;

class PlacesForms extends AbstractForms
{
    public static function getDefinitions() : array
    {
        return [
            'list' => [
                ['name' => 'id', 'label' => 'ID', 'sortField' => 'id'],
                ['name' => 'place_type-label', 'label' => trans('messages.Type'), 'sortField' => 'place_type_id'],
                ['name' => 'name', 'label' => trans('messages.Name'), 'sortField' => 'name'],
                ['name' => 'city', 'label' => trans('messages.City'), 'sortField' => 'city'],
                ['name' => 'state', 'label' => trans('messages.State'), 'sortField' => 'state'],
                ['name' => 'country-label', 'label' => trans('messages.country'), 'sortField' => 'country_code_id'],
                ['name' => 'buttons', 'sort' => false, 'with' => ['detail', 'edit', 'delete']]
            ],
        ];
    }
}

```


## Datatable Class

Create a Class `DataTable` in `Livewire/Places`:

```php

<?php

namespace Anton\Http\Livewire\Places;

use Livewire\WithPagination;
use Anton\Http\Livewire\DataTableWithRequest;

/**
 * Places DataTable
 **/

class DataTable extends DataTableWithRequest
{
    use WithPagination;

    public $endpoint = '/places';

    public $formtype = 'list';  // key in array of forms in PlacesForms.php

    public $model = 'Anton\Models\Place';

    public $view = 'places.data-table';
}

```

## Index view 

In `resources/views/places/index.blade.php:

```html

@extends('master')

@section('content')

@if($user->isUserIntern())
    <p>{!! link_to_route('admin', trans('messages.Admin') ) !!} &gt; </p>
@endif

 <h2>{!! Lang::choice('messages.Existing', 2) !!} {!! trans('messages.Places') !!}</h2>

 @livewire('places.data-table')


@stop
```

## Livewire View 

In `resources/views/livewire/places/data-table`: 

```html 
@include('includes._data-table')
```

## Controller

Make sure that the controller gets these two public attributes and it uses the `Controller.php` as parent:

``` 
class PlacesController extends BaseController
{
    public $modelClass = '\Anton\Models\Place';

    public $endpoint = 'places';

``` 

## Model 

### dtQuery()

The Model should have a `dtQuery()` Method:  

```
public function scopeDtQuery($query, $params)
    {
        $search = $params['search'] ?? '';
        $locale = \App::getLocale();

        $query = $query->selectRaw('places.id as id,
                           tt.label as place_type,
                           places.name as name,
                           places.city as city,
                           places.state as state,
                           ct.label as country,
                           places.description')
            ->leftJoin('terms as t', 'places.place_type_id', '=', 't.id')
            ->leftJoin('term_translations as tt', function($join) use ($locale) {
                $join->on('t.id', '=', 'tt.term_id')
                     ->where('tt.locale', $locale);
                })
            ->leftJoin('countries as c', 'places.country_code_id', '=', 'c.id')
            ->leftJoin('country_translations as ct', function($join) use ($locale) {
                $join->on('c.id', '=', 'ct.country_id')
                     ->where('ct.locale', $locale);
            });

        if ($search) {
            $query->where('places.name', 'like', '%'.$search.'%')
                  ->orWhere('tt.label', 'like', '%'.$search.'%')
                  ->orWhere('places.city', 'like', '%'.$search.'%')
                  ->orWhere('places.state', 'like', '%'.$search.'%')
                  ->orWhere('ct.label', 'like', '%'.$search.'%')
                  ->orWhere('places.description', 'like', '%'.$search.'%');
        }
        // \Log::debug($query->toSql());
        
        return $query;
    }
```

The `$param['search']` is for filtering the table. 

You can simplify the `scopeDtQuery` method by creating accessors, however, if for example a translation label is needed or a valuelist is used, then a join will reduce the number of queries.

### Attributes and Accessors

For each column name of the table there must be an attribute or an accessor with this name. If the accessor uses a term it is best to use a static variable for the valuelist within the accessor to reduce the database queries:

```
public function getPlaceTypeLabelAttribute()
{
    static $placeTypeLabels;

    if (!isset($placeTypeLabels)) {
        $placeTypeLabels = Term::getValueList('place_type');
    }

    return $placeTypeLabels[$this->place_type_id] ?? '';
}
```

## Cotroller Methods

In order to get the Links work we have to implement the show, edit and destroy methods in the controller. 

