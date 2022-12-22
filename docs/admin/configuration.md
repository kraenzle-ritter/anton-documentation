# Configuration

## .env File



## Favicons

Favicons können pro Installation individuell eingebunden werden. Man benötigt mindestens eine quadratische Vorlage von 256x256 Pixel, die weiteren Auflösungen können automatisch erstellt werden (unter Admin -> Upload Logo und Bilder). Ausnahme ist die [SVG Grafik für Safari](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/pinnedTabs/pinnedTabs.html) (`safari-pinned-tab.svg`), die manuell erstellt und hochgeladen werden muss. Aus dem Ordner favicon (im customers Ordner) werden folgende Dateien eingebunden:

- android-icon-192x192.png
- android-icon-256x256.png
- apple-icon-114x114.png
- apple-icon-120x120.png
- apple-icon-144x144.png
- apple-icon-152x152.png
- apple-icon-180x180.png
- apple-icon-57x57.png
- apple-icon-60x60.png
- apple-icon-72x72.png
- apple-icon-76x76.png
- favicon-16x16.png
- favicon-32x32.png
- favicon-96x96.png
- manifest.json
- safari-pinned-tab.svg 

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
