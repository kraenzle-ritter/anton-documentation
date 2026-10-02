# API authentication

## Overview

Anton uses **API tokens** to authenticate external requests. This allows other systems to access the Anton API securely.

## Creating an API token

1. Log in as an admin
2. Open the **user administration**
3. Select the user → **Show**
4. In the **API tokens** section, enter a **name** that says what the token is
   for (e.g. "nightly export script"), and an **expiry date** if needed
   (leave it empty for a token without expiry; 18 January 2038 at the latest)
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

### No token in the URL

The query parameter `?api_token=` is no longer accepted. A request that sends `api_token` in the URL or in a form receives **401** with a note to send the token in the header — even if it also carries a valid header:

```json
{"error": "The api_token parameter is no longer accepted. Send the token in the header: Authorization: Bearer <token>"}
```

Tokens in the URL end up in web server access logs, in browser histories and in referer headers; the bearer header has none of these problems. Anton logs every such request (without the token content), so that an integration that was missed shows up.

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
| **Token in the header only** | A token in the URL is refused (401) |
| **Keep tokens secret** | Never store tokens in public code or repositories |
| **Use HTTPS** | Always send API requests over encrypted connections |
| **One token per purpose** | A token of its own per script or system, so that one can be revoked alone |
| **Set an expiry date** | For temporary access; revoke the token immediately if compromise is suspected |
| **Minimal rights** | Equip API users only with the permissions they need |

## Public API

If the setting `public_api` is activated, certain endpoints can be queried without a token — **for reading only** (`GET`, `HEAD`). The protected endpoints continue to require authentication.

**Writing always takes the token of an account with the editor role or higher**, public API or not: creating and changing persons and organisations (`POST /api/actors`, `PUT /api/actors/{id}`), places (`POST /api/places`, `POST /api/places/{id}`), SIP submissions (`POST /api/sips/import`), ingest callbacks (`POST /api/ingest/confirm|failed/{id}`) and `POST /api/ai-cataloging/usage`. Without a token they answer `401`, with the token of an account lacking that role `403`.

Regenerating the TEI exports (`GET /api/tei/refresh`, `?ids=` on `/api/tei/actors|places|keywords`) takes a token of any role; without one they answer `401`.

The authority endpoints `/api/actors`, `/api/places` and `/api/keywords` (lists, selection, TEI, Beacon, reconciliation) answer without a token as long as the archive is public (`public_access`). When it is closed, they too require a token or a login; without one they answer `401`.
