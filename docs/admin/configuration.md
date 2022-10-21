# Configuration

## .env File


## Settings
We go here through the most important `settings` which only can be set by the superuser.

### abo and maximum_storage 

abo should contain "basic", "standard" or "pro".

`maximum_storage` should contain the disk space in GB. It is used by the command `anton:check-disk-space`.

## form-objects-list

To get an additional column with thumbs in the result lists, copy this into the setting:

```json
[{
    "name":"identifier", "label":"Identifier", "sortField":"identifier"},{"name":"any_title","label":"Title","sortField":"title"},{"name":"creationDateLabel", "label":"Date", "sortField":"object_creation_min"},
    {"name":"lod_extent","label":"Level of description","sortField":"level_of_description_id"},
    {"name":"other_information","label":"Other information","sort":false},{"name":"first_image","label":"Image","sort":false},
    {"name":"buttons","sort":false,"with":["content","detail","edit","move","delete"]}]
```

## searchfields and search_fields_extern

If you want to configure the searchfields for the advanced search you can fill this setting with a json object. You can find the full json here: 

[https://kr.anton.ch/admin/searchfields](https://kr.anton.ch/admin/searchfields ) 
