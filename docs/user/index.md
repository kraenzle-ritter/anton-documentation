# Einstieg

Anton ist eine webbasierte Archivdatenbank. Sie richtet sich nach ISAD(G) und
bildet Bestände als Baum ab — vom Archiv über Bestände und Serien bis zum
einzelnen Dokument. Zu jeder [Verzeichnungseinheit](objects.md) lassen sich
Medien, [Akteure](actors.md), [Orte](places.md) und
[Schlagwörter](keywords.md) erfassen.

Diese Dokumentation beschreibt die Arbeit mit Anton aus Sicht der Erschliessung.
Für Installation und Konfiguration siehe den Admin-Bereich.

## Die Oberfläche

Oben steht die Navigation. Ihr Inhalt ist pro Archiv konfigurierbar; in der
Regel finden sich dort:

- der **Katalog** — der Einstieg in die Tektonik
- **Admin** — trotz des Namens die Sammelseite für alle angemeldeten Benutzer,
  mit den Einstiegspunkten zu Akteuren, Orten, Schlagwörtern, Standorten,
  Import, Export, Statistik und den Einstellungen
- **Hilfe** — die Hilfe in der Anwendung; sie zeigt die Felder, Wertelisten und
  Erschliessungsregeln **dieses** Archivs
- die **Suche** rechts oben

!!! note "Beschriftungen weichen ab"
    Jedes Archiv kann die Beschriftungen anpassen. Wo hier «Katalog» steht, kann
    in der eigenen Installation «Archivplan» stehen, statt «Akteure» auch
    «Akteurinnen/Akteure». Gemeint ist jeweils dasselbe.

## Rollen

Was jemand sieht und darf, hängt an der Rolle:

| Rolle | Darf |
|---|---|
| (nicht angemeldet) | Den öffentlichen Katalog durchsuchen — sofern das Archiv ihn freigibt |
| Benutzer:in | Dasselbe, angemeldet; eigenes Profil, Benachrichtigungen |
| Interne:r Benutzer:in | Zusätzlich Standorte, Ausleihen, Originalmedien herunterladen |
| Ausleihverwaltung | Zusätzlich die Ausleihen verwalten |
| Bearbeiter:in | Erschliessen: Datensätze anlegen, ändern, verschieben, löschen; Import; Medien |
| Administration | Einstellungen, Formulare, Benutzerkonten, Export, Statistik |

Wer erschliesst, braucht mindestens die Rolle **Bearbeiter:in**. Die Tasten zum
Anlegen, Verschieben und Löschen erscheinen nur mit dieser Berechtigung — fehlen
sie, liegt es an der Rolle.

## Anmelden

Die Anmeldung erfolgt mit Benutzername und Passwort. Je nach Archiv stehen
zusätzlich [Zwei-Faktor-Authentifizierung](2FA.md) und
[Passkeys](passkey.md) zur Verfügung.

## Wo weiterlesen

Der Einstieg in die tägliche Arbeit ist
[Verzeichnungseinheiten](objects.md); wie der Baum aufgebaut ist und wie sich
Datensätze umhängen lassen, steht unter
[Tektonik und Verschieben](hierarchy.md). Warum die eigene Maske anders aussieht
als die Beispiele hier, erklärt [Formulare und Felder](forms.md).
