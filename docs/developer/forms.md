# Forms

!!! Bug "Achtung"
    Forms does not ork for AntonObjects yet.

- `$modus`: detail, edit, create, list
- `$scope`: intern, extern

### Valuelists for select2

#### Api

```
api/valuelists/{name}/{locale}?format=select2
```

|name in the route | internal name |
|---|---|
| authority_types | authority_type |
| detail_of_description_values | detail_of_description |
| languages | languages |
| level_of_description | level_of_description |
| locations | location |
| objectform_types | objectformtypes |
| object_types | object_type |
| period_of_protection_values | period_of_protection |
| private_values | private |
| status_of_description_values | status_of_description |
| vacat_values | vacat |

