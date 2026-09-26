Mit den Einstellungen kann Anton an die Bedürfnisse der Benutzerinnen angepasst werden. Die Einstellungen beziehen sich auf eine Anton-Instanz. Manche Einstellungen können von Admins geändert werden.

## Grundlegende Einstellungen
Die Einstellungen werden bei der Installation gesetzt.

### abo
### additional_superusers
### identifier_pattern
### maximum_storage
### no_automatic_identifiers
### period_of_protection_values
### possible_children
### public_access
### recordgroups_for_identifier_base

## Theme
### custom_css

Eigene CSS-Regeln für das ganze Archiv. Für eine Hausschrift braucht es keinen
Link zu Google Fonts: Die freien Schriften, die mit Anton ausgeliefert werden
(Archivo, DejaVu Sans, Fira Sans, Lato, Libre Franklin, Lora, Merriweather,
Oswald, Roboto), bindet eine Zeile ein:

```css
@import url('/fonts/local-fonts.css');

body { font-family: 'Lora', Georgia, serif; }
```

Die Schrift kommt dann vom eigenen Server; die Adressen der Besucher:innen
gehen an niemanden sonst.
### theme

## Persönliche Einstellungen

Neben den instanzweiten Einstellungen hat jede Person im eigenen Profil einige
persönliche Voreinstellungen. Dazu gehört das Anzeigen der
[Feld-Hilfetexte](forms.md#hilfetexte-zu-feldern) direkt in der
Bearbeitungsmaske (im Standard aus).
