# Serveranforderungen

Anton ist eine [Laravel](https://laravel.com/)-12-Anwendung.

## Grundlage

| Baustein | Anforderung |
|---|---|
| [PHP](https://www.php.net/) | **8.3** oder neuer |
| [MySQL](https://www.mysql.com/de/) | 8.0.35 oder neuer |
| [Apache](https://httpd.apache.org/) | 2.4 mit `mod_rewrite` und `.htaccess`, betrieben mit PHP-FPM |
| Betriebssystem | [Ubuntu](https://ubuntu.com/) LTS[^OS] |
| [Supervisor](http://supervisord.org/) | für die Hintergrundverarbeitung — **nicht optional** |
| [Composer](https://getcomposer.org), [Git](https://git-scm.com/), [SSH](https://www.openssh.com/) | für Installation und Aktualisierung |
| E-Mail-Versand | z.B. sendmail |

!!! note "MariaDB"
    MySQL ist die Vorgabe. **MariaDB 10.11+** lässt sich für Selbsthosting
    alternativ konfigurieren. Die beiden behandeln die Achsenreihenfolge von
    Geokoordinaten unterschiedlich; Anton erkennt die Datenbank beim Start und
    stellt sich darauf ein.

!!! warning "Ohne Supervisor steht Anton still"
    Uploads, Konversionen, Import und Export laufen als Hintergrundaufträge.
    Ist der Supervisor nicht in Betrieb, staut sich alles in der Warteschlange,
    ohne dass eine Fehlermeldung erscheint. Der Reiter **Supervisor** im
    [Anton Doctor](doctor.md) zeigt den Zustand.

## PHP-Extensions

- OpenSSL
- PDO mit MySQL-Treiber (`pdo_mysql`)
- Imagick
- Mbstring
- Tokenizer
- XML und DOM
- Ctype
- JSON
- Zip
- GD
- cURL
- Fileinfo
- Exif
- Intl

!!! important "Imagick ist die Extension, nicht nur das Programm"
    Anton verarbeitet Bilder über die **PHP-Extension** Imagick, nicht über den
    Aufruf von ImageMagick auf der Kommandozeile. Fehlt `php-imagick`, läuft die
    Installation durch und die Bildkonversionen scheitern erst später im
    Hintergrund — ohne sichtbare Fehlermeldung.

## Programme

Anton ruft externe Programme auf. Fehlt eines, schlagen die zugehörigen
Verarbeitungsschritte fehl — meist still. Der Reiter **Binaries** im
[Anton Doctor](doctor.md) prüft, ob alle vorhanden sind.

| Programm | Wofür |
|---|---|
| [ImageMagick](https://imagemagick.org/) (`convert`, `identify`) | Bildkonversionen und Vorschaubilder |
| [Ghostscript](https://www.ghostscript.com/) (`gs`) | PDF-Zugriffskopien |
| [poppler-utils](https://poppler.freedesktop.org/) (`pdftotext`, `pdftoppm`) | PDF-Volltext und Seitenvorschau |
| [ffmpeg](https://www.ffmpeg.org/) | Video- und Audiokonversionen, technische Metadaten |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | Texterkennung (OCR) |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/) | OCR-Textebene in PDFs |
| [qpdf](https://qpdf.sourceforge.io/) | PDF-Verarbeitung |
| [img2pdf](https://gitlab.mister-muffin.de/josch/img2pdf) | Bilder zu PDF zusammenfassen |
| `mysql`, `mysqldump` | Sicherungen und Wiederherstellung |
| `unzip` | SIP-Pakete und Importe entpacken |
| `awk`, `du`, `git` | Betriebs- und Diagnosewerkzeuge |

## Optional

Diese Software ist nicht Voraussetzung für den Betrieb. Ohne sie fehlt jeweils
eine bestimmte Funktion — Anton läuft weiter.

| Software | Ohne sie fehlt |
|---|---|
| [Siegfried](https://www.itforarchivists.com/siegfried) (`sf`) | Die Formaterkennung über PRONOM — und damit die Risikobewertung im [Preservation Planning](preservation-planning.md). Ohne Siegfried bleibt die PRONOM-ID leer. |
| [Fido](https://github.com/openpreserve/fido) | Alternative zur Formaterkennung; Anton nutzt, was vorhanden ist |
| [Typesense](https://typesense.org/) | Die [schnelle Suche](typesense.md) und die Galerie V2. Die klassische Volltextsuche und Galerie funktionieren ohne. |

!!! note "Siegfried kommt aus einem eigenen Paket-Repository"
    Siegfried ist nicht in den Ubuntu-Quellen. Es wird über das Repository von
    itforarchivists.com installiert.

[^OS]: Andere Linux- oder Unix-Systeme sollten ebenso funktionieren. Massgeblich ist, dass PHP 8.3 und die oben genannten Programme zur Verfügung stehen.
