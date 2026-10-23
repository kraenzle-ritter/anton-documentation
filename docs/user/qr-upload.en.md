# QR code upload

With the QR code upload, files can be uploaded directly from a smartphone to an archival object – without having to log in on the mobile device.

## Use cases

- **On site in the archive**: quickly take photographs of documents or objects and assign them directly to the right object  
- **Teamwork**: share the QR code so that colleagues can upload files to an object  
- **External staff**: temporary upload access without an Anton account 

## Setting up the QR code upload

The `upload-qr-lods` setting contains the levels of description for which the QR upload button is displayed, for example files and items `[5,6]`. To deactivate the QR upload, an empty array `[]` is saved, or the content of the field is deleted.

The button is shown to accounts with the role **Editor** or **Admin**, as for uploading through the form. An upload code applies to one record and expires after `upload-qr-token-minutes` (60 minutes unless set otherwise).

## Activating the upload

### 1. Open the object

Navigate to the desired unit of description (a file or an item, for example).

### 2. Generate the QR code

1. Click the **QR Upload** button (📱 icon) in the toolbar
2. A modal opens with:
   - a **QR code** to scan
   - an **upload URL** to copy or share
   - a **token** (validity configurable, default: 1 hour)

### 3. Choose processing options (optional)

Image processing options can be activated in the modal:

| Option | Description | Tool on the server |
|--------|-------------|---|
| **HEIC → JPEG** | Convert iPhone images (HEIC/HEIF) to JPEG automatically; the HEIC is kept as a version of the medium | ImageMagick (`magick`, with libheif) |
| **Images → PDF** | Combine several uploaded images losslessly into one PDF | `img2pdf` |
| **OCR** | Perform text recognition (makes PDFs searchable); scans become PDF/A-2b, a PDF with text stays PDF | `ocrmypdf` + Tesseract (deu+eng) |

These settings are saved and apply to all uploads.

### Pipeline details (for admins)

The pipeline runs in this order:

```
1. BEFORE IMPORT (synchronous)
   HEIC → magick       → JPG (HEIC kept as a version)
   JPGs → img2pdf      → PDF
   PDF  → ocrmypdf     → PDF/A-2b for scans, otherwise PDF, with OCR text layer (master)

2. IMPORT
   addAntonMedium() → event MediumAdded

3. AFTER IMPORT (async, queue)
   MediumIdentifyAndConvert
   ├─ PRONOM identification
   ├─ cloud sync (if configured)
   ├─ thumbnail generation
   └─ RefreshFulltext
      └─ pdftotext → media_texts (full-text index)
```

The pipeline is controlled centrally via the `image-upload-processing` setting
(array). Possible values: `heic2jpg`, `images2pdf`, `ocr`.

Example with all three steps activated:

```php
Setting::setValue('image-upload-processing', ['heic2jpg', 'images2pdf', 'ocr']);
```

Prerequisites on the server:

- ImageMagick with HEIF support (libheif)
- `img2pdf` (Python tool)
- `ocrmypdf` with `tesseract-ocr-deu` and `tesseract-ocr-eng`
- `pdftotext` (package `poppler-utils`) — also needed for full-text extraction

Anton does **not** fail silently if a tool is missing — the pipeline stage
concerned is skipped and documented in the log.
