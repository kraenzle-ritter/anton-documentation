# API authentication

## Overview

Anton uses **API tokens** to authenticate external requests. This allows other systems to access the Anton API securely.

## Creating an API token

1. Log in as an admin
2. Open the **user administration**
3. Select the user → **Show**
4. In the **API tokens** section, enter a **name** that says what the token is
   for (e.g. "nightly export script"), and an **expiry date** if needed
5. Click **Create API token**

The token is shown **once**, right after it was created. Copy it then. Anton
stores only a hash and cannot show the token again later. If it is lost, create
a new one and revoke the old one.

An account can have several tokens, for instance one per script or system. Each
token has the rights of its account.

## Managing tokens

The account's detail page lists its tokens with name, "Last used" and expiry
date. **Revoke** invalidates a token immediately. An expired token is marked
"expired" and refused.

- **Legacy API token:** A token created before Anton v0.100.0 keeps working
  unchanged. It appears in the list as "Legacy API token" and can be revoked,
  but no longer displayed.
- **agate-handoff:** A click on "Open in agate" creates a token of its own for
  that handoff, valid for 12 hours. Anton removes expired handoff tokens at the
  next handoff.
- Only a superuser creates and revokes the tokens of a superuser account.
- The account itself sees its tokens but cannot create or revoke any.

## API request with a token

### Bearer token 

The token is passed as a **bearer token** in the `Authorization` header:

```bash
curl -X GET "https://your-anton-instance.ch/api/objects" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Accept: application/json"
```

### Query parameter (deprecated — will be removed in a future Anton version)

!!! warning "Deprecated"
    The query parameter `?api_token=` will be removed from Anton. Please switch existing integrations to the bearer header. Anton logs every call using `?api_token=` as a deprecation notice (without the token content). Anyone still accessing Anton this way should get in touch so that we can accompany the migration.

For backwards compatibility, the **legacy** API token (created before Anton v0.100.0) is currently also accepted as a query parameter `api_token`. New tokens are accepted in the header only:

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
| **One token per purpose** | A token of its own per script or system, so that one can be revoked alone |
| **Set an expiry date** | For temporary access; revoke the token immediately if compromise is suspected |
| **Minimal rights** | Equip API users only with the permissions they need |

## Public API

If the setting `public_api` is activated, certain endpoints can be queried without a token. The protected endpoints continue to require authentication.

The authority endpoints `/api/actors`, `/api/places` and `/api/keywords` (lists, selection, TEI, Beacon, reconciliation) answer without a token as long as the archive is public (`public_access`). When it is closed, they too require a token or a login; without one they answer `401`.
