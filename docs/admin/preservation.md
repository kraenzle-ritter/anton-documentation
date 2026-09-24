# Langzeitarchivierung: Überblick

Anton übernimmt digitale Unterlagen geprüft, bewahrt die Master unverändert,
erkennt ihre Formate und hält fest, wie gut sie sich erhalten lassen. Die
Speicherung selbst und ihre Redundanz leistet die Betriebsinfrastruktur; bei
Installationen mit angebundenem Langzeitarchiv übernimmt dieses die
Bitstream-Sicherung. Diese Seite zeigt, wie sich die Aufgaben verteilen, und
verweist auf die Detailseiten. Sie beantwortet ausserdem die Frage, welches
Artefakt eine **Sicherung** ist und welches eine **Publikationsansicht**.

## Aufgabenteilung

Die digitale Langzeitarchivierung besteht aus mehreren Schichten. Anton deckt
die fachlichen ab, der Betrieb die Speicherung:

| Aufgabe | Anton | Betrieb | Angebundenes Langzeitarchiv |
|---|---|---|---|
| Prüfsummen bei der Übernahme | prüft jede Datei eines SIP gegen das Paket | | |
| Prüfsumme pro Datei | berechnet beim Upload MD5 und SHA-512 und legt sie ab | | |
| Formaterkennung und Risiko | PRONOM-ID, NARA-Bewertung, [Preservation Planning](preservation-planning.md) | stellt Siegfried bzw. Fido bereit | |
| Master und Zugriffskopien | bewahrt den Master unverändert, erzeugt `web` und `thumb` | | |
| Integritätsprüfung | bringt `media:check`, `media:snapshot` und `media:repair` mit, protokolliert die Prüfungen | legt den Rhythmus als Cronjob fest, richtet die Sicherung für `media:repair` ein | übernimmt die Fixity der Master |
| Redundante Speicherung | | Kopien an mehreren Standorten | Bitstream-Sicherung |
| Formatentscheide | zeigt Formate mit Handlungsbedarf | | |

**Bei Anton as a Service** ist k & r der Betrieb. **On Premises** ist es die
betreibende Institution.

## Die Kette

### Übernahme

Beim [SIP-Ingest](sip-ingest.md) nach eCH-0160 prüft Anton für **jede Datei im
Paket** die in der `metadata.xml` deklarierte Prüfsumme nach: Der Hash wird über
die tatsächliche Datei neu berechnet und verglichen. Weicht er ab, schlägt die
Validierung fehl. Der Algorithmus stammt aus dem Paket selbst, ist also nicht auf
MD5 festgelegt. Zusätzlich merkt sich Anton die Prüfsumme des SIP-ZIPs und weist
bereits eingespielte Pakete ab.

### Speicherung

Für jede Mediendatei berechnet Anton beim Upload eine **MD5-** und eine
**SHA-512-Prüfsumme** in einem Lesedurchgang und legt beide in der Datenbank ab.
SHA-512 ist der Referenzwert für die Integritätsprüfung, wie ihn OCFL und BagIt
empfehlen; MD5 bleibt für die Anbindung an DIMAG und für das Erkennen doppelter
Importe. Für Medien aus der Zeit vor Version 0.98 rechnet
[`media:checksum`](console-commands.md#mediachecksum) SHA-512 nach — und prüft
dabei jede Datei gegen ihre MD5. Der **Master bleibt unverändert**; die
Ableitungen (`web`, `thumb`) sind Zugriffskopien.

### Formaterkennung und Risiko

Beim Upload identifiziert Anton das Format über **Siegfried** bzw. **Fido** und
hält die **PRONOM-ID** fest; daraus leitet es die Risikobewertung nach dem
**NARA Digital Preservation Framework** ab. Für Altbestände lässt sich das mit
[`media:identify`](console-commands.md#mediaidentify) nachtragen. Ausgewertet wird das im
[Preservation Planning](preservation-planning.md).

!!! note "Siegfried oder Fido auf dem Server"
    Die Erkennung nutzt Siegfried oder Fido, die auf dem Server installiert
    sind. Fehlt das Programm, gelingt der Upload trotzdem, nur bleibt die
    Erkennung leer. [`anton:doctor`](doctor.md) meldet ein fehlendes `sf` darum
    als Fehler. Der Reiter «Nicht identifizierte Medien» zeigt, wie vollständig
    die Erkennung im Bestand ist.

### Formatentscheide

Anton migriert keine Master in Archivformate. Ob eine Datei in ein anderes
Format überführt wird, entscheidet das Archiv. Das Preservation Planning liefert dafür
die Grundlage: Es zeigt, welche Formate im Bestand liegen, welches Risiko NARA
ihnen zuweist und welche Handlung NARA empfiehlt.

### Abgabe

Siehe [Sicherung oder Publikation?](#sicherung-oder-publikation) weiter unten.

## Integrität prüfen

Zwei Befehle prüfen den Bestand gegen die gespeicherten Prüfsummen:

| Befehl | Was er tut |
|---|---|
| [`media:check --levels=4`](console-commands.md#mediacheck) | Liest jede Datei neu, berechnet die Prüfsumme frisch (SHA-512, wo vorhanden, sonst MD5) und vergleicht sie mit der Datenbank. Mit `--log-integrity-check` wird jede Prüfung als Ereignis protokolliert — so entsteht eine nachweisbare Historie. Eine fehlende Datei ist ein Befund, die Prüfung läuft weiter. |
| [`media:snapshot --verify --git`](console-commands.md#mediasnapshot) | Schreibt einen Prüfsummen-Schnappschuss aller Medien, vergleicht ihn gegen die Datenbank und committet Änderungen in ein lokales Git-Repository. Damit ist nachvollziehbar, was sich zwischen zwei Läufen verändert hat. |

!!! note "Den Rhythmus legt der Betrieb fest"
    Wie oft die Prüfung läuft, bestimmt ein Cronjob pro Installation. So lässt
    sich der Rhythmus der Grösse des Bestands anpassen: Ein vollständiger
    Durchlauf liest jede Datei, und bei mehreren Terabyte will das geplant sein.

    **Bei Anton as a Service** richtet k & r die Prüfung ein (Stand September
    2026 für die grossen Archive). **On Premises** richtet die betreibende
    Institution den Auftrag selbst ein; die Befehle stehen dafür bereit.

Davon zu unterscheiden ist [`anton:doctor`](console-commands.md): Es prüft die
**Konsistenz der Datenbank** — Hierarchie, Signaturen, abgeleitete Felder — und
ob die Dateien vorhanden sind. Die Prüfsummen vergleichen die beiden Befehle oben.

### Wenn die Prüfung anschlägt

Weicht eine Datei von ihrer Prüfsumme ab, holt
[`media:repair`](console-commands.md#mediarepair) sie aus der **lokalen Sicherung**
zurück: Es geht die Stände vom neuesten zum ältesten durch (täglich, monatlich,
jährlich) und nimmt den ersten, dessen Prüfsumme mit dem gespeicherten
Referenzwert übereinstimmt. Die beschädigte Fassung wird nicht gelöscht, sondern
in eine Quarantäne kopiert; jeder Vorgang steht als Ereignis in der Historie der
Datei.

Anton ersetzt eine Datei nur durch eine, deren Inhalt nachweislich dem Original
entspricht. Und die Anwendung selbst erreicht die Sicherung nicht: Nur root liest
sie, `media:repair` läuft als root und verweigert die Reparatur, wenn die
Sicherung für andere offen ist. Bei vielen Abweichungen
auf einmal repariert es nichts und schlägt Alarm, denn dann liegt die Ursache
anderswo (Platte, Einhängung, Schadsoftware).

Findet sich lokal kein passender Stand — etwa weil die Datei jünger ist als die
Sicherung —, holen wir sie bei **Anton as a Service** von Hand von einem der
externen Backupserver zurück. Die Meldung von `media:repair` nennt dafür alles
Nötige. Mandanten mit DIMAG sind ausgenommen: Dort liegt der Master im
Langzeitarchiv.

!!! note "Einrichtung durch den Betrieb"
    `media:repair` braucht eine lokale Sicherung, welche die Mediendateien
    enthält, nur für root erreichbar ist und in der Konfiguration steht
    (siehe [Installation](installation.md#selbstreparatur-aus-der-lokalen-sicherung)).
    Wo das nicht eingerichtet ist, meldet der Befehl das und tut nichts.

## Redundante Speicherung

Die redundante Speicherung ist Sache der Infrastruktur: Anton schreibt in einen
lokalen Speicher und optional in einen Cloud-Speicher, die Kopien darunter legt
der Betrieb an. Bei **Anton as a Service** liegen die Daten in
[drei Kopien an drei Standorten](../faq/longterm_archives.md) (gesamthaft
sechsfache Redundanz); **on Premises** verantwortet das die betreibende
Institution.

## Sicherung oder Publikation?

Die wichtigste Unterscheidung, und die am leichtesten zu verwechselnde:

| Artefakt | Zweck |
|---|---|
| **Nativer Export** (`anton:export-native`) | **Sicherung.** Verlustfrei und wieder einlesbar: Metadaten in allen Sprachen, Ereignisse, Textfelder — auch private —, Normdaten-Bezüge über UUID und die **Master-Medien**. |
| **SQL-Dump** | **Sicherung.** Das einzige Artefakt mit Benutzern, Einstellungen, Formularen und der Datei-Provenienz (PRONOM/NARA-Historie). Enthält keine Mediendateien. |
| [**DIP**](download-dip.md) (BagIt) und [**OCFL**](download-ocfl.md) | **Abgabepakete.** Medien und Metadaten gebündelt, mit Prüfsummen im Manifest. |
| [**RDF/CIDOC**](download-rdf.md), **EAD**, **TEI**, **Memobase** | **Publikationsansichten.** Gefiltert und verlustbehaftet — aus ihnen lässt sich Anton nicht wiederherstellen. |
| [**A+ Bundle mit `--include-protected --include-originals`**](download-rdf.md#migrations-export) | **Migrationspaket.** Graph inklusive gesperrter Daten plus Originaldateien — für den Weg in ein *anderes* System. Kein Restore-Werkzeug nach Anton, und wegen der enthaltenen Personendaten nicht öffentlich zu hosten. |

!!! danger "Ein RDF- oder EAD-Export ist kein Backup"
    Diese Formate sind für Recherche und Austausch gebaut. Ihnen fehlen unter
    anderem die UUIDs und die Rohwerte; im Standardfall sind private Inhalte
    herausgefiltert. Für eine Sicherung braucht es den nativen Export **und**
    den SQL-Dump.

    Das gilt auch dann, wenn mit `--include-protected --include-originals`
    exportiert wird: dieses Paket ist als **Migrationsweg hinaus** gedacht. Ein
    Rückweg wäre mit Aufwand konstruierbar, ein Werkzeug dafür gibt es nicht.

Die Provenienz einer Datei (Formaterkennung, NARA-Bewertung, Integritätsprüfungen)
führt Anton in der Datenbank; sie reist deshalb mit dem SQL-Dump. DIP und OCFL
sichern die Dateien über die Prüfsummen im Manifest und geben diese Provenienz
nicht als PREMIS oder METS aus.

Welche Daten jedes Format im Einzelnen mitnimmt, welche nur im SQL-Dump stehen und
wer welches Artefakt auslösen kann, zeigt die [Export-Matrix](export-matrix.md).
Kurz: Der SQL-Dump und die Standard-Exporte gehen über die Oberfläche, der native
Round-Trip und das Migrationspaket nur über die CLI.

Für die [statische Publikation](statische-publikation.md) eines Bestandes als
eigenständige Website gibt es ein eigenes Bundle.

## Mit angebundenem Langzeitarchiv

Bei Installationen mit [DIMAG-Anbindung](inge.md) übergibt Anton jede
Mediendatei beim Upload über die Middleware Inge an DIMAG und führt Buch, ob die
Übergabe verifiziert ist — siehe [Upload-Status](dimag-uploads.md). Danach liegt
die Bitstream-Sicherung des Masters bei DIMAG.

!!! note "Die Fixity liegt dann bei DIMAG"
    Auf diesen Installationen prüft das Langzeitarchiv die Master. `media:check`
    überspringt sie deshalb mit dem Hinweis, dass die Dateien in DIMAG liegen.
    Auf Wunsch löscht Anton nach verifizierter Übergabe die lokale Kopie.
