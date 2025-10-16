# Gosteli-Archiv

## Schrift Lausanne installieren 

Für MS Word. Als root:

```bash
cp /usr/local/prj/anton/gosteli/public/fonts/TWKLausanne-300.woff /usr/share/fonts/
fc-cache -f -v
```

## Fotoprojekt: Import Fotodateien

Erster Testimport (2025-09-29)

````
art anton:import --env gosteli -vv --update --locale de ../customers/gosteli/metadata_to_import/agof-180-81-08-import-images-and-update.xlsx --import --default-excel-column identifier
```

!!! note: "--default-excel-column identifier"
    Default ist `id`. Hier sollen die Datensätze aber nach der Signatur (`identifier`) gefunden werden, deshalb gibt es keine Spalte `id`.
