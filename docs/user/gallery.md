# Mediengalerie

Die Mediengalerie zeigt die Bilder eines Archivs als Kachelraster — ein
visueller Einstieg neben der [Suche](search.md). Sie liegt unter `/gallery`.

!!! note "Nicht überall verlinkt"
    Anton hängt die Galerie nicht selbst in die Navigation. Ob sie im Menü
    erscheint, entscheidet jedes Archiv für sich; sonst ist sie nur über die
    Adresse erreichbar.

## Zwei Varianten

| Variante | Filter |
|---|---|
| Klassische Galerie | Eine Filterzeile über dem Raster; welche Felder sie enthält, ist pro Archiv konfigurierbar |
| Galerie V2 | Eine Seitenleiste mit Facetten und **Trefferzahlen** je Bestand, Schlagwort und Medientyp, dazu ein Jahresbereich |

V2 setzt eine Typesense-Suchmaschine voraus und wird schrittweise eingeführt;
welche Variante ein Archiv nutzt, ist eingestellt. Die Kacheln und die
Grossansicht sind in beiden identisch.

## Was erscheint in der Galerie

Ein Bild erscheint nur, wenn **alle** Bedingungen erfüllt sind:

- Es ist nicht als «nicht in der Galerie zeigen» markiert. Diese Markierung
  wirkt für **alle**, auch für angemeldete Bearbeitende.
- Es ist nicht als gesperrtes Medium markiert.
- Für Aussenstehende zusätzlich: die Verzeichnungseinheit ist nicht gesperrt,
  ihr Status ist nicht «Entwurf», und die [Schutzfrist](access.md) ist
  abgelaufen.

Angemeldete interne Benutzer sehen also mehr als die Öffentlichkeit — die
Markierung «nicht in der Galerie zeigen» überstimmt aber jede Rolle.

Zusätzlich lässt sich pro Archiv einschränken, welche Bestände die Galerie
überhaupt zeigt — getrennt für intern und öffentlich.

## Bilder aus der Galerie nehmen

Die Markierung wird in der Medienverwaltung unter **Admin → Medien** gesetzt.
Sie ist der richtige Weg für Bilder, die zwar erschlossen, aber nicht
schaufensterwürdig sind — Rückseiten, Fehlbelichtungen, technische Aufnahmen.

Für Bilder, die aus rechtlichen Gründen nicht gezeigt werden dürfen, ist
dagegen die [Schutzfrist](access.md) oder das Sperren des Mediums das richtige
Mittel: Die Galerie-Markierung ist eine Anzeigeentscheidung, keine
Zugangsbeschränkung.
