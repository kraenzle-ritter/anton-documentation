# PDF: Formate und wesentliche Eigenschaften

Diese Seite legt für PDF fest, welche Fassungen Anton bevorzugt und akzeptiert, welche Eigenschaften eines PDF erhalten bleiben müssen und was Anton davon heute misst oder prüft. Sie gehört zur Reihe je Formatkategorie (anton#687), nach den [Bildern](formate-bild.md). Textformate wie DOCX, ODT und TXT erhalten eine eigene Seite; PDF, das nur Fotos enthält, behandelt die Seite für Bilder.

Was hier steht, braucht Anton für drei Dinge: um zu dokumentieren, was ein PDF ausmacht (NDSA Cn-1.1), um zu prüfen, ob es das noch tut (Cn-2.1), und um nach einer Migration zu belegen, dass nichts Wesentliches verloren ging ([`media:migrate`](console-commands.md#mediamigrate)).

## Formate {#formate}

| Stufe | Format | Bedingung |
|---|---|---|
| bevorzugt | PDF/A-2u | |
| bevorzugt | PDF/A-2b | für Scans mit OCR |
| akzeptiert | PDF/A-1a, PDF/A-1b, PDF/A-2a | |
| akzeptiert | PDF/A-4 | ohne eingebettete Dateien (nicht 4f) |
| akzeptiert | PDF 1.0 bis 1.7, PDF 2.0 | Schriften eingebettet; ohne Passwort zu öffnen |
| nicht akzeptiert | PDF/A-3, PDF/A-4f | eingebettete Dateien beliebigen Typs |
| nicht akzeptiert | PDF, das sich nur mit Passwort öffnen lässt | |

**Bevorzugt** ist PDF/A-2u. PDF/A-2 erlaubt, was PDF/A-1 noch verbot (Transparenz, Ebenen, JPEG 2000), und «u» verlangt, dass jedes Zeichen einem Unicode-Zeichen zugeordnet ist: Der Text lässt sich dann suchen, kopieren und vorlesen, nicht nur ansehen. So empfiehlt es die KOST. Bei Scans stammt der Text aus der OCR und ist ohnehin nur so gut wie die Erkennung; dort genügt PDF/A-2b, das nur die Erscheinung der Seite sichert. Die NARA führt PDF/A-1 und PDF/A-2 als bevorzugte Übernahmeformate.

**Akzeptiert** ist, wie bei den Bildern, was sich mit verbreiteten, quelloffenen Werkzeugen lesen lässt und voraussichtlich lesbar bleibt. Gewöhnliches PDF gehört dazu: Die NARA stuft PDF 1.7 und 2.0 mit geringem, PDF 1.0 bis 1.6 mit mittlerem Risiko ein und belässt beide, die KOST hält PDF «grundsätzlich» für archivtauglich. Anton wandelt PDF bei der Übernahme nicht nach PDF/A um. Nach den [Formatentscheiden](preservation.md#formatentscheide) migriert Anton erst, wenn sich eine Datei nicht mehr darstellen lässt, und eine Umwandlung nach PDF/A ist nach der KOST auch später «meist problemlos» möglich.

**Nicht akzeptiert** ist PDF/A-3. Es gleicht PDF/A-2, darf aber Dateien beliebigen Typs einbetten, etwa ein Word-Dokument oder eine Excel-Tabelle hinter einer Rechnung. Diese Dateien lassen sich weder erkennen noch prüfen, und Anton sieht sie nicht: Sie hätten weder PUID noch Formatprüfung noch Nutzungskopie. Die KOST lehnt PDF/A-3 aus diesem Grund ab. Dasselbe gilt für PDF/A-4f. Ablieferstellen liefern stattdessen PDF/A-2 und die eingebetteten Dateien als eigene Dateien. Kommt ein PDF/A-3 trotzdem an, nimmt Anton es heute an wie jedes PDF; ob es Dateien einbettet, misst Anton noch nicht (anton#713).

Ein PDF, das sich nur mit Passwort öffnen lässt, kann Anton weder prüfen noch darstellen. Ein PDF, das nur das Drucken oder Kopieren sperrt, lässt sich öffnen; es ist akzeptiert, und Anton hält die Verschlüsselung als Risiko fest.

Auch hier gilt: Ein Archiv führt [möglichst wenige Formate](formate-bild.md#formate). Wer PDF selbst erzeugt, etwa beim Scannen oder beim Export aus einer Textverarbeitung, wählt PDF/A-2. Die Ablieferstelle bettet alle Schriften ein, vermeidet JavaScript, Verschlüsselung, eingebettetes Audio und Video sowie die Kompression JBIG2: Ihre verlustbehaftete Mustererkennung kann Zeichen unbemerkt vertauschen, etwa eine 6 durch eine 8.

## Wesentliche Eigenschaften

Gruppiert wie bei der NARA nach Erscheinung, Struktur, Verhalten und Kontext. Die NARA unterscheidet, ob ein Dokument wegen seines Inhalts oder als Beweis seiner Form aufbewahrt wird. Bei einem Protokoll zählt der Text, bei einer Publikation, einem Plan oder einer Urkunde auch, wie die Seite aussieht. Die Tabelle trennt darum zwei Stufen: «immer» und «bei fester Erscheinung».

| Gruppe | Eigenschaft | Stufe | Quelle |
|---|---|---|---|
| Erscheinung | Zahl und Folge der Seiten | immer | NARA |
| | Bilder und Grafiken | immer | NARA |
| | Formulare und Anmerkungen | immer | NARA |
| | Seitengrösse und Ausrichtung | bei fester Erscheinung | NARA |
| | Schriften mit Schnitt und Grösse | bei fester Erscheinung | NARA, KOST |
| | Farbe | bei fester Erscheinung | NARA, KOST |
| Struktur | Text, der sich extrahieren lässt, in Unicode | immer | NARA, KOST |
| | Lesezeichen (Gliederung) | immer | NARA |
| | eingebettete Dateien | immer | NARA, KOST |
| Verhalten | Das PDF lässt sich darstellen. | immer | NARA |
| | Verweise innerhalb des Dokuments | immer | NARA |
| Kontext | eingebettete Metadaten (XMP, Titel, Autor, Datum, Sprache) | immer | NARA |

Eingebettete Dateien stehen hier, obwohl PDF/A-3 nicht akzeptiert ist: Auch ein gewöhnliches PDF kann Anhänge tragen, und wo sie vorkommen, gehören sie zum Dokument.

Nicht erhalten werden müssen JavaScript, Aktionen, die Programme starten (`/Launch`), und Verweise auf andere Dateien (`/GoToR`) oder ins Web (`/URI`). Sie führen aus der Datei hinaus, und ihr Ziel bewahrt das Archiv nicht. Anton hält sie als Risiko fest, damit sichtbar ist, was in einer Migration wegfällt. Dasselbe gilt für die Verschlüsselung.

Die Fassung (PDF 1.4, PDF/A-2b) ist keine Eigenschaft, die erhalten bleiben muss. Sie wird festgehalten, weil sie sagt, was das PDF verspricht und wogegen es geprüft wird.

## Was Anton misst und prüft

Stand: Version 0.111.

| Eigenschaft | Gemessen | Geprüft |
|---|---|---|
| Zahl der Seiten | bei jeder Formatprüfung mit qpdf bzw. pdftocairo | nein, es gibt noch keine Migration von PDF |
| Darstellbar | – | bei der Übernahme und nächtlich mit [`media:validate-formats`](console-commands.md#mediavalidate-formats): qpdf; gründlich mit pdftocairo Seite für Seite, Fehler bei JPEG 2000 prüft MuPDF nach; auch beim Erzeugen der Nutzungskopie |
| Schriften eingebettet | – | Warnung, wo das PDF Text zeigt, der eine nicht eingebettete Schrift braucht (pdffonts) |
| Seitengrösse und Ausrichtung | nein (anton#713) | nein |
| Text extrahierbar | nein (anton#713) | nein |
| Eingebettete Dateien | nein (anton#713) | nein |
| JBIG2 | nein (anton#713) | nein |
| Formulare | nein | Warnung bei einem Formular ohne Felder |
| Lesezeichen, Anmerkungen, Metadaten | nein | nein |
| JavaScript, Aktionen, Verweise | Anzahl je Art (qpdf, pdfinfo) | Warnung |
| Verschlüsselung | ja | Warnung |
| PDF/A-Konformität | Stufe, die das PDF beansprucht | mit veraPDF, wenn ein PDF sich als PDF/A ausgibt und veraPDF installiert ist; eine Abweichung ist eine Warnung |

Die Befunde stehen im Ereignis `format-validation` des Mediums und, zusammengezählt, unter [Preservation Planning → «Formatprüfung»](preservation-planning.md#formatpruefung).

## Grenzen

- Anton misst Seitengrösse, extrahierbaren Text, eingebettete Dateien und JBIG2 nicht (anton#713). Darum lässt sich auch nicht sagen, wie viele PDF/A-3 mit Anhängen im Bestand liegen.
- veraPDF prüft nur, was sich als PDF/A ausgibt. Ein gewöhnliches PDF wird nicht gegen PDF/A geprüft, und ein PDF/A, das seine Kennung im XMP verloren hat, auch nicht.
- Die OCR im [QR-Upload](../user/qr-upload.md) und im Stapel-Upload schreibt gewöhnliches PDF, nicht PDF/A-2b (anton#712).
- Die Nutzungskopie (Ghostscript, `/ebook`) verkleinert Bilder für die Ansicht. Sie ist keine Normalisierung und kein Ersatz für den Master.
- «Darstellbar» heisst, die Werkzeuge lesen und rendern jede Seite ohne Fehler. Ob die Seite richtig aussieht, prüfen sie nicht.

## Was eine Migration prüfen muss

Anton kennt noch keine Regel, die PDF umwandelt. Kommt eine, etwa PDF nach PDF/A-2, muss danach gelten:

- Die Zahl der Seiten ist gleich.
- Seitengrösse und Ausrichtung jeder Seite sind gleich.
- Der extrahierbare Text ist gleich, abgesehen von Leerraum.
- Alle Schriften sind eingebettet.
- veraPDF bestätigt die Ziel-Fassung.
- Formulare, Anmerkungen, Lesezeichen und Metadaten sind übernommen, oder ihr Wegfall ist im Ereignis festgehalten.
- Die abgelieferte Datei bleibt als [Original](preservation.md#behaltene-originale), denn Ghostscript schreibt Schriften und Bilder neu.

## Quellen

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Textual and Word Processing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_TextualAndWordProcessing.md), Plan Date 2023-11-22. Wesentliche Eigenschaften in vier Gruppen, die Unterscheidung nach Inhalt und Beweiswert, bevorzugte und akzeptierte Übernahmeformate.
- NARA: [Preservation Action Plan for Presentation and Publishing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_PresentationAndPublishing.md), Plan Date 2023-12-05. Dieselben Eigenschaften für Publikationen, dazu eingebettetes Audio und Video.
- NARA: [Preservation Action Plan, Format-Tabelle](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), Stand 2026-03-20. Risiko und Handlung je PDF-Fassung.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Übernahmeformate, auf die sich die Pläne beziehen.
- KOST, Katalog archivischer Dateiformate (KaD), Version 7.1, Mai 2026: [Text, Zusammenfassung](https://kost-ceco.ch/cms/kad_text_intro_de.html), [PDF](https://kost-ceco.ch/cms/kad_pdf_de.html), [PDF/A-2](https://kost-ceco.ch/cms/kad_pdfa2_de.html) und [PDF/A-3](https://kost-ceco.ch/cms/kad_pdfa3_de.html). Empfohlene und akzeptierte Fassungen, PDF/A-2u, Ablehnung von PDF/A-3, Bedingungen für gewöhnliches PDF, JBIG2.
- [veraPDF](https://verapdf.org/): quelloffener Prüfer für PDF/A, von der PDF Association und der Open Preservation Foundation.
- Archivematica 1.17: [Preservation planning](https://www.archivematica.org/en/docs/archivematica-1.17/user-manual/preservation/preservation-planning/). Zum Vergleich: Die Format Policy Registry sieht für PDF eine Normalisierung nach PDF/A mit Ghostscript vor, jedes Archiv kann das ändern; wesentliche Eigenschaften legt Archivematica nicht fest, und nach der Normalisierung prüft es keine.
- NDSA: [Levels of Digital Preservation, Version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), März 2026, Anforderungen Cn-1.1 und Cn-2.1.
