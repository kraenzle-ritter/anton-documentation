# API authentication

## Overview

Anton uses **API tokens** to authenticate external requests. This allows other systems to access the Anton API securely.

## Creating an API token

### Generating a token for a user

1. Log in as an admin
2. Open the **user administration**
3. Select the user → **Show**
4. Click the **"Set api token"** button
5. The token is generated automatically (60 characters)

### Displaying the token

The generated token is visible in the `api_token` field in the user detail view.

## API request with a token

### Bearer token 

The token is passed as a **bearer token** in the `Authorization` header:

```bash
curl -X GET "https://your-anton-instance.ch/api/objects" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Accept: application/json"
```

### Query parameter (deprecated — will be removed in a future Anton version)

!!! warning "Deprecated since v0.70.x"
    The query parameter `?api_token=` will be removed from Anton. Please switch existing integrations to the bearer header. Since v0.70.x, Anton logs every call using `?api_token=` as a deprecation notice (without the token content). Anyone still accessing Anton this way should get in touch so that we can accompany the migration.

For backwards compatibility, the token is currently also accepted as a query parameter `api_token`:

```bash
# DEPRECATED — please switch to the bearer header
curl -X GET "https://your-anton-instance.ch/api/objects?api_token=YOUR_API_TOKEN" \
  -H "Accept: application/json"
```

Why remove it? Tokens in the URL end up in web server access logs, in the browser history and in referer headers — the bearer header has none of these problems.

### Examples

**Retrieving objects (bearer):**
```bash
curl "https://your-anton-instance.ch/api/objects" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

**Retrieving a single actor:**
```bash
curl "https://your-anton-instance.ch/api/actors/123" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

**Search with additional parameters:**
```bash
curl "https://your-anton-instance.ch/api/actors?search=Müller" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Example with JavaScript

```javascript
const apiToken = 'YOUR_API_TOKEN';

fetch('https://your-anton-instance.ch/api/objects', {
  headers: {
    'Authorization': `Bearer ${apiToken}`,
    'Accept': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

### Example with Python

```python
import requests

api_token = 'YOUR_API_TOKEN'
url = 'https://your-anton-instance.ch/api/objects'

headers = {
    'Authorization': f'Bearer {api_token}',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
```

## Security notes

| Recommendation | Description |
|------------|--------------|
| **Use bearer tokens** | A bearer token in the header is more secure than a query parameter |
| **Keep tokens secret** | Never store tokens in public code or repositories |
| **Use HTTPS** | Always send API requests over encrypted connections |
| **Renew tokens regularly** | Generate a new token if compromise is suspected |
| **Minimal rights** | Equip API users only with the permissions they need |

## Public API

If the setting `public_api` is activated, certain endpoints can be queried without a token. The protected endpoints continue to require authentication.
