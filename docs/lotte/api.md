# Lotte: API-Referenz

Lotte bietet eine REST-Schnittstelle für Clients wie Anton. Diese Seite erklärt die Grundsätze und listet darunter jede Route; die Liste wird aus der OpenAPI-Beschreibung erzeugt, die mit Lotte gepflegt und dort gegen die Routen getestet wird. Die Beschreibung selbst gibt es zum Herunterladen: [openapi.yaml](openapi.yaml) (OpenAPI 3.1).

## Grundsätze {#grundsaetze}

Jede Anfrage nennt den Mandanten im Pfad, `/t/<slug>/…`. Lotte wählt zuerst die Datenbank dieses Mandanten und prüft erst dann den Schlüssel, als Bearer-Token in der Kopfzeile `Authorization`. Ein Schlüssel gilt darum nur für seinen eigenen Mandanten, und jeder trägt eine Reihe von Befugnissen (`read`, `ingest`, `jobs`, `withdraw`, `metadata`; siehe [Clients und Schlüssel](operation.md#clients)). Ohne Schlüssel antworten nur `/health` und die signierten Adressen unter `/s/<slug>/…`.

```bash
curl -H "Authorization: Bearer <schlüssel>" https://<lotte>/t/<slug>/whoami
```

Objekte stehen im Pfad mit ihrer UUID; in Antworten und im Änderungsfeed heissen sie mit ihrer OCFL-ID `urn:uuid:<uuid>`. Fehler antworten mit JSON, `{"message": "…"}`, bei ungültigen Angaben zusätzlich mit `errors` je Feld.

| Status | Bedeutung |
|---|---|
| 202 | eine Ableitung oder der Text ist noch nicht da und steht jetzt in der Warteschlange; nach `Retry-After` Sekunden wieder fragen |
| 401 | kein Schlüssel, ein widerrufener Schlüssel oder einer eines anderen Mandanten |
| 403 | dem Schlüssel fehlt die Befugnis der Route; bei signierten Adressen: Signatur falsch oder abgelaufen |
| 404 | kein solcher Mandant, oder kein solches Objekt, Paket oder solcher Auftrag dieses Mandanten bzw. Clients |
| 409 | die Anfrage passt nicht zum Zustand des Pakets oder zu den bisher empfangenen Bytes |
| 410 | das Objekt ist zurückgezogen; die Antwort nennt den Grund |
| 422 | ungültige Angaben, oder es fehlt die Kopfzeile `Idempotency-Key` |

## Wiederholen ohne Doppel {#idempotenz}

`POST /packages` und `POST /jobs` verlangen die Kopfzeile `Idempotency-Key`, einen Schlüssel des Clients für diese eine Anfrage. Kommt dieselbe Anfrage mit demselben Schlüssel noch einmal, etwa weil die Antwort verloren ging, antwortet Lotte mit 200 und dem Paket bzw. Auftrag vom ersten Mal und legt nichts neu an. Auch `check`, `commit` und `discard` eines Pakets und das Zurückziehen eines Objekts lassen sich wiederholen: Die zweite Anfrage ändert nichts und antwortet mit dem Stand nach der ersten.

## Hochladen in Teilen {#hochladen}

Eine Datei eines Pakets geht mit `PUT /t/<slug>/packages/<paket>/files/<n>` als rohe Bytes; `<n>` ist ihre Stelle in der Beschreibung, ab 0. Grosse Dateien gehen in Teilen, je mit `Content-Range`; Lotte nimmt nur den Teil, der dort beginnt, wo der letzte aufhörte, und antwortet mit `Upload-Offset`. Nach einem Abbruch sagt `HEAD` auf dieselbe Adresse, wie viele Bytes angekommen sind.

```bash
curl -X PUT -H "Authorization: Bearer <schlüssel>" \
     -H "Content-Range: bytes 0-1048575/52428800" \
     --data-binary @teil-1 https://<lotte>/t/<slug>/packages/<paket>/files/0
curl -I -H "Authorization: Bearer <schlüssel>" https://<lotte>/t/<slug>/packages/<paket>/files/0
```

## Das Änderungsfeed lesen {#aenderungsfeed}

Ein Client merkt sich die letzte Folgenummer, die er verarbeitet hat, und fragt mit ihr nach: `GET /t/<slug>/changes?since=<folge>&limit=<1…1000>`. Die Antwort enthält die Einträge danach, in Reihenfolge, und `next`, die Nummer für die nächste Anfrage; ist nichts Neues da, bleibt `next` gleich. Weil Einträge in der Reihenfolge ihrer Nummer sichtbar werden und nie geändert werden, geht keiner verloren. Welche Arten es gibt, steht im [Überblick](index.md#aenderungsfeed) und unten bei [ChangeKind](#schema-changekind).

## Signierte Adressen {#signierte-adressen}

Ein Browser hat keinen Schlüssel. Für ihn gibt `GET /t/<slug>/objects/<objekt>/derivatives/<ableitung>/url` eine signierte Adresse unter `/s/<slug>/…` zurück, die einige Minuten gilt (Vorgabe 15). Sie liefert nur eine fertige Ableitung, stellt nichts in die Warteschlange und antwortet bei einem zurückgezogenen Objekt mit 410.

## Alle Routen {#routen}

!!! note "Automatisch erzeugt"
    Dieser Abschnitt wird aus Lottes `openapi.yaml` erzeugt (`scripts/gen-api-reference.py`); die Beschreibungen stehen in der Sprache des Codes (Englisch).

<!-- BEGIN generated api reference -->

Version `0.1.0-draft` · [OpenAPI-Beschreibung herunterladen](openapi.yaml)

### Client {#tag-client}

What a key belongs to and may do.

#### `GET /t/{tenant}/whoami` {#op-whoami}

**The customer, client and abilities of the key.** A client's first check; needs a valid key but no ability.

Zugang: Schlüssel, keine besondere Befugnis

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The key's customer, client and abilities. | `application/json` [Whoami](#schema-whoami) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |

### Objects {#tag-objects}

OCFL objects, one per medium; their files, metadata copy and withdrawal.

#### `GET /t/{tenant}/objects/{object}` {#op-objects-show}

**An object with its versions, files and events.** The OCFL inventory as the client needs it: every version with its files (logical path, sha512 digest, size), the head, the client's reference and the preservation events of the head (`metadata/events.json`).

Zugang: Schlüssel mit Befugnis `read`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The object. | `application/json` [ArchiveObject](#schema-archiveobject) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 410 | The object is withdrawn; the answer names the reason. | `application/json` [WithdrawnError](#schema-withdrawnerror) |

#### `DELETE /t/{tenant}/objects/{object}` {#op-objects-withdraw}

**Withdraw an object.** Writes a new version whose `metadata/object.json` says `withdrawn` (reason, time, client) and adds a `withdrawal` event; removes the derivative and text files and their rows; adds `object.withdrawn` to the feed. The content stays in OCFL until an operator purges it (`lotte:purge`; the rule when that is allowed is not decided yet). Afterwards the object, its files, derivatives, text and signed URLs answer 410; jobs skip it. Withdrawing it again answers 200 with `withdrawn: false` and adds no version.

Zugang: Schlüssel mit Befugnis `withdraw`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |

**Anfrage** (`application/json`): object

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `reason` | string | ja | Why the object is withdrawn; kept in the object and in the feed. |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The object is withdrawn (by this request or before). | `application/json` [WithdrawalResult](#schema-withdrawalresult) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 422 | The request is invalid. | `application/json` [ValidationError](#schema-validationerror) |

#### `GET /t/{tenant}/objects/{object}/files/{path}` {#op-objects-file}

**A file of an object, of the head or an earlier version.** Streamed as an attachment.

Zugang: Schlüssel mit Befugnis `read`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |
| `path` | Pfad | ja | string | The logical path inside the object, slashes included, e.g. `data/scan.tif` or `metadata/description.json`. |
| `version` | Abfrage | nein | string | The OCFL version (`v1`, `v2`, …); the head when not given. · `^v[0-9]+$` |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The file. | `application/octet-stream` |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such object, version, or file in that version. | `application/json` [Error](#schema-error) |
| 410 | The object is withdrawn; the answer names the reason. | `application/json` [WithdrawnError](#schema-withdrawnerror) |

#### `PUT /t/{tenant}/objects/{object}/metadata` {#op-objects-metadata}

**A new metadata copy.** The JSON body, as sent, becomes the new `metadata/description.json` in a new version with a `metadata modification` event, and the feed gets `object.metadata_updated`. The same copy again adds no version and answers 200 with `updated: false`. What is in the copy is the client's; Lotte does not interpret it.

Zugang: Schlüssel mit Befugnis `metadata`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |

**Anfrage** (`application/json`): object

The metadata copy (a JSON object, not a list).

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The head after the request. | `application/json` [MetadataResult](#schema-metadataresult) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 410 | The object is withdrawn; the answer names the reason. | `application/json` [WithdrawnError](#schema-withdrawnerror) |
| 422 | The request is invalid. | `application/json` [ValidationError](#schema-validationerror) |

### Derivatives {#tag-derivatives}

Access copies, thumbnails, posters and text, kept outside OCFL and made again at will.

#### `GET /t/{tenant}/objects/{object}/derivatives/{conversion}` {#op-objects-derivative}

**A derivative of an object.** The file when it is ready. Not made yet: 202 with `Retry-After`, and the conversion is queued; a request never converts by itself.

Zugang: Schlüssel mit Befugnis `read`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |
| `conversion` | Pfad | ja | string | The conversion: `web` (access copy), `thumb` (thumbnail), `poster` (video still); which ones an object has depends on its MIME type. The text has its own route. · `^[a-z0-9_-]+$` |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The derivative. | `image/jpeg`<br>`application/pdf`<br>`video/mp4`<br>`audio/mpeg` |
| 202 | Not made yet; queued now. Ask again after `Retry-After` seconds. · Kopfzeilen: `Retry-After` | `application/json` object |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such object, a conversion the object does not have, or a derivative given up after three failed attempts (then with `status: failed`). | `application/json` object |
| 410 | The object is withdrawn; the answer names the reason. | `application/json` [WithdrawnError](#schema-withdrawnerror) |

#### `GET /t/{tenant}/objects/{object}/derivatives/{conversion}/url` {#op-objects-derivative-url}

**A short-lived signed URL to a derivative.** For a browser that has no key: a URL below `/s/{tenant}/…`, valid for a few minutes (default 15). Only for a ready derivative; otherwise the same answers as the derivative itself.

Zugang: Schlüssel mit Befugnis `read`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |
| `conversion` | Pfad | ja | string | The conversion: `web` (access copy), `thumb` (thumbnail), `poster` (video still); which ones an object has depends on its MIME type. The text has its own route. · `^[a-z0-9_-]+$` |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The signed URL. | `application/json` [SignedUrl](#schema-signedurl) |
| 202 | Not made yet; queued now. Ask again after `Retry-After` seconds. · Kopfzeilen: `Retry-After` | `application/json` object |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such object, a conversion the object does not have, or a derivative given up after three failed attempts (then with `status: failed`). | `application/json` object |
| 410 | The object is withdrawn; the answer names the reason. | `application/json` [WithdrawnError](#schema-withdrawnerror) |

#### `GET /t/{tenant}/objects/{object}/text` {#op-objects-text}

**The text of an object.** Extracted text (PDF text layer, office documents, plain text) or, where the customer has OCR on, text by OCR; as written, UTF-8. Not made yet: 202 with `Retry-After`, and queued.

Zugang: Schlüssel mit Befugnis `read`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The text. | `text/plain` |
| 202 | Not made yet; queued now. Ask again after `Retry-After` seconds. · Kopfzeilen: `Retry-After` | `application/json` object |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such object, a conversion the object does not have, or a derivative given up after three failed attempts (then with `status: failed`). | `application/json` object |
| 410 | The object is withdrawn; the answer names the reason. | `application/json` [WithdrawnError](#schema-withdrawnerror) |

#### `GET /s/{tenant}/objects/{object}/derivatives/{conversion}` {#op-signed-derivative}

**A derivative behind a signed URL.** No key and no session, only a valid signature, as issued by `GET /t/{tenant}/objects/{object}/derivatives/{conversion}/url`. Serves a ready derivative only and never queues one.

Zugang: ohne Schlüssel

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `object` | Pfad | ja | string (uuid) | The object's UUID (the OCFL ID without `urn:uuid:`). |
| `conversion` | Pfad | ja | string | The conversion: `web` (access copy), `thumb` (thumbnail), `poster` (video still); which ones an object has depends on its MIME type. The text has its own route. · `^[a-z0-9_-]+$` |
| `expires` | Abfrage | ja | integer |  |
| `signature` | Abfrage | ja | string |  |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The derivative. | `image/jpeg`<br>`application/pdf`<br>`video/mp4`<br>`audio/mpeg` |
| 403 | The signature is missing, wrong or expired, or the URL was changed. | `application/json` [Error](#schema-error) |
| 404 | No such customer or object, or the derivative is not ready. | `application/json` [Error](#schema-error) |
| 410 | The object is withdrawn; the answer names the reason. | `application/json` [WithdrawnError](#schema-withdrawnerror) |

### Ingest {#tag-ingest}

Ingest in two steps: describe a package, upload its files (resumable), have them checked, then commit (one OCFL object per accepted file) or discard. A package neither committed nor discarded is discarded after the retention time (default 7 days).

#### `POST /t/{tenant}/packages` {#op-packages-store}

**Describe a package.** The first step of an ingest: the files to come, each with a name, the client's reference (unique per customer, it names the object later), an optional delivered checksum, a metadata copy and the size. The package is `open` until its files are uploaded and checked. The same `Idempotency-Key` again answers 200 with the package created the first time and creates nothing.

Zugang: Schlüssel mit Befugnis `ingest`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `Idempotency-Key` | Kopfzeile | ja | string | The client's key for this request; the same key again creates nothing twice. Missing or empty answers 422. |

**Anfrage** (`application/json`): [PackageDescription](#schema-packagedescription)

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | A package with this key exists already; it is returned unchanged. | `application/json` [Package](#schema-package) |
| 201 | The package was created. | `application/json` [Package](#schema-package) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 422 | The `Idempotency-Key` header is missing, or the description is invalid. | `application/json` [ValidationError](#schema-validationerror) |

#### `GET /t/{tenant}/packages/{package}` {#op-packages-show}

**A package with the result per file.** A client sees its own packages only.

Zugang: Schlüssel mit Befugnis `ingest`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `package` | Pfad | ja | string (uuid) |  |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The package. | `application/json` [Package](#schema-package) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |

#### `PUT /t/{tenant}/packages/{package}/files/{n}` {#op-packages-upload}

**Upload a file or the next part of it.** The body is the raw bytes. Without `Content-Range` the part starts at offset 0. Only the next part is taken: its first byte must be the `Upload-Offset` so far, otherwise 409. Only while the package is `open`.

Zugang: Schlüssel mit Befugnis `ingest`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `package` | Pfad | ja | string (uuid) |  |
| `n` | Pfad | ja | integer | The file's position in the description, from 0. |
| `Content-Range` | Kopfzeile | nein | string | `bytes <first>-<last>/<total>` or `bytes <first>-<last>/*`; `<first>` must equal the current `Upload-Offset`. · `^bytes [0-9]+-[0-9]+/([0-9]+\|\*)$` |

**Anfrage** (`application/octet-stream`): string

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 204 | The part was written. · Kopfzeilen: `Upload-Offset` |  |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 409 | The request does not fit the package's state (e.g. a commit before the check, an upload after it, discarding a committed package) or the bytes received so far (a part not starting at `Upload-Offset`). | `application/json` [Error](#schema-error) |

#### `HEAD /t/{tenant}/packages/{package}/files/{n}` {#op-packages-offset}

**How many bytes of a file have arrived.** To resume an interrupted upload, send the next part from `Upload-Offset`.

Zugang: Schlüssel mit Befugnis `ingest`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `package` | Pfad | ja | string (uuid) |  |
| `n` | Pfad | ja | integer | The file's position in the description, from 0. |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The bytes received so far. · Kopfzeilen: `Upload-Offset` |  |
| 401 | No valid key for this customer (no body on HEAD). |  |
| 403 | The key lacks the ability (no body on HEAD). |  |
| 404 | No such package of this client, or no such file (no body on HEAD). |  |

#### `POST /t/{tenant}/packages/{package}/check` {#op-packages-check}

**Have the files checked.** Queues the checks on the customer's queue: virus check, delivered checksum, format policy (preingest and normalisation by the customer's rules and the package's route), identification, format validation, consistency of extension, content and PRONOM ID, and characteristics. The package is `checking`, then `provisional` with a result per file (`accepted`, or `refused` with a reason). Asking again while it is checking or provisional changes nothing.

Zugang: Schlüssel mit Befugnis `ingest`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `package` | Pfad | ja | string (uuid) |  |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The package after the request. | `application/json` [Package](#schema-package) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 409 | The request does not fit the package's state (e.g. a commit before the check, an upload after it, discarding a committed package) or the bytes received so far (a part not starting at `Upload-Offset`). | `application/json` [Error](#schema-error) |

#### `POST /t/{tenant}/packages/{package}/commit` {#op-packages-commit}

**Commit a checked package.** Writes one OCFL object per accepted file, with the check events and an ingestion event, removes the working files and queues each new object's derivatives and text; the feed gets `object.created` per object. Refused files are left out. A package committed before answers as it did then. Only a `provisional` package can be committed.

Zugang: Schlüssel mit Befugnis `ingest`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `package` | Pfad | ja | string (uuid) |  |
| `Idempotency-Key` | Kopfzeile | nein | string | Recorded with the commit. |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The committed package; each accepted file names its object. | `application/json` [Package](#schema-package) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 409 | The request does not fit the package's state (e.g. a commit before the check, an upload after it, discarding a committed package) or the bytes received so far (a part not starting at `Upload-Offset`). | `application/json` [Error](#schema-error) |

#### `POST /t/{tenant}/packages/{package}/discard` {#op-packages-discard}

**Discard a package.** Removes the working files and marks the package `discarded`; the feed gets `package.discarded` with `by: client`. A package discarded before stays as it is; a committed package cannot be discarded.

Zugang: Schlüssel mit Befugnis `ingest`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `package` | Pfad | ja | string (uuid) |  |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The discarded package. | `application/json` [Package](#schema-package) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 409 | The request does not fit the package's state (e.g. a commit before the check, an upload after it, discarding a committed package) or the bytes received so far (a part not starting at `Upload-Offset`). | `application/json` [Error](#schema-error) |

### Jobs {#tag-jobs}

derive, ocr, verify and migrate over objects or a committed package, asynchronous, idempotent by key.

#### `POST /t/{tenant}/jobs` {#op-jobs-store}

**Create a job.** A job over objects or the objects of a committed package, run on the customer's queue in slices with progress and a result per object. `derive` makes missing derivatives and text (`options.conversion`, `options.retry_failed`); `ocr` makes text by OCR whether the customer has OCR on or not; `verify` checks fixity against the inventory and, with `options.ocfl`, validates each object with a second OCFL implementation — it adds no version, a finding is recorded as a failed fixity event; `migrate` applies one format policy rule (`options.rule`) and writes a new version only when the result passes the rule's verification, format validation and identification; `options.probe` only reports. Withdrawn objects are skipped. Every job ends with `job.finished` in the feed. The same `Idempotency-Key` again answers 200 with the job created the first time; a job that is over is never run again.

Zugang: Schlüssel mit Befugnis `jobs`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `Idempotency-Key` | Kopfzeile | ja | string | The client's key for this request; the same key again creates nothing twice. Missing or empty answers 422. |

**Anfrage** (`application/json`): [JobRequest](#schema-jobrequest)

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | A job with this key exists already; it is returned as it stands. | `application/json` [Job](#schema-job) |
| 201 | The job was created and queued. | `application/json` [Job](#schema-job) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 422 | The `Idempotency-Key` header is missing, or the request is invalid: an unknown kind, neither or both of objects and package, an object not of this customer, a package not committed by this client, an unknown rule or conversion. | `application/json` [ValidationError](#schema-validationerror) |

#### `GET /t/{tenant}/jobs/{job}` {#op-jobs-show}

**A job with its progress and results.** A client sees its own jobs only. Needs `jobs` or `read`.

Zugang: Schlüssel mit Befugnis `jobs` oder Schlüssel mit Befugnis `read`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `job` | Pfad | ja | string (uuid) |  |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The job. | `application/json` [Job](#schema-job) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |

### Changes {#tag-changes}

The change feed, append-only, in a monotonic sequence.

#### `GET /t/{tenant}/changes` {#op-changes}

**The change feed after a cursor.** The entries after `since`, in sequence order, and `next`: the last sequence returned, or `since` when there is nothing new. Each entry is written in the same database transaction as the change it reports; entries become visible in sequence order, so a cursor never skips one. No entry is ever changed or deleted. The feed is the customer's: every client with `read` sees all of it.

Zugang: Schlüssel mit Befugnis `read`

**Parameter**

| Name | Ort | Pflicht | Typ | Beschreibung |
|---|---|---|---|---|
| `tenant` | Pfad | ja | string | The customer's slug, as listed in the server's tenants file. An unknown slug answers 404. |
| `since` | Abfrage | nein | integer | The client's cursor; 0 for the beginning. · Vorgabe: `0` |
| `limit` | Abfrage | nein | integer | Vorgabe: `100` |

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | The next entries. | `application/json` [ChangesPage](#schema-changespage) |
| 401 | No key, a revoked key, or a key of another customer. | `application/json` [Error](#schema-error) |
| 403 | The key lacks the ability the route needs. | `application/json` [Error](#schema-error) |
| 404 | No such customer, or no such object, package or job of this customer (or client). | `application/json` [Error](#schema-error) |
| 422 | The request is invalid. | `application/json` [ValidationError](#schema-validationerror) |

### Monitoring {#tag-monitoring}

Statuses for monitoring, without a key and without content.

#### `GET /health` {#op-health}

**Health of the service and of each customer.** The storage base, and per customer its database, its folder (`ocfl/`, `derivatives/`, `text/`, `work/` writable) and its queue (a job waiting too long, derivatives given up). Statuses only; no content, no session, `Cache-Control: no-store`. The same check as `lotte:health`.

Zugang: ohne Schlüssel

**Antworten**

| Status | Beschreibung | Inhalt |
|---|---|---|
| 200 | Nothing is critical (the status may be `warning`). | `application/json` [Health](#schema-health) |
| 503 | At least one check is critical. | `application/json` [Health](#schema-health) |

### Datenstrukturen {#schemas}

#### Error {#schema-error}

| Feld | Typ | Beschreibung |
|---|---|---|
| `message` | string |  |

#### ValidationError {#schema-validationerror}

| Feld | Typ | Beschreibung |
|---|---|---|
| `message` | string |  |
| `errors` | object |  |

#### WithdrawnError {#schema-withdrawnerror}

| Feld | Typ | Beschreibung |
|---|---|---|
| `message` | `The object is withdrawn.` |  |
| `id` | [ObjectId](#schema-objectid) |  |
| `state` | `withdrawn` |  |
| `reason` | string |  |
| `withdrawn_at` | string (date-time) |  |

#### ObjectId {#schema-objectid}

string · The OCFL object ID, `urn:uuid:<uuid v7>`. · `^urn:uuid:[0-9a-f-]{36}$`

#### HealthStatus {#schema-healthstatus}

string · Werte: `ok`, `warning`, `critical`

#### CheckResult {#schema-checkresult}

| Feld | Typ | Beschreibung |
|---|---|---|
| `status` | [HealthStatus](#schema-healthstatus) |  |
| `message` | string |  |

#### Health {#schema-health}

| Feld | Typ | Beschreibung |
|---|---|---|
| `status` | [HealthStatus](#schema-healthstatus) |  |
| `checks` | object | Checks of the service as a whole (`storage`). |
| `tenants` | object | One result per customer, by slug. |

#### Whoami {#schema-whoami}

| Feld | Typ | Beschreibung |
|---|---|---|
| `tenant` | string |  |
| `client` | string |  |
| `abilities` | Liste von [Ability](#schema-ability) |  |

#### Ability {#schema-ability}

string · Werte: `read`, `ingest`, `jobs`, `withdraw`, `metadata`

#### Event {#schema-event}

A preservation event (PREMIS) as kept in `metadata/events.json`.

| Feld | Typ | Beschreibung |
|---|---|---|
| `type` | string | e.g. `virus check`, `fixity check`, `format identification`, `validation`, `ingestion`, `migration`, `metadata modification`, `withdrawal`. |
| `outcome` | string |  |
| `detail` | string |  |
| `agent` | string |  |
| `datetime` | string (date-time) |  |

#### ArchiveObject {#schema-archiveobject}

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | [ObjectId](#schema-objectid) |  |
| `reference` | string \| null | The client's reference, unique per customer. |
| `state` | string | Werte: `active`, `withdrawn` |
| `withdrawal` | object \| null |  |
| `head` | string | The newest version, e.g. `v2`. |
| `digest_algorithm` | `sha512` |  |
| `versions` | Liste von object |  |
| `versions[].version` | string |  |
| `versions[].created` | string (date-time) |  |
| `versions[].message` | string |  |
| `versions[].files` | Liste von object |  |
| `events` | Liste von [Event](#schema-event) | The events of the head. |

#### MetadataResult {#schema-metadataresult}

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | [ObjectId](#schema-objectid) |  |
| `head` | string |  |
| `updated` | boolean | false when the copy was the same and no version was added. |

#### WithdrawalResult {#schema-withdrawalresult}

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | [ObjectId](#schema-objectid) |  |
| `state` | `withdrawn` |  |
| `head` | string |  |
| `reason` | string |  |
| `withdrawn_at` | string (date-time) |  |
| `withdrawn` | boolean | true when this request withdrew the object, false when it was withdrawn before. |

#### DerivativeStatus {#schema-derivativestatus}

string · Werte: `missing`, `queued`, `ready`, `failed`

#### SignedUrl {#schema-signedurl}

| Feld | Typ | Beschreibung |
|---|---|---|
| `url` | string (uri) |  |
| `expires_at` | string (date-time) |  |

#### PackageDescription {#schema-packagedescription}

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `route` | string | nein | The route the files came by, as the client names it; the format policy decides by it (some routes are never refused for an invalid format). · Vorgabe: `upload` · `^[a-z0-9_-]+$` |
| `files` | Liste von object | ja |  |
| `files[].name` | string | ja | The file name; a path is cut to its last part. |
| `files[].reference` | string \| null | nein | The client's reference for the object to be; unique per customer. |
| `files[].checksum` | string \| null | nein | The delivered checksum; the file is refused when it does not match. · `^(md5\|sha1\|sha256\|sha512):[0-9a-fA-F]+$` |
| `files[].description` | object \| null | nein | The metadata copy; becomes `metadata/description.json`. |
| `files[].size` | integer \| null | nein |  |

#### PackageState {#schema-packagestate}

string · Werte: `open`, `checking`, `provisional`, `committed`, `discarded`

#### Package {#schema-package}

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | string (uuid) |  |
| `state` | [PackageState](#schema-packagestate) |  |
| `route` | string |  |
| `files` | Liste von object |  |
| `files[].n` | integer | The position, as in the upload route. |
| `files[].name` | string |  |
| `files[].reference` | string \| null |  |
| `files[].received` | integer | Bytes received. |
| `files[].status` | string | Werte: `pending`, `accepted`, `refused` |
| `files[].reason` | string \| null | Why the file was refused. |
| `files[].puid` | string \| null | The PRONOM ID found by the identification. |
| `files[].mime_type` | string \| null |  |
| `files[].normalized_name` | string \| null | The name after a format policy rule changed the file. |
| `files[].object` | [ObjectId](#schema-objectid) \| null | The object written at commit. |

#### JobKind {#schema-jobkind}

string · Werte: `derive`, `ocr`, `verify`, `migrate`

#### JobState {#schema-jobstate}

string · Werte: `queued`, `running`, `finished`, `failed`

#### JobRequest {#schema-jobrequest}

| Feld | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `kind` | [JobKind](#schema-jobkind) | ja |  |
| `target` | object | ja | Either `objects` or `package`, not both. |
| `target.objects` | Liste von string | nein |  |
| `target.package` | string | nein | A package of this client in state `committed`. |
| `options` | object | nein |  |
| `options.conversion` | string | nein | derive: only this conversion (`web`, `thumb`, `poster`, `text`). |
| `options.retry_failed` | boolean | nein | derive: also what failed fewer than three times. |
| `options.ocfl` | boolean | nein | verify: also validate each object with a second OCFL implementation. |
| `options.rule` | string | nein | migrate: the format policy rule, e.g. `tiff_zip`. |
| `options.probe` | boolean | nein | migrate: run the rule on copies and report; change nothing. |

#### Job {#schema-job}

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | string (uuid) |  |
| `kind` | [JobKind](#schema-jobkind) |  |
| `target` | object |  |
| `options` | object |  |
| `state` | [JobState](#schema-jobstate) |  |
| `total` | integer |  |
| `done` | integer |  |
| `failed` | integer |  |
| `results` | object | One result per object, by object ID. |
| `error` | string \| null |  |
| `created_at` | string (date-time) |  |
| `started_at` | string \| null (date-time) |  |
| `finished_at` | string \| null (date-time) |  |

#### ChangeKind {#schema-changekind}

string · `object.created` (committed from a package); `object.version_added` (migration, normalisation, a fixity finding); `object.metadata_updated`; `object.withdrawn`; `object.purged` (by an operator); `derivative.ready`; `derivative.failed` (every failure, with `attempts` and `given_up`; the text's with conversion `text`); `text.ready`; `package.discarded` (`by`: `client`, `operator` or `retention`); `job.finished`. · Werte: `object.created`, `object.version_added`, `object.metadata_updated`, `object.withdrawn`, `object.purged`, `derivative.ready`, `derivative.failed`, `text.ready`, `package.discarded`, `job.finished`

#### Change {#schema-change}

| Feld | Typ | Beschreibung |
|---|---|---|
| `sequence` | integer | Monotonic; never goes back. |
| `kind` | [ChangeKind](#schema-changekind) |  |
| `object` | [ObjectId](#schema-objectid) \| null | The object the entry is about; null for packages and jobs. |
| `at` | string (date-time) |  |
| `payload` | object | What a client needs, the object again as `id` where there is one: for object entries `head`, `file_name`, `size`, `digest`, `mime_type`, `puid` and `reference`; for derivatives `conversion`, `head` and size or `attempts`, `given_up`, `error`; for a withdrawal or purge `reason`; for packages `package`, `by`, `was`, `references`; for jobs `job`, `kind`, `state`, `total`, `done`, `failed`. |

#### ChangesPage {#schema-changespage}

| Feld | Typ | Beschreibung |
|---|---|---|
| `changes` | Liste von [Change](#schema-change) |  |
| `next` | integer | The cursor for the next request: the last sequence returned, or `since` when there was nothing new. |
<!-- END generated api reference -->
