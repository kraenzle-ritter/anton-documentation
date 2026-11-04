# Ansprechpersonen

Unter **Administration › Zuständigkeit und Vertrag › Ansprechpersonen** hält das Archiv fest, wer wofür zuständig ist. Was Kosten verursacht oder die Erhaltung der Dateien betrifft, gilt erst, wenn eine dieser Personen es per Mail bestätigt hat.

## Funktionen

| Funktion | Bestätigt mit der Befugnis | Erhält |
|---|---|---|
| Gesamtverantwortung | Vertrag und Ansprechpersonen | Bestellbestätigungen, Mitteilungen zum Vertrag |
| Digitale Archivierung | Digitale Archivierung ändern | Monatsbericht zu den Formaten, Befunde der Integritätsprüfung |
| Rechnung | – | Nutzungsauszug |
| Technik | – | Wartungs- und Update-Hinweise |

Pro Funktion lassen sich mehrere Personen eintragen, als **Konto** dieser Installation oder als **Adresse ohne Konto** (mit Name). Bestätigen können nur Konten, die die Befugnis der Funktion haben; die Seite zeigt bei jeder Person, ob sie bestätigen kann. Adressen ohne Konto erhalten die Mitteilungen.

Alle Admins sehen die Seite. Personen eintragen und entfernen können Konten mit der Befugnis **Vertrag und Ansprechpersonen** (siehe [Benutzerverwaltung](users.md#befugnisse)). Jede Änderung steht im Sicherheitsprotokoll und geht per Mail an alle Personen der Funktion, an die eingetragene oder entfernte Person und an Kränzle & Ritter.

## Rechnungsadresse

Auf derselben Seite steht, wohin die Rechnungen gehen: Institution, Abteilung, zu Handen, Strasse, PLZ, Ort, Land, Mailadresse für Rechnungen, Bestell- oder Referenznummer, Kostenstelle, UID/MWST-Nummer, Versand (per Mail als PDF, per Post oder eBill) und eine Bemerkung. Bei Versand per Mail ist die Mailadresse Pflicht.

Die Adresse pflegen Konten mit der Befugnis **Vertrag und Ansprechpersonen**. Jede Änderung steht im Sicherheitsprotokoll und geht mit altem und neuem Wert per Mail an die Ansprechpersonen für Rechnung und Gesamtverantwortung und an Kränzle & Ritter. Die Buchhaltung von Kränzle & Ritter übernimmt die Adresse von hier (`GET /api/billing-address`, mit dem Token eines Admin-Kontos).

## Bestätigung per Mail

1. Anton schickt die Anfrage an jede Person der Funktion, die bestätigen kann, mit einem eigenen Link. Die Mail nennt den Wortlaut, um den es geht.
2. Der Link führt zur Seite in Anton; er gilt 14 Tage. **Das Öffnen bestätigt noch nichts**: Mailprogramme rufen Links zur Prüfung selbst auf.
3. Bestätigt oder abgelehnt wird mit der Schaltfläche auf der Seite, angemeldet mit dem Konto, auf das der Link ausgestellt ist. Eine Antwort genügt; danach ist die Anfrage geschlossen.
4. Die Antwort geht per Mail an alle Personen der Funktion und an Kränzle & Ritter.

Unten auf der Seite «Ansprechpersonen» stehen die Anfragen mit Stand (offen, bestätigt, abgelehnt, abgelaufen) und wer wann geantwortet hat. Festgehalten wird der Wortlaut so, wie er gezeigt wurde.

Ein Superuser von Kränzle & Ritter kann nicht für das Archiv bestätigen, solange er nicht als Ansprechperson eingetragen ist.

Angefragt werden seit v0.118.0 der [Erhaltungsauftrag](preservation-mandate.md) und die Freigabe einzelner Migrationen. Buchungen folgen.
