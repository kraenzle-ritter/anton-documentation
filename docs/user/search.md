# Volltextsuche

Die Volltextsuche durchsucht alle relevanten Felder der Archivdatensätze gleichzeitig: Titel, Signaturen, Textfelder, verknüpfte Akteur:innen, Orte und Schlagwörter — und auch den per OCR erkannten Text aus PDFs und Bildern.

## Was wird durchsucht

Pro Archivobjekt werden für die Suche zusammengefasst:

- **Titel** des Objekts und aller übergeordneten Einheiten (Bestand → Serie → Dossier → Dokument)
- **Signaturen** (aktuelle und alte) sowie die interne ID
- **Bezeichnungen** der Erschliessungsebene, des Objekttyps, des Standorts
- **Datierungen**
- **Verknüpfte Schlagwörter** in allen vorhandenen Sprachvarianten
- **Verknüpfte Orte**
- **Verknüpfte Akteur:innen** (nur öffentlich sichtbare)
- **Textfelder**, die im externen Formular sichtbar sind
- **OCR-Text** aus Medien (PDFs, Bilder)

!!! note "Erweiterte Sicht für interne Bearbeitende"
    Für angemeldete interne Bearbeiter:innen werden zusätzlich durchsucht:

    - private Akteur:innen
    - alle Textfelder (auch nur intern sichtbare)
    - als privat markierte Objekte

## Suchverhalten

### Wortanfänge werden automatisch erkannt

Wildcards (`*`) sind nicht nötig — die Suche findet automatisch alle Wörter, die mit dem eingegebenen Suchbegriff **beginnen**.

| Suche | Findet |
|---|---|
| `alkohol` | „Alkohol", „Alkoholverbot", „alkoholisch" |
| `müller` | „Müller", „Müller-Weber", „Müllers" |

!!! warning "Aber nicht in der Wortmitte"
    `kohol` findet **nicht** „Alkohol". Die Suche greift nur am Wortanfang.

### Mehrere Wörter werden mit UND verknüpft

| Suche | Findet |
|---|---|
| `alkohol verbot` | Datensätze, in denen **beide** Begriffe vorkommen — sie können beliebig weit auseinander stehen |

### Anführungszeichen für exakte Phrasen

| Suche | Findet |
|---|---|
| `"rudolf leder"` | Nur Datensätze, in denen diese Wortfolge **genau so** vorkommt |
| `#rudolf leder#` | Identisch — `#` ist eine Alternativnotation für `"` |

Bei einer Phrase wird **nicht** automatisch nach Wortanfängen gesucht — die Phrase muss exakt vorkommen.

!!! warning "Sehr kurze Wörter werden auch in Phrasen ignoriert"
    Wörter unter 3 Zeichen und einige englische Stopwörter (`the`, `for`, `and`) fallen auch innerhalb von Anführungszeichen aus dem Vergleich. Eine Phrase wie `"AG Reinach"` matcht damit faktisch nur „Reinach".

### Begriffe mit Bindestrich

Begriffe mit Bindestrich (z. B. `Arp-Hagenbach`) werden automatisch wie eine Phrase behandelt: gesucht wird nach beiden Teilen direkt nebeneinander.

## Was nicht funktioniert

- **Begriffe unter 3 Zeichen** werden ignoriert (`ag`, `zb`).
- **Sehr häufige kurze Wörter** wie „und", „der", „die" sind aus dem Suchindex der Datenbank ausgeschlossen (sogenannte Stopwörter).
- **Suche in der Wortmitte** ist nicht möglich (siehe oben).

## Abgrenzung zur Gewichteten Suche

Die Volltextsuche durchsucht **Archivobjekte**. Die [Gewichtete Suche](weighted-search.md) ist eine andere Funktion und betrifft die Listenansichten von **Akteur:innen, Orten und Schlagwörtern** — dort werden Treffer nach Relevanz sortiert.
