# Preservation mandate

Under **Administration › Digital preservation › Preservation mandate** the archive decides who looks after its files. Storage, backup, checks and reports belong to the base offer either way; the mandate settles who acts on the reports.

## Two decisions

**Technical care by Kränzle & Ritter** (package «Technical care»). Kränzle & Ritter

- looks through the logs every month, clears anything unusual with the archive and confirms the [review](protokolle.md) on the archive's behalf;
- evaluates the format risks and maintains the format list and format rules;
- carries out migrations according to its own risk assessment, without asking in each case. Kränzle & Ritter draws on the recommendations of NARA's Digital Preservation Framework; they are not binding.

The following applies:

- With every migration the delivered file stays as a [kept original](preservation.md#behaltene-originale); the migration can be undone.
- Measures that discard the delivered file (such as `tiff_zip`) are included only if the archive ticks them.
- Formats (PRONOM IDs) and fonds (with everything below them) can be excluded.
- Kränzle & Ritter asks only when a measure needs more storage than booked, and then the overall responsibility.
- For ingest the archive decides whether the delivered file is kept beside a conversion (default: no, the conversion replaces it where the rule says so) and whether damaged or unreadable files are taken in and reported or refused (default: taken in and reported).

The principle: Anton keeps every file as it was taken in. Kränzle & Ritter migrates formats at risk into archival formats, such as print files to PDF/A, and only once the risk calls for it; migrations held in reserve cost storage and computing time without making the files any safer. The file taken in stays as a kept version, and the migration can be undone. Kränzle & Ritter checks every migration page by page and image by image, with checksums recorded before and after. A deliberate exception, which the archive can allow, is the lossless repacking of TIFF files (Deflate with predictor): Anton compares the pixels of every page before and after, and since the image content verifiably stays the same, it does not keep the delivered file. That saves storage and so costs.

Since the package costs, the **overall responsibility** confirms this decision. Its confirmation counts as ordering the package on the page [Contract](contract.md), revoking as cancelling.

**Own preservation strategy.** The archive carries digital preservation itself and describes its strategy: briefly, with a link to the document, or as a [strategy document](#strategy-document) in JSON. Kränzle & Ritter does not look through the logs or evaluate format risks and migrates only on the archive's order. If asked, Kränzle & Ritter helps to work out and file the strategy. A contact person for **digital preservation** confirms this decision.

## Strategy document

Every decision has a machine-readable strategy document following schema 1 of [kraenzle-ritter/preservation-strategy](https://github.com/kraenzle-ritter/preservation-strategy). Anton keeps it byte for byte as it was confirmed, together with its SHA-256 checksum.

- **Technical care:** Anton writes the document itself, from Kränzle & Ritter's template, the archive's choices on the page, the booked packages and the format rules as they apply to the archive. A rule that works on ingest appears as an ingest rule, in force as its switch stands; a rule `media:migrate` may apply appears as a preservation rule.
- **Own preservation strategy:** The archive can upload its document as a JSON file (at most 1 MB). The short description is then optional. Anton checks the file against the schema and refuses it with the errors found if it is invalid, written for the other decision (`variant` must be `own`) or excludes fonds this Anton does not hold. The document names fonds by their permanent address `https://<archive>/id/<uuid>`. Exclusions, lossy measures and the version are taken from the file.

The confirmation mail summarises the document and names its version and checksum. All admins can download the document of the decision in force and of every earlier one (JSON, with the checksum in the header `X-Content-SHA256`). Every migration resting on the preservation mandate names, in the [PREMIS rights statement](export-matrix.md), the version and checksum of the document in force at that time.

Under technical care a new confirmation is needed only when the archive changes its choices: decision, lossy measures, exclusions or ingest. When Kränzle & Ritter changes or switches a format rule, Anton writes a new version of the document under the same confirmation; the list of decisions shows it as a row of its own. The security log records every new version. If nothing changes, no new version is written.

Decisions from Anton 0.118.0 have no document yet. They keep holding and get one with their next confirmation.

## Granting, confirming, revoking

- Accounts holding **Change digital preservation** decide; all admins can view the page.
- The decision goes as a [confirmation by mail](contacts.md#confirmation-by-mail) to the contact persons concerned and holds once one of them confirms. The previous decision is superseded then. Without a named contact person who can confirm, nothing can be asked.
- Revoking takes effect at once. Kränzle & Ritter then migrates no file without an order from the archive; the contact persons and Kränzle & Ritter receive a mail.
- The wording is kept as it was confirmed, with its version. The list at the bottom of the page shows all earlier decisions.

## Single migrations

Without a decision, with an own strategy, or outside what the technical care covers, each migration needs an order from the archive: a confirmation by mail (`media:migrate --request-approval`, see [console commands](console-commands.md#mediamigrate)) or an agreement made outside Anton. The request names the rule, the number of files, their size and the estimated additional storage; the confirmation holds for exactly these files.

The [monthly report](protokolle.md) names every migration carried out with the number of files, the additional storage and the ground: preservation mandate, confirmation by mail or agreement.

!!! note "DIMAG"
    Archives that keep their masters in DIMAG have no preservation mandate here; preservation lies in DIMAG.
