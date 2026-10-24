# Other formats: containers and XML

This page completes the series per format category (anton#687) with what falls into none of the categories [images](formate-bild.md), [PDF](formate-pdf.md), [text](formate-text.md), [audio and video](formate-av.md), and [spreadsheets and presentations](formate-tabellen.md): packed files (ZIP, GZ, TAR) and XML. Subtitles are covered under [audio and video](formate-av.md#formate). With this, the k & r default list is complete: every extension the upload accepts has a level.

## Containers {#container}

| Level | Format | Condition |
|---|---|---|
| accepted, for extraction | ZIP, GZ (TGZ too), TAR | without a password or encryption |
| accepted, packed | the same | only where the package itself is the unit, for instance a database dump or the source code of an application |

A container is not an archival format but a wrapping. What counts is its content, and for that the pages of the respective category apply. NARA rates ZIP and TAR moderate risk, GZIP low risk, and for all three advises keeping the container but extracting the files («Retain but extract files from the container»). KOST does not list containers as a format; in general it advises against compression with undisclosed algorithms and against compressing data that is already compressed. ZIP, GZIP and TAR are disclosed and lossless.

When a container is uploaded to an object, Anton asks what to do with it: **Import as directory** extracts it and the files enter the archive one by one; **Save as file** stores it unopened. The k & r default is to extract. A delivery stays packed only where it counts as a whole and its parts say nothing on their own; at KBA, for instance, the database dump and the source code of the predecessor application have been kept this way since 2018.

A SIP comes packed too; Anton extracts it on import.

## XML {#xml}

| Level | Format | Condition |
|---|---|---|
| accepted, by arrangement | XML 1.0 in UTF-8 | well-formed, with a schema (XSD) and a description |

XML is the most durable format for structured data; KOST recommends it for that, NARA rates it low risk. In Anton, however, XML today occurs only as metadata, in SIPs (eCH-0160, EAD, METS), and the import turns it into records; that belongs to metadata, not to the holdings. If an archive wants to keep XML as content, for instance an edition in TEI or an export from a specialised application, the depositor supplies the schema, as XSD, not as DTD (KOST), and describes what the elements mean. This is to be arranged; a page of its own follows when the time comes.

## What Anton measures and checks

As of version 0.112.0.

| Property | Measured | Checked |
|---|---|---|
| Format | PRONOM PUID with Siegfried, as for all files | mismatch between extension, MIME type and PUID as a warning; a MIME type «application/zip» counts as saying nothing, since DOCX, XLSX and ODT are ZIP as well |
| Container: can be extracted | – | before an upload or SIP is extracted: not too many entries, not too large, no links among the entries (anton#726) |
| Content of a packed container | no | no |
| XML | no | no |

## Limits

- The format check does not look inside a container that stays packed. What it holds, in which format, and whether it can still be read, Anton does not know.
- The upload does not accept XML. Browsers run XML, like HTML and SVG, as a document; Anton therefore never shows such files directly but only offers them for download (anton#640).
- Whether XML is well-formed or follows its schema, Anton does not check.

## Sources {#quellen}

- National Archives and Records Administration (NARA): [Preservation Action Plan, format table](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), as of 2026-03-20. ZIP and TAR moderate, GZIP and XML low risk; for containers «Retain but extract files from the container».
- KOST, Katalog archivischer Dateiformate (KaD), version 7.1, May 2026: [XML](https://kost-ceco.ch/cms/kad_xml_de.html), [Recommendation](https://kost-ceco.ch/cms/kad_recommendation_de.html) (structured data as XML) and [Data compression](https://kost-ceco.ch/cms/kad_compression_de.html). XSD rather than DTD, compression only disclosed and not twice.
- NDSA: [Levels of Digital Preservation, version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), March 2026, requirements Cn-1.1, Cn-2.1 and Cn-2.2.
