# Zugang, Sperre und Schutzfrist

Anton regelt den Zugang auf drei Ebenen: über die Rolle der Person, über die
Einstellung, ob das Archiv überhaupt öffentlich ist, und am einzelnen Datensatz
über zwei getrennte Dinge — die **Sperre** und die **Schutzfrist**.

## Ist das Archiv öffentlich?

Die Einstellung **public_access** entscheidet, ob Aussenstehende den Katalog
sehen. Ist sie ausgeschaltet, steht die Datenbank nur angemeldeten Personen
offen. Ist sie eingeschaltet, ist der Katalog öffentlich — was einzelne
Datensätze zeigen, regeln dann Sperre und Schutzfrist.

Welche Rolle was darf, steht im [Einstieg](index.md#rollen).

## Sperre und Schutzfrist

> Die **Schutzfrist** schützt die Unterlagen, der Datensatz bleibt auffindbar.
> Die **Sperre** verbirgt den ganzen Datensatz, auch seine Beschreibung.

| | Datensatz gesperrt | Schutzfrist |
|---|---|---|
| Beschreibung (Titel, Daten, Verzeichnung) | unsichtbar | sichtbar und auffindbar |
| Bilder und Dokumente | unsichtbar | erst ab «Frei ab» |
| untergeordnete Einheiten | immer mitgesperrt | Typ: nein; «Frei ab» von Hand: ja |
| zeitlich begrenzt | nein | ja |

Sichtbar bleibt beides für interne Benutzer:innen, Bearbeitende und die
Administration. Ein Archiv kann die Felder umbenannt haben; seit Anton 0.108
heissen sie im Standard so wie hier.

## Datensatz gesperrt

Das Feld **Datensatz gesperrt** verbirgt den ganzen Datensatz vor der
Öffentlichkeit: Beschreibung, Medien und alle untergeordneten Einheiten. Er
erscheint weder in der Suche noch über Schnittstellen (API, OAI, Sitemap). Die
Sperre vererbt sich immer nach unten — unter einem gesperrten Datensatz gibt es
keinen öffentlichen.

## Schutzfrist

Die Schutzfrist schützt nur die Unterlagen und Digitalisate: Unterliegt eine
Verzeichnungseinheit noch einer Schutzfrist, bleibt der Datensatz sichtbar und
auffindbar, die Bilder und Dokumente jedoch nicht.

Anton rechnet für jeden Datensatz **ein** Jahr aus, ab dem er frei ist.
Massgeblich ist:

1. **Das Feld «Frei ab».** Dieser Wert hat Vorrang und **wirkt im Baum nach
   unten** auf alle untergeordneten Einheiten.
2. **Sonst die Schutzfrist des gewählten Typs**, gerechnet ab dem
   Entstehungsdatum. Typ-Schutzfristen gelten **nur für den Datensatz selbst**
   und vererben sich nicht.

Das Feld **Schutzfrist** wählt den Typ. Im Standard sind drei hinterlegt:

| Typ | Frist |
|---|---|
| öffentlich | keine — sofort frei |
| Standard Schutzfrist | 30 Jahre |
| verlängerte Schutzfrist | 70 Jahre |

Die Fristen sind pro Archiv konfigurierbar: Typen lassen sich umbenennen,
ergänzen und in der Dauer ändern; ebenso ist «dauernd geschützt» möglich. Die
Pflege ist Superusern vorbehalten; bei Anton as a Service ist dafür k & r
zuständig.

!!! note "«Frei ab» ist das erste freie Jahr"
    Bei Entstehung 1990 und 30 Jahren Frist steht dort 2021: ab 2021 sind die
    Unterlagen frei. Bis 0.107 hiess das Feld «Sperrfrist bis» oder «Schutzfrist bis» — der Wert war
    schon immer das erste freie Jahr.

## Einzelne Medien: nur intern

**Einzelne Medien** lassen sich in der Bearbeitungsmaske auf **nur intern**
setzen. Das gilt ohne Frist und nur für dieses Medium; Datensatz und übrige
Medien bleiben, wie sie sind.

## Einzelne Bereiche freigeben

Einer Person mit der Rolle Benutzer:in lässt sich der Zugang zu bestimmten
Zweigen öffnen. In der Benutzerverwaltung werden dazu die IDs der Datensätze als
kommagetrennte Liste eingetragen. Eine ID steht immer für den **ganzen Zweig**
darunter.

## Status der Beschreibung

Das Feld ist für Bestände gedacht. Steht ein Bestand auf **Entwurf**, ist er nur
für interne Benutzer:innen, Bearbeitende und die Administration zugänglich.
