# Lotte: Überblick

Lotte ist das Digitale Archiv hinter Anton: ein eigener Dienst, der jede Mediendatei als OCFL-Objekt aufbewahrt und alles übernimmt, was mit den Bytes zu tun hat. Anton behält die Erschliessung und entscheidet, wer was sehen darf. Kurz: der Inhalt in Anton, die Technik in Lotte. Lotte ist eine eigene Laravel-Anwendung mit eigener Datenbank je Mandant, eigener Warteschlange und eigener Kommandozeile; sie läuft weiter, prüft und migriert auch dann, wenn Anton gerade gewartet oder einmal ersetzt wird.

!!! note "Im Aufbau"
    Lotte ist entwickelt, aber noch nicht an Anton angebunden und noch nicht produktiv im Einsatz (anton#857). Bis dahin übernimmt Anton Dateien wie bisher selbst, siehe [Digitales Archiv: Überblick](../admin/preservation.md). Die Schnittstelle kann sich bis zur Anbindung noch ändern; diese Seiten beschreiben den Stand des Dienstes.

Die Seiten dieses Abschnitts:

- [Betrieb](operation.md): Installation, Mandanten, Clients und Schlüssel, Worker, wiederkehrende Aufgaben, Sicherung, Überwachung und Wiederherstellung;
- [Befehlsreferenz](commands.md): alle Befehle `lotte:*`;
- [API-Referenz](api.md): alle Routen, erzeugt aus der OpenAPI-Beschreibung.

## Aufgabenteilung {#aufgabenteilung}

| Lotte | Anton |
|---|---|
| die Dateien: Master, behaltene Fassungen, OCFL-Objekte | Erschliessung, Normdaten, Beziehungen |
| Prüfsummen, Integrität, Virenprüfung | wer was sehen darf: Rechte, Schutzfristen, Sperren |
| Formaterkennung, Formatprüfung, Format Policy, Migration | Suche, Galerie, Benutzeroberfläche |
| Ableitungen, OCR, Text aus Dateien | Benutzer:innen, Rollen, Befugnisse |
| Erhaltungsereignisse (PREMIS), Aufträge | |

Lotte ruft Anton nie auf, weder für eine Prüfung noch für einen Status oder Metadaten. Was Lotte braucht, kommt mit der Anfrage. Anton ist ein Client mit einem Schlüssel und holt Änderungen selbst ab, über das [Änderungsfeed](#aenderungsfeed). Fällt eine Seite für eine Wartung aus, bleibt nichts hängen. Öffentlich zugänglich ist in Lotte nichts: Jede Route mit Inhalt verlangt einen Schlüssel; ob etwas öffentlich gezeigt wird, entscheidet Anton.

## Ein Dienst je Server {#ein-dienst-je-server}

Lotte läuft einmal je Server, mit eigenen Mandanten: einmal auf dem Server, der die Anton-Installationen von Anton as a Service trägt, und einmal auf dem Server einer Institution, die ihre Dateien bei sich behalten will. Einen zentralen Dienst für alle Installationen gibt es nicht; die Dateien eines Archivs verlassen seine Infrastruktur nicht, und ein Ausfall trifft nur die Archive dieses Servers. Jeder Anton-Mandant spricht mit genau einem Lotte-Mandanten auf seinem eigenen Server.

## Eine Datenbank und ein Ordner je Mandant {#mandanten}

Ein Mandant ist ein Kunde des Dienstes, benannt mit seinem Slug in der Mandanten-Datei des Servers. Jeder Mandant hat eine eigene Datenbank und einen eigenen Ordner, und nichts von ihm liegt anderswo:

- die Datenbank `<slug>_archiv`, auf derselben MySQL-Instanz wie die Anton-Datenbank des Mandanten, mit einem eigenen Datenbankbenutzer von Lotte: Antons Benutzer hat darauf keine Rechte und Lottes keine auf Antons Datenbank;
- der Ordner `<basis>/<slug>/` mit vier Bereichen:

| Bereich | Inhalt |
|---|---|
| `ocfl/` | das Archiv: die OCFL Storage Root (OCFL 1.1) |
| `derivatives/` | Nutzungskopien, Vorschaubilder, Posterbilder; jederzeit neu erzeugbar |
| `text/` | Text aus OCR und Textextraktion; jederzeit neu erzeugbar |
| `work/` | Pakete vor dem Abschluss, Arbeitskopien |

So lässt sich ein Mandant allein wiederherstellen, übergeben, auf einen anderen Server verschieben oder löschen, mit seinem Datenbank-Dump und seinem Ordner, ohne einen anderen Mandanten zu berühren. Der Ordner ist das Archiv, die Datenbank ein Index darüber und der laufende Betrieb (Clients, offene Pakete, Aufträge, Änderungsfeed). Den Objektindex und den Stand der Ableitungen baut [`lotte:rebuild-index`](commands.md#lotte-rebuild-index) aus dem Ordner allein wieder auf.

## Ein OCFL-Objekt je Medium {#ocfl-objekt}

Jede Mediendatei wird ein OCFL-Objekt, mit SHA-512 als Prüfsumme. Die ID vergibt Lotte selbst, `urn:uuid:<uuid>` (zeitlich geordnet); die Referenz des Clients (bei Anton Mandant und Medien-Nummer) wird festgehalten und ist je Mandant eindeutig, aber nicht Teil der ID. Ein Objekt je Medium, weil ein Datensatz umnummeriert und verschoben und eine Ablieferung aufgeteilt werden kann, ein Medium aber bleibt, was es ist. Ein Objekt enthält:

| Pfad im Objekt | Inhalt |
|---|---|
| `data/<datei>` | der Master, wie geliefert oder migriert |
| `metadata/description.json` | die Kopie der Metadaten, die der Client mitschickt (bei Anton: Signatur, Titel, Pfad in der Tektonik, Ablieferung, Rechte) |
| `metadata/events.json` | die Erhaltungsereignisse (PREMIS): Prüfungen bei der Übernahme, Fixity, Migration, Zurückziehen |
| `metadata/object.json` | die Referenz des Clients und der Zustand (aktiv oder zurückgezogen) |
| `metadata/characteristics.json` | technische Merkmale von PDF, Text, Audio und Video |

Jede Änderung ist eine neue Version: eine Migration, eine neue Metadaten-Kopie, ein Befund der Fixity-Prüfung, das Zurückziehen. Was vorher galt, bleibt in der früheren Version, bitgenau; eine nach einer Format-Regel behaltene gelieferte Datei ist die erste Version, das Ergebnis die zweite. Geschrieben wird je Objekt nacheinander, in ein neues Versionsverzeichnis, das erst fertig an seinen Platz kommt. Weil alles im Objekt steht, lässt es sich ohne Lottes Datenbank lesen, prüfen und wiederherstellen. Neben der OCFL-Bibliothek, die schreibt, prüft eine zweite Umsetzung (`ocfl-py`) jedes Objekt: in den Tests und auf Wunsch im Bestand ([`lotte:verify --ocfl`](commands.md#lotte-verify)).

## Übernahme in zwei Schritten {#uebernahme}

Eine Übernahme geht in zwei Schritten: Lotte nimmt die Dateien geprüft, aber vorläufig an; erst der Abschluss macht sie zu OCFL-Objekten. Dazwischen legt der Client seine eigenen Datensätze an, und misslingt das, verwirft er das Paket.

1. **Paket beschreiben und hochladen.** Der Client beschreibt ein Paket: je Datei Name, Referenz, auf Wunsch die gelieferte Prüfsumme, die Metadaten-Kopie und die Grösse. Dann lädt er die Dateien hoch, auch in Teilen; ein abgebrochener Upload geht dort weiter, wo er aufhörte.
2. **Prüfen.** Lotte prüft jede Datei als Auftrag in der Warteschlange des Mandanten: Viren (ClamAV), gelieferte Prüfsumme, Format Policy (Preingest und Normalisierung nach den Regeln des Mandanten und dem Weg, auf dem die Dateien kamen), Formaterkennung (Siegfried), Formatprüfung, Übereinstimmung von Endung, Inhalt und PRONOM-ID, technische Merkmale. Das Paket ist danach **vorläufig**, mit einem Ergebnis je Datei: übernommen, oder abgewiesen mit Grund.
3. **Abschliessen oder verwerfen.** Mit `commit` schreibt Lotte je übernommene Datei ein OCFL-Objekt mit den Ereignissen der Prüfungen und einem Übernahme-Ereignis und stellt Ableitungen und Text in die Warteschlange. Mit `discard` verwirft der Client das Paket; nichts bleibt. Ein Paket, das weder abgeschlossen noch verworfen wird, verwirft [`lotte:prune-packages`](commands.md#lotte-prune-packages) nach der Aufbewahrungsfrist (Vorgabe 7 Tage).

Jeder Schritt lässt sich wiederholen, ohne dass etwas doppelt entsteht: Ein Paket mit demselben `Idempotency-Key` wird nicht zweimal angelegt, ein abgeschlossenes Paket antwortet beim zweiten `commit` wie beim ersten. Die Prüfungen sind dieselben wie in Antons eigener Übernahme ([Prüfungen bei jeder Übernahme](../admin/preservation.md#prufungen-bei-jeder-ubernahme)); Lotte hat sie übernommen. Operatoren übernehmen einen Ordner mit [`lotte:ingest`](commands.md#lotte-ingest).

## Ableitungen und Text {#ableitungen}

Ableitungen (Nutzungskopie `web`, Vorschaubild `thumb`, Posterbild `poster` bei Video) und Text kommen nie ins OCFL-Objekt. Lotte erzeugt sie aus dem Master der neuesten Version und legt sie in `derivatives/` und `text/` ab, zum Wegwerfen: Was dort liegt, lässt sich jederzeit neu erzeugen. Welche Ableitungen ein Objekt hat, hängt von seinem MIME-Typ ab; Werkzeuge und Einstellungen sind dieselben wie in Anton. Text kommt aus der Textebene eines PDF, aus Office-Dokumenten und Textdateien, und wo der Mandant OCR eingeschaltet hat, auch aus Bildern und PDF ohne Textebene (ocrmypdf); er bleibt, wie er geschrieben steht, ohne die Aufbereitung für Antons Suche.

Je Objekt und Ableitung führt Lotte einen Stand: fehlt, in der Warteschlange, bereit, fehlgeschlagen, mit Zahl der Versuche. Nach drei Fehlschlägen versucht Lotte es nicht mehr; [`lotte:health`](commands.md#lotte-health) meldet solche Ableitungen als Warnung. Die API liefert eine fertige Ableitung aus; eine, die noch nicht da ist, stellt sie in die Warteschlange und antwortet mit 202. Für einen Browser ohne Schlüssel gibt es kurzlebige signierte Adressen (Vorgabe 15 Minuten).

## Aufträge {#auftraege}

Vier Arten von Aufträgen laufen über Objekte oder über die Objekte eines abgeschlossenen Pakets, in der Warteschlange des Mandanten, in Abschnitten, mit Fortschritt und einem Ergebnis je Objekt:

| Auftrag | Was er tut |
|---|---|
| `derive` | erzeugt fehlende Ableitungen und Text, auf Wunsch nur eine Ableitung oder auch Fehlgeschlagenes |
| `ocr` | erzeugt Text mit OCR, auch wenn der Mandant OCR nicht eingeschaltet hat |
| `verify` | prüft jede Datei gegen das Inventar (Fixity), auf Wunsch zusätzlich das ganze Objekt mit `ocfl-py`. Eine Prüfung legt keine Version an; wann und mit welchem Ergebnis ein Objekt geprüft wurde, steht im Index und im Ergebnis des Auftrags. Nur ein Befund kommt ins Objekt, als fehlgeschlagenes Fixity-Ereignis in einer neuen Version. |
| `migrate` | wendet eine Regel der Format Policy auf eine Arbeitskopie des Masters an und schreibt nur dann eine neue Version, wenn das Ergebnis die Prüfung der Regel, die Formatprüfung und die Formaterkennung besteht; die frühere Datei bleibt in der Version davor. Als Probelauf berichtet der Auftrag nur. |

Ein Auftrag mit demselben `Idempotency-Key` entsteht nicht zweimal, und ein abgeschlossener Auftrag läuft nie noch einmal. Zurückgezogene Objekte überspringt jeder Auftrag mit dem Grund als Ergebnis. Operatoren legen dieselben Aufträge mit [`lotte:ocr`](commands.md#lotte-ocr), [`lotte:verify`](commands.md#lotte-verify) und [`lotte:migrate-format`](commands.md#lotte-migrate-format) an; [`lotte:derive`](commands.md#lotte-derive) erzeugt Ableitungen direkt.

## Änderungsfeed {#aenderungsfeed}

Was mit Objekten, Paketen und Aufträgen geschieht, schreibt Lotte in ein Änderungsfeed je Mandant, in eine fortlaufende Folge. Ein Client holt mit `GET /t/<slug>/changes?since=<folge>` die Einträge nach seinem Stand und merkt sich den letzten selbst; Lotte schickt nichts von sich aus. Einträge gibt es für:

| Art | Wann |
|---|---|
| `object.created` | ein Objekt ist aus einem Paket entstanden |
| `object.version_added` | eine neue Version durch Migration, Normalisierung oder einen Fixity-Befund |
| `object.metadata_updated` | eine neue Metadaten-Kopie |
| `object.withdrawn` | das Objekt ist zurückgezogen |
| `object.purged` | ein Operator hat den Inhalt gelöscht |
| `derivative.ready` / `text.ready` | eine Ableitung bzw. der Text ist bereit |
| `derivative.failed` | jeder Fehlschlag, mit Zahl der Versuche und ob Lotte aufgibt |
| `package.discarded` | ein Paket ist verworfen, vom Client, von einem Operator oder nach der Aufbewahrungsfrist |
| `job.finished` | ein Auftrag ist zu Ende |

Ein Eintrag entsteht in derselben Datenbank-Transaktion wie die Änderung im Index, die er meldet: Beides ist da oder keines. Die OCFL-Version wird vorher geschrieben; scheitert die Transaktion, ist das Objekt seinem Index voraus, bis `lotte:rebuild-index` ihn nachführt. Einträge werden in der Reihenfolge ihrer Folgenummer sichtbar, ein Client überspringt also keinen, und kein Eintrag wird je geändert oder gelöscht. `lotte:rebuild-index` schreibt keine Einträge; wo der Befehl den Index geändert hat, sagt er es, und die Clients gleichen diese Objekte neu ab.

## Zurückziehen und Löschen {#zurueckziehen-und-loeschen}

Ein Client löscht in Lotte nichts, er zieht zurück. Ein **zurückgezogenes** Objekt bekommt eine neue Version, in der `metadata/object.json` den Zustand mit Grund, Zeitpunkt und Client festhält und ein Ereignis das Zurückziehen; seine Ableitungen und sein Text werden entfernt. Danach antworten das Objekt, seine Dateien, Ableitungen, Text und signierten Adressen mit 410 und dem Grund, Aufträge überspringen es. Der Inhalt bleibt im Archiv, und `lotte:rebuild-index` stellt den Zustand aus dem Ordner wieder her.

**Löschen** des Inhalts (Datenschutz, ein Gerichtsentscheid) darf nur ein Operator, auf der Kommandozeile mit [`lotte:purge`](commands.md#lotte-purge): nur ein zurückgezogenes Objekt, mit Grund und Name des Operators, ohne `--confirm` als Probelauf, der sagt, was ginge. Der Befehl entfernt das Verzeichnis des Objekts und seine Zeilen im Index und hält fest, wer es wann und warum gelöscht hat, in der Datenbank und als `object.purged` im Änderungsfeed; ein gelöschtes Objekt hinterlässt so eine Spur, auch wenn sein Inhalt weg ist.

!!! warning "Die Regel für das Löschen ist noch nicht entschieden"
    Wann das Löschen eines zurückgezogenen Objekts erlaubt ist (Fristen, Freigaben, wer entscheidet), ist offen. `lotte:purge` prüft heute nur, dass das Objekt zurückgezogen ist.
