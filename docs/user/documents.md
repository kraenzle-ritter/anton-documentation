# Dokumente

Das Modul «Dokumente» bietet einen eigenen Zugang zu ausgewählten PDFs — etwa
Geschäftsberichten oder Publikationen, die ein Archiv gezielt zum Lesen
anbieten will. Es ist ein Schaufenster neben der [Suche](search.md), nicht ein
weiterer Weg in die Tektonik.

Die Übersicht liegt unter `/documents` und lässt sich von der eigenen Website
aus verlinken. Die Dokumente erscheinen dort nach Gruppen geordnet, jede Gruppe
mit einem kurzen Erläuterungstext.

!!! note "Einrichtung erforderlich"
    Das Modul zeigt nur etwas, wenn es eingerichtet ist — siehe
    [Dokumente einrichten](../admin/documents.md). Ohne Konfiguration führt der
    Aufruf zurück auf die Startseite.

## Voraussetzung an die Erschliessung

Im Modul entspricht **ein Dokument einer Verzeichnungseinheit**. Wer es nutzen
will, erschliesst die PDFs also einzeln und nicht gesammelt in einem Dossier.

## Der Viewer

Beim Öffnen eines Dokuments erscheint links der Inhalt des Feldes **Form und
Inhalt**, rechts das PDF.

Ein Inhaltsverzeichnis lässt sich einfach als Liste in das Textfeld schreiben:

```markdown
Inhalt:
- Erstes Kapitel (S. 5)
- Zweites Kapitel (S. 17)
```

### Wenn die Seitenzahlen nicht stimmen

Häufig weichen die gedruckten Seitenzahlen von den PDF-Seiten ab — ein Bericht
mit Titelblatt und Vorwort beginnt seine Seite 5 vielleicht auf PDF-Seite 17.
Damit der Sprung trotzdem an der richtigen Stelle landet, lässt sich die
PDF-Seite als Kommentar hinter den Eintrag setzen:

```markdown
Inhalt:
- Erstes Kapitel (S. 5) <!-- 17 -->
- Zweites Kapitel (S. 17) <!-- 29 -->
```

Angezeigt wird weiterhin die gedruckte Seitenzahl; gesprungen wird an die
PDF-Seite im Kommentar. Für Lesende bleibt der Kommentar unsichtbar.
