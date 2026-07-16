# Schweizerisches Kunstarchiv SIK-ISEA

## 2026-03-06 Notes (scope and content für dok erzeugen)

Wunsch des Archivs: Alle Bestände mit der Signatur DOK sollen unter «Form und
Inhalt» denselben Text erhalten wie im Rechercheportal — bei den bestehenden
DOK-Signaturen ergänzt und bei künftigen Importen automatisch ausgefüllt.

Der Text lautet:

> Die Dokumentationsdossiers enthalten in der Regel eine Sammlung von Einladungskarten, Zeitungsartikeln, biografischen und bibliografischen Informationen zu den Kunstschaffenden. Der Umfang eines Dossiers kann stark variieren – vom Einzeldokument bis zu umfangreichen Konvoluten.

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
