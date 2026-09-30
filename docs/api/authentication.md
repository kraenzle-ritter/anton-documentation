# API-Authentifizierung

## Übersicht

Anton verwendet **API-Tokens** für die Authentifizierung von externen Anfragen. Dies ermöglicht es anderen Systemen, sicher auf die Anton-API zuzugreifen.

## API-Token erstellen

1. Als Admin einloggen
2. **Benutzerverwaltung** öffnen
3. Benutzer:in auswählen → **Anzeigen**
4. Im Abschnitt **API-Tokens** eine **Bezeichnung** eingeben, die sagt, wofür der
   Token ist (z. B. «Skript Nachtexport»), bei Bedarf ein **Ablaufdatum**
5. **API-Token erstellen** klicken

Der Token wird **einmal** angezeigt, direkt nach dem Erstellen. Kopieren Sie ihn
dann. Anton speichert nur einen Hash und kann den Token später nicht mehr
zeigen. Geht er verloren, erstellen Sie einen neuen und widerrufen den alten.

Ein Konto kann mehrere Tokens haben, etwa einen pro Skript oder System. Jeder
Token hat die Rechte seines Kontos.

## Tokens verwalten

Die Detailseite des Kontos listet seine Tokens mit Bezeichnung, «Zuletzt benutzt»
und Ablaufdatum. **Widerrufen** macht einen Token sofort ungültig. Ein
abgelaufener Token ist als «abgelaufen» markiert und wird abgewiesen.

- **Bisheriger API-Token:** Ein Token, der vor Anton v0.100.0 erstellt wurde,
  funktioniert unverändert weiter. Er erscheint in der Liste als «Bisheriger
  API-Token» und lässt sich widerrufen, aber nicht mehr anzeigen.
- **agate-handoff:** Ein Klick auf «In agate öffnen» erzeugt einen eigenen Token
  für diese Übergabe, 12 Stunden gültig. Abgelaufene Übergabe-Tokens räumt Anton
  bei der nächsten Übergabe weg.
- Tokens eines Superuser-Kontos erstellt und widerruft nur ein Superuser.
- Das Konto selbst sieht seine Tokens, kann aber keine erstellen oder
  widerrufen.

## API-Anfrage mit Token

### Bearer-Token 

Der Token wird als **Bearer-Token** im `Authorization`-Header übergeben:

```bash
curl -X GET "https://ihre-anton-instanz.ch/api/objects" \
  -H "Authorization: Bearer IHR_API_TOKEN" \
  -H "Accept: application/json"
```

### Query-Parameter (deprecated — wird in einer künftigen Anton-Version entfernt)

!!! warning "Veraltet"
    Der Query-Parameter `?api_token=` wird aus Anton entfernt werden. Stellen Sie bestehende Integrationen auf Bearer-Header um. Anton loggt jeden Aufruf mit `?api_token=` als Deprecation-Hinweis (ohne Token-Inhalt). Wer noch über diesen Weg zugreift, sollte sich melden, damit wir die Migration begleiten können.

Aus Rückwärtskompatibilität wird der **bisherige** API-Token (vor Anton v0.100.0 erstellt) derzeit zusätzlich als Query-Parameter `api_token` akzeptiert. Neue Tokens gelten nur im Header:

```bash
# DEPRECATED — bitte auf Bearer-Header umstellen
curl -X GET "https://ihre-anton-instanz.ch/api/objects?api_token=IHR_API_TOKEN" \
  -H "Accept: application/json"
```

Warum weg? Tokens in der URL landen in Web-Server-Access-Logs, im Browser-Verlauf und in Referer-Headern — der Bearer-Header hat keines dieser Probleme.

### Beispiele

**Objekte abrufen (Bearer):**
```bash
curl "https://ihre-anton-instanz.ch/api/objects" \
  -H "Authorization: Bearer IHR_API_TOKEN"
```

**Einzelne Akteur:in abrufen:**
```bash
curl "https://ihre-anton-instanz.ch/api/actors/123" \
  -H "Authorization: Bearer IHR_API_TOKEN"
```

**Suche mit zusätzlichen Parametern:**
```bash
curl "https://ihre-anton-instanz.ch/api/actors?search=Müller" \
  -H "Authorization: Bearer IHR_API_TOKEN"
```

### Beispiel mit JavaScript

```javascript
const apiToken = 'IHR_API_TOKEN';

fetch('https://ihre-anton-instanz.ch/api/objects', {
  headers: {
    'Authorization': `Bearer ${apiToken}`,
    'Accept': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

### Beispiel mit Python

```python
import requests

api_token = 'IHR_API_TOKEN'
url = 'https://ihre-anton-instanz.ch/api/objects'

headers = {
    'Authorization': f'Bearer {api_token}',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
```

## Sicherheitshinweise

| Empfehlung | Beschreibung |
|------------|--------------|
| **Bearer-Token verwenden** | Bearer-Token im Header ist sicherer als Query-Parameter |
| **Token geheim halten** | Tokens niemals in öffentlichem Code oder Repositories speichern |
| **HTTPS verwenden** | API-Anfragen immer über verschlüsselte Verbindungen senden |
| **Ein Token pro Zweck** | Pro Skript oder System ein eigener Token, damit sich einer allein widerrufen lässt |
| **Ablaufdatum setzen** | Für befristete Zugänge; bei Verdacht auf Kompromittierung den Token sofort widerrufen |
| **Minimale Rechte** | API-Benutzer:innen nur mit notwendigen Berechtigungen ausstatten |

## Öffentliche API

Falls das Setting `public_api` aktiviert ist, können bestimmte Endpunkte ohne Token abgefragt werden. Die geschützten Endpunkte erfordern weiterhin Authentifizierung.

Die Normdaten-Endpunkte `/api/actors`, `/api/places` und `/api/keywords` (Listen, Auswahl, TEI, Beacon, Abgleich) beantworten Anfragen ohne Token, solange das Archiv öffentlich ist (`public_access`). Ist es geschlossen, verlangen auch sie einen Token oder eine Anmeldung; ohne antworten sie mit `401`.
