# Georg Fischer Konzernarchiv

## TIFF-Bilder aus einem Bestand sollen nicht in der Bildgalerie gezeigt werden

```sql
update media
set dont_show_in_gallery = 1
where mime_type = 'image/tiff'
and (file_name like 'gfa_17_%'
and `dont_show_in_gallery` is null
```

## Akteure inkl. Vorkommen in Antonevents, Keywords und Resourcen: Exportieren für Kontrollen (2026-02-11)

```sql
select a.*, ae.cnt as events, ao.cnt as keywords, r.cnt as links 
FROM actors a
LEFT JOIN (
    SELECT actor_id, COUNT(*) AS cnt
    FROM antonevents
    GROUP BY actor_id
) ae ON ae.actor_id = a.id
LEFT JOIN (
    SELECT actor_id, COUNT(*) AS cnt
    FROM actors_objects
    GROUP BY actor_id
) ao ON ao.actor_id = a.id
LEFT JOIN (
   SELECT resourceable_id, COUNT(*) AS cnt
	FROM resources
	WHERE resourceable_type = 'Anton\\Models\\Actor'
	GROUP BY resourceable_id
) r ON r.resourceable_id = a.id
```
