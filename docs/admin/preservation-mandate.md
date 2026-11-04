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
- Für die Übernahme legt das Archiv fest, ob die gelieferte Datei neben einer Umwandlung erhalten bleibt (Vorgabe: nein, die Umwandlung ersetzt sie, wo die Regel es vorsieht) und ob beschädigte oder unlesbare Dateien übernommen und gemeldet oder zurückgewiesen werden (Vorgabe: übernehmen und melden).

Der Grundsatz dabei: Anton bewahrt jede Datei so, wie sie übernommen wurde. Gefährdete Formate migriert Kränzle & Ritter in Archivformate, etwa Druckvorlagen nach PDF/A, und zwar erst, wenn das Risiko es verlangt; Migrationen auf Vorrat kosten Speicher und Rechenzeit, ohne die Dateien sicherer zu machen. Die übernommene Datei bleibt dabei als behaltene Fassung erhalten, und die Migration lässt sich rückgängig machen. Jede Migration prüft Kränzle & Ritter Seite für Seite und Bild für Bild, mit festgehaltenen Prüfsummen vorher und nachher. Eine bewusste Ausnahme, die das Archiv zulassen kann, ist das verlustfreie Umpacken von TIFF-Dateien (Deflate mit Predictor): Anton vergleicht die Bildpunkte jeder Seite vorher und nachher, und weil der Bildinhalt nachweislich gleich bleibt, behält es die gelieferte Datei nicht. Das spart Speicher und damit Kosten.

Weil das Paket kostet, bestätigt die **Gesamtverantwortung** diese Festlegung. Ihre Bestätigung gilt zugleich als Bestellung des Pakets auf der Seite [Vertrag](contract.md), der Widerruf als Kündigung.

**Eigene Erhaltungsstrategie.** Das Archiv trägt die digitale Archivierung selbst und beschreibt seine Strategie: kurz, mit Link auf das Dokument, oder als [Strategiedokument](#strategiedokument) im JSON-Format. Kränzle & Ritter sieht keine Protokolle durch, wertet keine Formatrisiken aus und migriert nur im Auftrag des Archivs. Beim Ausarbeiten und Hinterlegen der Strategie hilft Kränzle & Ritter auf Wunsch. Diese Festlegung bestätigt eine Ansprechperson für **digitale Archivierung**.

## Strategiedokument

Jede Festlegung hat ein maschinenlesbares Strategiedokument nach dem Schema 1 von [kraenzle-ritter/preservation-strategy](https://github.com/kraenzle-ritter/preservation-strategy). Anton bewahrt es Byte für Byte auf, wie es bestätigt wurde, zusammen mit seiner SHA-256-Prüfsumme.

- **Technische Betreuung:** Anton schreibt das Dokument selbst, aus der Vorlage von Kränzle & Ritter, den Angaben des Archivs auf der Seite, den gebuchten Paketen und den Formatregeln, wie sie für das Archiv gelten. Eine Regel, die bei der Übernahme wirkt, steht darin als Regel der Übernahme, so wie ihr Schalter steht; eine Regel, die `media:migrate` anwenden darf, als Regel der Erhaltung.
- **Eigene Erhaltungsstrategie:** Das Archiv kann sein Dokument als JSON-Datei hochladen (höchstens 1 MB). Dann ist die Kurzbeschreibung wahlfrei. Anton prüft die Datei gegen das Schema und weist sie mit den gefundenen Fehlern zurück, wenn sie ungültig ist, für die andere Festlegung geschrieben ist (`variant` muss `own` sein) oder Bestände ausnimmt, die es in diesem Anton nicht gibt. Bestände nennt das Dokument mit ihrer dauerhaften Adresse `https://<archiv>/id/<uuid>`. Ausschlüsse, verlustbehaftete Massnahmen und die Fassung übernimmt Anton aus der Datei.

Die Bestätigungsmail fasst das Dokument zusammen und nennt Fassung und Prüfsumme. Alle Admins können das Dokument der geltenden und jeder früheren Festlegung herunterladen (JSON, mit der Prüfsumme im Kopf `X-Content-SHA256`). Jede Migration, die auf dem Erhaltungsauftrag beruht, nennt im [PREMIS-Rechte-Eintrag](export-matrix.md) Fassung und Prüfsumme des Dokuments, das zu diesem Zeitpunkt galt.

Bei der technischen Betreuung braucht es eine neue Bestätigung nur, wenn das Archiv etwas an seinen Angaben ändert: Festlegung, verlustbehaftete Massnahmen, Ausschlüsse oder Übernahme. Ändert Kränzle & Ritter eine Formatregel oder schaltet eine um, schreibt Anton eine neue Fassung des Dokuments unter derselben Bestätigung; die Liste der Festlegungen zeigt sie als eigene Zeile. Das Sicherheitsprotokoll hält jede neue Fassung fest. Bleibt alles gleich, entsteht keine neue Fassung.

Festlegungen aus Anton 0.118.0 haben noch kein Dokument. Sie gelten weiter und erhalten eines mit der nächsten Bestätigung.

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
