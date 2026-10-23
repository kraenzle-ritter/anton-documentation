# Tabellen und Präsentationen: Formate und wesentliche Eigenschaften

Diese Seite legt für Tabellen und Präsentationen fest, in welchen Formaten Anton sie bevorzugt und akzeptiert, welche Eigenschaften erhalten bleiben müssen und was Anton davon heute misst oder prüft. Sie gehört zur Reihe je Formatkategorie (anton#687), nach den [Bildern](formate-bild.md), [PDF](formate-pdf.md), [Text](formate-text.md) sowie [Audio und Video](formate-av.md). Datenbanken gehören nicht hierher.

Was hier steht, braucht Anton für drei Dinge: um zu dokumentieren, was eine Tabelle oder Präsentation ausmacht (NDSA Cn-1.1), um zu prüfen, ob sie das noch tut (Cn-2.1), und um nach einer Migration zu belegen, dass nichts Wesentliches verloren ging ([`media:migrate`](console-commands.md#mediamigrate)).

## Formate {#formate}

### Tabellen

| Stufe | Format | Bedingung |
|---|---|---|
| bevorzugt | ODS (OpenDocument Spreadsheet) | ohne Passwort |
| bevorzugt | XLSX | ohne Passwort |
| bevorzugt | CSV in UTF-8 | für reine Daten, mit Beschreibung |
| akzeptiert | XLS | solange LibreOffice es liest |
| akzeptiert | PDF/A | nur als zusätzliche Ansicht neben dem Original |

### Präsentationen

| Stufe | Format | Bedingung |
|---|---|---|
| bevorzugt | ODP (OpenDocument Presentation) | ohne Passwort |
| bevorzugt | PDF/A-2u | wo die Folien fest sind; siehe [PDF](formate-pdf.md) |
| akzeptiert | PPTX, PPT | solange LibreOffice sie liest |

**Tabellen:** Bevorzugt sind ODS und XLSX im Originalformat. Nur dort bleiben Formeln, versteckte Zeilen und Blätter erhalten; die KOST empfiehlt beide und rät von einer Umwandlung zwischen ihnen ab. ODS steht vorn, wie ODT bei [Text](formate-text.md#formate); die NARA bevorzugt es und stuft es mit geringem Risiko ein, XLSX mit mittlerem. XLS liest LibreOffice; die KOST rät, es nach XLSX umzuwandeln, die NARA nur bei Fassungen vor Excel 97. Nach dem Grundsatz bleibt es, bis es sich nicht mehr lesen lässt. Für reine Daten ohne Formeln und Formatierung ist CSV in UTF-8 das dauerhafteste Format; die NARA bevorzugt es. Weil CSV keinen festen Standard hat und sich nicht prüfen lässt, liefert die Ablieferstelle eine Beschreibung mit: Trennzeichen, Maskierung von Trennzeichen und Zeilenumbrüchen, Anführungszeichen, Zahl der Felder, Kodierung und Datentypen (KOST). PDF/A hält nur die Erscheinung, nicht die Rechnung, und eine Umwandlung nach PDF/A muss «sogar sehr kritisch beurteilt werden» (KOST): als Ansicht neben dem Original, nicht an seiner Stelle.

**Präsentationen:** Bevorzugt ist ODP, wie ODT und ODS; die NARA bevorzugt es, die KOST lehnt ODP ab, aus denselben Gründen wie ODT. Wo die Folien fest sind, etwa bei einem Vortrag, der so gehalten wurde, liefert die Ablieferstelle besser zusätzlich PDF/A-2u. PPTX stuft die NARA mit geringem Risiko ein, die KOST akzeptiert es. Keynote liest LibreOffice nur unvollständig; die Ablieferstelle exportiert es als PPTX oder PDF.

Das Original bleibt bei beiden Master. Anton wandelt bei der Übernahme nicht um.

Auch hier gilt: Ein Archiv führt [möglichst wenige Formate](formate-bild.md#formate). Die Ablieferstelle liefert ohne Passwort und Schreibschutz und schaltet die automatische Aktualisierung von Datumsfeldern aus.

## Wesentliche Eigenschaften

Gruppiert wie bei der NARA nach Erscheinung, Struktur, Verhalten und Kontext. Die Prüffragen sind dieselben wie bei [Text](formate-text.md#wesentliche-eigenschaften); bei Tabellen fragt die NARA zusätzlich, ob das Entfernen eines Blatts den Inhalt verändert.

### Tabellen

| Gruppe | Eigenschaft | Quelle |
|---|---|---|
| Erscheinung | Formatierung, wo sie etwas aussagt (bedingte Formatierung, Farbcodes) | NARA |
| | Diagramme und Grafiken | NARA |
| | Kommentare | NARA |
| | Pivot-Tabellen | NARA |
| Struktur | Werte jeder Zelle | NARA |
| | Blätter mit ihren Namen | NARA |
| | Zahl der Zeilen und Spalten, auch der versteckten | NARA |
| | Zeichenkodierung und, bei CSV, Trennzeichen und Maskierung | NARA, KOST |
| Verhalten | Formeln, wo sie erklären, wie gerechnet wurde, oder eine Pivot-Tabelle von ihnen abhängt | NARA, KOST |
| | Verweise innerhalb der Datei | NARA |
| Kontext | Verweise auf andere Dateien und Datenquellen: festgehalten | NARA |

Wesentlich ist nach der NARA zuerst der Wert in der Zelle, nicht die Formel: «The final data in the cell itself is the core feature». Die Formel zählt, wo sie den Wert erklärt. Nicht erhalten werden müssen Makros und fixierte Zeilen oder Spalten. Verweise auf andere Dateien oder ins Web hält Anton fest; ihr Ziel bewahrt das Archiv nur, wenn es mitgeliefert wurde.

### Präsentationen

| Gruppe | Eigenschaft | Quelle |
|---|---|---|
| Erscheinung | Folien und ihre Reihenfolge | NARA |
| | Text, Tabellen, Bilder und Grafiken | NARA |
| | Seitengrösse und Ausrichtung, Schriften, Farbe, wo die Folien fest sind | NARA |
| | eingebettetes Audio und Video | NARA |
| Struktur | Sprechernotizen | NARA |
| | Gliederung | NARA |
| Verhalten | Verweise innerhalb der Datei | NARA |
| Kontext | eingebettete Metadaten (Titel, Autor, Daten, Sprache) | NARA |

Sprechernotizen zählen, wenn sie enthalten, was nicht auf den Folien steht; das ist oft so. Animationen und Übergänge müssen nicht erhalten bleiben, solange die Folien ohne sie vollständig und lesbar sind (NARA).

## Was Anton misst und prüft

Stand: Version 0.111.1.

| Eigenschaft | Gemessen | Geprüft |
|---|---|---|
| Format | PRONOM-PUID mit Siegfried, wie bei allen Dateien | Widerspruch zwischen Endung, MIME-Typ und PUID als Warnung |
| Öffnen lässt es sich | – | nein, die Formatprüfung kennt keine Tabellen und Präsentationen |
| Text | XLSX und PPTX für den Volltext (nicht mit `fulltext-from-webpdf`); ODS, ODP, XLS, PPT und CSV nicht (anton#719) | nein |
| Zeichenkodierung (CSV) | nein (anton#719) | nein |
| alle übrigen Eigenschaften | nein | nein |

## Grenzen

- Für Tabellen entsteht keine Nutzungskopie; sie erscheinen als Download unter «Weitere Dateien». Das ist entschieden: Eine Tabelle als PDF zerfällt bei breiten Blättern über viele Seiten und zeigt versteckte Zeilen nicht.
- Für Präsentationen entsteht noch keine Nutzungskopie; geplant ist eine PDF-Kopie über LibreOffice wie bei Text (anton#719). Sie zeigt die Folien, nicht die Sprechernotizen.
- ODS, ODP, XLS, PPT und CSV kommen nicht in den Volltext (anton#719).
- Der Upload nimmt XLSX, XLS und CSV an, ODS nur zum Teil, PPTX, PPT und ODP nicht (anton#719).
- Bei CSV hält Anton weder Kodierung noch Trennzeichen fest (anton#719).
- Ob eine Tabelle Formeln, versteckte Zeilen, Makros oder Verweise auf andere Dateien enthält, misst Anton nicht.

## Was eine Migration prüfen muss

Anton kennt noch keine Regel, die Tabellen oder Präsentationen umwandelt. Kommt eine, etwa XLS nach XLSX, muss danach gelten:

- Tabellen: Die Werte jeder Zelle sind gleich, in allen Blättern; Zahl der Blätter, Zeilen und Spalten ist gleich, versteckte eingeschlossen; Formeln und Kommentare sind übernommen.
- Präsentationen: Zahl und Reihenfolge der Folien sind gleich; Sprechernotizen und eingebettete Medien sind übernommen.
- Die eingebetteten Metadaten sind übernommen.
- Die abgelieferte Datei bleibt als [Original](preservation.md#behaltene-originale).

## Quellen {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Spreadsheets](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_Spreadsheets.md), Plan Date 2023-11-22. Wesentliche Eigenschaften, Prüffragen, Werte vor Formeln, Zählwerte, Übernahmeformate.
- NARA: [Preservation Action Plan for Presentation and Publishing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_PresentationAndPublishing.md), Plan Date 2023-12-05. Folienreihenfolge, Sprechernotizen, Animationen, Übernahmeformate.
- NARA: [Preservation Action Plan, Format-Tabelle](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), Stand 2026-03-20. Risiko und Handlung je Format: ODS, ODP, CSV, PPTX gering; XLSX, XLS mittel; alte XLS nach ODS; Keynote nach PPTX oder PDF.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Übernahmeformate, auf die sich die Pläne beziehen.
- KOST, Katalog archivischer Dateiformate (KaD), Version 7.1, Mai 2026: [Tabellenkalkulation, Zusammenfassung](https://kost-ceco.ch/cms/kad_spreadsheet_intro_de.html), [CSV](https://kost-ceco.ch/cms/kad_csv_de.html) und [Text, Zusammenfassung](https://kost-ceco.ch/cms/kad_text_intro_de.html) (zu PPTX und ODP). Originalformat als vorläufige Lösung, keine Umwandlung zwischen XLSX und ODS, PDF/A kritisch, Beschreibung von CSV.
- [LibreOffice](https://www.libreoffice.org/): quelloffene Bürosoftware, liest ODS, XLSX, XLS, ODP, PPTX und PPT.
- NDSA: [Levels of Digital Preservation, Version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), März 2026, Anforderungen Cn-1.1 und Cn-2.1.
