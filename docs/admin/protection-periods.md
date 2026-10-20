# Schutzfristen

Die Schutzfristen bestimmen, wann die Unterlagen und Medien einer
Verzeichnungseinheit öffentlich werden; die Beschreibung bleibt sichtbar. Den
ganzen Datensatz verbirgt nur das Feld **Datensatz gesperrt**. Wie beides beim
Erschliessen wirkt, beschreibt [Zugang, Sperre und Schutzfrist](../user/access.md)
— diese Seite behandelt die Einrichtung.

## Wie Anton rechnet

Anton ermittelt für jeden Datensatz **ein** Jahr «Frei ab» und hält es
gespeichert. Katalog, Galerie und Suche lesen alle denselben Wert — es gibt
keine zweite Rechnung an anderer Stelle. Massgeblich ist:

1. Das Feld **Frei ab** am Datensatz. Es hat Vorrang und **wirkt nach unten**
   auf den ganzen Teilbaum.
2. Sonst die Frist des im Feld **Schutzfrist** gewählten
   Typs, gerechnet ab dem Entstehungsdatum. Typ-Fristen gelten **nur für den
   Datensatz selbst** und vererben sich nicht.

!!! note "Eine Quelle für die Frist"
    Katalog, Galerie und Suche rechnen die Frist an genau einer Stelle — sie
    können also nicht auseinanderlaufen.

## Datensätze ohne Entstehungsdatum

Eine Typ-Frist wird ab dem **Ende** des Entstehungszeitraums gerechnet, also ab
dem Feld **Entstehung bis**. Fehlt dieses, lässt sich das Jahr «Frei ab» nicht
ermitteln — die Unterlagen bleiben dann **geschützt**, bis eine der beiden
Angaben nachgetragen wird (die Beschreibung bleibt sichtbar):

* das **Entstehungsdatum bis**, oder
* ein **Frei ab** direkt am Datensatz.

!!! important "Beide Datumsfelder ausfüllen"
    Anton erwartet, dass **Entstehung von** und **Entstehung bis** gesetzt sind.
    Bei einem einzelnen Datum stehen in beiden Feldern derselbe Wert. Ein
    ausgefülltes «von» allein genügt nicht: Für die Frist zählt das Ende des
    Zeitraums, und Anton rät es nicht aus dem Anfang — eine 80-Jahre-Frist ab
    1933 endet anders als ab 1965, und welcher der beiden Werte gemeint ist,
    weiss nur das Archiv.

!!! note "Wen das betrifft"
    Betroffen sind nur Datensätze, bei denen jemand tatsächlich eine Frist
    gewählt hat. Ohne gewählte Schutzfrist bleibt ein Datensatz frei, auch ohne
    Entstehungsdatum.

    Welche Datensätze im eigenen Bestand betroffen sind, lässt sich auf
    Anfrage auswerten — bei Anton as a Service über k & r. Sinnvollerweise
    trägt man die fehlenden Entstehungsdaten nach, statt die Unterlagen
    geschützt zu lassen.

## Die Typen pflegen

Jeder Eintrag der Werteliste trägt:

| Angabe | Bedeutung |
|---|---|
| **Dauer in Jahren** | Frist ab Entstehungsdatum |
| **öffentlich** | keine Frist — sofort frei |
| **dauernd geschützt** | Unterlagen nie frei, Beschreibung sichtbar |

Im Standard sind drei Typen hinterlegt: **öffentlich** (0 Jahre), **Standard
Schutzfrist** (30 Jahre) und **verlängerte Schutzfrist** (70 Jahre). Typen
lassen sich umbenennen, ergänzen und in der Dauer ändern.

!!! important "Superusern vorbehalten"
    Der Editor liegt unter `/admin/protection-periods` und ist Superusern
    vorbehalten — mit der Rolle `admin` ist er nicht erreichbar. Bei Anton as a
    Service ist dafür k & r zuständig.

Für Archive ohne dauernden Schutz ist «dauernd geschützt» optional; es muss
nicht konfiguriert sein.

## Was das angezeigte Jahr bedeutet

«Frei ab» ist das erste Jahr, in dem die Einheit **frei** ist. Bei Entstehung
1990 und 30 Jahren Frist also 2021, nicht 2020. Bis 0.107 hiess das Feld
«Sperrfrist bis»; der Wert war schon damals das erste freie Jahr.

## Bezeichnungen der Felder

Seit 0.108 heissen die Felder im Standard **Datensatz gesperrt**,
**Schutzfrist** und **Frei ab**, mit Hilfetexten, die den Unterschied nennen.
Hat ein Archiv eigene Bezeichnungen oder Hilfetexte gesetzt, bleiben sie beim
Update stehen. `anton:access-labels` listet sie neben dem Standard;
`anton:access-labels --adopt` übernimmt den Standard, wenn das Archiv es will.

## Beim Ändern einer Frist

Eine geänderte Dauer wirkt auf **alle** Datensätze dieses Typs — auch auf
bestehende. Das Jahr «Frei ab» wird neu ermittelt, Medien können damit
schlagartig öffentlich werden oder verschwinden. Eine Änderung an den Fristen
ist deshalb keine Kleinigkeit und gehört geprüft, bevor sie auf einem
produktiven Archiv landet.
