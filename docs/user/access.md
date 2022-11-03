## Benutzergruppen

Es gibt verschieden Benutzergruppen mit unterschiedlichen Berechtigungen:

- nicht eingeschriebene User (`guest`)
- eingeschriebene User (`user`)
- eingeschriebene UserIntern (`userIntern`)
- Ausleihe-Verwalter:in (`loan_admin`)
- Bearbeiter:in (`editor`)
- Administrator:in (`admin`)

Admins können Benutzer:innen verwalten und ihre Rolle ändern.

## Settings

In den Voreinstellungen kann angegeben werden, ob das gesamte Archiv öffentlich oder nicht öffentlich zugänglich sein soll (public_access). Ist diese Einstellung auf 0 gesetzt, so ist die Datenbank nur für eingeschriebene User, Editoren und Admins zugänglich.

Ist diese Einstellung auf 1 gesetzt handelt es sich um eine grundsätzlich öffentlich zugängliche Anton-Datenbank.

## Feld Zugangsbestimmungen / Sperrfrist
Ist ein Objekt noch gesperrt, kann zwar der Datensatz aufgerufen werden, nicht aber die Bilder und Dokumente. Die Sperrfristen sind in den Voreinstellungen (`period_of_protection_values`) ersichtlich und können durch k & r angepasst werden. Es gibt drei Stufen: öffentlich, standard und verlängerte Sperrfrist.

## Nur Medien sperren
Im Editformular können hochgeladene Medien gesperrt werden.

## Feld Gesperrt
Wenn das Feld auf 1 gesetzt wurde, sind der Datensatz, sämtliche Kinder und die dazugehörigen Assets nur für UserIntern, Editoren und Admins zugänglich.

Einzelnen Usern (`user`) kann der Zugang zu bestimmten Bereichen der Datenbank ermöglicht werden, indem bei ihnen Ids freigegeben werden. Dies geschieht über die Benutzerinnen/Benutzerverwaltung. Dabei sind die IDs der Datensätze als kommaseparierte Liste einzugeben. Eine ID steht dabei immer für den gesamten Zweig des Erschliessungsbaums.

## Feld Status der Beschreibung
Das Feld ist für Bestände gedacht. Wenn der Bestand auf "Entwurf" gesetzt wird, ist der Bestand nur für UserIntern, Editoren und Admins zugänglich.
