# Spreadsheets and presentations: formats and significant properties

This page sets out, for spreadsheets and presentations, which formats Anton prefers and accepts, which properties must be preserved, and what Anton measures or checks of them today. It belongs to the series per format category (anton#687), after [images](formate-bild.md), [PDF](formate-pdf.md), [text](formate-text.md), and [audio and video](formate-av.md). Databases are not covered here.

Anton needs this for three things: to document what makes up a spreadsheet or presentation (NDSA Cn-1.1), to verify that it still does (Cn-2.1), and to prove after a migration that nothing significant was lost ([`media:migrate`](console-commands.md#mediamigrate)).

## Formats {#formate}

### Spreadsheets

| Level | Format | Condition |
|---|---|---|
| preferred | ODS (OpenDocument Spreadsheet) | without a password |
| preferred | CSV in UTF-8 | for plain data, with a description |
| accepted | XLSX | without a password |
| accepted | XLS | as long as LibreOffice reads it |
| accepted | PDF/A | only as an additional view beside the original |

### Presentations

| Level | Format | Condition |
|---|---|---|
| preferred | ODP (OpenDocument Presentation) | without a password |
| preferred | PDF/A-2u | where the slides are fixed; see [PDF](formate-pdf.md) |
| accepted | PPTX, PPT | as long as LibreOffice reads them |

**Spreadsheets:** Preferred is ODS, as ODT is for [text](formate-text.md#formate); NARA prefers it and rates it low risk. XLSX is accepted, as DOCX is: NARA considers it acceptable, at moderate risk, and KOST recommends it. Both stay in their original format, since only there do formulas, hidden rows and sheets survive; KOST advises against converting between them. LibreOffice reads XLS; KOST advises converting it to XLSX, NARA only for versions before Excel 97. Under the principle it stays until it can no longer be read. For plain data without formulas or formatting, CSV in UTF-8 is the most durable format; NARA prefers it. Since CSV has no fixed standard and cannot be validated, the depositor supplies a description: delimiter, escaping of delimiters and line breaks, quotes, number of fields, encoding and data types (KOST). PDF/A holds only the appearance, not the calculation, and a conversion to PDF/A «must be judged very critically indeed» (KOST): as a view beside the original, not in its place.

**Presentations:** Preferred is ODP, like ODT and ODS; NARA prefers it, KOST rejects ODP for the same reasons as ODT. Where the slides are fixed, for instance for a talk given as it stands, the depositor had better also deliver PDF/A-2u. NARA rates PPTX low risk, KOST accepts it. LibreOffice reads Keynote only partly; the depositor exports it as PPTX or PDF.

In both cases the original stays the master. Anton does not convert at ingest.

Here too: an archive keeps [as few formats as possible](formate-bild.md#formate). The depositor delivers without password or write protection and switches off automatic updating of date fields.

## Significant properties

Grouped as NARA does into appearance, structure, behaviour and context. The questions are the same as for [text](formate-text.md#wesentliche-eigenschaften); for spreadsheets NARA also asks whether deleting a sheet changes the content.

### Spreadsheets

| Group | Property | Source |
|---|---|---|
| Appearance | formatting where it conveys information (conditional formatting, colour coding) | NARA |
| | charts and graphics | NARA |
| | comments | NARA |
| | pivot tables | NARA |
| Structure | value of every cell | NARA |
| | sheets with their names | NARA |
| | number of rows and columns, hidden ones included | NARA |
| | character encoding and, for CSV, delimiter and escaping | NARA, KOST |
| Behaviour | formulas, where they explain how a value was calculated or a pivot table depends on them | NARA, KOST |
| | links within the file | NARA |
| Context | links to other files and data sources: recorded | NARA |

According to NARA, what counts first is the value in the cell, not the formula: «The final data in the cell itself is the core feature». The formula counts where it explains the value. Not to be preserved are macros and frozen rows or columns. Links to other files or to the web are recorded; the archive keeps their target only if it was delivered along.

### Presentations

| Group | Property | Source |
|---|---|---|
| Appearance | slides and their order | NARA |
| | text, tables, images and graphics | NARA |
| | page size and orientation, fonts, colour, where the slides are fixed | NARA |
| | embedded audio and video | NARA |
| Structure | speaker notes | NARA |
| | outline | NARA |
| Behaviour | links within the file | NARA |
| Context | embedded metadata (title, author, dates, language) | NARA |

Speaker notes count when they hold what is not on the slides; that is often the case. Animations and transitions need not be preserved, as long as the slides are complete and legible without them (NARA).

## What Anton measures and checks

As of version 0.111.1.

| Property | Measured | Checked |
|---|---|---|
| Format | PRONOM PUID with Siegfried, as for all files | mismatch between extension, MIME type and PUID as a warning |
| Can be opened | – | only indirectly for presentations: LibreOffice must read them to make the access copy, which is validated like a PDF; for spreadsheets no |
| Text | for full text: XLSX, ODS, PPTX, ODP and CSV directly, PPT from the PDF access copy; XLS not | no |
| Character encoding and dialect (CSV) | encoding, byte order mark, line endings, delimiter (comma, semicolon, tab, pipe) and number of fields in the first line, with libmagic at ingest | – |
| all other properties | no | no |

## Limits

- No access copy is made for spreadsheets; they appear as a download under «Other files». This is decided: a spreadsheet as PDF falls apart over many pages when sheets are wide, and does not show hidden rows.
- For presentations (ODP, PPTX, PPT) LibreOffice makes a PDF access copy as for [text](formate-text.md) (anton#719); they then appear under «Documents» in the PDF viewer. The copy shows the slides, not the speaker notes. A server without LibreOffice Impress makes none.
- XLS does not reach the full-text index.
- For CSV the delimiter is inferred: the one that splits the first line, quotes respected, into the most fields. It does not replace the depositor's description.
- Whether a spreadsheet contains formulas, hidden rows, macros or links to other files, Anton does not measure.

## What a migration must check

Anton has no rule yet that converts spreadsheets or presentations. When one comes, for instance XLS to XLSX, afterwards:

- Spreadsheets: the value of every cell is the same, in all sheets; the number of sheets, rows and columns is the same, hidden ones included; formulas and comments are carried over.
- Presentations: number and order of slides are the same; speaker notes and embedded media are carried over.
- The embedded metadata is carried over.
- The delivered file stays as an [original](preservation.md#behaltene-originale).

## Sources {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Spreadsheets](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_Spreadsheets.md), plan date 2023-11-22. Significant properties, questions, values before formulas, counts, transfer formats.
- NARA: [Preservation Action Plan for Presentation and Publishing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_PresentationAndPublishing.md), plan date 2023-12-05. Slide order, speaker notes, animations, transfer formats.
- NARA: [Preservation Action Plan, format table](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), as of 2026-03-20. Risk and action per format: ODS, ODP, CSV, PPTX low; XLSX, XLS moderate; old XLS to ODS; Keynote to PPTX or PDF.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Transfer formats the plans refer to.
- KOST, Katalog archivischer Dateiformate (KaD), version 7.1, May 2026: [Spreadsheets, summary](https://kost-ceco.ch/cms/kad_spreadsheet_intro_de.html), [CSV](https://kost-ceco.ch/cms/kad_csv_de.html) and [Text, summary](https://kost-ceco.ch/cms/kad_text_intro_de.html) (on PPTX and ODP). Original format as a provisional solution, no conversion between XLSX and ODS, PDF/A critical, description of CSV.
- [LibreOffice](https://www.libreoffice.org/): open-source office suite, reads ODS, XLSX, XLS, ODP, PPTX and PPT.
- NDSA: [Levels of Digital Preservation, version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), March 2026, requirements Cn-1.1 and Cn-2.1.
