# Tektonik und Verschieben

Alle Verzeichnungseinheiten hängen in einer Baumstruktur, der Tektonik. Jede
Einheit hat genau eine übergeordnete Einheit — mit Ausnahme der Archive auf
oberster Ebene.

## Verzeichnungsstufen

Die Stufen folgen ISAD(G) und bestimmen, was unter einer Einheit angelegt werden
darf:

| Stufe | Zulässige Untereinheiten |
|---|---|
| Archiv | Bestandsgruppe, Bestand |
| Bestandsgruppe | Bestandsgruppe, Bestand |
| Bestand | Serie, Klasse, Dossier, Einzelstück |
| Klasse | Serie, Klasse, Dossier, Einzelstück |
| Serie | Serie, Dossier, Einzelstück |
| Dossier | Dossier, Einzelstück |
| Einzelstück | Einzelstück |

Ein Bestand innerhalb eines Bestands ist nicht zulässig und wird von Anton
abgewiesen.

## Navigation im Baum

Anton stellt die Tektonik nicht als aufklappbaren Baum dar, sondern zweiteilig:

- Über jedem Datensatz steht der **Pfad** — die Kette der übergeordneten
  Einheiten, treppenartig eingerückt und verlinkt.
- Unter der Detailansicht steht der Abschnitt **Inhalt** mit der Liste der
  untergeordneten Einheiten.

## Datensätze verschieben

Verschoben wird in zwei Schritten: zuerst wird der Datensatz vorgemerkt, dann
das Ziel angesteuert.

1. Auf dem zu verschiebenden Datensatz die Taste **Verschieben** anklicken. Es
   erscheint ein gelbes Band mit dem Hinweis «Zu verschiebender Datensatz» samt
   Signatur und Titel. Mit dem ✕ im Band lässt sich der Vorgang abbrechen.
2. Zum Zieldatensatz navigieren. Das Band bleibt dabei sichtbar.
3. Im Band die gewünschte Stelle wählen: **vor**, **in** oder **hinter** diesen
   Datensatz.

!!! tip "Kein Link im Band sichtbar?"
    Die Links erscheinen nur, wenn die Verzeichnungsstufe an der Zielstelle
    zulässig ist. Ein Dossier lässt sich nicht «in» ein Einzelstück verschieben —
    dort bietet das Band keine Auswahl an. Ein Blick auf die Tabelle oben zeigt,
    ob die gewünschte Stelle überhaupt möglich ist.

Mehrere Datensätze lassen sich gemeinsam verschieben; ihre Reihenfolge bleibt am
Ziel erhalten. Archive auf oberster Ebene können nicht verschoben werden. Ebenso
wenig lässt sich ein Datensatz in seinen eigenen Teilbaum verschieben — Anton
weist dies ab und überspringt den betroffenen Datensatz.

Beim Verschieben ändert sich die Signatur **nicht**. Sie ist nach dem Verschieben
gegebenenfalls von Hand anzupassen.
