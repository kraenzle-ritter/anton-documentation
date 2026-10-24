# Übrige Formate: Container und XML

Diese Seite ergänzt die Reihe je Formatkategorie (anton#687) um das, was in keine der Kategorien [Bilder](formate-bild.md), [PDF](formate-pdf.md), [Text](formate-text.md), [Audio und Video](formate-av.md) und [Tabellen und Präsentationen](formate-tabellen.md) fällt: gepackte Dateien (ZIP, GZ, TAR) und XML. Untertitel stehen bei [Audio und Video](formate-av.md#formate). Damit ist die Vorgabeliste von k & r vollständig: Jede Endung, die der Upload annimmt, hat eine Stufe.

## Container {#container}

| Stufe | Format | Bedingung |
|---|---|---|
| akzeptiert, zum Entpacken | ZIP, GZ (auch TGZ), TAR | ohne Passwort und Verschlüsselung |
| akzeptiert, gepackt | dieselben | nur wo das Paket selbst die Einheit ist, etwa ein Datenbankabzug oder der Quellcode einer Anwendung |

Ein Container ist kein Archivformat, sondern eine Verpackung. Was zählt, ist sein Inhalt: Für ihn gelten die Seiten der jeweiligen Kategorie. Die NARA stuft ZIP und TAR mit mittlerem, GZIP mit geringem Risiko ein und rät bei allen dreien, den Container zu behalten, die Dateien aber herauszuholen («Retain but extract files from the container»). Die KOST führt Container nicht als Format; sie rät allgemein von Kompression mit nicht offengelegten Verfahren und vom erneuten Komprimieren schon komprimierter Daten ab. ZIP, GZIP und TAR sind offengelegt und verlustfrei.

Lädt man einen Container zu einem Objekt hoch, fragt Anton, was damit geschehen soll: als Verzeichnis importieren, dann entpackt Anton ihn und die Dateien kommen einzeln ins Archiv, oder als Datei speichern, dann bleibt er ungeöffnet. Anton fragt bei jedem Paket; vorgeschlagen ist das Entpacken, wie es k & r empfiehlt (anton#737). Beim Speichern als Datei sieht Anton nicht hinein: kein Format, keine Formatprüfung, keine Nutzungskopie für den Inhalt. Gepackt bleibt eine Sendung nur, wo sie als Ganzes gilt und ihre Teile einzeln nichts aussagen; bei KBA etwa liegen so seit 2018 der Abzug der Datenbank und der Quellcode der Vorgängeranwendung.

Wie Anton ein Paket behandelt, hängt vom Weg ab:

| Weg | Paket |
|---|---|
| SIP-Import | wird immer entpackt |
| Verzeichnis-Import | wird immer entpackt |
| Medien zu einem Objekt hochladen | Anton fragt |
| Upload-Link | wird nicht angenommen |
| Medien zum Excel-Import | wird nicht angenommen; entpackt ins Importverzeichnis legen |

## XML {#xml}

| Stufe | Format | Bedingung |
|---|---|---|
| akzeptiert, nach Absprache | XML 1.0 in UTF-8 | wohlgeformt, mit Schema (XSD) und Beschreibung |

XML ist für strukturierte Daten das dauerhafteste Format; die KOST empfiehlt es dafür, die NARA stuft es mit geringem Risiko ein. In Anton kommt XML heute aber nur als Metadaten vor, in den SIPs (eCH-0160, EAD, METS), und der Import macht daraus Verzeichnungseinheiten; das gehört zu den Metadaten, nicht zum Bestand. Will ein Archiv XML als Inhalt ablegen, etwa eine Edition in TEI oder einen Export aus einer Fachanwendung, liefert die Ablieferstelle das Schema mit, als XSD, nicht als DTD (KOST), und beschreibt, was die Elemente bedeuten. Das ist abzusprechen; eine eigene Seite folgt, wenn es so weit ist.

## Was Anton misst und prüft

Stand: Version 0.112.0.

| Eigenschaft | Gemessen | Geprüft |
|---|---|---|
| Format | PRONOM-PUID mit Siegfried, wie bei allen Dateien | Widerspruch zwischen Endung, MIME-Typ und PUID als Warnung; ein MIME-Typ «application/zip» gilt dabei als nichtssagend, weil auch DOCX, XLSX und ODT ZIP sind |
| Container: lässt sich entpacken | – | vor dem Entpacken eines Uploads oder SIP: nicht zu viele Einträge, nicht zu gross, keine Verweise unter den Einträgen (anton#726) |
| Inhalt eines gepackten Containers | nein | nein |
| XML | nein | nein |

## Grenzen

- In einen Container, der gepackt bleibt, sieht die Formatprüfung nicht hinein. Was darin liegt, welches Format es hat und ob es noch lesbar ist, weiss Anton nicht.
- Über den Upload nimmt Anton XML nicht an. Browser führen XML wie HTML und SVG als Dokument aus; Anton zeigt solche Dateien darum nie direkt an, sondern bietet sie nur zum Herunterladen (anton#640).
- Ob XML wohlgeformt ist oder seinem Schema folgt, prüft Anton nicht.

## Quellen {#quellen}

- National Archives and Records Administration (NARA): [Preservation Action Plan, Format-Tabelle](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), Stand 2026-03-20. ZIP und TAR mittleres, GZIP und XML geringes Risiko; bei Containern «Retain but extract files from the container».
- KOST, Katalog archivischer Dateiformate (KaD), Version 7.1, Mai 2026: [XML](https://kost-ceco.ch/cms/kad_xml_de.html), [Empfehlung](https://kost-ceco.ch/cms/kad_recommendation_de.html) (strukturierte Daten als XML) und [Datenkompression](https://kost-ceco.ch/cms/kad_compression_de.html). XSD statt DTD, Kompression nur offengelegt und nicht doppelt.
- NDSA: [Levels of Digital Preservation, Version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), März 2026, Anforderungen Cn-1.1, Cn-2.1 und Cn-2.2.
