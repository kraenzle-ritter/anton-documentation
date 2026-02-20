# Gosteli-Archiv

## Schrift Lausanne installieren 

Für MS Word. Als root:

```bash
cp /usr/local/prj/anton/gosteli/public/fonts/TWKLausanne-300.woff /usr/share/fonts/
fc-cache -f -v
```

## Fotoprojekt: Import Fotodateien

### Erster Testimport (2025-09-29)

````
art anton:import --env gosteli -vv --update --locale de ../customers/gosteli/metadata_to_import/agof-180-81-08-import-images-and-update.xlsx --import --default-excel-column identifier
```

!!! note: "--default-excel-column identifier"
    Default ist `id`. Hier sollen die Datensätze aber nach der Signatur (`identifier`) gefunden werden, deshalb gibt es keine Spalte `id`.

### Zweite Tranche (2025-10-24)

- Umbenennung der Dateien gemäss Excel-Liste (AGoF 110)

#### Import mit Excelliste (AGoF_110)
- Excel-Liste vorbereiten (Spalten: identifier, media)
- Excel-Liste in `metadata_to_import` ablegen (20251024_import_fotos_agof_110.xlsx)
- Bilder in `assets_to_import` verschieben


```bash 
php artisan anton:import --env gosteli 20251024_import_fotos_agof_110.xlsx --default-excel-column identifier --copy-media -vv --update --import
```

#### Import von Files (AGoF_180)

Signatur und Altsignatur vertauscht: 
AGoF 180:584:87-124  AGoF 180-87-124

```bash
for f in ../customers/gosteli/assets_to_import/*.tif; do art anton:import-file "$f" --identifier-from-filename --check -vv --env gosteli; done
```

und dann

```bash
for f in ../customers/gosteli/assets_to_import/*.tif; do art anton:import-file "$f" --identifier-from-filename -vv --env gosteli; done
```
