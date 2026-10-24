# Audio und Video: Formate und wesentliche Eigenschaften

Diese Seite legt für Ton- und Videoaufnahmen fest, in welchen Formaten Anton sie bevorzugt und akzeptiert, welche Eigenschaften erhalten bleiben müssen und was Anton davon heute misst oder prüft. Sie gehört zur Reihe je Formatkategorie (anton#687), nach den [Bildern](formate-bild.md), [PDF](formate-pdf.md) und [Text](formate-text.md). Die Festlegung ist vorläufig: Sie wird in der Praxis erprobt und nachgeführt, wo sie sich nicht bewährt.

Was hier steht, braucht Anton für drei Dinge: um zu dokumentieren, was eine Aufnahme ausmacht (NDSA Cn-1.1), um zu prüfen, ob sie das noch tut (Cn-2.1), und um nach einer Migration zu belegen, dass nichts Wesentliches verloren ging ([`media:migrate`](console-commands.md#mediamigrate)).

## Formate {#formate}

### Audio

| Stufe | Format | Bedingung |
|---|---|---|
| bevorzugt | WAV bzw. Broadcast Wave (BWF) mit LPCM | |
| bevorzugt | FLAC | |
| akzeptiert | MP3, AAC (M4A), AIFF, Ogg Vorbis, Opus, WMA | solange ffmpeg sie liest |

### Video

| Stufe | Format | Bedingung |
|---|---|---|
| bevorzugt | Originalcodec in einem gängigen Container, wie geliefert | digital entstandenes Video |
| bevorzugt | MKV mit FFV1 und FLAC | Digitalisierung analoger Träger |
| bevorzugt | MP4 mit H.264 | wo Speicher knapp ist |
| akzeptiert | MOV (auch ProRes), AVI, MPEG-2, MPEG-TS, MXF, WebM, WMV, MP4 mit HEVC oder AV1 | solange ffmpeg sie liest |

### Untertitel

| Stufe | Format | Bedingung |
|---|---|---|
| akzeptiert | SubRip (SRT), WebVTT | in UTF-8, als Begleitdatei zur Aufnahme |

**Bevorzugt** sind beim Ton die unkomprimierten oder verlustfrei komprimierten Formate WAV/BWF und FLAC; so empfehlen es die NARA und die KOST. Bei Video zählt zuerst der Codec: Ein digital entstandenes Video wird nicht neu kodiert, denn jede verlustbehaftete Neukodierung verliert Information und kann Artefakte erzeugen (KOST). Bei der Digitalisierung analoger Träger entsteht der Master verlustfrei, als MKV mit FFV1 für das Bild und FLAC für den Ton (KOST); Memoriav und die Schweizerische Nationalphonothek empfehlen für den Ton 96 kHz und 24 Bit, die NARA mindestens 44,1 kHz und 16 Bit, besser 96 kHz und 24 Bit, für Video 10 Bit. MP4 mit H.264 ist die Wahl, wo ein verlustfreier Master zu viel Speicher braucht; Bewertungsentscheid, wie bei JPEG für Bilder.

**Akzeptiert** ist, wie bei den Bildern, was sich mit verbreiteten, quelloffenen Werkzeugen lesen lässt und voraussichtlich lesbar bleibt; für Ton und Video ist das ffmpeg, das auch ProRes, WMV und MXF dekodiert. Verlustbehaftet komprimierte Aufnahmen (MP3, AAC, H.264) werden nicht in ein verlustfreies Format umgewandelt: Der Verlust bleibt, die Datei wird nur grösser (KOST). Die NARA rät, WMV nach AVI umzuwandeln; nach dem Grundsatz bleibt es, bis ffmpeg es nicht mehr liest.

Ein Wechsel des Containers ist ohne Verlust möglich: Die Spuren werden unverändert in einen anderen Container verschoben, etwa von MOV nach MKV (KOST). Das ist die schonendste Form der Normalisierung.

**Untertitel** liegen als Begleitdatei neben der Aufnahme, nicht in ihr. SRT und WebVTT sind reiner Text mit Zeitmarken; die NARA stuft SRT mit geringem Risiko ein. Weil SRT keine feste Zeichenkodierung kennt, liefert die Ablieferstelle UTF-8. Untertitel, die als Spur im Container stecken, etwa in MKV oder MP4, bleiben dort; Anton zählt sie als Spur.

Auch hier gilt: Ein Archiv führt [möglichst wenige Formate](formate-bild.md#formate).

## Wesentliche Eigenschaften

Gruppiert wie bei der NARA nach Erscheinung, Struktur, Verhalten und Kontext. Die NARA verlangt, bei einer Umwandlung digital entstandenen Materials dieselben Abtastwerte, dieselbe Kanalbelegung und, wo das neue Format es erlaubt, dieselbe Kompression zu behalten.

| Gruppe | Eigenschaft | gilt für | Quelle |
|---|---|---|---|
| Erscheinung | Breite und Höhe in Pixeln, Seitenverhältnis | Video | NARA |
| | Bildrate, Zeilensprung | Video | NARA |
| | Bittiefe und Farbunterabtastung | Video | NARA |
| | Farbraum | Video | NARA |
| Struktur | Dauer | Audio, Video | NARA |
| | Zahl und Art der Spuren (Bild, Ton, Untertitel) | Audio, Video | NARA |
| | Kanäle und Kanalbelegung (mono, stereo, 5.1) | Audio, Video | NARA |
| | Abtastrate und Bittiefe | Audio, Video | NARA |
| | Inhalt jeder Spur, wo das Format verlustfrei ist | Audio, Video | Anton |
| | Codec und Kompression: festgehalten, nicht erhalten | Audio, Video | NARA, KOST |
| Verhalten | Die Aufnahme lässt sich abspielen, Bild und Ton synchron. | Audio, Video | NARA |
| Kontext | eingebettete Metadaten (Titel, Urheber, Aufnahmedatum, bei BWF die Kodierungsgeschichte) | Audio, Video | NARA |

Codec und Kompression sind keine Eigenschaften, die erhalten bleiben müssen. Sie werden festgehalten, weil sie sagen, ob die anderen Eigenschaften verlustfrei vorliegen; und eine Migration soll sie nur ändern, wo es nötig ist.

Der Inhalt einer Spur lässt sich bei verlustfreien Formaten über eine Prüfsumme je Spur belegen, das Gegenstück zur Pixelsignatur bei Bildern: Bleibt sie nach einem Containerwechsel oder einer verlustfreien Umwandlung gleich, ist kein Bild und kein Sample verändert.

## Was Anton misst und prüft

Stand: Version 0.112.0.

| Eigenschaft | Gemessen | Geprüft |
|---|---|---|
| Container, Dauer, Bitrate, Zahl der Bild-, Ton-, Untertitel- und Datenspuren | mit ffprobe bei der Übernahme; für ältere Aufnahmen trägt sie [`media:validate-formats`](console-commands.md#mediavalidate-formats) nach | nein |
| Bild: Codec, Bitrate, Breite und Höhe, Seitenverhältnis (SAR, DAR), Bildrate, Zeilensprung, Pixelformat und Bittiefe, Farbraum | ebenso, für die erste Bildspur; ein Titelbild zählt nicht als Bildspur | nein |
| Ton: Codec, Bitrate, Kanäle und Kanalbelegung, Abtastrate, Bittiefe | ebenso, für die erste Tonspur | nein |
| alle Spuren | ebenso, je Spur eine Zeile mit Art und Codec | nein |
| Inhalt jeder Spur | bei einer Migration: MD5 der dekodierten Bilder und Samples je Spur (`ffmpeg -f streamhash`, Ton als 64-Bit-Gleitkommazahl), vorher und nachher | nach einer Migration mit [`media:migrate`](console-commands.md#mediamigrate): jede Spur mit gleicher Prüfsumme; dazu vergleicht ffprobe Spuren, Kanäle, Abtastrate, Bildgrösse, Bildrate und Dauer (anton#717) |
| Abspielbar | – | bei der Übernahme liest ffprobe den Container; nachts mit [`media:validate-formats`](console-commands.md#mediavalidate-formats) dekodiert ffmpeg jedes Bild und jedes Sample, jede Fehlermeldung zählt; dazu beim Erstellen der Nutzungskopie |
| Eingebettete Metadaten | nein | nein |

Die gemessenen Werte stehen am Medium unter **Technische Merkmale**; die Bitrate seit v0.112.0. Nach einer Migration misst `media:migrate` sie neu. Der Memobase-, der RiC- und der A+-Export lesen Dauer, Codec, Bitrate, Bildgrösse, Abtastrate und Seitenverhältnis von dort (anton#720); die früheren Spalten `av_*` und `media:extract-av-metadata` gibt es nicht mehr.

## Grenzen

- Kennwerte im Einzelnen misst Anton nur für die erste Bild- und die erste Tonspur; weitere Spuren sind nur gezählt und mit Art und Codec aufgeführt.
- Für Aufnahmen, die vor v0.111.1 übernommen wurden, trägt der nächtliche Lauf `media:validate-formats` die Merkmale nach; bis dahin fehlen sie auch in den Exporten.
- Eine Regel, die Ton oder Video umwandelt, gibt es noch nicht. Kommt eine, belegt `media:migrate` sie Spur für Spur; geht dabei etwas verloren, bleibt der Master, wie er war. Damit taugt die Prüfung nur für verlustfreie Ziele. Eine Regel, die die Endung ändert, lehnt `media:migrate` ab; ein Containerwechsel etwa von MOV nach MKV geht darum heute nicht.
- Nutzungskopien entstehen als MP3 für Ton und als MP4 mit H.264, Posterbild und Vorschaubild für Video, aus allen Formaten oben, auch FFV1 und ProRes (anton#718). Der Upload nimmt sie an und behält ihre Endung.
- Untertitel als Begleitdatei nimmt der Upload nicht an; SRT und WebVTT fehlen unter den erlaubten Endungen. Eine Untertitelspur im Container misst Anton nur als Spur, ihren Text nicht.
- «Abspielbar» heisst, ffmpeg dekodiert die Aufnahme ohne Fehlermeldung. Ob Bild und Ton gut sind, prüft es nicht.

## Was eine Migration prüfen muss

Wandelt `media:migrate` eine Aufnahme um, muss danach gelten:

- Dauer, Zahl und Art der Spuren, Kanäle, Abtastrate, Auflösung und Bildrate sind gleich.
- Bei verlustfreiem Ziel (Containerwechsel, FFV1, FLAC) ist die Prüfsumme jeder Spur gleich. Das prüft `media:migrate` seit v0.111.1 selbst.
- Die eingebetteten Metadaten sind übertragen.
- Die gelieferte Datei bleibt als [Original](preservation.md#behaltene-originale), wenn das Ziel verlustbehaftet ist.

## Quellen {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Digital Audio](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_DigitalAudio.md) und [Preservation Action Plan for Digital Video](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_DigitalVideo.md), Plan Date 2024-11 (PDF-Fassungen vom 2024-12-18). Wesentliche Eigenschaften, Anforderungen an Digitalisierung und Umwandlung, Übernahmeformate. Als bevorzugtes Videoformat nennt der Plan «AV1 Image File Format (AVIF)», ein Bildformat; das ist offensichtlich ein Fehler und hier nicht übernommen.
- NARA: [Preservation Action Plan, Format-Tabelle](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), Stand 2026-03-20. Risiko und Handlung je Format; Matroska und FFV1 führt sie nicht.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Übernahmeformate, auf die sich die Pläne beziehen.
- Federal Agencies Digital Guidelines Initiative (FADGI): [Significant Properties for Digital Video](https://www.digitizationguidelines.gov/guidelines/FADGI-SignificantPropertiesDigitalVideo2024.pdf), 2024. Vom Videoplan der NARA als Grundlage genannt.
- KOST, Katalog archivischer Dateiformate (KaD), Version 7.1, Mai 2026: [Audio, Zusammenfassung](https://kost-ceco.ch/cms/kad_audio_intro_de.html) und [Video, Zusammenfassung](https://kost-ceco.ch/cms/kad_video_intro_de.html). Empfohlene und akzeptierte Formate, keine Umwandlung verlustbehafteter Aufnahmen, Codec vor Container, verlustfreier Containerwechsel, MKV mit FFV1 und FLAC als Archivmaster.
- [FFmpeg](https://ffmpeg.org/): quelloffene Werkzeuge zum Lesen, Prüfen und Umwandeln von Ton und Video.
- NDSA: [Levels of Digital Preservation, Version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), März 2026, Anforderungen Cn-1.1 und Cn-2.1.
