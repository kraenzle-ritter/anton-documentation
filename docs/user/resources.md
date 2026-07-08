# Externe Ressourcen (Metagrid, GND, Wikidata …)

Akteur:innen, Orte und Schlagwörter können mit Einträgen in externen
Normdatenbanken und Nachschlagewerken verknüpft werden – etwa mit der
[Gemeinsamen Normdatei (GND)](https://gnd.network/), mit
[Wikidata](https://www.wikidata.org/) oder mit
[Metagrid](https://metagrid.ch/). Metagrid nimmt dabei eine Sonderrolle ein:
Es ist kein einzelnes Nachschlagewerk, sondern ein **Verknüpfungsdienst**, der
Einträge zur selben Person über viele Schweizer Forschungs- und
Gedächtnisinstitutionen hinweg zusammenführt (z. B. Historisches Lexikon der
Schweiz, Dodis, Sozialarchiv, Wirtschaftsarchiv).

## Wie Verknüpfungen entstehen

Beim Bearbeiten einer Akteurin, eines Ortes oder eines Schlagworts kann in den
Providern nach passenden Einträgen gesucht und der richtige Treffer als
Ressource gespeichert werden. Anton legt daraufhin einen Link in einer eigenen
`resources`-Tabelle ab – die Verknüpfung gehört danach zum Datensatz.

!!! note "Lokale Kopie"
    Anton hält die externen Links als **lokale Kopie** und zeigt sie von dort
    an. Beim Aufruf einer Akteurin wird nicht bei jedem Seitenaufruf live bei
    Metagrid, GND oder Wikidata angefragt. Das macht die Anzeige schnell und
    unabhängig von der Verfügbarkeit der externen Dienste – bedeutet aber, dass
    neu hinzugekommene externe Links erst nach einem **Abgleich** erscheinen.

## Abgleich (Synchronisation)

Der Abgleich erfolgt über das Kommando `resources:sync`. Es geht alle
Entitäten durch, die bereits eine Ressource eines Providers besitzen, fragt den
jeweiligen Provider erneut ab und ergänzt neu verfügbare Links. Zusätzlich
bereinigt der Lauf doppelte Einträge und vereinheitlicht Provider-Bezeichnungen.

```bash
php artisan resources:sync --env={slug}
```

!!! info "Automatischer Abgleich"
    In den produktiven Installationen läuft dieser Abgleich **automatisiert und
    wiederkehrend** als geplanter Job. Die Frequenz ist pro Installation
    konfigurierbar und wird bei Bedarf angepasst; ein manueller Eingriff pro
    neuem Link ist nicht nötig. Neue Verknüpfungen tauchen also von selbst auf –
    spätestens beim nächsten geplanten Lauf.

## Zwei Richtungen

Für das Zusammenspiel mit einem Verknüpfungsdienst wie Metagrid lohnt es sich,
zwei Richtungen auseinanderzuhalten. Sie sind voneinander unabhängig.

### Anton als Quelle: neue Akteur:innen bekannt machen

Wird in Anton eine neue Akteurin erfasst, so ist es Sache des Verknüpfungsdienstes
und der beteiligten Partner, diesen Eintrag aufzunehmen und – wo passend – auf
Anton zurückzuverlinken. Ob und wie oft ein Partner (z. B. das Historische
Lexikon der Schweiz) seine Verlinkungen aktualisiert, bestimmt der Partner bzw.
der Verknüpfungsdienst, nicht Anton.

Antons Beitrag zu dieser Richtung ist zweierlei:

- die **Verknüpfung** der Akteurin mit dem Eintrag im Verknüpfungsdienst und
- die Bereitstellung der Personendaten über die
  [Anton-API](../api/index.md), so dass Partner sie periodisch abgreifen können
  (seitenweise, gefiltert nach Entitätstyp).

!!! warning "Voraussetzung: Partnerschaft bei Metagrid"
    Diese Richtung – die eigenen Akteur:innen für den Verknüpfungsdienst
    sichtbar zu machen – funktioniert **nur**, wenn sich die Institution zuvor
    als **Partner bei Metagrid angemeldet** hat. Ohne diese Partnerschaft
    werden die in Anton erfassten Personen von Metagrid nicht aufgenommen und
    entstehen dort auch keine Rücklinks. Die Anmeldung erfolgt direkt bei
    [Metagrid](https://metagrid.ch/) und ist unabhängig vom technischen
    Abgleich in Anton.

!!! tip "Praxis"
    Ein Eintrag, der publiziert wurde, *bevor* es die zugehörige Akteurin in
    Anton gab, enthält zunächst keinen Rücklink auf Anton – der Zieldatensatz
    existierte damals ja noch nicht. Ob solche Altbestände nachträglich
    aktualisiert werden, hängt am Aktualisierungsrhythmus des jeweiligen
    Partners. Fragen zur Abgleichsfrequenz oder zu Rücklinks richten sich daher
    an den Verknüpfungsdienst bzw. den Partner.

### Anton als Konsument: neue Links übernehmen

Kommen beim Verknüpfungsdienst neue Partnerinstitutionen hinzu, entstehen
zusätzliche Verlinkungsmöglichkeiten für bestehende Akteur:innen. Diese neuen
Links erscheinen in Anton **nach dem nächsten Abgleich** – also durch den oben
beschriebenen, geplanten `resources:sync`-Lauf. Es ist kein manuelles Vorgehen
pro Link erforderlich; der wiederkehrende Abgleich zieht die neu verfügbaren
Verknüpfungen automatisch nach.

## Zusammengefasst

- Externe Links werden lokal gespeichert und von dort angezeigt.
- Ein geplanter, wiederkehrender Abgleich hält den lokalen Bestand aktuell und
  übernimmt neu verfügbare Links selbständig.
- Wie schnell **andere** Institutionen eine neue Anton-Akteurin aufnehmen,
  bestimmen diese Institutionen bzw. der Verknüpfungsdienst – nicht Anton.
- Damit die eigenen Akteur:innen überhaupt bei Metagrid erscheinen, muss die
  Institution als **Partner bei Metagrid angemeldet** sein.
