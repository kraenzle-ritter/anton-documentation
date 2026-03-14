# Gewichtete Suche (Admin)

Die gewichtete Suche ermöglicht eine relevanzbasierte Sortierung von Suchergebnissen für Akteur:innen, Orte und Schlagwörter.

## Konfiguration

### Globale Aktivierung

Die gewichtete Suche kann global für die API aktiviert werden:

```php
// In Tinker oder Seeder
Setting::setValue('search_weighted_enabled', true);  // Aktivieren
Setting::setValue('search_weighted_enabled', false); // Deaktivieren (Standard)
```

!!! info "Benutzereinstellungen"
    Jeder Benutzer kann die gewichtete Suche in seinen persönlichen Einstellungen konfigurieren:
    
    - **Standard**: Folgt der globalen Einstellung
    - **An**: Immer aktiviert (überschreibt globale Einstellung)
    - **Aus**: Immer deaktiviert (überschreibt globale Einstellung)

### API-Parameter

Bei API-Anfragen kann die gewichtete Suche per Parameter gesteuert werden:

```
GET /api/actors?search=Müller&weighted=true
GET /api/places?search=Zürich&weighted=true
GET /api/keywords?search=Archiv&weighted=true
```

Der API-Parameter hat die höchste Priorität und überschreibt sowohl Benutzer- als auch globale Einstellungen.

## Feldgewichtungen

Die Relevanz-Berechnung basiert auf konfigurierbaren Feldgewichtungen. Höhere Werte bedeuten höhere Relevanz.

### Standard-Gewichtungen

#### Akteur:innen (`search_weight_actors`)

| Feld | Gewicht | Beschreibung |
|------|---------|--------------|
| name | 10 | Hauptname |
| alternative_names | 7 | Alternative Namen |
| variants | 5 | Namensvarianten |
| abbreviations | 5 | Abkürzungen |
| type_label | 3 | Typ-Bezeichnung |
| description | 2 | Beschreibung |
| sources | 1 | Quellenangaben |
| comment | 1 | Kommentar (nur für interne Benutzer) |

#### Orte (`search_weight_places`)

| Feld | Gewicht | Beschreibung |
|------|---------|--------------|
| name | 10 | Ortsname |
| city | 8 | Stadt |
| state | 6 | Kanton/Bundesland |
| alternative_names | 5 | Alternative Namen |
| variants | 5 | Namensvarianten |
| abbreviations | 5 | Abkürzungen |
| address | 3 | Adresse |
| description | 2 | Beschreibung |
| sources | 1 | Quellenangaben |
| comment | 1 | Kommentar |

#### Schlagwörter (`search_weight_keywords`)

| Feld | Gewicht | Beschreibung |
|------|---------|--------------|
| label | 10 | Bezeichnung |
| description | 5 | Beschreibung |
| name | 3 | Interner Name |

### Gewichtungen anpassen

```php
// Beispiel: Gewichtungen für Akteur:innen anpassen
Setting::setValue('search_weight_actors', [
    'name' => 15,              // Name stark erhöhen
    'alternative_names' => 10, // Alternative Namen wichtiger
    'variants' => 5,
    'abbreviations' => 5,
    'type_label' => 3,
    'description' => 2,
    'sources' => 1,
    'comment' => 1,
]);
```

## Relevanz-Berechnung

Die Relevanz wird wie folgt berechnet:

| Trefferart | Multiplikator |
|------------|---------------|
| Exakte Übereinstimmung | Gewicht × 3 |
| Treffer am Wortanfang | Gewicht × 2 |
| Treffer enthält Begriff | Gewicht × 1 |

**Beispiel**: Suche nach "Müller" mit Gewicht `name = 10`:

- Exakter Treffer "Müller" → 10 × 3 = 30 Punkte
- "Müller-Weber" (beginnt mit) → 10 × 2 = 20 Punkte  
- "Anna Müller" (enthält) → 10 × 1 = 10 Punkte

## Prioritätsreihenfolge

Die Aktivierung der gewichteten Suche folgt dieser Priorität:

1. **API-Parameter** (`?weighted=true/false`) – höchste Priorität
2. **Benutzereinstellung** – nur wenn explizit "An" oder "Aus" gewählt (nicht "Standard")
3. **Globale Einstellung** (`search_weighted_enabled` in Settings) – Fallback

Wenn ein Benutzer "Standard" wählt, wird die globale Einstellung verwendet.

## Update durchführen

Nach einem Update muss der Seeder ausgeführt werden, um die Standard-Gewichtungen zu initialisieren:

```bash
php artisan db:seed --class=Update --env=<environment>
```

## Technische Details

- Trait: `Anton\Traits\HasWeightedSearch`
- Models: `Actor`, `Place`, `Keyword`
- Methode: `scopeDtQuery()` mit Option `weighted => true`
