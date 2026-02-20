# QR-Code Upload

Mit dem QR-Code Upload können Dateien direkt vom Smartphone zu einem Archivobjekt hochgeladen werden – ohne dass man sich auf dem Mobilgerät einloggen muss.

## Anwendungsfälle

- **Vor Ort im Archiv**: Schnell Fotos von Dokumenten oder Objekten machen und direkt dem richtigen Objekt zuordnen  
- **Teamarbeit**: QR-Code teilen, damit Kollegen Dateien zu einem Objekt hochladen können  
- **Externe Mitarbeiter**: Temporärer Upload-Zugang ohne Anton-Account 

## QR-Code Upload einrichten

Die Einstellung `upload-qr-lods` enthält die Verzeichnungsstufen bei denen der QR-Upload Button eingeblendet wird, also z.B. Dossiers und Einzestücke `[5,6]`. Um den QR-Uplaod zu deaktivieren, wird ein leeres Array gespeichert `[]` bzw. der Inhalt des Feldes gelöscht.

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

| Option | Beschreibung |
|--------|-------------|
| **HEIC → JPEG** | iPhone-Bilder (HEIC/HEIF) automatisch in JPEG konvertieren |
| **Bilder → PDF** | Mehrere hochgeladene Bilder zu einem PDF kombinieren |
| **OCR** | Texterkennung durchführen (macht PDFs durchsuchbar) |

Diese Einstellungen werden gespeichert und gelten für alle Uploads.
