# Kommentare

Kommentare sind interne Arbeitsnotizen an einer Verzeichnungseinheit — für
alles, was zum Datensatz gehört, aber keine Erschliessungsinformation ist:
«Die Person auf dem Foto ist vermutlich Hans Meier», «Die Datierung stimmt
nicht», «Bildausschnitt prüfen».

Wie damit gearbeitet wird, beschreibt [Kommentare](../user/comments.md) —
diese Seite behandelt die Einrichtung.

## Kommentar oder Textfeld?

Beides sind Textbereiche am Datensatz, und sie erfüllen verschiedene Zwecke.

| | Textfeld | Kommentar |
|---|---|---|
| Teil der Erschliessung | ja | nein |
| im Objektformular bearbeitbar | ja | nein, eigener Bereich |
| Verfasser:in und Datum | nein | ja |
| Status offen/erledigt | nein | ja |
| in Exporten | je nach Feld | **nie** |
| im Volltext auffindbar | ja | nein |

Faustregel: Was jemand von aussen über Ihr Archiv erfahren soll, ist ein
Textfeld. Was Ihre Mitarbeitenden untereinander festhalten oder noch
abarbeiten müssen, ist ein Kommentar.

## Einschalten

Kommentare sind ausgeschaltet, solange Sie nichts tun. Nach einem Update
ändert sich in Ihrem Archiv nichts.

Es gibt dafür **eine einzige Einstellung**. Unter *Administration →
Einstellungen*:

| Einstellung | Werte | Vorgabe |
|---|---|---|
| `comments_min_role` | leer, `user`, `user_intern`, `loan_admin`, `editor`, `admin` | **leer** |

**Leer heisst aus.** Kein Kommentarbereich, keine Arbeitsliste, nichts zu
sehen. Sobald Sie eine Rolle eintragen, sind Kommentare eingeschaltet — und
die eingetragene Rolle ist zugleich die **niedrigste, die schreiben darf**.

Ein unbekannter Wert (Tippfehler) gilt als leer, also als ausgeschaltet.
Anton rät hier nicht auf die freizügigere Seite.

!!! note "Das Feld ist bereits im Formular"
    Beim Update auf v0.86 legt Anton das Feld «Kommentare» an und stellt es
    ans Ende Ihres **internen Detailformulars**. Solange die Einstellung leer
    ist, zeichnet es nichts — Sie sehen also nichts, bis Sie es wollen.

    Wo der Bereich steht, bestimmen weiterhin Sie: im
    [Formular-Editor](forms.md) lässt er sich verschieben, in weitere
    Formulare aufnehmen oder ganz entfernen. Haben Sie ihn einmal verschoben
    oder entfernt, rührt ein späteres Update die Platzierung nicht mehr an.

## Wer sieht was

| Rolle | sieht | schreibt | abhaken | Arbeitsliste |
|---|---|---|---|---|
| nicht angemeldet | – | – | – | – |
| `user` (extern) | nur eigene | ab Mindestrolle | – | – |
| `user_intern`, `loan_admin`, `editor` | alle | ab Mindestrolle | ja | ja |
| `admin` | alle | ja | ja | ja |

Eigene Kommentare darf jede Person ändern und löschen, fremde nur die
Administration.

!!! important "Die Vorgabe lässt externe Beiträge zu"
    Mit `comments_min_role = user` darf jede **angemeldete** Person einen
    Hinweis hinterlassen — der Fall «Auf diesem Foto ist mein Grossvater».
    Solche Personen sehen ausschliesslich ihre eigenen Beiträge, nie die
    Ihres Teams, und können nichts abhaken.

    Wollen Sie das nicht, setzen Sie die Mindestrolle auf `user_intern`. Dann
    bleiben Kommentare vollständig unter Ihren Mitarbeitenden.

    Nicht angemeldete Besucher:innen können unter keinen Umständen
    kommentieren oder Kommentare sehen.

## Missbrauchsschutz

Weil auch externe Personen schreiben können, gilt:

* **Reiner Text.** Kein Markdown, kein HTML — anders als bei Textfeldern.
* **Höchstens 5000 Zeichen** pro Kommentar.
* **Höchstens 20 Kommentare pro Konto und Stunde.**
* In der Arbeitsliste steht bei jedem Eintrag die **Rolle** der verfassenden
  Person, so ist ein externer Beitrag sofort erkennbar.

Eine Freischaltung braucht es nicht: Externe Beiträge sind für andere externe
Personen ohnehin unsichtbar. Die Administration kann jeden Kommentar löschen.

## Wo Kommentare nicht auftauchen

* In **keinem Export** — nicht in EAD, EAD3, TEI, Dublin Core, RDF oder DIP.
  Einzige Ausnahme ist der SQL-Dump, der definitionsgemäss ein vollständiges
  Backup der Datenbank ist. Siehe [Export-Matrix](export-matrix.md).
* In **keiner öffentlichen Ansicht**.
* **Nicht im Volltext** des Datensatzes. Kommentare finden Sie über die
  Arbeitsliste, nicht über die normale Suche — sonst mischten sich
  Arbeitsnotizen unter die Treffer Ihrer Recherchen.

## Was Kommentare nicht können

Keine Antworten auf Kommentare, keine Zuweisung an bestimmte Personen, keine
Benachrichtigungen. Es gibt offen und erledigt, mehr nicht — das deckt das
Abarbeiten ab, ohne einen Arbeitsablauf zu erzwingen.
