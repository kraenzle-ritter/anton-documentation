# Markdown

In Anton lassen sich die Texte in den Textfeldern mit der Auszeichnungssprache [Markdown](https://de.wikipedia.org/wiki/Markdown) formatieren. Markdown ist einfach und schnell zu erlernen. Ausserdem bleiben die Textdaten relativ sauber, weil nur sehr wenige zusätzliche Zeichen und Konventionen die Formatierungen ermöglichen. 

[ [Ausführliche Informationen](https://www.markdownguide.org/basic-syntax/) ]


Die wichtigsten Formatierungsmöglichkeiten in Anton:

### Neue Zeilen, neue Absätze

Neue Zeilen werden mit zwei Leerzeichen am Ende einer Linie angezeigt. 

Neue Absätze durch eine Leerzeile.

### Titel 

Titel können mit `#` am Zeilenbeginn erstellt werden, wobei ein `#` und ein folgendes Leerzeichen einen Titel der ersten Ebene, zwei `##` und ein folgendes Leerzeichen einen Titel der zweiten Ebene markiert, usw.:

```markdown
# Titel Ebene 1
## Titel Ebene 2
```
Ergibt: 
<div class="myframe">
<h1>Titel Ebene 1</h1>
<h2>Titel Ebene 2</h2>
</div>

### Aufzählungen

Aufzählungen können mit `-` oder `*` am Zeilenbeginn oder wenn nummeriert mit `1.`, `2.` mit nachfolgendem Leerzeichen erstellt werden. Auch Unterpunkte sind möglich, die dann eingerückt werden.

```markdown
- Griechische Philosohen
    - Aristoteles
    - Platon
- Römische Philosophen
    - Cicero
```

### Externe Links 

Der Text, der verlinkt werden soll, wird in eckige Klammern gesetzt. Das Ziel des Links in runde Klammern dahinter.

```markdown
[Dieser Text wird verlinkt](https://ziel_des_links.ch)
```

### Verweise innerhalb von Anton 

Die Verweise innerhalb von Anton funktionieren wie die Links. Als Ziel wird die jeweilige relative URL angegeben:

```markdown
[Anton](/actors/2)
```

Der Verweis führt dann auf den Akteur mit der ID 2. Ganz ähnlich lassen sich
Verzeichnungseinheiten verlinken; das Ziel ist dann `/objects/123`.

### Signaturen werden automatisch verlinkt

Signaturen müssen in der Regel gar nicht von Hand verlinkt werden: Wird in einem
Textfeld eine Signatur erwähnt, erkennt Anton sie in der **Detailansicht** und
macht daraus einen Verweis auf die Suche. In der Bearbeitungsansicht bleibt der
Text unangetastet, damit er bearbeitbar bleibt.

!!! note "Nicht in jedem Archiv"
    Die Erkennung stützt sich auf ein Suchmuster, das pro Archiv hinterlegt ist.
    Ist keines konfiguriert, bleiben Signaturen im Text unverlinkt.

### Hervorhebungen

Für Hervorhebungen können `*kursiv*` (*kursiv*) oder `**` (**fett**) oder `***` (***fett und kursiv***) verwendet werden. 
