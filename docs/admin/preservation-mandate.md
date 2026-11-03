# Erhaltungsauftrag

Unter **Administration › Digitale Archivierung › Erhaltungsauftrag** legt das Archiv fest, wer seine Dateien betreut. Speicher, Sicherung, Prüfungen und Berichte gehören in beiden Fällen zum Grundangebot; der Auftrag regelt, wer aus den Berichten heraus handelt.

## Zwei Festlegungen

**Technische Betreuung durch Kränzle & Ritter** (Paket «Technische Betreuung»). Kränzle & Ritter

- sieht die Protokolle jeden Monat durch, klärt Auffälliges mit dem Archiv und bestätigt die [Durchsicht](protokolle.md) im Namen des Archivs;
- wertet die Formatrisiken aus und pflegt Formatliste und Formatregeln;
- führt Migrationen nach eigener Risikobewertung durch, ohne im Einzelfall nachzufragen. Die Empfehlungen des Digital Preservation Framework der NARA zieht Kränzle & Ritter bei; bindend sind sie nicht.

Dabei gilt:

- Bei jeder Migration bleibt die übernommene Datei als [behaltenes Original](preservation.md#behaltene-originale); die Migration lässt sich rückgängig machen.
- Massnahmen, die die übernommene Datei verwerfen (etwa `tiff_zip`), gehören nur dazu, wenn das Archiv das ankreuzt.
- Formate (PRONOM-IDs) und Bestände (mit allem darunter) lassen sich ausnehmen.
- Nachgefragt wird nur, wenn eine Massnahme mehr Speicher braucht als gebucht; dann bei der Gesamtverantwortung.

Weil das Paket kostet, bestätigt die **Gesamtverantwortung** diese Festlegung. Ihre Bestätigung gilt zugleich als Bestellung des Pakets auf der Seite [Vertrag](contract.md), der Widerruf als Kündigung.

**Eigene Erhaltungsstrategie.** Das Archiv trägt die digitale Archivierung selbst und beschreibt seine Strategie (kurz, mit Link auf das Dokument). Kränzle & Ritter sieht keine Protokolle durch, wertet keine Formatrisiken aus und migriert nur im Auftrag des Archivs. Diese Festlegung bestätigt eine Ansprechperson für **digitale Archivierung**.

## Erteilen, bestätigen, widerrufen

- Festlegen können Konten mit der Befugnis **Digitale Archivierung ändern**; ansehen können die Seite alle Admins.
- Die Festlegung geht als [Bestätigung per Mail](contacts.md#bestatigung-per-mail) an die zuständigen Ansprechpersonen und gilt, sobald eine von ihnen bestätigt. Die bisherige Festlegung ist damit abgelöst. Ohne eingetragene Ansprechperson, die bestätigen kann, lässt sich nichts anfragen.
- Widerrufen gilt sofort. Danach migriert Kränzle & Ritter keine Datei ohne Auftrag des Archivs; die Ansprechpersonen und Kränzle & Ritter erhalten eine Mail.
- Festgehalten wird der Wortlaut, wie er bestätigt wurde, mit seiner Fassung. Die Liste unten auf der Seite zeigt alle bisherigen Festlegungen.

## Einzelne Migrationen

Ohne Festlegung, bei eigener Strategie oder ausserhalb dessen, was die Betreuung deckt, braucht jede Migration einen Auftrag des Archivs: eine Bestätigung per Mail (`media:migrate --request-approval`, siehe [Konsolenbefehle](console-commands.md#mediamigrate)) oder eine Vereinbarung ausserhalb von Anton. Die Anfrage nennt die Regel, die Zahl der Dateien, ihre Grösse und den geschätzten zusätzlichen Speicher; die Bestätigung gilt für genau diese Dateien.

Der [Monatsbericht](protokolle.md) nennt jede durchgeführte Migration mit der Zahl der Dateien, dem zusätzlichen Speicher und der Grundlage: Erhaltungsauftrag, Bestätigung per Mail oder Vereinbarung.

!!! note "DIMAG"
    Archive, die ihre Master in DIMAG ablegen, haben hier keinen Erhaltungsauftrag; die Erhaltung liegt in DIMAG.
