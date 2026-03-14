# Schweizerisches Kunstarchiv SIK-ISEA

## 2026-03-06 Notes (scope and content für dok erzeugen)

Lieber Andreas

Wir haben für alle Bestände mit der Signatur DOK einen Text für unser Rechercheportal verfasst, den wir auch gerne in ANTON unter Form und Inhalt hätten. Wäre es möglich, dieses Feld bei den bestehenden DOK-Signaturen zu ergänzen und bei künftigen Importen automatisch auszufüllen? Wieviel Zeit bräuchtest Du für die Anpassung?

Der Text lautet:
Die Dokumentationsdossiers enthalten in der Regel eine Sammlung von Einladungskarten, Zeitungsartikeln, biografischen und bibliografischen Informationen zu den Kunstschaffenden. Der Umfang eines Dossiers kann stark variieren – vom Einzeldokument bis zu umfangreichen Konvoluten.
Herzlicher Gruss
Michael

```sql
INSERT INTO notes (object_id, note_type_id, text)
SELECT o.id,18,"Die Dokumentationsdossiers enthalten in der Regel eine Sammlung von Einladungskarten, Zeitungsartikeln, biografischen und bibliografischen Informationen zu den Kunstschaffenden. Der Umfang eines Dossiers kann stark variieren – vom Einzeldokument bis zu umfangreichen Konvoluten."
FROM objects o
WHERE o.identifier LIKE 'SIK-ISEA, DOK%'
AND NOT EXISTS (
    SELECT 1
    FROM notes n
    WHERE n.object_id = o.id
      AND n.note_type_id = 18
);
```
