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

## Akteure entsperren (2026-04-27)

Aktuell gesperrte Akteure entsperren, wenn  
- verstorben (Datum bis nicht leer)
- Geburtsdatum über 100 Jahre (Datum von < 1926)
- Akteur mit externen Links verknüpft

Vorschau
```sql
SELECT
      a.id,
      JSON_UNQUOTE(JSON_EXTRACT(a.label, '$.de')) AS label_de,
      a.date_start,
      a.date_end,
      CASE
          WHEN a.date_end IS NOT NULL AND a.date_end <> '0000-00-00' THEN 'verstorben'
          WHEN a.date_start IS NOT NULL AND a.date_start <> '0000-00-00' AND
  a.date_start < '1926-01-01' THEN 'vor 1926 geboren'
          WHEN EXISTS (
              SELECT 1 FROM resources r
              WHERE r.resourceable_type = 'App\\Models\\Actor'
                AND r.resourceable_id   = a.id
          ) THEN 'externe Links'
      END AS reason
  FROM actors a
  WHERE a.private = 1
    AND (
          (a.date_end   IS NOT NULL AND a.date_end   <> '0000-00-00')
       OR (a.date_start IS NOT NULL AND a.date_start <> '0000-00-00' AND a.date_start
  < '1926-01-01')
       OR EXISTS (
              SELECT 1 FROM resources r
              WHERE r.resourceable_type = 'App\\Models\\Actor'
                AND r.resourceable_id   = a.id
          )
    )
  ORDER BY label_de;
```

Entsperrung
```sql
UPDATE actors a
  SET a.private    = 0,
      a.updated_at = NOW(),
      a.updated_by = 'anton'
  WHERE a.private = 1
    AND (
          (a.date_end   IS NOT NULL AND a.date_end   <> '0000-00-00')
       OR (a.date_start IS NOT NULL AND a.date_start <> '0000-00-00' AND a.date_start
  < '1926-01-01')
       OR EXISTS (
              SELECT 1 FROM resources r
              WHERE r.resourceable_type = 'App\\Models\\Actor'
                AND r.resourceable_id   = a.id
          )
    );
```
