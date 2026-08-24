# SIP ingest (eCH-0160)

Anton enables the import/ingest of Submission Information Packages (SIP) in accordance with eCH-0160, whereby the files (dossiers) and documents are imported into the archival arrangement.

On the standard: [https://ech.ch/de/ech/ech-0160/1.2.0](https://ech.ch/de/ech/ech-0160/1.2.0)

!!! note "Since v0.62.0: unified import hub"
    All import paths — SIP, Excel, directory, agate — are brought together under `/import` (four tabs). The old URLs (`/sip/validation`, `/sip/ingest`, `/sip/inbox`) redirect transparently to the appropriate tab. See [user/import.md](../user/import.md) for the UI overview.

!!! note "agate SIP import (since v0.61.0)"
    BagIt SIPs sent by agate (the Anton preparation tool) via HTTP run through a separate path with NARA category mapping and an inbox. Details: [agate-sip.md](agate-sip.md).

### Requirements

#### Anton
- Accession archive: no longer needed. Up to v0.87.x a SIP ingest filed a receipt there; since v0.88.0 the run is in the import log (see [Import](../user/import.md#import-log)).
- The archive hierarchy (`parents`) must already exist in Anton.
- If the reference codes in the archive hierarchy have a prefix, this has to be set (setting: `identifier-prefix`).
- With the setting `strict_sip_validation`, Anton issues an error during validation if a file is not found in the SIP.
- Anton form (`default_intern`):
    - `sip_id`: links to the run in the import log this record came from (should be in the `default_intern` form).

!!! note "Example for identifier-prefix"
    The parent element (`<ordnungssystemposition>`) of the `<dossier>` corresponds to the `parent` in Anton. The `parent` in Anton is determined on the basis of the content of the `<nummer>` element in the SIP. If, for example, this number is "0.6.6" but the archival reference code is "A.1.4.0.6.6", the prefix has to be filled in accordingly with "A.1.4.".
