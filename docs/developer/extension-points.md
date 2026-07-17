# Erweiterungspunkte

Archive haben Sonderwünsche — eine eigene Signaturlogik, ein besonderes
Word-Findbuch, eine Formatnormalisierung. Anton beantwortet das mit **einem
durchgehenden Muster**, statt den Kern pro Kunde zu forken:

> Mandantenspezifisches Verhalten wird eingehängt, indem eine **Klasse über eine
> Einstellung benannt** wird — oder als kundenspezifische Subklasse existiert.
> Der Kern bleibt unverändert.

Wer diesen Satz verinnerlicht, findet die meisten Erweiterungsnähte von selbst.
Diese Seite zählt die wichtigsten auf.

## Signaturbildung

Die Einstellung `identifier_generator` enthält entweder einen der eingebauten
Modi (`standard`, `recordgroup_as_base`, `id_identifier`, `manual_identifiers`)
oder den **voll qualifizierten Klassennamen** eines eigenen Generators. Anton
instanziiert ihn und ruft `getNewIdentifier(...)` auf:

```php
$generator = setting('identifier_generator');
// z.B. 'Anton\Models\IdentifierGenerators\KaeNewIdentifier'
return (new $generator($this))->getNewIdentifier($level_of_description_id, …);
```

Eigene Generatoren liegen unter `app/Models/IdentifierGenerators/`
(`KaeNewIdentifier`, `StopNewIdentifier` als Vorlagen). So kann ein Archiv den
Standort in die Signatur ziehen oder ein ganz eigenes Schema fahren, ohne dass
der Standardgenerator davon weiss.

## Exporter

Die Export-Schicht ist nach dieser Naht gebaut. Wer sie erweitert, hält sich an
zwei Regeln (siehe auch `CLAUDE.md`, Abschnitt *Exporter layout*):

- Builder, DTOs und Format-Logik gehören unter
  `app/Services/Exporter/<Format>/`, **nie** in einen HTTP-Controller.
- Ein Controller unter `app/Http/Controllers/Exporter/` ist nur ein
  Route-Handler.

Zwei konkrete Erweiterungsmuster:

**TEI über eine Factory.** `custom_teiexporter` ist eine Einstellung, die pro
Entität (`actors`, `places`, `keywords` …) eine Exporter-Klasse benennt. Die
`TeiExporterFactory` löst sie auf und fällt sonst auf die Standard-Exporter
zurück. So bekommt ein Archiv ein Sonderformat (etwa das Opera-Format von ZBZ),
ohne den Standard anzufassen.

**Kundenspezifische Subklassen.** Word-Findbücher existieren als
`AntonWordExport` und davon abgeleitete Varianten (`CasparwolfWordExport`,
`GosteliWordExport`, `ArchivdatenWordExport`); das DIP hat eine ZH-Variante
(`ZhCreateDip`). Das Muster: vom Standard erben, das Abweichende überschreiben.

!!! important "Die Export-Matrix mitpflegen"
    Wer ein Exportformat hinzufügt oder ändert, was ein bestehendes ausgibt,
    aktualisiert die [Export-Matrix](../admin/export-matrix.md) im selben
    Zug — Archive entscheiden danach, was eine Sicherung ist. Die Regel steht
    auch in `CLAUDE.md`.

## Medien-Konversionen

Die Standard-Konversionen (`web`, `thumb`, `poster`) stehen in
`config/conversions.php`. Für Abweichendes lässt sich ein **eigenes
Konversionsskript** hinterlegen: `media:conversions --conversion-script=…` liest
es aus dem `scripts/`-Verzeichnis des Mandanten (`customers/{slug}/scripts/`).
Damit kann ein Archiv etwa eine Normalisierung fahren, die der Kern nicht kennt.

## Formulare und Wertelisten

Kein Code, sondern Daten — aber die wichtigste «Erweiterung» überhaupt: Felder,
Formularsätze und Wertelisten macht ein Archiv über die Oberfläche oder über
Seeder. Details unter [Das Formularsystem](forms.md). Seeder überschreiben
bestehende Konfigurationen bewusst nicht.

## Mandanten-Assets

Jenseits von Code und Datenbank liegt Mandantenspezifisches unter
`customers/{slug}/` — Logo und Favicons, die genannten Konversionsskripte, Pfade
für Import und Reset. Das ist der Ort für alles, was zur Installation, aber
nicht zum Code gehört.

## Die Grenze

Der Preis dieses Musters: Kundenklassen und benannte Einstellungen sind über den
Baum verstreut. Bevor man einen neuen Sonderfall als eigene Klasse baut, lohnt
die Frage, ob er nicht als **Konfiguration** ausgedrückt werden kann — ein
Formularsatz, eine Werteliste, eine Einstellung. Konfiguration überlebt
Refactorings; eine Kundenklasse muss mitgezogen werden.
