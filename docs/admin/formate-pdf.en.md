# PDF: formats and significant properties

This page sets out, for PDF, which versions Anton prefers and accepts, which properties of a PDF must be preserved, and what Anton measures or checks of them today. It belongs to the series per format category (anton#687), after [images](formate-bild.md). Text formats such as DOCX, ODT and TXT are on the page [Text](formate-text.md); PDF containing photographs only is covered by the page on images.

Anton needs this for three things: to document what makes up a PDF (NDSA Cn-1.1), to verify that it still does (Cn-2.1), and to prove after a migration that nothing significant was lost ([`media:migrate`](console-commands.md#mediamigrate)).

## Formats {#formate}

| Level | Format | Condition |
|---|---|---|
| preferred | PDF/A-2u | |
| preferred | PDF/A-2b | for scans with OCR |
| accepted | PDF/A-1a, PDF/A-1b, PDF/A-2a | |
| accepted | PDF/A-4 | without embedded files (not 4f) |
| accepted | PDF 1.0 to 1.7, PDF 2.0 | fonts embedded; opens without a password |
| not accepted | PDF/A-3, PDF/A-4f | embedded files of any type |
| not accepted | PDF that opens only with a password | |

**Preferred** is PDF/A-2u. PDF/A-2 allows what PDF/A-1 still forbade (transparency, layers, JPEG 2000), and «u» requires every character to map to a Unicode character: the text can then be searched, copied and read aloud, not only looked at. This is what KOST recommends. In scans the text comes from OCR and is only as good as the recognition anyway; there PDF/A-2b, which secures only the appearance of the page, suffices. OCR in Anton writes PDF/A-2b for scans; a PDF that already has text stays plain PDF, so that Ghostscript does not rewrite its fonts and vector text (anton#712). NARA lists PDF/A-1 and PDF/A-2 as preferred transfer formats.

**Accepted** is, as with images, what widespread open-source tools can read and will in all likelihood go on reading. Plain PDF belongs to it: NARA rates PDF 1.7 and 2.0 low risk and PDF 1.0 to 1.6 moderate risk and retains both; KOST considers PDF suitable for archiving «in principle». Anton does not convert PDF to PDF/A at ingest. Following the [format decisions](preservation.md#formatentscheide), Anton migrates only when a file can no longer be rendered, and according to KOST a conversion to PDF/A is «mostly unproblematic» later as well.

**Not accepted** is PDF/A-3. It equals PDF/A-2 but may embed files of any type, such as a Word document or an Excel sheet behind an invoice. These files can be neither identified nor validated, and Anton does not see them: they would have no PUID, no format validation, no access copy. KOST rejects PDF/A-3 for this reason. The same holds for PDF/A-4f. Depositors deliver PDF/A-2 instead, and the embedded files as files of their own. If a PDF/A-3 arrives nevertheless, Anton takes it in like any PDF and records embedded files with their types as a risk. In the holdings on umberto PDF/A-3 is an exception: on 2026-10-23, among some 70,000 validated PDFs, a single one claimed to be PDF/A-3.

A PDF that opens only with a password can be neither validated nor rendered by Anton. A PDF that only locks printing or copying can be opened; it is accepted, and Anton records the encryption as a risk.

Here too: an archive keeps [as few formats as possible](formate-bild.md#formate). Whoever produces PDF, for instance when scanning or exporting from a word processor, chooses PDF/A-2. The depositor embeds all fonts and avoids JavaScript, encryption, embedded audio and video, and JBIG2 compression: its lossy pattern matching can swap characters unnoticed, such as a 6 for an 8.

## Significant properties {#wesentliche-eigenschaften}

Grouped as NARA does into appearance, structure, behaviour and context. NARA distinguishes whether a document is kept for its content or as evidence of its form. For minutes the text counts; for a publication, a plan or a deed, what the page looks like counts as well. The table therefore separates two levels: «always» and «where appearance is fixed».

| Group | Property | Level | Source |
|---|---|---|---|
| Appearance | number and order of pages | always | NARA |
| | images and graphics | always | NARA |
| | forms and annotations | always | NARA |
| | page size and orientation | where appearance is fixed | NARA |
| | fonts with style and size | where appearance is fixed | NARA, KOST |
| | colour | where appearance is fixed | NARA, KOST |
| Structure | text that can be extracted, in Unicode | always | NARA, KOST |
| | bookmarks (outline) | always | NARA |
| | embedded files | always | NARA, KOST |
| Behaviour | The PDF can be rendered. | always | NARA |
| | links within the document | always | NARA |
| Context | embedded metadata (XMP, title, author, date, language) | always | NARA |

Embedded files appear here although PDF/A-3 is not accepted: a plain PDF can carry attachments too, and where they occur they belong to the document.

Not to be preserved are JavaScript, actions that start programs (`/Launch`), and links to other files (`/GoToR`) or to the web (`/URI`). They lead out of the file, and the archive does not keep their targets. Anton records them as a risk, so that it is visible what a migration drops. The same applies to encryption.

The version (PDF 1.4, PDF/A-2b) is not a property that must be preserved. It is recorded because it says what the PDF promises and what it is checked against.

## What Anton measures and checks

As of version 0.111.1.

| Property | Measured | Checked |
|---|---|---|
| Version | PDF version, at ingest with poppler | – |
| Number of pages | at ingest with poppler, at every format validation with qpdf or pdftocairo | no, there is no migration of PDF yet |
| Renderable | – | at ingest and nightly with [`media:validate-formats`](console-commands.md#mediavalidate-formats): qpdf; thorough with pdftocairo page by page, JPEG 2000 errors rechecked with MuPDF; also when the access copy is made |
| Fonts embedded | number of fonts | warning where the PDF shows text that needs a font not embedded (pdffonts) |
| Page size and orientation | most common page size in mm, number of different sizes, landscape pages and rotated pages | no |
| Text extractable | fonts without a Unicode mapping (ToUnicode) | no; such a font is a characteristic, not a risk: with standard encodings the text can still be extracted, only the PDF does not meet PDF/A-2u that way |
| Images | number of images | – |
| Embedded files | number and types | warning |
| JBIG2 | number of images using JBIG2 | warning |
| Forms and annotations | form (AcroForm or XFA), number of fields and of annotations | warning for a form without fields |
| Bookmarks, metadata | no | no |
| JavaScript, actions, links | number per kind (qpdf, pdfinfo) | warning |
| Encryption | yes | warning |
| PDF/A conformance | level the PDF claims | with veraPDF, when a PDF claims to be PDF/A and veraPDF is installed; a deviation is a warning |

The characteristics appear on the medium under **Technical characteristics**; for older PDFs [`media:validate-formats`](console-commands.md#mediavalidate-formats) fills them in, as long as the medium has no other characteristics yet. The findings are in the medium's `format-validation` event and, totalled, under [Preservation Planning → «Format validation»](preservation-planning.md#formatpruefung).

## Limits

- Anton reads page sizes for the first 2000 pages only.
- If a medium already has other characteristics, for instance from a TIFF rule, `media:validate-formats` does not fill in the PDF characteristics.
- Anton does not measure bookmarks and embedded metadata.
- veraPDF checks only what claims to be PDF/A. A plain PDF is not checked against PDF/A, nor is a PDF/A that has lost its identification in the XMP.
- If the conversion to PDF/A fails during OCR in the [QR upload](../user/qr-upload.md), OCR writes plain PDF. The reason is shown in the medium's upload actions (`pdfa_fallback`).
- The access copy (Ghostscript, `/ebook`) shrinks images for viewing. It is no normalisation and no replacement for the master.
- «Renderable» means the tools read and render every page without error. They do not check whether the page looks right.

## What a migration must check

Anton has no rule yet that converts PDF. When one comes, for instance PDF to PDF/A-2, afterwards:

- The number of pages is the same.
- Page size and orientation of every page are the same.
- The extractable text is the same, apart from whitespace.
- All fonts are embedded.
- veraPDF confirms the target version.
- Forms, annotations, bookmarks and metadata are carried over, or their loss is recorded in the event.
- The delivered file stays as an [original](preservation.md#behaltene-originale), since Ghostscript rewrites fonts and images.

## Sources {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Textual and Word Processing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_TextualAndWordProcessing.md), plan date 2023-11-22. Significant properties in four groups, the distinction between content and evidential value, preferred and acceptable transfer formats.
- NARA: [Preservation Action Plan for Presentation and Publishing](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_PresentationAndPublishing.md), plan date 2023-12-05. The same properties for publications, plus embedded audio and video.
- NARA: [Preservation Action Plan, format table](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), as of 2026-03-20. Risk and action per PDF version.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Transfer formats the plans refer to.
- KOST, Katalog archivischer Dateiformate (KaD), version 7.1, May 2026: [Text, summary](https://kost-ceco.ch/cms/kad_text_intro_de.html), [PDF](https://kost-ceco.ch/cms/kad_pdf_de.html), [PDF/A-2](https://kost-ceco.ch/cms/kad_pdfa2_de.html) and [PDF/A-3](https://kost-ceco.ch/cms/kad_pdfa3_de.html). Recommended and accepted versions, PDF/A-2u, rejection of PDF/A-3, conditions for plain PDF, JBIG2.
- [veraPDF](https://verapdf.org/): open-source PDF/A validator, by the PDF Association and the Open Preservation Foundation.
- Archivematica 1.17: [Preservation planning](https://www.archivematica.org/en/docs/archivematica-1.17/user-manual/preservation/preservation-planning/). For comparison: the format policy registry provides normalisation of PDF to PDF/A with Ghostscript, which each archive can change; Archivematica defines no significant properties and checks none after normalisation.
- NDSA: [Levels of Digital Preservation, version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), March 2026, requirements Cn-1.1 and Cn-2.1.
