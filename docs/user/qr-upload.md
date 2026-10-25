# QR-Code Upload

Mit dem QR-Code Upload können Dateien direkt vom Smartphone zu einem Archivobjekt hochgeladen werden – ohne dass man sich auf dem Mobilgerät einloggen muss.

## Anwendungsfälle

- **Vor Ort im Archiv**: Schnell Fotos von Dokumenten oder Objekten machen und direkt dem richtigen Objekt zuordnen  
- **Teamarbeit**: QR-Code teilen, damit Kolleg:innen Dateien zu einem Objekt hochladen können  
- **Externe Mitarbeitende**: Temporärer Upload-Zugang ohne Anton-Account 

## QR-Code Upload einrichten

Die Einstellung `upload-qr-lods` enthält die Verzeichnungsstufen bei denen der QR-Upload Button eingeblendet wird, also z.B. Dossiers und Einzelstücke `[5,6]`. Um den QR-Upload zu deaktivieren, wird ein leeres Array gespeichert `[]` bzw. der Inhalt des Feldes gelöscht.

Den Knopf sehen Konten mit der Rolle **Editor** oder **Admin**, wie beim Hochladen über das Formular. Ein Upload-Code gilt für einen Datensatz und läuft nach `upload-qr-token-minutes` ab (60 Minuten, wenn nichts anderes eingestellt ist).

## Upload aktivieren

### 1. Objekt öffnen

Navigiere zur gewünschten Verzeichnungseinheit (z.B. ein Dossier oder ein Einzelstück).

### 2. QR-Code generieren

1. Klicke auf den **QR Upload** Button (📱 Symbol) in der Toolbar
2. Ein Modal öffnet sich mit:
   - **QR-Code** zum Scannen
   - **Upload-URL** zum Kopieren/Teilen
   - **Token** (Gültigkeit konfigurierbar, Standard: 1 Stunde)

### 3. Verarbeitungsoptionen wählen (optional)

Im Modal können Bildverarbeitungsoptionen aktiviert werden:

| Option | Beschreibung | Werkzeug auf dem Server |
|--------|-------------|---|
| **HEIC → JPEG** | iPhone-Bilder (HEIC/HEIF) automatisch in JPEG konvertieren; das HEIC bleibt als Version des Mediums erhalten | ImageMagick (`magick`, mit libheif) |
| **Bilder → PDF** | Mehrere hochgeladene Bilder verlustfrei zu einem PDF kombinieren | `img2pdf` |
| **OCR** | Texterkennung durchführen (macht PDFs durchsuchbar); Scans werden PDF/A-2b, PDF mit Text bleibt PDF | `ocrmypdf` + Tesseract (deu+eng) |

Diese Einstellungen werden gespeichert und gelten für alle Uploads.

Nach dem Speichern meldet die Seite, dass die Dateien empfangen sind. Verarbeitet und abgelegt werden sie im Hintergrund; beim Objekt erscheinen sie, sobald das geschehen ist, bei vielen Scans mit OCR nach einigen Minuten. Ein OCR-Lauf bricht nach 600 Sekunden ab (`OCRMYPDF_TIMEOUT`), die Datei wird dann ohne Textebene abgelegt.

### Pipeline-Details (für Admins)

Die Pipeline läuft in dieser Reihenfolge ab:

```
0. IM REQUEST
   Token und Dateien prüfen → Job ProcessTokenUpload

1. BEFORE IMPORT (Queue, ProcessTokenUpload)
   HEIC → magick       → JPG (HEIC bleibt als Version)
   JPGs → img2pdf      → PDF
   PDF  → ocrmypdf     → PDF/A-2b bei Scans, sonst PDF, mit OCR-Textebene (Master)

2. IMPORT
   addAntonMedium() → Event MediumAdded

3. AFTER IMPORT (async, Queue)
   MediumIdentifyAndConvert
   ├─ PRONOM-Identifikation
   ├─ Cloud-Sync (falls konfiguriert)
   ├─ Thumbnail-Generierung
   └─ RefreshFulltext
      └─ pdftotext → media_texts (Volltext-Index)
```

Die Pipeline wird über das Setting `image-upload-processing` (Array) zentral
gesteuert. Mögliche Werte: `heic2jpg`, `images2pdf`, `ocr`.

Beispiel: alle drei Schritte aktiviert:

```php
Setting::setValue('image-upload-processing', ['heic2jpg', 'images2pdf', 'ocr']);
```

Voraussetzungen auf dem Server:

- ImageMagick mit HEIF-Unterstützung (libheif)
- `img2pdf` (Python-Tool)
- `ocrmypdf` mit `tesseract-ocr-deu` und `tesseract-ocr-eng`
- `pdftotext` (Paket `poppler-utils`) — wird auch für die Volltext-
  Extraktion gebraucht

Anton fällt **nicht** still aus, wenn ein Tool fehlt — die betreffende
Pipeline-Stufe wird übersprungen und im Log dokumentiert.
