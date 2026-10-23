# Images: formats and significant properties

This page sets out, for raster images, which formats Anton prefers and accepts, which properties of an image must be preserved, and what Anton measures or checks of them today. It is the first page of a series per format category (anton#687); PDF/text, audio and video follow. Vector graphics are not covered here.

Anton needs this for three things: to document what makes up an image (NDSA Cn-1.1), to verify that it still does (Cn-2.1), and to prove after a migration that nothing significant was lost ([`media:migrate`](console-commands.md#mediamigrate)).

## Formats

| Level | Format | Condition |
|---|---|---|
| preferred | TIFF with Deflate (ZIP) and predictor 2 | greyscale and colour, 8 or 16 bits per channel |
| accepted | TIFF in another form | uncompressed, LZW, CCITT G4 (bitonal), JPEG-compressed, BigTIFF, multi-page |
| accepted | JPEG | |
| accepted | PNG | |
| accepted | JPEG 2000 (JP2) | |
| accepted | HEIC/HEIF | stays the master, access copy JPEG |
| accepted | GIF, BMP, WebP | |
| accepted | DNG | |
| accepted | camera raw (CR2, CR3, NEF, ARW and others) | as long as LibRaw reads it |
| accepted | PDF/A | if it contains only images, such as scans without a text layer or with an OCR layer |
| accepted | PDF | if it contains photographs only |

**Preferred** means: this is what Anton recommends to depositors, and it is the form into which the rule [`tiff_zip`](preservation.md#regeln-fuer-dateien) losslessly repacks uncompressed TIFF and LZW without a predictor. Deflate with predictor 2 saves 38–66 % over uncompressed without changing a single pixel, and libtiff, ImageMagick, GIMP and Photoshop read it. It is not part of baseline TIFF, however; KOST recommends baseline with LZW or CCITT. Bitonal images are better left in CCITT G4, which compresses them more; `tiff_zip` therefore skips them.

**Accepted** is what widespread open-source tools can read and will in all likelihood go on reading. Anton takes in the file and keeps it in its format. Following the [format decisions](preservation.md#formatentscheide), Anton migrates only when a file can no longer be rendered. Images already compressed with loss (JPEG, JPEG-compressed TIFF, lossy JP2) are not converted to a lossless format: the lost information does not come back, the file would only grow (KOST says the same).

As a rule, we recommend keeping as few different formats as possible in one archive, so that preservation planning stays simple in the long run: every format has to be watched, checked and perhaps one day migrated (KOST says the same). The list of accepted formats says what Anton can preserve, not what an archive should collect. Where a holding brings many formats, it is therefore normalised before ingest where possible: by the depositor or with the [file rules](preservation.md#regeln-fuer-dateien) that Anton applies before the file becomes the master. Lossy images are the exception (see above).

PDF is listed here because some image holdings arrive as PDF. As soon as a PDF carries text, forms or links, the page on PDF/text applies.

HEIC/HEIF, as mobile phones deliver it, stays the master as it is; Anton converts only the access copy to JPEG. This is what NARA recommends as long as the file renders well. HEIF is an open ISO standard (ISO/IEC 23008-12), free tools (libheif, libde265) read it; the catch is HEVC compression with its patent pools, which is why Windows, Photoshop and some browsers do not open HEIC out of the box. HEIC is smaller than a JPEG made from it, and every conversion loses what the file holds besides the main image (depth map, HDR gain map). At ingest HEIC can be converted to JPEG, for archives where storage is expensive and the file should open everywhere, with a second lossy encoding; the [QR upload](../user/qr-upload.md) offers this today (`heic2jpg`, off by default). Conversion to TIFF is possible at any time later, without further loss but about ten times larger, with [`media:migrate`](console-commands.md#mediamigrate), once the rule for it exists (anton#710).

GIF, BMP and WebP are read by all common tools and browsers. NARA advises converting BMP; under the principle above it stays until that changes. DNG is an open Adobe specification based on TIFF; NARA rates it low risk, KOST considers it unsuitable for long-term preservation. Camera raw is specific to each maker and model and undisclosed; the open-source LibRaw reads it and has been maintained for this for many years. NARA advises conversion, and depositors who can should rather deliver DNG or TIFF. DNG and camera raw hold sensor data, the image only arises when it is developed; what matters there is that the sensor data is preserved, and a TIFF made from it does not replace the original. For JP2, BMP, DNG and camera raw no access copy is made yet (anton#711).

## Significant properties

Grouped as NARA does into appearance, structure, behaviour and context. The column «Source» names who considers the property significant; the sources are listed [below](#quellen).

| Group | Property | Source |
|---|---|---|
| Appearance | width and height in pixels, and so the aspect ratio | InSPECT, NARA |
| | bit depth and number of channels, including alpha | InSPECT, NARA |
| | colour space and ICC profile | NARA, LoC |
| | orientation (EXIF Orientation) | NARA |
| | pixel content, where the format is lossless | Anton |
| Structure | resolution in dpi (for scans, the scale to the original) | InSPECT, NARA |
| | number of pages in a multi-page TIFF | LoC, KOST |
| | compression: recorded, not preserved | NARA, KOST |
| Behaviour | The image can be rendered. | NARA |
| | for GIF and WebP, the animation | LoC |
| Context | embedded metadata (EXIF, IPTC, XMP), such as date taken, creator, rights | NARA |

Colour space counts here, unlike in InSPECT. InSPECT did not consider it significant because it changes in almost every migration. For scans of photographs, posters and maps, however, colour is content, and Anton migrates only when needed anyway. A migration that changes the colour space must carry the ICC profile along.

Compression is not a property that must be preserved. It is recorded because it tells whether the other properties are held losslessly.

Layers, editing steps and preview images in a TIFF are not significant behaviour: they belong to the software the image was made with, not to the image.

## What Anton measures and checks

As of version 0.111.

| Property | Measured | Checked |
|---|---|---|
| Width and height | TIFF at ingest with exiftool, when `tiff_zip` is switched on | via the pixel signature after `tiff_zip` and `media:migrate` |
| Bit depth and channels | likewise | likewise |
| Colour space and ICC profile | likewise (name of the profile) | no |
| Orientation | no | no |
| Pixel content | pixel signature per page with ImageMagick, only for `tiff_zip` and `media:migrate` | yes, must stay the same, otherwise the delivered file remains |
| Resolution | no | no |
| Number of pages | TIFF with exiftool, as above, previews counted separately | via the pixel signature per page |
| Compression | TIFF with exiftool, as above | – |
| Renderable | – | at ingest and nightly with [`media:validate-formats`](console-commands.md#mediavalidate-formats): TIFF with tiffinfo (thorough: `-D`), JPEG, PNG, JP2, GIF, BMP and WebP with ImageMagick, HEIC, DNG and camera raw not yet (anton#710, anton#711); also when the access copy is made |
| Embedded metadata | no | `tiff_zip` carries it over with exiftool but does not compare it |

Measured values appear on the medium under **Technical characteristics** and in the dry run before a spreadsheet import.

## Limits

- For JPEG, PNG, JP2, HEIC, GIF, BMP, WebP, DNG and camera raw Anton records no characteristics, only PUID, MIME type and size. Likewise for TIFF from SIPs and for TIFF in archives that have not switched on `tiff_zip`.
- Anton measures orientation and resolution for no format.
- Embedded metadata is carried over by `tiff_zip` but not compared. Nothing proves that all fields are still present after a migration.
- Anton does not check whether a PDF contains photographs only.
- Format validation does not cover HEIC/HEIF yet, and `heic2jpg` discards the HEIC (anton#710).
- For JP2, BMP, DNG and camera raw no access copy is made, and format validation does not cover DNG and camera raw (anton#711).
- The check «renderable» means the tool reads the file without error. It does not check whether the colours are right.

## What a migration must check

When `media:migrate` converts an image, afterwards:

- Width, height, number of pages, bit depth and channels are the same.
- With a lossless target, the pixel signature of every page is the same.
- The ICC profile is carried along, or the conversion is recorded in the event.
- The embedded metadata is carried over.
- The delivered file stays as an [original](preservation.md#behaltene-originale) when the target is lossy.

Today `media:migrate` checks only the pixel signature. With a lossless target it covers the first and second points, not the others.

## Sources {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Digital Still Image](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_DigitalStillImage.md), plan date 2024-11. Significant properties in four groups, preferred and acceptable formats.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Transfer formats the plan refers to.
- Lynne Montague, Adrian Brown, Gareth Knight, Stephen Grace: [InSPECT, Significant Properties Testing Report: Raster Images](https://significantproperties.kdl.kcl.ac.uk/rasterimages-testingreport.html), King's College London, 2009 ([PDF on Figshare](https://figshare.com/articles/journal_contribution/InSPECT_Significant_Properties_Testing_Report_Raster_Images/7137803)). Properties derived from NISO Z39.87 and tested on migrations between TIFF, JPEG and GIF.
- NISO Z39.87, Data Dictionary – Technical Metadata for Digital Still Images, and its XML schema: [MIX, Library of Congress](https://www.loc.gov/standards/mix/). The vocabulary of technical image metadata.
- Library of Congress, Sustainability of Digital Formats: [Still Image, Quality and Functionality Factors](https://www.loc.gov/preservation/digital/formats/content/still_quality.shtml). Rendering, resolution, colour maintenance, spectral bands, functionality beyond rendering.
- KOST, Katalog archivischer Dateiformate (KaD), version 7.1, May 2026: [Image, summary](https://kost-ceco.ch/cms/kad_image_intro_de.html) and [TIFF](https://kost-ceco.ch/cms/kad_tiff_de.html). Recommended and accepted image formats, archival TIFF, no immediate conversion of lossy images.
- NARA: [Preservation Action Plan, format table](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), as of 2026-03-20. Risk and action per format, among them HEIC («Moderate Risk», leave as is while it renders well).
- Library of Congress, Sustainability of Digital Formats: [HEIF (fdd000525)](https://loc.gov/preservation/digital/formats/fdd/fdd000525.shtml), with HEIC (fdd000526). Disclosure, adoption, HEVC patents.
- [LibRaw](https://www.libraw.org/): open-source library for reading camera raw formats.
- Archivematica 1.17: [Preservation planning](https://www.archivematica.org/en/docs/archivematica-1.17/user-manual/preservation/preservation-planning/). For comparison: identification with Siegfried, characterisation with ExifTool, no defined significant properties, no check of properties after normalisation.
- NDSA: [Levels of Digital Preservation, version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), March 2026, requirements Cn-1.1 and Cn-2.1.
