# API-Authentifizierung

## Übersicht

Anton verwendet **API-Tokens** für die Authentifizierung von externen Anfragen. Dies ermöglicht es anderen Systemen, sicher auf die Anton-API zuzugreifen.

## API-Token erstellen

### Token für Benutzer generieren

1. Als Admin einloggen
2. **Benutzerverwaltung** öffnen
3. Benutzer auswählen → **Anzeigen**
4. Button **"Set api token"** klicken
5. Der Token wird automatisch generiert (60 Zeichen)

### Token anzeigen

Der generierte Token ist im Feld `api_token` in der Benutzerdetailansicht sichtbar.

## API-Anfrage mit Token

### Bearer-Token 

Der Token wird als **Bearer-Token** im `Authorization`-Header übergeben:

```bash
curl -X GET "https://ihre-anton-instanz.ch/api/objects" \
  -H "Authorization: Bearer IHR_API_TOKEN" \
  -H "Accept: application/json"
```

### Query-Parameter (deprecated — wird in einer künftigen Anton-Version entfernt)

!!! warning "Veraltet seit v0.70.x"
    Der Query-Parameter `?api_token=` wird aus Anton entfernt werden. Stellen Sie bestehende Integrationen auf Bearer-Header um. Anton loggt seit v0.70.x jeden Aufruf mit `?api_token=` als Deprecation-Hinweis (ohne Token-Inhalt). Wer noch über diesen Weg zugreift, sollte sich melden, damit wir die Migration begleiten können.

Aus Rückwärtskompatibilität wird der Token derzeit zusätzlich als Query-Parameter `api_token` akzeptiert:

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

**Einzelnen Akteur abrufen:**
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
| **Token regelmässig erneuern** | Bei Verdacht auf Kompromittierung neuen Token generieren |
| **Minimale Rechte** | API-Benutzer nur mit notwendigen Berechtigungen ausstatten |

## Öffentliche API

Falls das Setting `public_api` aktiviert ist, können bestimmte Endpunkte ohne Token abgefragt werden. Die geschützten Endpunkte erfordern weiterhin Authentifizierung.
