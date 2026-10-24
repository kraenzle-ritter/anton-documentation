# Formatliste

Die Formatliste sagt, welche Formate ein Archiv bevorzugt und akzeptiert, Format für Format nach PRONOM-PUID. Anton prüft jede Datei bei der Übernahme dagegen (anton#690).

- **Vorgabe:** Ohne eigene Liste gilt die Liste von k & r. Sie ist die maschinenlesbare Fassung der Format-Seiten ([Bilder](formate-bild.md), [PDF](formate-pdf.md), [Text](formate-text.md), [Audio und Video](formate-av.md), [Tabellen und Präsentationen](formate-tabellen.md), [Container und XML](formate-uebrige.md)). Es sind Antons eigene Regeln; wo NARA und KOST auseinandergehen, etwa bei ODT und DOCX, folgt sie der NARA.
- **Eigene Liste:** Unter **Admin → Preservation Planning → Formatliste** sieht ein Admin die geltende Liste, die Medien ausserhalb davon und kann eine eigene Liste speichern: Stufen ändern, Einträge entfernen, eigene PUIDs hinzufügen. Die eigene Liste ersetzt die Vorgabe ganz; ein Knopf führt zur Vorgabe zurück. Jede Änderung steht im Sicherheitsprotokoll.
- **Warnen, nicht abweisen:** Steht das Format einer Datei nicht auf der Liste oder ist es nicht akzeptiert, übernimmt Anton sie trotzdem. Wer sie hochgeladen hat, sieht nach dem Speichern einen Hinweis (beim QR-Upload auf der Upload-Seite), und am Medium steht das Ereignis «Formatliste» als gelbe Prüfung. Bei Excel-, SIP- und Verzeichnisimport gibt es nur das Ereignis.
- **Gleiche PUID, verschiedene Bedingungen:** Ein PUID unterscheidet nicht alles, was die Format-Seiten unterscheiden. TIFF mit Deflate und TIFF mit LZW haben denselben PUID; die Prüfung nimmt die beste Stufe. Bedingungen wie «ohne Passwort» stehen nur als Text da.
- **Archivdateien:** Wird ein ZIP, GZ oder TAR als Verzeichnis importiert, wird jede entpackte Datei geprüft; als Datei gespeichert, sieht Anton nicht hinein.

Die Tabellen unten sind aus Anton erzeugt (`scripts/gen-format-list.py`), PUIDs nach der DROID-Signaturdatei V125.

<!-- BEGIN generated format list -->

### Bilder

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| bevorzugt | TIFF mit Deflate (ZIP) und Predictor 2 | Graustufen und Farbe, 8 oder 16 Bit je Kanal | `fmt/353` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | TIFF in anderer Form | unkomprimiert, LZW, CCITT G4, JPEG-komprimiert, BigTIFF, mehrseitig | `fmt/353`, `fmt/1917`, `x-fmt/387`, `x-fmt/388`, `x-fmt/399` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | JPEG |  | `fmt/41`, `fmt/42`, `fmt/43`, `fmt/44`, `x-fmt/398`, `x-fmt/390`, `x-fmt/391`, `fmt/645`, `fmt/1507` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | PNG |  | `fmt/11`, `fmt/12`, `fmt/13`, `fmt/935` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | JPEG 2000 (JP2) |  | `x-fmt/392` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | HEIC/HEIF | bleibt Master, Nutzungskopie JPEG | `fmt/1101` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | GIF, BMP, WebP |  | `fmt/3`, `fmt/4`, `fmt/114`, `fmt/115`, `fmt/116`, `fmt/117`, `fmt/118`, `fmt/119`, `fmt/566`, `fmt/567`, `fmt/568` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | DNG |  | `fmt/436`, `fmt/152`, `fmt/437`, `fmt/438`, `fmt/730`, `fmt/1841`, `fmt/1842`, `fmt/1943` | [formate-bild](formate-bild.md#formate) |
| akzeptiert | Kamera-RAW (CR2, CR3, NEF, ARW und andere) | solange LibRaw sie liest | `fmt/593`, `fmt/592`, `fmt/1595`, `fmt/202`, `fmt/191`, `fmt/1127`, `fmt/1126`, `fmt/668`, `fmt/642`, `fmt/662`, `fmt/1781`, `fmt/661`, `fmt/1061`, `fmt/1062` | [formate-bild](formate-bild.md#formate) |

### PDF

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| bevorzugt | PDF/A-2u |  | `fmt/478` | [formate-pdf](formate-pdf.md#formate) |
| bevorzugt | PDF/A-2b | für Scans mit OCR | `fmt/477` | [formate-pdf](formate-pdf.md#formate) |
| akzeptiert | PDF/A-1a, PDF/A-1b, PDF/A-2a |  | `fmt/95`, `fmt/354`, `fmt/476` | [formate-pdf](formate-pdf.md#formate) |
| akzeptiert | PDF/A-4 | ohne eingebettete Dateien (nicht 4f) | `fmt/1910`, `fmt/1911` | [formate-pdf](formate-pdf.md#formate) |
| akzeptiert | PDF 1.0 bis 1.7, PDF 2.0 | Schriften eingebettet; ohne Passwort zu öffnen | `fmt/14`, `fmt/15`, `fmt/16`, `fmt/17`, `fmt/18`, `fmt/19`, `fmt/20`, `fmt/276`, `fmt/1129`, `fmt/2050`, `fmt/2052` | [formate-pdf](formate-pdf.md#formate) |
| nicht akzeptiert | PDF/A-3, PDF/A-4f | eingebettete Dateien beliebigen Typs | `fmt/479`, `fmt/480`, `fmt/481`, `fmt/1912` | [formate-pdf](formate-pdf.md#formate) |

### Text

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| bevorzugt | ODT (OpenDocument Text) | ohne Passwort | `fmt/136`, `fmt/290`, `fmt/291`, `fmt/1756`, `fmt/2044` | [formate-text](formate-text.md#formate) |
| bevorzugt | TXT | bevorzugt in UTF-8; andere Kodierungen akzeptiert | `x-fmt/111` | [formate-text](formate-text.md#formate) |
| akzeptiert | DOCX | ohne Passwort | `fmt/412`, `fmt/1827` | [formate-text](formate-text.md#formate) |
| akzeptiert | DOC, RTF | solange LibreOffice sie liest | `fmt/37`, `fmt/38`, `fmt/39`, `fmt/40`, `fmt/609`, `fmt/45`, `fmt/50`, `fmt/52`, `fmt/53`, `fmt/355`, `fmt/969` | [formate-text](formate-text.md#formate) |

### Tabellen

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| bevorzugt | ODS (OpenDocument Spreadsheet) | ohne Passwort | `fmt/137`, `fmt/294`, `fmt/295`, `fmt/1755`, `fmt/2045` | [formate-tabellen](formate-tabellen.md#formate) |
| bevorzugt | CSV in UTF-8 | für reine Daten, mit Beschreibung | `x-fmt/18` | [formate-tabellen](formate-tabellen.md#formate) |
| akzeptiert | XLSX | ohne Passwort | `fmt/214`, `fmt/1828` | [formate-tabellen](formate-tabellen.md#formate) |
| akzeptiert | XLS | solange LibreOffice es liest | `fmt/55`, `fmt/56`, `fmt/57`, `fmt/59`, `fmt/61` | [formate-tabellen](formate-tabellen.md#formate) |

### Präsentationen

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| bevorzugt | ODP (OpenDocument Presentation) | ohne Passwort | `fmt/138`, `fmt/292`, `fmt/293`, `fmt/1754`, `fmt/2046` | [formate-tabellen](formate-tabellen.md#formate) |
| akzeptiert | PPTX, PPT | solange LibreOffice sie liest | `fmt/215`, `fmt/1829`, `fmt/125`, `fmt/126` | [formate-tabellen](formate-tabellen.md#formate) |

### Audio

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| bevorzugt | WAV bzw. Broadcast Wave (BWF) mit LPCM |  | `fmt/6`, `fmt/141`, `fmt/142`, `fmt/143`, `fmt/1`, `fmt/2`, `fmt/527`, `fmt/703`, `fmt/704`, `fmt/705`, `fmt/706`, `fmt/707`, `fmt/708`, `fmt/709`, `fmt/710`, `fmt/711`, `fmt/712`, `fmt/713` | [formate-av](formate-av.md#formate) |
| bevorzugt | FLAC |  | `fmt/279` | [formate-av](formate-av.md#formate) |
| akzeptiert | MP3, AAC (M4A), AIFF, Ogg Vorbis, Opus, WMA | solange ffmpeg sie liest | `fmt/134`, `fmt/2094`, `fmt/596`, `fmt/1812`, `fmt/414`, `fmt/203`, `fmt/944`, `fmt/946`, `fmt/132` | [formate-av](formate-av.md#formate) |

### Video

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| bevorzugt | MKV (mit FFV1 und FLAC) | Digitalisierung analoger Träger | `fmt/569` | [formate-av](formate-av.md#formate) |
| bevorzugt | MP4 (mit H.264) | wo Speicher knapp ist; MP4 mit HEVC oder AV1 ist akzeptiert | `fmt/199` | [formate-av](formate-av.md#formate) |
| akzeptiert | MOV (auch ProRes), AVI, MPEG-2, MPEG-TS, MXF, WebM, WMV | solange ffmpeg sie liest | `x-fmt/384`, `fmt/797`, `fmt/5`, `x-fmt/385`, `x-fmt/386`, `fmt/640`, `fmt/649`, `fmt/585`, `fmt/1055`, `fmt/200`, `fmt/783`, `fmt/784`, `fmt/785`, `fmt/786`, `fmt/787`, `fmt/788`, `fmt/789`, `fmt/790`, `fmt/791`, `fmt/573`, `fmt/133`, `fmt/441` | [formate-av](formate-av.md#formate) |
| akzeptiert | SubRip (SRT), WebVTT | in UTF-8, als Begleitdatei zur Aufnahme | `fmt/1218`, `fmt/1454` | [formate-av](formate-av.md#formate) |

### Container und XML

| Stufe | Format | Bedingung | PUIDs | Seite |
|---|---|---|---|---|
| akzeptiert | ZIP, GZ (auch TGZ), TAR | zum Entpacken; gepackt nur, wo das Paket selbst die Einheit ist; ohne Passwort | `x-fmt/263`, `x-fmt/266`, `x-fmt/265` | [formate-uebrige](formate-uebrige.md#container) |
| akzeptiert | XML 1.0 | nach Absprache; in UTF-8, wohlgeformt, mit Schema (XSD) und Beschreibung | `fmt/101`, `fmt/1776` | [formate-uebrige](formate-uebrige.md#xml) |

<!-- END generated format list -->
