## Orte


### Geokoordinaten

Anton unterstützt die Erfassung und Verwaltung von geografischen Koordinaten für Orte (Punkte). Das System kann verschiedene Koordinatenformate automatisch verarbeiten und in einem einheitlichen Format speichern. Besitzt ein Ort Geokooridnaten, wird in der Detailansicht eine Karte mit der Lokalisierung angezeigt.


#### Unterstützte Koordinatenformate

**1. WGS84 (Dezimalgrad)** - Standard für GPS und Online-Karten  
Format: `Breitengrad Längengrad` | Beispiel: `47.3769 8.5417` (Zürich)

**2. Schweizer Landeskoordinaten LV95** - Aktuelles CH-System  
Format: `Rechtswert Hochwert` | Beispiel: `2683141 1247637` oder `2'683'141 1'247'637`

**3. Schweizer Landeskoordinaten LV03** - Früheres CH-System  
Format: `Rechtswert Hochwert` | Beispiel: `683141 247637`

!!! info "Automatische Konvertierung"
    Anton erkennt das Format automatisch und konvertiert alle Koordinaten in WGS84.

#### Eingabe in Anton

##### Über Geonames
1. Ort erstellen oder bearbeiten
2. In der rechten Spalte Ort mit Geonames identifizieren
3. Kooridnaten werden automatisch übernommen

##### Über das Orte-Formular
1. Ort erstellen oder bearbeiten
2. Im Feld "Koordinaten" die Werte eingeben
3. Format wird automatisch erkannt und konvertiert

##### Unterstützte Eingabeformate
- Mit oder ohne Vorzeichen
- Mit oder ohne Tausendertrennzeichen (`'` oder ` `)
- Durch Leerzeichen oder Komma getrennt
- Dezimalstellen optional
