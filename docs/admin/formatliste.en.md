# Format list

The format list says which formats an archive prefers and accepts, format by format by PRONOM PUID. Anton checks every file against it when taking it in (anton#690).

- **Default:** Without a list of its own, the list of k & r applies. It is the machine-readable version of the format pages ([images](formate-bild.md), [PDF](formate-pdf.md), [text](formate-text.md), [audio and video](formate-av.md), [spreadsheets and presentations](formate-tabellen.md), [containers and XML](formate-uebrige.md)). These are Anton's own rules; where NARA and KOST part ways, as with ODT and DOCX, it follows NARA.
- **Own list:** Under **Admin → Preservation Planning → Format list** an admin sees the list in force and the media outside it, and can save an own list: change levels, remove entries, add PUIDs. The own list replaces the default entirely; a button goes back to the default. Every change is recorded in the security log.
- **Warn, do not refuse:** If a file's format is not on the list or not accepted, Anton takes it all the same. Whoever uploaded it sees a notice after saving, and the medium carries the event «Format list» as a yellow check. The QR upload, whose files are stored in the background, and Excel, SIP and directory imports record the event only.
- **One PUID, different conditions:** A PUID does not tell apart everything the format pages do. TIFF with Deflate and TIFF with LZW share one PUID; the check takes the best level. Conditions such as «without a password» are text only.
- **Archive files:** A ZIP, GZ or TAR imported as a directory has each extracted file checked; saved as a file, Anton does not look inside.

The tables below are generated from Anton (`scripts/gen-format-list.py`), PUIDs after DROID signature file V125.

<!-- BEGIN generated format list -->

### Images

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| preferred | TIFF with Deflate (ZIP) and Predictor 2 | greyscale and colour, 8 or 16 bits per channel | `fmt/353` | [formate-bild](formate-bild.md#formate) |
| accepted | TIFF in other forms | uncompressed, LZW, CCITT G4, JPEG-compressed, BigTIFF, multi-page | `fmt/353`, `fmt/1917`, `x-fmt/387`, `x-fmt/388`, `x-fmt/399` | [formate-bild](formate-bild.md#formate) |
| accepted | JPEG |  | `fmt/41`, `fmt/42`, `fmt/43`, `fmt/44`, `x-fmt/398`, `x-fmt/390`, `x-fmt/391`, `fmt/645`, `fmt/1507` | [formate-bild](formate-bild.md#formate) |
| accepted | PNG |  | `fmt/11`, `fmt/12`, `fmt/13`, `fmt/935` | [formate-bild](formate-bild.md#formate) |
| accepted | JPEG 2000 (JP2) |  | `x-fmt/392` | [formate-bild](formate-bild.md#formate) |
| accepted | HEIC/HEIF | stays master, access copy JPEG | `fmt/1101` | [formate-bild](formate-bild.md#formate) |
| accepted | GIF, BMP, WebP |  | `fmt/3`, `fmt/4`, `fmt/114`, `fmt/115`, `fmt/116`, `fmt/117`, `fmt/118`, `fmt/119`, `fmt/566`, `fmt/567`, `fmt/568` | [formate-bild](formate-bild.md#formate) |
| accepted | DNG |  | `fmt/436`, `fmt/152`, `fmt/437`, `fmt/438`, `fmt/730`, `fmt/1841`, `fmt/1842`, `fmt/1943` | [formate-bild](formate-bild.md#formate) |
| accepted | Camera RAW (CR2, CR3, NEF, ARW and others) | as long as LibRaw reads them | `fmt/593`, `fmt/592`, `fmt/1595`, `fmt/202`, `fmt/191`, `fmt/1127`, `fmt/1126`, `fmt/668`, `fmt/642`, `fmt/662`, `fmt/1781`, `fmt/661`, `fmt/1061`, `fmt/1062` | [formate-bild](formate-bild.md#formate) |

### PDF

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| preferred | PDF/A-2u |  | `fmt/478` | [formate-pdf](formate-pdf.md#formate) |
| preferred | PDF/A-2b | for scans with OCR | `fmt/477` | [formate-pdf](formate-pdf.md#formate) |
| accepted | PDF/A-1a, PDF/A-1b, PDF/A-2a |  | `fmt/95`, `fmt/354`, `fmt/476` | [formate-pdf](formate-pdf.md#formate) |
| accepted | PDF/A-4 | without embedded files (not 4f) | `fmt/1910`, `fmt/1911` | [formate-pdf](formate-pdf.md#formate) |
| accepted | PDF 1.0 to 1.7, PDF 2.0 | fonts embedded; opens without a password | `fmt/14`, `fmt/15`, `fmt/16`, `fmt/17`, `fmt/18`, `fmt/19`, `fmt/20`, `fmt/276`, `fmt/1129`, `fmt/2050`, `fmt/2052` | [formate-pdf](formate-pdf.md#formate) |
| not accepted | PDF/A-3, PDF/A-4f | embedded files of any type | `fmt/479`, `fmt/480`, `fmt/481`, `fmt/1912` | [formate-pdf](formate-pdf.md#formate) |

### Text

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| preferred | ODT (OpenDocument Text) | without a password | `fmt/136`, `fmt/290`, `fmt/291`, `fmt/1756`, `fmt/2044` | [formate-text](formate-text.md#formate) |
| preferred | TXT | preferably UTF-8; other encodings accepted | `x-fmt/111` | [formate-text](formate-text.md#formate) |
| accepted | DOCX | without a password | `fmt/412`, `fmt/1827` | [formate-text](formate-text.md#formate) |
| accepted | DOC, RTF | as long as LibreOffice reads them | `fmt/37`, `fmt/38`, `fmt/39`, `fmt/40`, `fmt/609`, `fmt/45`, `fmt/50`, `fmt/52`, `fmt/53`, `fmt/355`, `fmt/969` | [formate-text](formate-text.md#formate) |

### Spreadsheets

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| preferred | ODS (OpenDocument Spreadsheet) | without a password | `fmt/137`, `fmt/294`, `fmt/295`, `fmt/1755`, `fmt/2045` | [formate-tabellen](formate-tabellen.md#formate) |
| preferred | CSV in UTF-8 | for plain data, with a description | `x-fmt/18` | [formate-tabellen](formate-tabellen.md#formate) |
| accepted | XLSX | without a password | `fmt/214`, `fmt/1828` | [formate-tabellen](formate-tabellen.md#formate) |
| accepted | XLS | as long as LibreOffice reads it | `fmt/55`, `fmt/56`, `fmt/57`, `fmt/59`, `fmt/61` | [formate-tabellen](formate-tabellen.md#formate) |

### Presentations

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| preferred | ODP (OpenDocument Presentation) | without a password | `fmt/138`, `fmt/292`, `fmt/293`, `fmt/1754`, `fmt/2046` | [formate-tabellen](formate-tabellen.md#formate) |
| accepted | PPTX, PPT | as long as LibreOffice reads them | `fmt/215`, `fmt/1829`, `fmt/125`, `fmt/126` | [formate-tabellen](formate-tabellen.md#formate) |

### Audio

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| preferred | WAV or Broadcast Wave (BWF) with LPCM |  | `fmt/6`, `fmt/141`, `fmt/142`, `fmt/143`, `fmt/1`, `fmt/2`, `fmt/527`, `fmt/703`, `fmt/704`, `fmt/705`, `fmt/706`, `fmt/707`, `fmt/708`, `fmt/709`, `fmt/710`, `fmt/711`, `fmt/712`, `fmt/713` | [formate-av](formate-av.md#formate) |
| preferred | FLAC |  | `fmt/279` | [formate-av](formate-av.md#formate) |
| accepted | MP3, AAC (M4A), AIFF, Ogg Vorbis, Opus, WMA | as long as ffmpeg reads them | `fmt/134`, `fmt/2094`, `fmt/596`, `fmt/1812`, `fmt/414`, `fmt/203`, `fmt/944`, `fmt/946`, `fmt/132` | [formate-av](formate-av.md#formate) |

### Video

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| preferred | MKV (with FFV1 and FLAC) | digitisation of analogue carriers | `fmt/569` | [formate-av](formate-av.md#formate) |
| preferred | MP4 (with H.264) | where storage is scarce; MP4 with HEVC or AV1 is accepted | `fmt/199` | [formate-av](formate-av.md#formate) |
| accepted | MOV (ProRes too), AVI, MPEG-2, MPEG-TS, MXF, WebM, WMV | as long as ffmpeg reads them | `x-fmt/384`, `fmt/797`, `fmt/5`, `x-fmt/385`, `x-fmt/386`, `fmt/640`, `fmt/649`, `fmt/585`, `fmt/1055`, `fmt/200`, `fmt/783`, `fmt/784`, `fmt/785`, `fmt/786`, `fmt/787`, `fmt/788`, `fmt/789`, `fmt/790`, `fmt/791`, `fmt/573`, `fmt/133`, `fmt/441` | [formate-av](formate-av.md#formate) |
| accepted | SubRip (SRT), WebVTT | in UTF-8, as a companion file to the recording | `fmt/1218`, `fmt/1454` | [formate-av](formate-av.md#formate) |

### Containers and XML

| Level | Format | Condition | PUIDs | Page |
|---|---|---|---|---|
| accepted | ZIP, GZ (TGZ too), TAR | to be extracted; packed only where the package itself is the unit; without a password | `x-fmt/263`, `x-fmt/266`, `x-fmt/265` | [formate-uebrige](formate-uebrige.md#container) |
| accepted | XML 1.0 | by agreement; UTF-8, well-formed, with a schema (XSD) and a description | `fmt/101`, `fmt/1776` | [formate-uebrige](formate-uebrige.md#xml) |

<!-- END generated format list -->
