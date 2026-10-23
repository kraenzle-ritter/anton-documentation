# Text: formats and significant properties

This page sets out, for text documents, which formats Anton prefers and accepts, which properties must be preserved, and what Anton measures or checks of them today. It belongs to the series per format category (anton#687), after [images](formate-bild.md) and [PDF](formate-pdf.md). Spreadsheets (XLSX, ODS, CSV) and presentations (PPTX, ODP) are on a [page of their own](formate-tabellen.md).

Anton needs this for three things: to document what makes up a text document (NDSA Cn-1.1), to verify that it still does (Cn-2.1), and to prove after a migration that nothing significant was lost ([`media:migrate`](console-commands.md#mediamigrate)).

## Formats {#formate}

| Level | Format | Condition |
|---|---|---|
| preferred | ODT (OpenDocument Text) | without a password |
| preferred | PDF/A-2u | where appearance counts; see [PDF](formate-pdf.md) |
| preferred | TXT in UTF-8 | for plain text |
| accepted | DOCX | without a password |
| accepted | TXT in another encoding | ASCII, ISO-8859, UTF-16 |
| accepted | DOC, RTF | as long as LibreOffice reads them |

**Preferred** is ODT: an open ISO standard (ISO/IEC 26300), which NARA prefers in all versions and rates low risk. KOST, by contrast, rejects ODT because of fonts not embedded, macros and limited adoption; it names the same shortcomings for DOCX, which it accepts nevertheless. Anton follows NARA here. Where appearance counts, as with a deed or a publication, the depositor had better deliver PDF/A-2u, since a text document has no fixed pages. Plain text lasts best as TXT in UTF-8.

**Accepted** is, as with images, what widespread open-source tools can read and will in all likelihood go on reading; for text documents that is LibreOffice. NARA rates DOCX low risk; KOST considers it «conceivable» if its shortcomings can be mastered. NARA rates DOC moderate and RTF mostly low risk and advises conversion, DOC to ODT, RTF to PDF keeping the original. Under the principle they stay until they can no longer be read. TXT in an encoding other than UTF-8 is accepted when the encoding is known and recorded; the file itself does not state it (KOST).

A text document has no fixed pages. Page breaks and appearance arise only when it is opened, with whatever fonts the computer has at hand. What «where appearance is fixed» means for PDF, a text document cannot reliably hold. The original therefore stays the master, and Anton does not convert at ingest, not even to PDF/A as KOST recommends for the active phase: a conversion loses tracked changes, comments and fields.

Here too: an archive keeps [as few formats as possible](formate-bild.md#formate). The depositor uses standard fonts, delivers without password or write protection, and switches off automatic updating of date fields: otherwise opening the file in the archive overwrites the document's date (KOST).

## Significant properties {#wesentliche-eigenschaften}

Grouped as NARA does into appearance, structure, behaviour and context, with the same distinction as for [PDF](formate-pdf.md#wesentliche-eigenschaften): if a document is kept for its content, the text counts; if it is kept as evidence of its form, what it looks like counts as well.

| Group | Property | Level | Source |
|---|---|---|---|
| Appearance | text with paragraphs, lists and tables | always | NARA |
| | images and graphics | always | NARA |
| | footnotes, headers and footers | always | NARA |
| | page size and orientation | where appearance is fixed | NARA |
| | fonts with style, size and emphasis | where appearance is fixed | NARA, KOST |
| | colour | where appearance is fixed | NARA |
| Structure | character encoding | always | NARA, KOST |
| | outline (headings) | always | NARA |
| | links within the document | always | NARA |
| | embedded objects | always | NARA, KOST |
| Behaviour | The document can be opened. | always | NARA |
| | tracked changes and comments | always, where present | NARA |
| Context | embedded metadata (title, author, dates created and modified, language) | always | NARA |

Tracked changes and comments are often invisible when the document is opened, but can be content: a deleted passage, an objection in the margin. A conversion to PDF loses them or prints them along, depending on the settings.

Not to be preserved are macros and fields that update when the document is opened (date, page number, table of contents). They run code or change the document; what is preserved is the value they showed at deposit. NARA advises checking macros for their function before removing them. NARA's counts (words, characters, paragraphs, tables, graphics) are not properties to be preserved but an aid for checking completeness after a conversion.

## What Anton measures and checks

As of version 0.111.1.

| Property | Measured | Checked |
|---|---|---|
| Format | PRONOM PUID with Siegfried, as for all files | mismatch between extension, MIME type and PUID as a warning |
| Can be opened | – | only indirectly: format validation does not cover text formats, but for ODT, DOCX, DOC and RTF LibreOffice must read the document to make the access copy, which is validated like a PDF |
| Character encoding (TXT) | encoding, byte order mark and line endings with libmagic at ingest | – |
| Text | for full text: ODT and DOCX directly, DOC and RTF from the PDF access copy (with `fulltext-from-webpdf` DOCX too); TXT and Markdown, converted to UTF-8 | no |
| all other properties | no | no |

## Limits

- For TXT the access copy is the text in UTF-8 (iconv); the master stays unchanged. For ODT, DOCX, DOC and RTF LibreOffice makes a PDF access copy (anton#714); the document then appears under «Documents» in the PDF viewer. A server without LibreOffice makes none, and the document stays a download under «Other files». Older documents get the copy only with [`media:conversions`](console-commands.md).
- The access copy is a view, not evidence of appearance. LibreOffice does not always render DOCX the way Word does: fonts, page breaks, tables and fields may differ.
- Upload takes ODT, DOCX, DOC, RTF and TXT; the QR upload only images and PDF.
- For TXT ingested before version 0.111.1 the encoding is not recorded; full text and access copy detect it when they are made.
- libmagic detects an encoding only by likelihood. Anton reads ISO-8859-1 and unknown 8-bit encodings as Windows-1252, which matches ISO-8859-1 wherever that is defined and adds typographic quotes and dashes.
- Format validation does not cover text formats. Anton notices a damaged DOCX or ODT only when it cannot be opened.
- Whether a document contains macros, automatic fields, tracked changes or embedded objects, Anton does not measure.

## What a migration must check

Anton has no rule yet that converts text documents. When one comes, for instance DOC to ODT or DOCX to PDF/A-2u, afterwards:

- The text is the same, apart from whitespace; the counts (words, paragraphs, tables, graphics) match.
- Images, tables, footnotes, headers and footers are carried over.
- Tracked changes and comments are carried over, or their loss is recorded in the event.
- The embedded metadata, the dates in particular, are carried over and not replaced by the date of the conversion.
- The delivered file stays as an [original](preservation.md#behaltene-originale).

## Sources {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Textual and Word Processing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_TextualAndWordProcessing.md), plan date 2023-11-22. Significant properties in four groups, questions on content and evidential value, counts, preferred and acceptable transfer formats.
- NARA: [Preservation Action Plan, format table](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), as of 2026-03-20. Risk and action per format: TXT, ODT and DOCX low, retain; DOC moderate, to ODT; RTF to PDF keeping the original.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Transfer formats the plan refers to.
- KOST, Katalog archivischer Dateiformate (KaD), version 7.1, May 2026: [Text, summary](https://kost-ceco.ch/cms/kad_text_intro_de.html), [TXT](https://kost-ceco.ch/cms/kad_txt_de.html), [OOXML](https://kost-ceco.ch/cms/kad_ooxml_de.html) and [ODF](https://kost-ceco.ch/cms/kad_odf_de.html). Recommended PDF/A, accepted TXT and DOCX, rejected ODT; risks of word-processing formats (fields, fonts, macros, encryption), character encoding of TXT.
- [LibreOffice](https://www.libreoffice.org/): open-source office suite, reads ODT, DOCX, DOC and RTF.
- NDSA: [Levels of Digital Preservation, version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), March 2026, requirements Cn-1.1 and Cn-2.1.
