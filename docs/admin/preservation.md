# Langzeitarchivierung: Überblick

Anton deckt Teile der digitalen Langzeitarchivierung ab und überlässt andere
bewusst der Infrastruktur oder einem angebundenen Langzeitarchiv. Diese Seite
ordnet ein, was wo passiert, und verweist auf die Detailseiten. Sie beantwortet
vor allem die Frage, welches Artefakt eine **Sicherung** ist und welches eine
**Publikationsansicht**.

## Die Kette

### Übernahme

Beim [SIP-Ingest](sip-ingest.md) nach eCH-0160 prüft Anton für **jede Datei im
Paket** die in der `metadata.xml` deklarierte Prüfsumme nach: Der Hash wird über
die tatsächliche Datei neu berechnet und verglichen. Weicht er ab, schlägt die
Validierung fehl. Der Algorithmus stammt aus dem Paket selbst, ist also nicht auf
MD5 festgelegt. Zusätzlich merkt sich Anton die Prüfsumme des SIP-ZIPs und weist
bereits eingespielte Pakete ab.

### Speicherung

Für jede Mediendatei berechnet Anton beim Upload eine **MD5-Prüfsumme** und legt
sie in der Datenbank ab. Der **Master bleibt unverändert**; die Ableitungen
(`web`, `thumb`) sind Zugriffskopien.

### Formaterkennung und Risiko

Beim Upload identifiziert Anton das Format über **Siegfried** bzw. **Fido** und
hält die **PRONOM-ID** fest; daraus leitet es die Risikobewertung nach dem
**NARA Digital Preservation Framework** ab. Für Altbestände lässt sich das mit
[`media:identify`](console-commands.md#mediaidentify) nachtragen. Ausgewertet wird das im
[Preservation Planning](preservation-planning.md).

!!! note "Abhängig vom Server"
    Die Erkennung setzt voraus, dass Siegfried oder Fido auf dem Server
    installiert sind. Fehlen beide, bleibt die PRONOM-ID leer — und ohne sie
    gibt es auch keine Risikobewertung. Der Reiter «Nicht identifizierte Medien»
    zeigt, wie vollständig die Erkennung ist.

### Abgabe

Siehe [Sicherung oder Publikation?](#sicherung-oder-publikation) weiter unten.

## Integrität prüfen

Anton bringt die Werkzeuge mit, führt sie aber nicht von sich aus aus:

| Befehl | Was er tut |
|---|---|
| [`media:check --levels=4`](console-commands.md#mediacheck) | Liest jede Datei neu, berechnet die MD5 frisch und vergleicht sie mit der Datenbank. Mit `--log-integrity-check` wird jede Prüfung als Ereignis protokolliert — so entsteht eine nachweisbare Historie. |
| [`media:snapshot --verify --git`](console-commands.md#mediasnapshot) | Schreibt einen Prüfsummen-Schnappschuss aller Medien, vergleicht ihn gegen die Datenbank und committet Änderungen in ein lokales Git-Repository. Damit ist nachvollziehbar, was sich zwischen zwei Läufen verändert hat. |

!!! important "Einzurichten, nicht eingebaut"
    Anton führt **keine** wiederkehrende Integritätsprüfung von selbst aus — es
    gibt keinen eingebauten Zeitplan. Die Prüfung wird pro Installation als
    Cronjob eingerichtet. Zurzeit ist das für die grossen Archive eingerichtet;
    für weitere Installationen ist k & r zuständig.

Davon zu unterscheiden ist [`anton:doctor`](console-commands.md): Es prüft die
**Konsistenz der Datenbank** — Hierarchie, Signaturen, abgeleitete Felder — und
ob die Dateien vorhanden sind. Prüfsummen vergleicht es nicht.

## Sicherung oder Publikation?

Die wichtigste Unterscheidung, und die am leichtesten zu verwechselnde:

| Artefakt | Zweck |
|---|---|
| **Nativer Export** (`anton:export-native`) | **Sicherung.** Verlustfrei und wieder einlesbar: Metadaten in allen Sprachen, Ereignisse, Textfelder — auch private —, Normdaten-Bezüge über UUID und die **Master-Medien**. |
| **SQL-Dump** | **Sicherung.** Das einzige Artefakt mit Benutzern, Einstellungen, Formularen und der Datei-Provenienz (PRONOM/NARA-Historie). Enthält keine Mediendateien. |
| [**DIP**](download-dip.md) (BagIt) und [**OCFL**](download-ocfl.md) | **Abgabepakete.** Medien und Metadaten gebündelt, mit Prüfsummen im Manifest. |
| [**RDF/CIDOC**](download-rdf.md), **EAD**, **TEI**, **Memobase** | **Publikationsansichten.** Gefiltert und verlustbehaftet — aus ihnen lässt sich Anton nicht wiederherstellen. |

!!! danger "Ein RDF- oder EAD-Export ist kein Backup"
    Diese Formate sind für Recherche und Austausch gebaut. Ihnen fehlen unter
    anderem die UUIDs, die Rohwerte und die Schutzfristen; private Inhalte sind
    herausgefiltert. Für eine Sicherung braucht es den nativen Export **und**
    den SQL-Dump.

Welche Daten jedes Format im Einzelnen mitnimmt und welche nur im SQL-Dump
stehen, zeigt die [Export-Matrix](export-matrix.md).

Für die [statische Publikation](statische-publikation.md) eines Bestandes als
eigenständige Website gibt es ein eigenes Bundle.

## Was Anton nicht tut

Damit keine falschen Erwartungen entstehen:

- **Keine Formatmigration.** Anton erzeugt Zugriffskopien, aber normalisiert
  nicht in Archivformate — kein TIFF nach JPEG2000, kein PDF/A, keine
  Video-Normalisierung. Das Preservation Planning **weist auf Handlungsbedarf
  hin, handelt aber nicht**.
- **Kein PREMIS, kein METS.**
- **Keine Speicherredundanz.** Die redundante Speicherung leistet die
  Betriebsinfrastruktur, nicht die Anwendung: Beim Betrieb durch k & r liegen
  die Daten in [drei Kopien an drei Standorten](../faq/longterm_archives.md)
  (gesamthaft sechsfache Redundanz). Anton selbst kennt davon nichts — es sieht
  einen lokalen Speicher und optional einen Cloud-Speicher und kann die
  Redundanz weder anzeigen noch überwachen.

## Mit angebundenem Langzeitarchiv

Bei Installationen mit [DIMAG-Anbindung](inge.md) übergibt Anton jede
Mediendatei beim Upload über die Middleware Inge an DIMAG und führt Buch, ob die
Übergabe verifiziert ist — siehe [Upload-Status](dimag-uploads.md). Danach liegt
die Bitstream-Sicherung des Masters bei DIMAG.

!!! note "Anton prüft dann nicht mehr selbst"
    Auf diesen Installationen überspringt `media:check` die Integritätsprüfung
    der Master mit dem Hinweis, dass die Dateien in DIMAG liegen. Die Fixity
    verantwortet dort das Langzeitarchiv. Auf Wunsch löscht Anton nach
    verifizierter Übergabe die lokale Kopie.
