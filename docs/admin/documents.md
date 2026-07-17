# Dokumente einrichten

Das Modul [Dokumente](../user/documents.md) wird über die Einstellung
`documents-navigation` (ID 261) konfiguriert. Sie enthält ein JSON-Objekt, das
die Gruppen der Übersichtsseite beschreibt. Ohne gültigen Eintrag leitet
`/documents` auf die Startseite zurück und meldet dies angemeldeten Benutzern.

## Aufbau

Jeder Schlüssel des Objekts ist eine Gruppe und wird zum Slug in der URL
(`/documents/geschäftsberichte`). Pro Gruppe:

| Feld | Bedeutung |
|---|---|
| `title` | Überschrift der Gruppe, je Sprache |
| `comment` | Erläuterungstext unter der Überschrift, je Sprache |
| `parent_id` | ID der Verzeichnungseinheit, unterhalb derer alle Dokumente der Gruppe liegen |
| `regex` | zurzeit ohne Funktion, `null` setzen |

## Beispiel

```json
{
    "geschäftsberichte": {
        "title": {
            "de": "Geschäftsberichte",
            "en": "Annual Reports"
        },
        "comment": {
            "de": "Deutscher Kommentar",
            "en": "English Comment"
        },
        "parent_id": 9367,
        "regex": null
    },
    "publikationen": {
        "title": {
            "de": "Publikationen",
            "en": "Publications"
        },
        "comment": {
            "de": "Kommentar",
            "en": ""
        },
        "parent_id": 12319,
        "regex": null
    }
}
```

## Erschliessung

Das Modul geht davon aus, dass **jedes Dokument einer eigenen
Verzeichnungseinheit** entspricht. Alle Einheiten unterhalb der jeweiligen
`parent_id` erscheinen in der Gruppe.

Der Text, den der Viewer links neben dem PDF anzeigt, stammt aus dem Feld
**Form und Inhalt**. Wie sich daraus ein springendes Inhaltsverzeichnis bauen
lässt — auch bei abweichenden Seitenzahlen — steht unter
[Dokumente](../user/documents.md#der-viewer).

## Verlinken

Die Übersicht ist unter `/documents` erreichbar und kann von der eigenen
Website aus verlinkt werden.
