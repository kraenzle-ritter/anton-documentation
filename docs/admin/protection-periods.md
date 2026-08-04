# Schutzfristen

Die Schutzfristen bestimmen, wann die Medien einer Verzeichnungseinheit
öffentlich werden. Wie sie beim Erschliessen wirken, beschreibt
[Zugang und Schutzfristen](../user/access.md) — diese Seite behandelt die
Einrichtung.

## Wie Anton rechnet

Anton ermittelt für jeden Datensatz **ein** Freigabejahr und hält es
gespeichert. Katalog, Galerie und Suche lesen alle denselben Wert — es gibt
keine zweite Rechnung an anderer Stelle. Massgeblich ist:

1. Das Feld **Schutzfrist bis** am Datensatz. Es hat Vorrang und **vererbt sich
   nach unten** an den ganzen Teilbaum.
2. Sonst die Frist des im Feld **Zugangsbestimmungen / Sperrfrist** gewählten
   Typs, gerechnet ab dem Entstehungsdatum. Typ-Fristen gelten **nur für den
   Datensatz selbst** und vererben sich nicht.

!!! note "Vereinheitlicht seit v0.78"
    Vor Version 0.78 rechneten mehrere Stellen die Frist unabhängig voneinander
    aus, was zu Abweichungen zwischen Katalog, Galerie und Suche führen konnte.
    Seither gibt es genau eine Quelle. Nach dem Aktualisieren wird das
    Freigabejahr für den Bestand einmalig neu berechnet.

## Datensätze ohne Entstehungsdatum

Eine Typ-Frist wird ab dem **Ende** des Entstehungszeitraums gerechnet, also ab
dem Feld **Entstehung bis**. Fehlt dieses, lässt sich das Freigabejahr nicht
ermitteln — der Datensatz bleibt dann **gesperrt**, bis eine der beiden Angaben
nachgetragen wird:

* das **Entstehungsdatum bis**, oder
* ein **Schutzfrist bis** direkt am Datensatz.

!!! important "Beide Datumsfelder ausfüllen"
    Anton erwartet, dass **Entstehung von** und **Entstehung bis** gesetzt sind.
    Bei einem einzelnen Datum stehen in beiden Feldern derselbe Wert. Ein
    ausgefülltes «von» allein genügt nicht: Für die Frist zählt das Ende des
    Zeitraums, und Anton rät es nicht aus dem Anfang — eine 80-Jahre-Frist ab
    1933 endet anders als ab 1965, und welcher der beiden Werte gemeint ist,
    weiss nur das Archiv.

!!! warning "Geändert: früher wurden solche Datensätze angezeigt"
    Bis dahin rechnete Anton bei fehlendem Datum ab dem Jahr 0. Eine Frist von
    80 Jahren lief damit im Jahr 81 ab, also längst — der Datensatz galt als
    frei und war öffentlich sichtbar, obwohl eine Frist gesetzt war. Beim
    Aktualisieren verschwinden diese Datensätze aus der öffentlichen Ansicht.

    Betroffen sind nur Datensätze, bei denen jemand tatsächlich eine Frist
    gewählt hat. Ohne gewählte Sperrfrist bleibt ein Datensatz frei, auch ohne
    Entstehungsdatum.

    Welche Datensätze im eigenen Bestand betroffen sind, lässt sich auf
    Anfrage auswerten — bei Anton as a Service über k & r. Sinnvollerweise
    trägt man die fehlenden Entstehungsdaten nach, statt die Einträge
    gesperrt zu lassen.

## Die Typen pflegen

Jeder Eintrag der Werteliste trägt:

| Angabe | Bedeutung |
|---|---|
| **Dauer in Jahren** | Frist ab Entstehungsdatum |
| **öffentlich** | keine Frist — sofort frei |
| **nie freigeben** | dauerhaft gesperrt |

Im Standard sind drei Typen hinterlegt: **öffentlich** (0 Jahre), **Standard
Schutzfrist** (30 Jahre) und **verlängerte Schutzfrist** (70 Jahre). Typen
lassen sich umbenennen, ergänzen und in der Dauer ändern.

!!! important "Superusern vorbehalten"
    Der Editor liegt unter `/admin/protection-periods` und ist Superusern
    vorbehalten — mit der Rolle `admin` ist er nicht erreichbar. Bei Anton as a
    Service ist dafür k & r zuständig.

Für Archive ohne dauerhafte Sperren ist «nie freigeben» optional; es muss nicht
konfiguriert sein.

## Was das angezeigte Jahr bedeutet

Angezeigt wird das erste Jahr, in dem die Einheit **frei** ist. Bei Entstehung
1990 und 30 Jahren Frist also 2021, nicht 2020.

## Beim Ändern einer Frist

Eine geänderte Dauer wirkt auf **alle** Datensätze dieses Typs — auch auf
bestehende. Das Freigabejahr wird neu ermittelt, Medien können damit
schlagartig öffentlich werden oder verschwinden. Eine Änderung an den Fristen
ist deshalb keine Kleinigkeit und gehört geprüft, bevor sie auf einem
produktiven Archiv landet.
