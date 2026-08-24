# Medien 

Bei Import von Medien erstellt Anton normalerweise eine Benutzungskopie. Diese ist für die Verwendung im Web optimiert. Wenn sie nicht aus anderen Gründen gesperrt sind, haben externe User nur Zugriff auf diese Webversion.

## Medienformate

Grundsätzlich empfiehlt es sich, als Eingangsformate möglichst wenig verschiedene Formate zu verwenden. Das macht die Handhabung und langfristige Pflege überschaubarer und einfacher. Ausserdem gibt es Dateiformate, die für die Archivierung besser geeignet sind als andere. Darüber informieren zahlreiche staatliche Archive und auf digitale Langzeitarchivierung spezialisierte Stellen.  

Für die folgenden Formate werden in Anton Benutzungskopien angefertigt; eine Erweiterung ist bei Bedarf jederzeit einfach implementierbar. Der Import anderer Formate ist möglich, sollte aber wenn möglich getestet werden. Manche Formate werden nicht konvertiert (z.B. DOCX, XLSX, TXT, ZIP).

### Foto  
- TIFF  
- JPEG2000  
- PNG  
- JPEG

### Dokumente  
- PDF/A
- PDF

### Video
- MP4  
- Quicktime

### Audio
- WAF  
- MPEG  
- MP3  

## Technische Metadaten (AV)

Anton liest beim Upload via `ffprobe` automatisch technische Eigenschaften
aus und zeigt sie im Media-Tab der Detailseite an: Dauer, Auflösung,
Codec, Bitrate, Sample-Rate, Aspect-Ratio — soweit für die jeweilige
Datei sinnvoll. Bei Fotos wird nur die Bildgrösse angezeigt, bei Audio
keine Auflösung etc.

Die Werte werden auch im RDF-Export (Memobase-Profil) als EBUcore-Properties
mit ausgeliefert, siehe [RDF-Export](../admin/download-rdf.md). Für ältere
Bestandsmedien lassen sich die Felder per Backfill nachholen — siehe
[`media:extract-av-metadata`](../admin/console-commands.md#mediaextract-av-metadata).


## Reihenfolge der Medien ändern

Die Reihenfolge der Medien einer Verzeichnungseinheit lässt sich ändern,
ohne sie löschen und neu hochladen zu müssen.

Im **Medien-Reiter** der Verzeichnungseinheit steht bei jedem Medium ein Paar
Pfeiltasten (↑ ↓). Ein Klick verschiebt das Medium um eine Position innerhalb
seiner Sammlung. Beim ersten und beim letzten Medium ist die jeweilige Taste
deaktiviert.

Die Reihenfolge gilt für die Anzeige im Katalog, in der Galerie und im
Viewer — es ist dieselbe Reihenfolge, die beim Hochladen vergeben wird.

Bilder und Dokumente werden getrennt sortiert: Ein Bild kann nicht mit einem
Dokument den Platz tauschen.

Das Umsortieren ist eine sichtbare Änderung und wird entsprechend am
Datensatz vermerkt (Änderungsdatum, bearbeitende Person,
Bearbeitungsprotokoll). Nötig ist dafür dieselbe Berechtigung wie zum
Löschen eines Mediums.


## Originalmedien bereitstellen
Um für Kundinnen die originalen Medien bereitzustellen, kann man in einer Verzeichnungseinheit den Medien-Reiter aufrufen:

![Medienreiter](images/transfer-ordner-1.png)
 
Dort die Taste «Kopiere Master in den Transferordner» anklicken.

![Kopiere Master in den Transferordner](images/transfer-ordner-2.png)

Mit Klick auf «Link in die Zwischenablage kopieren» den Link kopieren.

![Kopiere Master in den Transferordner](images/transfer-ordner-3.png)

Den Link der Kund:in per Email zukommen lassen. Der Link ist eine Woche gültig, danach wird die kopierte Datei automatisch gelöscht.
