# Asla

## Bilder die auf private gesetzt sind, sollen auch intern nicht in der Galerie erscheinen

Lösung mit SQL Event:

```sql
show events
create event sync_private_media_dont_show_in_gallery
on schedule every 1 day
do
update media set dont_show_in_gallery = 1 where private_media = 1;
```
