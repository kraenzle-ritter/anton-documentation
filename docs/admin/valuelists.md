# Wertelisten

Wertelisten speisen die Auswahlfelder der Formulare — Objekttyp,
Verzeichnungsstufe, Akteurstyp, Schlagwort-Typ, Zugangsbestimmungen und weitere.
Einsehbar sind sie in der Anwendung unter **Hilfe → Wertelisten**; das ist
zugleich die verlässlichste Auskunft darüber, was im **eigenen** Archiv gilt.

## Aufbau

Jede Werteliste ist eine Taxonomie mit Einträgen. Ein Eintrag hat einen
technischen **Namen**, der fest bleibt, und eine **Beschriftung** je Sprache,
die frei ist. Beim Erschliessen wird die Beschriftung angezeigt, gespeichert
wird der Eintrag.

Daraus folgt das Wichtigste im Umgang mit Wertelisten:

!!! tip "Umbenennen ist harmlos, Löschen nicht"
    Die Beschriftung eines Eintrags lässt sich jederzeit ändern — bestehende
    Datensätze zeigen danach einfach den neuen Text. Wird ein Eintrag dagegen
    entfernt, verlieren die Datensätze, die ihn verwenden, ihren Wert.

## Erweiterbar oder fest

Nicht jede Werteliste darf ergänzt werden. Der Unterschied ist gewollt:

| Werteliste | Ergänzbar? |
|---|---|
| Schlagwort-Typ, Ortstyp, Objekttyp | ja — jedes Archiv nach eigenem Bedarf |
| Verzeichnungsstufe | nein — sie folgt ISAD(G), und Anton rechnet mit ihr |
| Akteurstyp | nein — Person, Familie, Körperschaft, Abteilung, Gruppe, Software sind im Code verankert |

Bei den festen Listen sind die **Beschriftungen** trotzdem frei übersetzbar. Ein
Archiv kann «Körperschaft» also «Organisation» nennen — nur die Liste selbst
nicht erweitern.

## Pflege

Wertelisten werden unter **Admin → Wertelisten** bearbeitet. Die Verzeichnungs­stufen
und andere systemnahe Listen sind Superusern vorbehalten; bei Anton as a Service
ist dafür k & r zuständig.

Welche Werteliste ein Auswahlfeld speist, legt das
[Formular](forms.md) fest — dieselbe Felddefinition kann in verschiedenen
Formularen auf verschiedene Listen zeigen.

## Schutzfristen

Die Zugangsbestimmungen sind eine Werteliste mit einer Besonderheit: An ihren
Einträgen hängen Fristen in Jahren. Sie werden deshalb getrennt gepflegt — siehe
[Schutzfristen](protection-periods.md).
