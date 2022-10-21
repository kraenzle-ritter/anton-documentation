Anton erstellt automatisch Signaturen. Mit dem Setting `no_automatic_identifiers` kann diese Funktion deaktiviert werden.

## Verzeichnungsstufen

Anton unterstützt standardmässig folgende Verzeichnungsstufen:

|Verzeichnungsstufe|Signaturbeispiel|Beschreibung|kann enthalten|
|:---------------- |:---------------|:-----------|:-------------|
| Archiv | KRA | Umfasssende Einheit einer Institution. Hat keine übergeordnete Verzeichnubgseinheit. | Bestandsgruppe, Bestand |
|Bestandsgruppe	|nicht signaturrelevant<sup>*</sup>| Es können Bestände logisch geordnet werden.|	Bestandsgruppe, Bestand|
|Bestand|KRA 3|Einheit einer Provenienz oder Ablieferung. Bestände werden pro Archiv durchnummeriert.|Klasse, Dossier, Einzelstück|
|Klasse|nicht signaturrelevant|Es können Dossiers logisch geordnet werden.|	Klasse, Dossier, Einzelstück|
|Dossier|KRA 3/22|Standard-Verzeichnungseinheit. Akte, Amtsbücher o.ä. werden auf Stufe Dossier verzeichnet. Dossiers werden pro Bestand durchnummeriert.|	Dossier, Einzelstück|
|Einzelstück|KRA 3/22.1|Unterste Verzeichnungsstufe für z.B. Fotografien, einzelne Schriftstücke.

<sup>*</sup> Mit dem Setting `recordgroups_for_identifier_base` kann die Bestandsgruppe als Ausgangspunkt Basissignaturen gemacht werden. Mit dem Setting `identifier_generator` kann die automatische Signaturbildung vollständig individuell implementiert werden.

Bestandsgruppen, Klassen, Dossiers und Einzelstücke können sich selbst enthalten (z.B. Teil-Dossiers).

## Signaturschema
Die Signatur setzt sich zusammen aus dem Archivkürzel, der Bestandsnummer und den Dossier- und Einzelstücknummern.

```
Archivkürzel Bestandsnummer/Dossiernummer.Einzelstücknummer
```

Dossiernummer und Einzelstücknummer können weiter verschachtelt werden. Jede weitere Stufe wird mit einem Punkt getrennt.

### Beispiele
> KRA, 22/1.5     (Archiv KRA;  Bestand 22; Dossier 1; Teildossier oder Einzelstück 5)

> Test, 1/1       (Archiv Test; Bestand  1; Einzelstück oder Dossier 1)

> HDR, 25/4.7.5   (Archiv HDR;  Bestand 25; Dossier 4; Teildossier 7;Teildossier oder Einzelstück 5)
