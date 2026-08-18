# Downloading a DIP

A **DIP** (Dissemination Information Package) is a ZIP package with which a
record and everything hanging below it can be passed on in a single step — for
handing over files to third parties, for example.

## How it works

In the detail view of a record — provided it is enabled for this level of
description — a **«DIP»** button appears in the download area. A click generates
the package and downloads it immediately. The file name is the reference code of
the record (e.g. `A.42.1.zip`).

If no button appears, the DIP download is not provided for at this level. Which
levels are enabled is determined by the administration.

## What is inside

The ZIP maps the record and all subordinate units as a folder structure:

- **media files** of all units contained, in folders named after the titles,
- a **Word finding aid** describing the content with metadata,
- a small **metadata file** (Dublin Core) for each media file,
- **checksums** (BagIt manifest) with which the completeness of the package can
  be verified later.

!!! tip "Size"
    A DIP contains **all** media of the record and its subordinate units. With
    extensive holdings the package can become large and creation may take a
    moment.

!!! note
    Depending on the archive, the package can also be delivered in a simplified
    form without a finding aid and metadata — in that case it contains only the
    folder structure with the original files.
