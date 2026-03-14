# Sprachkonfiguration in Anton

## Übersicht

Anton unterstützt mehrsprachige (DE, EN, FR und IT) Inhalte für verschiedene Felder (Titel, Textfelder, Keywords, etc.). Dieses Dokument beschreibt die verfügbaren Einstellungen und gibt Empfehlungen für die Konfiguration.

## Arten von Sprachen

In Anton gibt es zwei verschiedene Konzepte von "Sprache":

1. **UI-Sprache** (`app.locale`): Die Sprache der Benutzeroberfläche (Menüs, Labels, Meldungen)
2. **Inhaltssprachen** (`locales`): Die Sprachen, in denen Archivdaten erfasst werden können

## System-Einstellung: `locales`

| Eigenschaft | Wert |
|------------|------|
| Typ | Array |
| Scope | `localisation` |
| Beispiel | `["de", "en", "fr"]` |

Definiert, welche Sprachen für übersetzbare Felder verfügbar sind. 

**Wichtig:** Die **erste Sprache im Array ist die Hauptsprache** und wird als Fallback verwendet, wenn für eine andere Sprache kein Wert existiert.

**Übersetzbare Felder:**
- Titel (AntonObject)
- Note-Felder
- Keywords (name, use_for)
- Places (description)

## Benutzer-Einstellung: `show_all_locales_in_edit_forms`

| Eigenschaft | Wert |
|------------|------|
| Typ | Boolean |
| Standard | `false` |
| Ort | Profil → Einstellungen → Bearbeitung |

**Wenn aktiviert (`true`):**
- In Bearbeitungsformularen werden **separate Eingabefelder für jede konfigurierte Sprache** angezeigt
- Beispiel: Titel (DE), Titel (EN), Titel (FR)

**Wenn deaktiviert (`false`):**
- Nur **ein Eingabefeld** wird angezeigt (für die aktuelle UI-Sprache)
- Bereits eingegebene Werte in anderen Sprachen werden als Info angezeigt, aber nicht bearbeitet

## Fallback-Verhalten

Wenn für die aktuelle Sprache kein Wert existiert:
1. Anton verwendet den Wert der **ersten Sprache** aus `setting('locales')`
2. Falls auch dort nichts vorhanden: Suche in den weiteren konfigurierten Sprachen

In der Detailansicht wird für Editoren angezeigt, aus welcher Sprache der Wert stammt (z.B. "Titel (DE)").

## Empfehlung: Eine Sprache pro Feld

**Unsere Empfehlung ist, nur in einer Sprache pro Feld zu speichern** (`show_all_locales_in_edit_forms = false`).

### Gründe

1. **Konsistenz**: Wenn Titel in mehreren Sprachen erfasst werden, müssen alle Übersetzungen gepflegt werden. Bei Änderungen am Original werden die Übersetzungen oft nicht aktualisiert.

2. **Archivstandards**: In der archivischen Praxis werden Dokumente normalerweise in ihrer Originalsprache beschrieben, nicht übersetzt.

3. **Suchbarkeit**: Die Volltextsuche (`full_text`-Spalte) enthält alle Sprachversionen. Das kann zu verwirrenden Treffern führen.

4. **Wartungsaufwand**: Mehrsprachige Datenpflege erfordert deutlich mehr Ressourcen.

### Wann Mehrsprachigkeit sinnvoll ist

- Archive mit internationalem Publikum (z.B. wissenschaftliche Sammlungen)
- Bestände mit Dokumenten in verschiedenen Sprachen, wo die Titelaufnahme in der Originalsprache erfolgt
- Institutionen mit gesetzlicher Verpflichtung zur Mehrsprachigkeit

## Konfigurationsbeispiele

### Einsprachiges Archiv 

```php
// Setting: locales
["de"]
```
```php
// UserSettings
show_all_locales_in_edit_forms: false
```

### Zweisprachiges Archiv (DE/FR)

```php
// Setting: locales
["de", "fr"]
```
```php
// UserSettings (je nach Bedarf)
show_all_locales_in_edit_forms: false  // Empfohlen
```

### Internationales Archiv

```php
// Setting: locales
["en", "de", "fr", "it"]
```
```php
// UserSettings (für Übersetzer)
show_all_locales_in_edit_forms: true
```
