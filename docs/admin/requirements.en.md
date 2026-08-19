# Server requirements

Anton is a [Laravel](https://laravel.com/) 12 application.

## Foundation

| Component | Requirement |
|---|---|
| [PHP](https://www.php.net/) | **8.3** or newer |
| [MySQL](https://www.mysql.com/) | 8.0.35 or newer |
| [Apache](https://httpd.apache.org/) | 2.4 with `mod_rewrite` and `.htaccess`, operated with PHP-FPM |
| Operating system | [Ubuntu](https://ubuntu.com/) LTS[^OS] — 24.04 with Anton as a Service |
| [Supervisor](http://supervisord.org/) | for background processing — **not optional** |
| [Composer](https://getcomposer.org), [Git](https://git-scm.com/), [SSH](https://www.openssh.com/) | for installation and updates |
| Email dispatch | sendmail, for example |

!!! note "MariaDB"
    MySQL is the default. **MariaDB 10.11+** can be configured as an
    alternative for self-hosting. The two handle the axis order of
    geocoordinates differently; Anton detects the database at startup and
    adjusts accordingly.

!!! warning "Without Supervisor, Anton stands still"
    Uploads, conversions, import and export run as background jobs. If the
    supervisor is not running, everything piles up in the queue without any
    error message appearing. The **Supervisor** tab in
    [Anton Doctor](doctor.md) shows the state.

## PHP extensions

- OpenSSL
- PDO with MySQL driver (`pdo_mysql`)
- Imagick
- Mbstring
- Tokenizer
- XML and DOM
- Ctype
- JSON
- Zip
- GD
- cURL
- Fileinfo
- Exif
- Intl

!!! important "Imagick means the extension, not just the program"
    Anton processes images via the **PHP extension** Imagick, not by calling
    ImageMagick on the command line. If `php-imagick` is missing, the
    installation completes and the image conversions only fail later in the
    background — without a visible error message.

## Programs

Anton calls external programs. If one is missing, the corresponding processing
steps fail — usually silently. The **Binaries** tab in
[Anton Doctor](doctor.md) checks whether they are all present.

| Program | Purpose |
|---|---|
| [ImageMagick](https://imagemagick.org/) (`convert`, `identify`) | Image conversions and preview images |
| [Ghostscript](https://www.ghostscript.com/) (`gs`) | PDF access copies |
| [poppler-utils](https://poppler.freedesktop.org/) (`pdftotext`, `pdftoppm`) | PDF full text and page previews |
| [ffmpeg](https://www.ffmpeg.org/) | Video and audio conversions, technical metadata |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | Text recognition (OCR) |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/) | OCR text layer in PDFs |
| [qpdf](https://qpdf.sourceforge.io/) | PDF processing |
| [img2pdf](https://gitlab.mister-muffin.de/josch/img2pdf) | Combining images into a PDF |
| `mysql`, `mysqldump` | Backups and restoration |
| `unzip` | Unpacking SIP packages and imports |
| `awk`, `du`, `git` | Operating and diagnostic tools |

## Optional

This software is not a prerequisite for operation. Without it, a particular
function is missing in each case — Anton keeps running.

| Software | Without it, this is missing |
|---|---|
| [Siegfried](https://www.itforarchivists.com/siegfried) (`sf`) | Format identification via PRONOM — and thus the risk assessment in [preservation planning](preservation-planning.md). Without Siegfried, the PRONOM ID remains empty. |
| [Fido](https://github.com/openpreserve/fido) | Alternative for format identification; Anton uses whatever is present |
| [Typesense](https://typesense.org/) | The [instant search](typesense.md) and gallery V2. The classic full-text search and gallery work without it. |

!!! note "Siegfried comes from its own package repository"
    Siegfried is not in the Ubuntu sources. It is installed via the repository
    of itforarchivists.com.

[^OS]: Other Linux or Unix systems should work equally well. What matters is that PHP 8.3 and the programs listed above are available.
