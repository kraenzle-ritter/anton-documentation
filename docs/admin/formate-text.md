# Text: Formate und wesentliche Eigenschaften

Diese Seite legt für Textdokumente fest, in welchen Formaten Anton sie bevorzugt und akzeptiert, welche Eigenschaften erhalten bleiben müssen und was Anton davon heute misst oder prüft. Sie gehört zur Reihe je Formatkategorie (anton#687), nach den [Bildern](formate-bild.md) und [PDF](formate-pdf.md). Tabellen (XLSX, ODS, CSV) und Präsentationen (PPTX, ODP) stehen auf einer [eigenen Seite](formate-tabellen.md).

Was hier steht, braucht Anton für drei Dinge: um zu dokumentieren, was ein Textdokument ausmacht (NDSA Cn-1.1), um zu prüfen, ob es das noch tut (Cn-2.1), und um nach einer Migration zu belegen, dass nichts Wesentliches verloren ging ([`media:migrate`](console-commands.md#mediamigrate)).

## Formate {#formate}

| Stufe | Format | Bedingung |
|---|---|---|
| bevorzugt | ODT (OpenDocument Text) | ohne Passwort |
| bevorzugt | PDF/A-2u | wenn die Erscheinung zählt; siehe [PDF](formate-pdf.md) |
| bevorzugt | TXT in UTF-8 | für reinen Text |
| akzeptiert | DOCX | ohne Passwort |
| akzeptiert | TXT in anderer Kodierung | ASCII, ISO-8859, UTF-16 |
| akzeptiert | DOC, RTF | solange LibreOffice sie liest |

**Bevorzugt** ist ODT: ein offener ISO-Standard (ISO/IEC 26300), den die NARA in allen Versionen bevorzugt und mit geringem Risiko einstuft. Die KOST lehnt ODT dagegen ab, wegen nicht eingebetteter Schriften, Makros und geringer Verbreitung; dieselben Mängel nennt sie bei DOCX, das sie trotzdem akzeptiert. Anton folgt hier der NARA. Wo die Erscheinung zählt, etwa bei einer Urkunde oder einer Publikation, liefert die Ablieferstelle besser PDF/A-2u, denn ein Textdokument hat keine festen Seiten. Reiner Text ist am dauerhaftesten als TXT in UTF-8.

**Akzeptiert** ist, wie bei den Bildern, was sich mit verbreiteten, quelloffenen Werkzeugen lesen lässt und voraussichtlich lesbar bleibt; für Textdokumente ist das LibreOffice. DOCX stuft die NARA mit geringem Risiko ein, die KOST hält es für «denkbar», wenn sich seine Mängel meistern lassen. DOC und RTF stuft die NARA mit mittlerem bzw. meist geringem Risiko ein und rät zur Umwandlung, DOC nach ODT, RTF nach PDF mit behaltenem Original. Nach dem Grundsatz bleiben sie, bis sie sich nicht mehr lesen lassen. TXT in anderer Kodierung als UTF-8 ist akzeptiert, wenn die Kodierung bekannt ist und festgehalten wird; die Datei selbst nennt sie nicht (KOST).

Ein Textdokument hat keine festen Seiten. Seitenumbruch und Erscheinung entstehen erst beim Öffnen, mit den Schriften, die der Rechner gerade hat. Was bei PDF «bei fester Erscheinung» heisst, kann ein Textdokument nicht sicher halten. Darum bleibt das Original Master, und Anton wandelt bei der Übernahme nicht um, auch nicht nach PDF/A, wie es die KOST für die aktive Phase empfiehlt: Eine Umwandlung verliert Änderungsverfolgung, Kommentare und Felder.

Auch hier gilt: Ein Archiv führt [möglichst wenige Formate](formate-bild.md#formate). Die Ablieferstelle verwendet Standardschriften, liefert ohne Passwort und Schreibschutz und schaltet die automatische Aktualisierung von Datumsfeldern aus: Sonst überschreibt das Öffnen im Archiv das Datum des Dokuments (KOST).

## Wesentliche Eigenschaften {#wesentliche-eigenschaften}

Gruppiert wie bei der NARA nach Erscheinung, Struktur, Verhalten und Kontext, mit derselben Unterscheidung wie bei [PDF](formate-pdf.md#wesentliche-eigenschaften): Wird ein Dokument wegen seines Inhalts aufbewahrt, zählt der Text; wird es als Beweis seiner Form aufbewahrt, zählt auch, wie es aussieht.

| Gruppe | Eigenschaft | Stufe | Quelle |
|---|---|---|---|
| Erscheinung | Text mit Absätzen, Listen und Tabellen | immer | NARA |
| | Bilder und Grafiken | immer | NARA |
| | Fussnoten, Kopf- und Fusszeilen | immer | NARA |
| | Seitengrösse und Ausrichtung | bei fester Erscheinung | NARA |
| | Schriften mit Schnitt, Grösse und Auszeichnung | bei fester Erscheinung | NARA, KOST |
| | Farbe | bei fester Erscheinung | NARA |
| Struktur | Zeichenkodierung | immer | NARA, KOST |
| | Gliederung (Überschriften) | immer | NARA |
| | Verweise innerhalb des Dokuments | immer | NARA |
| | eingebettete Objekte | immer | NARA, KOST |
| Verhalten | Das Dokument lässt sich öffnen. | immer | NARA |
| | Änderungsverfolgung und Kommentare | immer, wo vorhanden | NARA |
| Kontext | eingebettete Metadaten (Titel, Autor, Erstellungs- und Änderungsdatum, Sprache) | immer | NARA |

Änderungsverfolgung und Kommentare sind oft unsichtbar, wenn man das Dokument öffnet, können aber Inhalt sein: eine gestrichene Passage, ein Einwand am Rand. Eine Umwandlung nach PDF verliert sie oder druckt sie mit, je nach Einstellung.

Nicht erhalten werden müssen Makros und Felder, die sich beim Öffnen aktualisieren (Datum, Seitenzahl, Verzeichnis). Sie führen Code aus oder verändern das Dokument; erhalten bleibt der Wert, den sie bei der Ablieferung zeigten. Die NARA rät, Makros vor dem Entfernen auf ihre Funktion zu prüfen. Die Zählwerte der NARA (Wörter, Zeichen, Absätze, Tabellen, Grafiken) sind keine Eigenschaften, die erhalten bleiben müssen, sondern ein Hilfsmittel, um nach einer Umwandlung die Vollständigkeit zu prüfen.

## Was Anton misst und prüft

Stand: Version 0.111.1.

| Eigenschaft | Gemessen | Geprüft |
|---|---|---|
| Format | PRONOM-PUID mit Siegfried, wie bei allen Dateien | Widerspruch zwischen Endung, MIME-Typ und PUID als Warnung |
| Öffnen lässt es sich | – | nur mittelbar: Die Formatprüfung kennt keine Textformate, aber für ODT, DOCX, DOC und RTF muss LibreOffice das Dokument lesen, um die Nutzungskopie zu erzeugen, und diese wird wie ein PDF geprüft |
| Zeichenkodierung (TXT) | Kodierung, Byte Order Mark und Zeilenenden mit libmagic bei der Übernahme | – |
| Text | für den Volltext: ODT und DOCX direkt, DOC und RTF aus der PDF-Nutzungskopie (mit `fulltext-from-webpdf` auch DOCX); TXT und Markdown, nach UTF-8 gewandelt | nein |
| alle übrigen Eigenschaften | nein | nein |

## Grenzen

- Für TXT entsteht als Nutzungskopie der Text in UTF-8 (iconv); der Master bleibt unverändert. Für ODT, DOCX, DOC und RTF rechnet LibreOffice eine PDF-Nutzungskopie (anton#714); das Dokument erscheint dann unter «Dokumente» im PDF-Viewer. Auf einem Server ohne LibreOffice entsteht keine, und das Dokument bleibt ein Download unter «Weitere Dateien». Ältere Dokumente erhalten die Kopie erst mit [`media:conversions`](console-commands.md).
- Die Nutzungskopie ist eine Ansicht, kein Beleg der Erscheinung. LibreOffice stellt DOCX nicht immer so dar wie Word: Schriften, Seitenumbruch, Tabellen und Felder können abweichen.
- Der Upload nimmt ODT, DOCX, DOC, RTF und TXT an; der QR-Upload nur Bilder und PDF.
- Für TXT, das vor Version 0.111.1 übernommen wurde, ist die Kodierung nicht festgehalten; Volltext und Nutzungskopie bestimmen sie, wenn sie entstehen.
- libmagic erkennt eine Kodierung nur nach Wahrscheinlichkeit. ISO-8859-1 und unbekannte 8-Bit-Kodierungen liest Anton als Windows-1252, das mit ISO-8859-1 übereinstimmt, wo dieses definiert ist, und dazu typografische Anführungszeichen und Striche kennt.
- Die Formatprüfung erfasst Textformate nicht. Ob ein DOCX oder ODT beschädigt ist, merkt Anton erst, wenn es sich nicht öffnen lässt.
- Ob ein Dokument Makros, automatische Felder, Änderungsverfolgung oder eingebettete Objekte enthält, misst Anton nicht.

## Was eine Migration prüfen muss

Anton kennt noch keine Regel, die Textdokumente umwandelt. Kommt eine, etwa DOC nach ODT oder DOCX nach PDF/A-2u, muss danach gelten:

- Der Text ist gleich, abgesehen von Leerraum; die Zählwerte (Wörter, Absätze, Tabellen, Grafiken) stimmen überein.
- Bilder, Tabellen, Fussnoten, Kopf- und Fusszeilen sind übernommen.
- Änderungsverfolgung und Kommentare sind übernommen, oder ihr Wegfall ist im Ereignis festgehalten.
- Die eingebetteten Metadaten, besonders die Daten, sind übernommen und nicht durch das Datum der Umwandlung ersetzt.
- Die abgelieferte Datei bleibt als [Original](preservation.md#behaltene-originale).

## Quellen {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Textual and Word Processing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_TextualAndWordProcessing.md), Plan Date 2023-11-22. Wesentliche Eigenschaften in vier Gruppen, Prüffragen nach Inhalt und Beweiswert, Zählwerte, bevorzugte und akzeptierte Übernahmeformate.
- NARA: [Preservation Action Plan, Format-Tabelle](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), Stand 2026-03-20. Risiko und Handlung je Format: TXT, ODT und DOCX gering, behalten; DOC mittel, nach ODT; RTF nach PDF mit behaltenem Original.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Übernahmeformate, auf die sich der Plan bezieht.
- KOST, Katalog archivischer Dateiformate (KaD), Version 7.1, Mai 2026: [Text, Zusammenfassung](https://kost-ceco.ch/cms/kad_text_intro_de.html), [TXT](https://kost-ceco.ch/cms/kad_txt_de.html), [OOXML](https://kost-ceco.ch/cms/kad_ooxml_de.html) und [ODF](https://kost-ceco.ch/cms/kad_odf_de.html). Empfohlen PDF/A, akzeptiert TXT und DOCX, abgelehnt ODT; Risiken der Textverarbeitungsformate (Felder, Schriften, Makros, Verschlüsselung), Zeichenkodierung bei TXT.
- [LibreOffice](https://www.libreoffice.org/): quelloffene Bürosoftware, liest ODT, DOCX, DOC und RTF.
- NDSA: [Levels of Digital Preservation, Version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), März 2026, Anforderungen Cn-1.1 und Cn-2.1.
