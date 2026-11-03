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

Since the package costs, the **overall responsibility** confirms this decision. Its confirmation counts as ordering the package on the page [Contract](contract.md), revoking as cancelling.

**Own preservation strategy.** The archive carries digital preservation itself and describes its strategy (briefly, with a link to the document). Kränzle & Ritter does not look through the logs or evaluate format risks and migrates only on the archive's order. A contact person for **digital preservation** confirms this decision.

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
