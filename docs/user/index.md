# Einstieg

Anton ist eine webbasierte Archivdatenbank. Sie richtet sich nach ISAD(G) und
bildet Bestände als Baum ab — vom Archiv über Bestände und Serien bis zum
einzelnen Dokument. Zu jeder [Verzeichnungseinheit](objects.md) lassen sich
Medien, [Akteur:innen](actors.md), [Orte](places.md) und
[Schlagwörter](keywords.md) erfassen.

Diese Dokumentation beschreibt die Arbeit mit Anton aus Sicht der Erschliessung.
Für Installation und Konfiguration siehe den Admin-Bereich.

## Die Oberfläche

Oben steht die Navigation. Ihr Inhalt ist pro Archiv konfigurierbar; in der
Regel finden sich dort:

- der **Einstieg in die Tektonik**. Wie er heisst, legt jedes Archiv selbst
  fest — «Katalog», «Archivplan» oder der Name des Archivs.
- **Admin** — trotz des Namens die Sammelseite für alle angemeldeten Benutzer:innen.
  Die Seite selbst ist mit **Administration** überschrieben und führt in Karten
  zu **Entitäten** (Akteur:innen, Orte, Schlagwörter, Standorte),
  **Benutzer:innen**, **Info**, **Import / Export** und
  **Einstellungen**. Welche Karten erscheinen, hängt von der Rolle ab.
- **Hilfe** — die Hilfe in der Anwendung; sie zeigt die Felder, Wertelisten und
  Erschliessungsregeln **dieses** Archivs
- die **Suche** rechts oben

!!! note "Beschriftungen weichen ab"
    Fast jede Beschriftung ist pro Archiv einstellbar — Menüeinträge ebenso wie
    Feldnamen. Diese Dokumentation verwendet die Bezeichnungen des
    Standardformulars; im eigenen Archiv können sie abweichen. Wo die
    Unterschiede besonders leicht verwirren, sind sie an Ort und Stelle
    vermerkt.

## Rollen

Was jemand sieht und darf, hängt an der Rolle. Anton führt sie unübersetzt, in
der Benutzerverwaltung stehen sie genau so:

| Rolle | Darf |
|---|---|
| (nicht angemeldet) | Den öffentlichen Katalog durchsuchen — sofern das Archiv ihn freigibt |
| `user` | Dasselbe, angemeldet; eigenes Profil, Benachrichtigungen |
| `user_intern` | Zusätzlich gesperrte Inhalte sehen, Standorte, Ausleihen, Originalmedien herunterladen |
| `loan_admin` | Zusätzlich die Ausleihen verwalten |
| `editor` | Erschliessen: Datensätze anlegen, ändern, verschieben, löschen; Import; Medien |
| `admin` | Einstellungen, Formulare, Benutzerkonten, Export, Statistik |
| `blocked` | Nichts — der Zugang ist gesperrt |

Jede Rolle schliesst die darüberliegenden Rechte der vorherigen mit ein.

Wer erschliesst, braucht mindestens `editor`. Die Tasten zum Anlegen,
Verschieben und Löschen erscheinen nur mit dieser Berechtigung — fehlen sie,
liegt es an der Rolle.

!!! note "Superuser"
    Über `admin` hinaus gibt es Superuser für Eingriffe wie Feldtypen,
    Wertelisten und Schutzfristen. Das ist keine Rolle in der
    Benutzerverwaltung, sondern eine gesondert hinterlegte Liste von Konten.

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
