# Georg Fischer Konzernarchiv

## TIFF-Bilder aus einem Beständ soll nicht in der Bildgalerie gezeigt werden

```sql
update media
set dont_show_in_gallery = 1
where mime_type = 'image/tiff'
and (file_name like 'gfa_17_%'
and `dont_show_in_gallery` is null
```
