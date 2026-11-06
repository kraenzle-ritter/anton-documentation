# Namen abgleichen mit OpenRefine

Anton bietet für Akteur:innen einen Abgleichdienst nach der [Reconciliation-API](https://reconciliation-api.github.io/specs/latest/). So lassen sich Namen aus einer Tabelle in [OpenRefine](https://openrefine.org/) den Einträgen eines Archivs zuordnen.

## Einrichten

1. In OpenRefine in der Spalte mit den Namen **Reconcile → Start reconciling** wählen.
2. **Add Standard Service** wählen und die Adresse des Archivs eintragen:

    ```
    https://<archiv>/api/actors/reconcile.json
    ```

3. Unter den Typen zum Beispiel **Person** oder **Körperschaft** wählen, oder ohne Typ abgleichen, und **Start Reconciling** drücken.

Gesucht wird nur in den Akteur:innen dieses Archivs. Bei einem öffentlichen Archiv braucht es keine Anmeldung; ist es nicht öffentlich, antwortet der Dienst mit 401.

## Ergebnis

Je Zeile schlägt Anton Einträge mit einer Punktzahl von 0 bis 100 vor. Automatisch zugeordnet wird nur ein eindeutiger, exakter bester Treffer, alle anderen Zeilen entscheidet man in OpenRefine. Der Name eines Vorschlags führt zur Seite des Eintrags.

## Grenzen

- Höchstens 50 Abfragen je Anfrage und 25 Treffer je Abfrage, ohne Angabe 5.
- Der Dienst deckt nur Akteur:innen ab, nicht Orte und Schlagworte.
- Er vergleicht nur den Namen: Weitere Spalten wie Lebensdaten oder GND-Nummer fliessen nicht ein.
- Daten aus Anton in die Tabelle nachladen (Data Extension) und Vorschläge beim Tippen (Suggest) gibt es nicht.

## Direkt abfragen

```bash
curl -X POST https://<archiv>/api/actors/reconcile \
  --data-urlencode 'queries={"q0":{"query":"Muster, Anna","type":"person","limit":3}}'
```
