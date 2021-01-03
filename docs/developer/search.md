# Search

## Adding a new Search Field 

- Add a new entry to the `searchfields` in `config/custom.php`.
- Add the new valuelist to `Term::getValueList()`. Don’t forget the break in the switch construction.
- Add a new case to `AntonObject::scopeDtQuery()`. If it is complicated, use a new scope.

## Create an individual List of available Search Fields 

Just create your own `searchfields` array in the `settings`. You can use all lines from the `config/custom.php`.

Grab the full list here: https://kr.anton.ch/admin/searchfields
