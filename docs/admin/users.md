# Benutzerverwaltung

Benutzerkonten werden über die Admin-Seite unter **Benutzer:innen**
verwaltet. Anlegen, Ändern und Löschen setzt die Rolle `admin` voraus.

## Ein Konto anlegen

Ein neues Konto braucht einen Benutzernamen und eine **E-Mail-Adresse**. Ein
Passwort setzen Sie nicht: Die Person erhält eine E-Mail mit einem Link und
wählt ihr Passwort selbst. So kennt es nur sie. Der Link gilt **72 Stunden**
und nur einmal.

Ist er abgelaufen oder kam die Mail nicht an, schicken Sie die Einladung auf
der Seite des Kontos mit **Einladung senden** erneut.

## Rollen

Anton führt die Rollen **unübersetzt** — in der Auswahlliste stehen sie genau
so:

| Rolle | Darf |
|---|---|
| `blocked` | Nichts; der Zugang ist gesperrt |
| `user` | Den Katalog sehen wie die Öffentlichkeit, dazu Profil und Benachrichtigungen |
| `user_intern` | Zusätzlich gesperrte Inhalte, Standorte (nur ansehen), Ausleihen, Originalmedien |
| `loan_admin` | Zusätzlich Ausleihen verwalten |
| `editor` | Erschliessen: anlegen, ändern, verschieben, löschen (inkl. Standorte); Import; Medien |
| `admin` | Einstellungen, Formulare, Benutzerkonten, Export, Statistik |

Jede Rolle schliesst die Rechte der darunterliegenden ein.

!!! tip "Konto sperren statt löschen"
    `blocked` ist der richtige Weg für Konten, die nicht mehr genutzt werden.
    Beim Löschen gehen die Bezüge verloren — in der Verzeichnungskontrolle steht
    dann ein Name ohne Konto.

## Superuser

Über `admin` hinaus gibt es Superuser für systemnahe Eingriffe: Feldtypen,
Wertelisten, [Schutzfristen](protection-periods.md), Deskriptoren, Logs und das
Zusammenführen von Orten.

**Superuser ist keine Rolle** und lässt sich in der Benutzerverwaltung nicht
vergeben. Massgeblich ist eine gesondert hinterlegte Liste von Benutzernamen;
sie enthält fest die Konten von k & r und lässt sich per Einstellung erweitern.

## Einzelne Bereiche freigeben

Einem Konto mit der Rolle `user` lässt sich der Zugang zu bestimmten Zweigen
öffnen — für Forschende, die an einem gesperrten Bestand arbeiten dürfen, ohne
alles zu sehen.

Dazu werden im Feld **Freigegebene IDs** die IDs der Verzeichnungseinheiten als
kommagetrennte Liste eingetragen. Eine ID steht immer für den **ganzen Zweig**
darunter — die Einheit selbst und alle untergeordneten.

In diesem Zweig sieht das Konto alles, was auch `user_intern` sieht: gesperrte
Verzeichnungen und Entwürfe, Medien unter Schutzfrist und gesperrte Medien, und
die interne Detailansicht. Ausserhalb des Zweigs sieht es, was Gäste sehen.

## API-Token

Für den Zugriff über die [API](../api/authentication.md) lässt sich pro Konto ein
Token erzeugen. Es erhält die Rechte des Kontos; ein Token für einen
Lesezugriff gehört deshalb an ein Konto mit entsprechend knapper Rolle, nicht an
ein Administrationskonto.

## Anmeldeverfahren

Neben Benutzername und Passwort stehen je nach Installation
[Zwei-Faktor-Authentifizierung](../user/2FA.md) und
[Passkeys](../user/passkey.md) zur Verfügung — siehe [Anmeldung](authentication.md).
