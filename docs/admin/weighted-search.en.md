# Weighted search (admin)

The weighted search enables relevance-based sorting of search results for actors, places and keywords.

## Configuration

### Global activation

The weighted search can be activated globally for the API:

```php
// In Tinker or a seeder
Setting::setValue('search_weighted_enabled', true);  // activate
Setting::setValue('search_weighted_enabled', false); // deactivate (default)
```

!!! info "User settings"
    All users can configure the weighted search in their personal settings:
    
    - **Default**: follows the global setting
    - **On**: always activated (overrides the global setting)
    - **Off**: always deactivated (overrides the global setting)

### API parameter

In API requests, the weighted search can be controlled by a parameter:

```
GET /api/actors?search=Müller&weighted=1
GET /api/places?search=Zürich&weighted=1
GET /api/keywords?search=Archiv&weighted=1
```

The API parameter has the highest priority and overrides both the user setting and the global setting.

## Field weightings

The relevance calculation is based on configurable field weightings. Higher values mean higher relevance.

### Default weightings

#### Actors (`search_weight_actors`)

| Field | Weight | Description |
|------|---------|--------------|
| name | 10 | Main name |
| alternative_names | 7 | Alternative names |
| variants | 5 | Name variants |
| abbreviations | 5 | Abbreviations |
| type_label | 3 | Type designation |
| description | 2 | Description |
| sources | 1 | Source references |
| comment | 1 | Comment (internal users only) |

#### Places (`search_weight_places`)

| Field | Weight | Description |
|------|---------|--------------|
| name | 10 | Place name |
| city | 8 | City |
| state | 6 | Canton/state |
| alternative_names | 5 | Alternative names |
| variants | 5 | Name variants |
| abbreviations | 5 | Abbreviations |
| address | 3 | Address |
| description | 2 | Description |
| sources | 1 | Source references |
| comment | 1 | Comment |

#### Keywords (`search_weight_keywords`)

| Field | Weight | Description |
|------|---------|--------------|
| label | 10 | Designation |
| description | 5 | Description |
| name | 3 | Internal name |

### Adapting the weightings

```php
// Example: adapting the weightings for actors
Setting::setValue('search_weight_actors', [
    'name' => 15,              // increase name strongly
    'alternative_names' => 10, // alternative names more important
    'variants' => 5,
    'abbreviations' => 5,
    'type_label' => 3,
    'description' => 2,
    'sources' => 1,
    'comment' => 1,
]);
```

## Relevance calculation

The relevance is calculated as follows:

| Type of hit | Multiplier |
|------------|---------------|
| Exact match | Weight × 3 |
| Hit at the beginning of a word | Weight × 2 |
| Hit contains the term | Weight × 1 |

**Example**: searching for "Müller" with weight `name = 10`:

- Exact hit "Müller" → 10 × 3 = 30 points
- "Müller-Weber" (begins with) → 10 × 2 = 20 points  
- "Anna Müller" (contains) → 10 × 1 = 10 points

## Order of priority

Activation of the weighted search follows this priority:

1. **API parameter** (`?weighted=true/false`) – highest priority
2. **User setting** – only if "On" or "Off" is explicitly chosen (not "Default")
3. **Global setting** (`search_weighted_enabled` in the settings) – fallback

If "Default" is chosen, the global setting is used.

## Carrying out the update

After an update, the seeder has to be run in order to initialise the default weightings:

```bash
php artisan db:seed --class=Update --env=<environment>
```

## Technical details

- Trait: `Anton\Traits\HasWeightedSearch`
- Models: `Actor`, `Place`, `Keyword`
- Method: `scopeDtQuery()` with the option `weighted => true`
