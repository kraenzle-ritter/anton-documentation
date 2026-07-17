# Zugang und Schutzfristen

Anton regelt den Zugang auf drei Ebenen: über die Rolle der Person, über die
Einstellung, ob das Archiv überhaupt öffentlich ist, und über Schutzfristen am
einzelnen Datensatz.

## Ist das Archiv öffentlich?

Die Einstellung **public_access** entscheidet, ob Aussenstehende den Katalog
sehen. Ist sie ausgeschaltet, steht die Datenbank nur angemeldeten Personen
offen. Ist sie eingeschaltet, ist der Katalog öffentlich — was einzelne
Datensätze zeigen, regeln dann die Schutzfristen.

Welche Rolle was darf, steht im [Einstieg](index.md#rollen).

## Schutzfristen

Unterliegt eine Verzeichnungseinheit noch einer Schutzfrist, bleibt der
Datensatz sichtbar, die Bilder und Dokumente jedoch nicht.

Anton rechnet für jeden Datensatz **ein** Freigabejahr aus. Massgeblich ist:

1. **Das Feld «Schutzfrist bis»** (Freigabejahr). Dieser Wert hat Vorrang und
   **vererbt sich im Baum nach unten** an alle untergeordneten Einheiten.
2. **Sonst die Schutzfrist des gewählten Typs**, gerechnet ab dem
   Entstehungsdatum. Typ-Schutzfristen gelten **nur für den Datensatz selbst**
   und vererben sich nicht.

Das Feld **Zugangsbestimmungen / Sperrfrist** wählt den Typ. Im Standard sind
drei hinterlegt:

| Typ | Frist |
|---|---|
| öffentlich | keine — sofort frei |
| Standard Schutzfrist | 30 Jahre |
| verlängerte Schutzfrist | 70 Jahre |

Die Fristen sind pro Archiv konfigurierbar: Typen lassen sich umbenennen,
ergänzen und in der Dauer ändern; ebenso ist «nie freigeben» möglich. Die
Pflege ist Superusern vorbehalten; bei Anton as a Service ist dafür k & r
zuständig.

!!! note "Das angezeigte Freigabejahr"
    Angezeigt wird das erste Jahr, in dem die Einheit **frei** ist — bei
    Entstehung 1990 und 30 Jahren Frist also 2021, nicht 2020.

## Unbefristet sperren

**Einzelne Medien** lassen sich in der Bearbeitungsmaske unbefristet sperren.

**Ganze Datensätze** sperrt das Feld **Gesperrt**. Es wirkt auf den Datensatz,
alle untergeordneten Einheiten und deren Medien; sichtbar bleiben sie nur für
interne Benutzer, Bearbeitende und die Administration.

## Einzelne Bereiche freigeben

Einer Person mit der Rolle Benutzer:in lässt sich der Zugang zu bestimmten
Zweigen öffnen. In der Benutzerverwaltung werden dazu die IDs der Datensätze als
kommagetrennte Liste eingetragen. Eine ID steht immer für den **ganzen Zweig**
darunter.

## Status der Beschreibung

Das Feld ist für Bestände gedacht. Steht ein Bestand auf **Entwurf**, ist er nur
für interne Benutzer, Bearbeitende und die Administration zugänglich.
