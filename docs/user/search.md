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
    Für angemeldete Benutzer:innen ab der Rolle `user_intern` werden zusätzlich durchsucht:

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

!!! note "Phrasen im Dokumententext"
    Führt das Archiv den Volltext **verdichtet** (Einstellung
    `optimize_fulltext`), stehen im Index nur die ersten Vorkommen jedes Wortes
    — Phrasen sind im Text von PDFs dann nur eingeschränkt auffindbar. Die
    Suche nach einzelnen Wörtern bleibt davon unberührt. Ob das zutrifft, weiss
    die Administration; siehe [Suchfelder](../admin/searchfields.md).

### Begriffe mit Bindestrich

Begriffe mit Bindestrich (z. B. `Arp-Hagenbach`) werden automatisch wie eine Phrase behandelt: gesucht wird nach beiden Teilen direkt nebeneinander.

## Was nicht funktioniert

- **Begriffe unter 3 Zeichen** werden ignoriert (`ag`, `zb`).
- **Sehr häufige kurze Wörter** wie „und", „der", „die" sind aus dem Suchindex der Datenbank ausgeschlossen (sogenannte Stopwörter).
- **Suche in der Wortmitte** ist nicht möglich (siehe oben).

## Boolesche Volltextsuche

Neben dem gewöhnlichen Suchfeld gibt es in der erweiterten Suche das Feld
**«Boolesche Volltextsuche»**. Es durchsucht dieselben Inhalte, versteht aber
Verknüpfungen — und verhält sich in einem Punkt **umgekehrt** zum normalen Feld.

!!! warning "Blosse Wörter sind hier ODER, nicht UND"
    Im gewöhnlichen Suchfeld müssen alle eingegebenen Wörter vorkommen. Im
    booleschen Feld genügt eines: `Maur Gemeinde` findet Datensätze mit «Maur»
    **oder** «Gemeinde». Wer beide verlangt, schreibt `Maur AND Gemeinde`.

### Die Operatoren

| Eingabe | Bedeutung |
|---|---|
| `Maur Gemeinde` | eines von beiden genügt |
| `Maur AND Gemeinde` | beide müssen vorkommen |
| `Maur OR Gemeinde` | ausdrücklich eines von beiden (die Vorgabe) |
| `Maur NOT Gemeinde` | «Maur», aber ohne «Gemeinde» |
| `+Maur -Gemeinde` | dasselbe in Kurzschreibweise |
| `"Feuerwehr Maur"` | die Wortfolge genau so |
| `Gemeinde*` | alle Wörter, die mit «Gemeinde» beginnen |

`AND`, `OR` und `NOT` schreibt man in Grossbuchstaben. Sie wirken auf beide
Seiten: `Maur AND Gemeinde` verlangt auch «Maur», nicht nur «Gemeinde». Ein
ausdrückliches Vorzeichen gewinnt gegen ein vorangehendes `AND` — `Maur AND
-Gemeinde` bleibt ein Ausschluss.

### Platzhalter

Der Stern steht **nur am Wortende**: `Gemeinde*` findet «Gemeindearchiv».
Voranstellen hilft nicht — bei `*archiv` wird der Stern entfernt und es bleibt
die gewöhnliche Suche nach «archiv», die Wörter mit diesem Anfang findet, nicht
Wörter mit dieser Endung. Innerhalb eines Wortes hat er keine Wirkung.

### Kurze Wörter

Wörter unter drei Zeichen stehen in keinem Suchindex der Datenbank. Anders als
im gewöhnlichen Feld fallen sie hier aber **nicht** aus der Suche: Anton sucht
sie stattdessen als Zeichenfolge im Text. `FC Maur` findet also, was es finden
soll — «FC» wird dabei auch mitten im Wort gefunden, weil diese Suche keine
Wortgrenzen kennt.

### Was das Feld nicht kann

- **Klammern** zur Gruppierung werden entfernt. `(a OR b) AND c` lässt sich
  nicht ausdrücken.
- **Ein einzelnes Anführungszeichen** wird verworfen statt als Fehler gemeldet:
  aus `"Feuerwehr` wird die gewöhnliche Suche nach «Feuerwehr».

## Abgrenzung zur Gewichteten Suche

Die Volltextsuche durchsucht **Archivobjekte**. Die [Gewichtete Suche](weighted-search.md) ist eine andere Funktion und betrifft die Listenansichten von **Akteur:innen, Orten und Schlagwörtern** — dort werden Treffer nach Relevanz sortiert.
