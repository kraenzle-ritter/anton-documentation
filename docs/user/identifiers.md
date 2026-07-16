# Signaturen

Anton erstellt Signaturen automatisch. Hier wird das Standardschema
beschrieben; die Signaturbildung ist pro Archiv über das Setting
`identifier_generator` umstellbar:

| Wert | Verhalten |
|---|---|
| `standard` | Das unten beschriebene Schema |
| `recordgroup_as_base` | Wie Standard, aber die Bestandsgruppe statt des Archivs als Basis |
| `id_identifier` | Fortlaufende Nummer |
| `manual_identifiers` | Keine automatische Vergabe — die Signatur wird von Hand eingegeben |

Darüber hinaus lässt sich eine archivspezifische Signaturbildung
programmieren. Die Einstellung wird beim Aufsetzen gewählt und ist im
Admin-Bereich nicht änderbar.

## Verzeichnungsstufen

|Verzeichnungsstufe|Signaturbeispiel|Beschreibung|kann enthalten|
|:---------------- |:---------------|:-----------|:-------------|
| Archiv | KRA | Umfassende Einheit einer Institution. Hat keine übergeordnete Verzeichnungseinheit. | Bestandsgruppe, Bestand |
|Bestandsgruppe	|nicht signaturrelevant| Es können Bestände logisch geordnet werden.|	Bestandsgruppe, Bestand|
|Bestand|KRA 3|Einheit einer Provenienz oder Ablieferung. Bestände werden pro Archiv durchnummeriert.|Serie, Klasse, Dossier, Einzelstück|
|Klasse|nicht signaturrelevant|Es können Dossiers logisch geordnet werden.|	Serie, Klasse, Dossier, Einzelstück|
|Serie|KRA 3/22|Verhält sich bzgl. Signaturen wie ein Dossier|	Serie, Dossier, Einzelstück|
|Dossier|KRA 3/22|Standard-Verzeichnungseinheit. Akte, Amtsbücher o.ä. werden auf Stufe Dossier verzeichnet. Dossiers werden pro Bestand durchnummeriert.|	Dossier, Einzelstück|
|Einzelstück|KRA 3/22.1|Unterste Verzeichnungsstufe für z.B. Fotografien, einzelne Schriftstücke.| Einzelstück |

Bestandsgruppen, Klassen, Serien, Dossiers und Einzelstücke können sich selbst
enthalten (z.B. Teil-Dossiers). Ein Bestand innerhalb eines Bestands ist
dagegen nicht zulässig.

Für **Archiv, Bestandsgruppe und Klasse** vergibt Anton keine Signatur — diese
Stufen sind nicht signaturrelevant und werden, falls gewünscht, von Hand
beschriftet.

## Signaturschema
Die Signatur setzt sich zusammen aus dem Archivkürzel, der Bestandsnummer und den Dossier- und Einzelstücknummern.

```
Archivkürzel Bestandsnummer/Dossiernummer.Einzelstücknummer
```

Dossiernummer und Einzelstücknummer können weiter verschachtelt werden. Jede weitere Stufe wird mit einem Punkt getrennt.

### Beispiele
> KRA, 22/1.5     (Archiv KRA;  Bestand 22; Serie oder Dossier 1; Teildossier oder Einzelstück 5)

> Test, 1/1       (Archiv Test; Bestand  1; Serie, Dossier oder Einzelstück 1)

> HDR, 25/4.7.5   (Archiv HDR;  Bestand 25; Serie oder Dossier 4; Serie oder (Teil-)dossier 7; Teildossier oder Einzelstück 5)

## Signaturen von Hand ändern

Die automatisch vergebene Signatur lässt sich überschreiben — das Feld
**Signatur** ist ein gewöhnliches Eingabefeld.

!!! warning "Signaturen sind nicht eindeutig"
    Anton erzwingt keine eindeutigen Signaturen. Wird eine bereits vergebene
    Signatur eingetragen, erscheint beim Speichern ein Hinweis mit Verweis auf
    die betroffenen Datensätze — gespeichert wird trotzdem. Der Hinweis ist
    bewusst nicht blockierend, weil Dubletten in der Praxis vorkommen.

Beim [Verschieben](hierarchy.md) eines Datensatzes bleibt die Signatur
unverändert. Sie ist danach gegebenenfalls von Hand anzupassen.

## Altsignatur

Für abgelöste Signaturen und Aktenzeichen steht das eigene Feld
**Altsignatur** zur Verfügung. Es wird von der [Volltextsuche](search.md)
mitdurchsucht.
