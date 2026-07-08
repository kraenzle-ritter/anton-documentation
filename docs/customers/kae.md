# Klosterarchiv Einsiedeln

## Pfad für Anton Backups 

`/usr/local/prj/backup/anton` 

## Probleme mit Tektonik

### Analyse
```
php artisan anton:doctor --closure --env=kae
php artisan anton:repair-closure-table --check --env=kae
```

### Reparatur
```
php artisan anton:doctor --closure --repair --env=kae
php artisan anton:repair-closure-table --force --backup --env=kae
```

Die Reparatur-Reihenfolge ist sowohl im Browser als auch CLI identisch:

- Orphaned Entries entfernen
- Missing Self-Links hinzufügen
- Missing Parent Paths reparieren
- Affected Descendants fixen
- Depth-Werte aktualisieren

## Zustand 19. März 2026
![alt text](images/kae_doctor.png)

## Fehler History ()
Die Reparatur hat auch das objects.history Feld falsch upgedated.


Lieber Herr Ritter, lieber Herr Kränzle,
gerade eben habe ich bei diesem Datensatz Klosterarchiv Einsiedeln (29315) festgestellt, dass bei der Verzeichniskontrolle steht, er sei am 19. März 2026 durch das Benutzerkonto von P. Gregor geändert worden. Hängt das wieder mit einer Änderung an der Datenbank zusammen, wie wir es kürzlich schon mal hatten, oder wurde das Benutzerkonto von P. Gregor tatsächlich nach seinem Tod verwendet?
Mit freundlichen Grüssen
P. Meinrad

Wir nehmen das updated_at Datum aus der history:

```sql
UPDATE objects
SET updated_at = STR_TO_DATE(
    TRIM(SUBSTRING_INDEX(TRIM(LEADING '\n' FROM history), '\n', 1)),
    '%Y-%m-%d %H:%i:%s / '
)
WHERE DATE(updated_at) = '2026-03-19'
  AND TIME(updated_at) BETWEEN '18:00:00' AND '18:59:59'
  AND history IS NOT NULL
  AND history != '';
```

Und mit leerer history (wenn wir keine history haben setzen wir updated_at = created_at)
```sql
UPDATE objects
SET updated_at = CASE
    WHEN history IS NULL OR TRIM(history) = '' OR TRIM(history) = '\n'
        THEN created_at
    ELSE
        STR_TO_DATE(
            TRIM(SUBSTRING_INDEX(TRIM(LEADING '\n' FROM history), '\n', 1)),
            '%Y-%m-%d %H:%i:%s / '
        )
END
WHERE DATE(updated_at) = '2026-03-19'
  AND TIME(updated_at) BETWEEN '18:00:00' AND '18:59:59';
```
