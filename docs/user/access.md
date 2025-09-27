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
Unterliegt ein Objekt noch einer Sperrfrist, kann zwar der Datensatz aufgerufen werden, nicht aber die Bilder und Dokumente.

Mit dem Feld «Schutzfrist bis» kann die Sperrfrist manuell eingegeben werden. Dieser Wert hat Priorität und vererbt sich im Archivbaum an alle Verzeichnungseinheiten unterhalb, sofern es dort nicht bereits schärfere Fristen gibt. 

Wird das Feld «Schutzfrist bis» nicht verwendet, greifen die Sperrfristen: Diese sind in den Voreinstellungen (`period_of_protection_values`) ersichtlich und können durch k & r angepasst werden. Es gibt drei Stufen: öffentlich, standard und verlängerte Sperrfrist. Es ist möglich weitere Werte zu verwenden und zu hinterlegen.

Die Schutzfristen sollten wie folgt funktionieren:

1. Freigabejahr: Dieses Feld hat Priorität und wird nach unten vererbt.  
2. Wenn eine Schutzfrist im Freigabejahr steht (original oder vererbt) wird diese verwendet.  
3. Wenn kein Freigabejahr angegeben ist gelten die Schutzfristen wie gehabt. Diese werden nicht vererbt!  

Für die Anzeige wird alles miteinander verrechnet. 

## Nur Medien unbefristet sperren
Im Editformular können hochgeladene Medien unbefristet gesperrt werden.

## Objekte unbefristet sperren
Wenn das Feld auf 1 gesetzt wurde, sind der Datensatz, sämtliche Kinder und die dazugehörigen Medien nur für UserIntern, Editoren und Admins zugänglich.

Einzelnen Usern (`user`) kann der Zugang zu bestimmten Bereichen der Datenbank ermöglicht werden, indem bei ihnen IDs freigegeben werden. Dies geschieht über die Benutzerinnen/Benutzerverwaltung. Dabei sind die IDs der Datensätze als kommaseparierte Liste einzugeben. Eine ID steht dabei immer für den gesamten Zweig des Erschliessungsbaums.

## Feld Status der Beschreibung
Das Feld ist für Bestände gedacht. Wenn der Bestand auf "Entwurf" gesetzt wird, ist der Bestand nur für UserIntern, Editoren und Admins zugänglich.
