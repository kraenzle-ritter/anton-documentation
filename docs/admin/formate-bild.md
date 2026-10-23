# Bilder: Formate und wesentliche Eigenschaften

Diese Seite legt für Rasterbilder fest, in welchen Formaten Anton sie bevorzugt und akzeptiert, welche Eigenschaften eines Bildes erhalten bleiben müssen und was Anton davon heute misst oder prüft. Sie ist die erste Seite einer Reihe je Formatkategorie (anton#687); [PDF](formate-pdf.md) ist geschrieben, Text, Audio und Video folgen. Vektorgrafiken gehören nicht hierher.

Was hier steht, braucht Anton für drei Dinge: um zu dokumentieren, was ein Bild ausmacht (NDSA Cn-1.1), um zu prüfen, ob es das noch tut (Cn-2.1), und um nach einer Migration zu belegen, dass nichts Wesentliches verloren ging ([`media:migrate`](console-commands.md#mediamigrate)).

## Formate {#formate}

| Stufe | Format | Bedingung |
|---|---|---|
| bevorzugt | TIFF mit Deflate (ZIP) und Predictor 2 | Graustufen und Farbe, 8 oder 16 Bit je Kanal |
| akzeptiert | TIFF in anderer Form | unkomprimiert, LZW, CCITT G4 (bitonal), JPEG-komprimiert, BigTIFF, mehrseitig |
| akzeptiert | JPEG | |
| akzeptiert | PNG | |
| akzeptiert | JPEG 2000 (JP2) | |
| akzeptiert | HEIC/HEIF | bleibt Master, Nutzungskopie JPEG |
| akzeptiert | GIF, BMP, WebP | |
| akzeptiert | DNG | |
| akzeptiert | Kamera-RAW (CR2, CR3, NEF, ARW und andere) | solange LibRaw sie liest |
| akzeptiert | PDF/A | wenn es nur Bilder enthält, etwa Scans ohne Textschicht oder mit OCR-Schicht |
| akzeptiert | PDF | wenn es ausschliesslich Fotos enthält |

**Bevorzugt** heisst: Das empfiehlt Anton Ablieferstellen, und dahin packt die Regel [`tiff_zip`](preservation.md#regeln-fuer-dateien) unkomprimierte TIFF und LZW ohne Predictor verlustfrei um. Deflate mit Predictor 2 spart gegenüber unkomprimiert 38–66 %, ohne dass sich ein Pixel ändert, und libtiff, ImageMagick, GIMP und Photoshop lesen es. Es gehört aber nicht zum Baseline-TIFF; die KOST empfiehlt Baseline mit LZW oder CCITT. Bitonale Bilder bleiben besser bei CCITT G4, das sie stärker verdichtet; `tiff_zip` lässt sie darum aus.

**Akzeptiert** ist, was sich mit verbreiteten, quelloffenen Werkzeugen lesen lässt und voraussichtlich lesbar bleibt. Anton übernimmt die Datei und behält sie in ihrem Format. Nach den [Formatentscheiden](preservation.md#formatentscheide) migriert Anton erst, wenn sich eine Datei nicht mehr darstellen lässt. Bereits verlustbehaftet komprimierte Bilder (JPEG, JPEG-komprimiertes TIFF, verlustbehaftetes JP2) werden nicht in ein verlustfreies Format umgewandelt: Die verlorene Information kommt nicht zurück, die Datei würde nur grösser (so auch die KOST).

Grundsätzlich empfehlen wir, in einem Archiv möglichst wenige verschiedene Formate zu führen, damit das Preservation Planning auf lange Sicht einfach bleibt: Jedes Format will beobachtet, geprüft und irgendwann vielleicht migriert werden (so auch die KOST). Die Liste der akzeptierten Formate sagt, was Anton erhalten kann, nicht, was ein Archiv sammeln soll. Wo ein Bestand viele Formate mitbringt, wird darum möglichst vor der Übernahme normalisiert: durch die Ablieferstelle oder mit den [Regeln für Dateien](preservation.md#regeln-fuer-dateien), die Anton anwendet, bevor die Datei zum Master wird. Ausgenommen sind verlustbehaftete Bilder (siehe oben).

PDF steht hier, weil manche Bildbestände als PDF ankommen. Sobald ein PDF Text, Formulare oder Links trägt, gilt die Seite für [PDF](formate-pdf.md).

HEIC/HEIF, wie es Mobiltelefone liefern, bleibt als Master, wie es ist; Anton rechnet nur die Nutzungskopie in JPEG um. So empfiehlt es die NARA, solange sich die Datei gut darstellen lässt. HEIF ist ein offener ISO-Standard (ISO/IEC 23008-12), freie Werkzeuge (libheif, libde265) lesen es; der Haken ist die Kompression HEVC mit ihren Patentpools, weshalb Windows, Photoshop und manche Browser HEIC nicht ohne Weiteres öffnen. HEIC ist kleiner als ein JPEG daraus, und jede Umwandlung verliert, was neben dem Hauptbild in der Datei steckt (Tiefenkarte, HDR-Gain-Map). Bei der Übernahme lässt sich HEIC nach JPEG umwandeln, für Archive, bei denen Speicher teuer ist und die Datei überall aufgehen soll, mit einer zweiten verlustbehafteten Kodierung; das bietet heute der [QR-Upload](../user/qr-upload.md) an (`heic2jpg`, voreingestellt aus). Das HEIC bleibt dabei als Version des Mediums erhalten, und die Umwandlung steht als Ereignis mit Werkzeug, Befehl und Prüfsummen im Protokoll. Nach TIFF lässt sich jederzeit später umwandeln, ohne weiteren Verlust, aber etwa zehnmal grösser, mit [`media:migrate`](console-commands.md#mediamigrate), sobald es die Regel dafür gibt; HEIC nach TIFF oder nach JPEG soll je Archiv als Regel wählbar werden (anton#710).

GIF, BMP und WebP lesen alle gängigen Werkzeuge und Browser. Die NARA rät bei BMP zur Umwandlung; nach dem Grundsatz oben bleibt es, bis sich das ändert. DNG ist eine offene Spezifikation von Adobe auf TIFF-Basis; die NARA stuft es als geringes Risiko ein, die KOST hält es für die Langzeitarchivierung nicht für geeignet. Kamera-RAW ist je Hersteller und Modell eigen und nicht offengelegt; quelloffen liest es LibRaw, das dafür seit vielen Jahren gepflegt wird. Die NARA rät zur Umwandlung, und wer kann, liefert besser DNG oder TIFF ab. Anton erkennt Kamera-RAW an der Endung, weil die Werkzeuge NEF, ARW und DNG für TIFF halten, und rechnet die Nutzungskopie über LibRaw aus dem ganzen Bild, nicht aus dem eingebetteten Vorschaubild. DNG und Kamera-RAW kommen heute nur über SIP oder Import ins Archiv, nicht über den Upload.

Ein TIFF aus RAW verliert etwas: RAW enthält die Sensordaten, und erst bei der Entwicklung werden Weissabgleich, Belichtung und Tonkurve festgelegt. Ein TIFF hält eine dieser Entwicklungen fest, und der Rest der Sensordaten fehlt danach. Was davon erhalten bleiben muss, hängt davon ab, was das Archiv erhalten will:

- **Das fertige Bild:** Dann genügt das entwickelte TIFF als Master.
- **Das Material, mit allen Möglichkeiten der späteren Bearbeitung:** Dann muss RAW oder DNG bleiben, etwa bei einem Fotografennachlass.

## Wesentliche Eigenschaften

Gegliedert wie bei der NARA in Erscheinung, Struktur, Verhalten und Kontext. Die Spalte «Quelle» nennt, wer die Eigenschaft für wesentlich hält; die Quellen stehen [unten](#quellen).

| Gruppe | Eigenschaft | Quelle |
|---|---|---|
| Erscheinung | Breite und Höhe in Pixeln, damit das Seitenverhältnis | InSPECT, NARA |
| | Bittiefe und Zahl der Kanäle, einschliesslich Alphakanal | InSPECT, NARA |
| | Farbraum und ICC-Profil | NARA, LoC |
| | Ausrichtung (EXIF Orientation) | NARA |
| | Pixelinhalt, wo das Format verlustfrei ist | Anton |
| Struktur | Auflösung in dpi (bei Scans der Massstab zum Original) | InSPECT, NARA |
| | Seitenzahl bei mehrseitigem TIFF | LoC, KOST |
| | Kompression: festhalten, nicht erhalten | NARA, KOST |
| Verhalten | Das Bild lässt sich darstellen. | NARA |
| | bei GIF und WebP die Animation | LoC |
| Kontext | eingebettete Metadaten (EXIF, IPTC, XMP), etwa Aufnahmedatum, Urheber:in, Rechte | NARA |

Der Farbraum zählt hier, anders als bei InSPECT. InSPECT hielt ihn nicht für wesentlich, weil er sich bei fast jeder Migration ändert. Bei Scans von Fotos, Plakaten und Karten ist die Farbe aber Inhalt, und Anton migriert ohnehin nur bei Bedarf. Ändert eine Migration den Farbraum, muss sie das ICC-Profil mitführen.

Die Kompression ist keine Eigenschaft, die erhalten bleiben muss. Sie wird festgehalten, weil sie sagt, ob die anderen Eigenschaften verlustfrei vorliegen.

Kein wesentliches Verhalten sind Ebenen, Bearbeitungsschritte und Vorschaubilder im TIFF: Sie gehören zur Software, mit der das Bild entstand, nicht zum Bild.

## Was Anton misst und prüft

Stand: Version 0.111, dazu anton#710 und #711 aus der nächsten Version.

| Eigenschaft | Gemessen | Geprüft |
|---|---|---|
| Breite und Höhe | TIFF bei der Übernahme mit exiftool, wenn `tiff_zip` eingeschaltet ist | über die Pixelsignatur nach `tiff_zip` und `media:migrate` |
| Bittiefe und Kanäle | ebenso | ebenso |
| Farbraum und ICC-Profil | ebenso (Name des Profils) | nein |
| Ausrichtung | nein | nein |
| Pixelinhalt | Pixelsignatur je Seite mit ImageMagick, nur bei `tiff_zip` und `media:migrate` | ja, muss gleich bleiben, sonst bleibt die gelieferte Datei |
| Auflösung | nein | nein |
| Seitenzahl | TIFF mit exiftool, wie oben, Vorschaubilder getrennt | über die Pixelsignatur je Seite |
| Kompression | TIFF mit exiftool, wie oben | – |
| Darstellbar | – | bei der Übernahme und nachts mit [`media:validate-formats`](console-commands.md#mediavalidate-formats): TIFF mit tiffinfo (gründlich: `-D`); JPEG, PNG, JP2, GIF, BMP, WebP, HEIC/HEIF, DNG und Kamera-RAW mit ImageMagick, das jedes Pixel dekodiert, nicht nur den Kopf liest; dazu beim Erstellen der Nutzungskopie |
| Eingebettete Metadaten | nein | `tiff_zip` überträgt sie mit exiftool, vergleicht sie aber nicht |

Gemessene Werte stehen am Medium unter **Technische Merkmale** und im Probelauf vor einem Tabellen-Import.

## Grenzen

- Für JPEG, PNG, JP2, HEIC, GIF, BMP, WebP, DNG und Kamera-RAW hält Anton keine Merkmale fest, nur PUID, MIME-Typ und Grösse. Ebenso für TIFF aus SIPs und für TIFF in Archiven, die `tiff_zip` nicht eingeschaltet haben.
- Ausrichtung und Auflösung misst Anton bei keinem Format.
- Eingebettete Metadaten werden bei `tiff_zip` übertragen, aber nicht verglichen. Ob nach einer Migration alle Felder noch da sind, belegt nichts.
- Ob ein PDF ausschliesslich Fotos enthält, prüft Anton nicht.
- HEIC nach TIFF oder nach JPEG lässt sich noch nicht je Archiv als Regel wählen; heute wandelt nur `heic2jpg` im QR-Upload (anton#710).
- DNG und Kamera-RAW nimmt der Upload nicht an, nur SIP und Import.
- Die Prüfung «darstellbar» heisst, das Werkzeug liest die Datei ohne Fehler. Ob die Farben stimmen, prüft sie nicht.

## Was eine Migration prüfen muss

Wandelt `media:migrate` ein Bild um, muss danach gelten:

- Breite, Höhe, Seitenzahl, Bittiefe und Kanäle sind gleich.
- Bei verlustfreiem Ziel ist die Pixelsignatur jeder Seite gleich.
- Das ICC-Profil ist mitgeführt, oder die Umrechnung ist im Ereignis festgehalten.
- Die eingebetteten Metadaten sind übertragen.
- Die gelieferte Datei bleibt als [Original](preservation.md#behaltene-originale), wenn das Ziel verlustbehaftet ist.

Heute prüft `media:migrate` nur die Pixelsignatur. Bei verlustfreiem Ziel deckt sie den ersten und den zweiten Punkt ab, die übrigen nicht.

## Quellen

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Digital Still Image](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/PreservationActionPlan_PDFs/NARA_PreservationActionPlan_DigitalStillImage_20250604.pdf), Plan Date 2025-06-04 ([Markdown-Fassung](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_DigitalStillImage.md) mit Stand 2024-11, dieselben Eigenschaften). Wesentliche Eigenschaften in vier Gruppen, bevorzugte und akzeptierte Formate.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Übernahmeformate, auf die der Plan verweist.
- Lynne Montague, Adrian Brown, Gareth Knight, Stephen Grace: [InSPECT, Significant Properties Testing Report: Raster Images](https://significantproperties.kdl.kcl.ac.uk/rasterimages-testingreport.html), King's College London, 2009 ([PDF auf Figshare](https://figshare.com/articles/journal_contribution/InSPECT_Significant_Properties_Testing_Report_Raster_Images/7137803)). Eigenschaften aus NISO Z39.87 abgeleitet und an Migrationen zwischen TIFF, JPEG und GIF erprobt.
- NISO Z39.87, Data Dictionary – Technical Metadata for Digital Still Images, und das XML-Schema dazu: [MIX, Library of Congress](https://www.loc.gov/standards/mix/). Das Vokabular der technischen Bildmetadaten.
- Library of Congress, Sustainability of Digital Formats: [Still Image, Quality and Functionality Factors](https://www.loc.gov/preservation/digital/formats/content/still_quality.shtml). Darstellung, Auflösung, Farbtreue, Spektralbänder, Funktionen über die Darstellung hinaus.
- KOST, Katalog archivischer Dateiformate (KaD), Version 7.1, Mai 2026: [Bild, Zusammenfassung](https://kost-ceco.ch/cms/kad_image_intro_de.html) und [TIFF](https://kost-ceco.ch/cms/kad_tiff_de.html). Empfohlene und akzeptierte Bildformate, archivtaugliches TIFF, keine sofortige Umwandlung verlustbehafteter Bilder.
- NARA: [Preservation Action Plan, Format-Tabelle](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), Stand 2026-03-20. Risiko und Handlung je Format, darunter HEIC («Moderate Risk», belassen, solange gut darstellbar).
- Library of Congress, Sustainability of Digital Formats: [HEIF (fdd000525)](https://loc.gov/preservation/digital/formats/fdd/fdd000525.shtml), dazu HEIC (fdd000526). Offenlegung, Verbreitung, Patente auf HEVC.
- [LibRaw](https://www.libraw.org/): quelloffene Bibliothek zum Lesen von Kamera-RAW.
- Archivematica 1.17: [Preservation planning](https://www.archivematica.org/en/docs/archivematica-1.17/user-manual/preservation/preservation-planning/). Zum Vergleich: Erkennung mit Siegfried, Charakterisierung mit ExifTool, keine festgelegten wesentlichen Eigenschaften, nach der Normalisierung keine Prüfung auf Eigenschaften.
- NDSA: [Levels of Digital Preservation, Version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), März 2026, Anforderungen Cn-1.1 und Cn-2.1.
