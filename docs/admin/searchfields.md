# Suchfelder

Welche Felder die **erweiterte Suche** anbietet, ist pro Archiv konfigurierbar.
Gesteuert wird das über die Einstellungen `searchfields` (intern) und
`search_fields_extern` (öffentlich) — die Trennung erlaubt, Aussenstehenden
weniger Suchmöglichkeiten zu geben als dem Archiv selbst.

## Die vollständige Liste

Die Einstellungen enthalten ein JSON-Objekt. Wer nur einzelne Felder ergänzen
oder entfernen will, geht am einfachsten von der vollständigen Liste aus. Die
eigene Installation gibt sie unter folgender Adresse aus:

```
https://<eigene-installation>/admin/searchfields
```

Von dort lässt sich der gewünschte Ausschnitt übernehmen. Als Referenz dient
auch die [Testinstallation](https://kr.anton.ch/admin/searchfields).

!!! note "Leer heisst Standard"
    Ist die Einstellung leer, verwendet Anton die eingebaute Vorgabe. Ein
    eigenes JSON ersetzt sie **vollständig** — es ist keine Ergänzung. Wer nur
    ein Feld hinzufügen will, übernimmt deshalb die ganze Liste und ergänzt es
    dort.

## Verhältnis zu den Formularen

Die Suchfelder sind Teil des Formularsystems: Sie stehen in eigenen
Formularsätzen für die interne und die öffentliche Suche. Die Beschriftung
eines Suchfelds folgt derselben Logik wie bei den
[Formularen](forms.md) — sie lässt sich überschreiben, sonst greift die
Übersetzung des Feldnamens.

## Volltext und schnelle Suche

Die erweiterte Suche ist nur einer von drei Wegen. Die
[Volltextsuche](../user/search.md) durchsucht einen zusammengefassten Index über
alle relevanten Felder und wird nicht über die Suchfelder gesteuert; die
[schnelle Suche](typesense.md) hat eine eigene Konfiguration.

### Verdichteter Volltext (`optimize_fulltext`)

Der gespeicherte Volltext lässt sich **verdichten**: Anton wirft dabei jede
Wortwiederholung weg und behält nur das erste Vorkommen. Das hält die Spalte
klein — bei Beständen mit PDF-Volltext macht der Dokumententext den weitaus
grössten Teil aus.

Der Preis ist die **Phrasensuche**. Wer verdichtet, verliert jede Nachbarschaft
zweier Wörter, die nicht schon beim ersten Vorkommen bestand: `"rudolf leder"`
findet den Datensatz dann nur, wenn die beiden Wörter zufällig gerade dort
nebeneinander standen. Die Suche nach einzelnen Wörtern bleibt unberührt.

Wer die Einstellung ändert, muss den Index **neu aufbauen** — verdichtet
gespeichert ist verdichtet, die Einstellung wirkt nur beim Schreiben:

```bash
php artisan anton:update-fulltext --env={slug}
```
