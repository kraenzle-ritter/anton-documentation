# DIMAG upload status

For archives with a DIMAG connection (Canton of Zurich municipalities such as
Opfikon, Lindau, Dürnten), Anton has since **v0.65.0** shown the transfer status
of every media file visibly in the UI — and reports structural errors to the
administration by email immediately.

Background: previously it could happen that a file was stored locally but not
successfully transferred to DIMAG (an expired password, missing write
permissions, DIMAG unreachable). Operators saw a green «record updated» and only
noticed at the next DIMAG audit that nothing had arrived. The trigger for the
implementation was an incident on 20 May 2026: a rotated password led to 30
minutes of silent downtime.

## What operators see

### Warning after saving

If the DIMAG transfer fails, a **yellow warning bar** appears after saving the
record:

> *«File was saved, but transfer to DIMAG failed. The administration has been
> notified.»*

This makes it immediately apparent that something is not right.

### Status badge per file

In the file list of a record (the «Files» tab) and in the expanded media view,
Anton shows a small badge per file:

| Badge | Status | Meaning |
|---|---|---|
| 🟢 **DIMAG** | ok | File arrived successfully in DIMAG |
| 🟡 **waiting for DIMAG** | pending | Transfer still running (queue job active) |
| 🔴 **DIMAG error** | failed | Transfer failed — the tooltip shows the error message |

The badge is visible only to **logged-in Anton users**, not to external
catalogue visitors. It is deliberately not built into gallery views (it would
disturb the public view).

## Admin notification

In the case of structural errors (expired password, DIMAG unreachable, missing
permissions), Anton automatically sends an email to the stored administration
address:

- **Who is notified:** the address from `setting('admin_email')` (or the tenant
  configuration default)
- **What it says:** error category, file ID, record ID, Anton URL
- **Throttling:** a separate rate limit bucket per error type
  (`email-exceptions:dimag:auth_failed`, `:permission_denied`, `:unreachable`,
  `:unknown`), 10 mails per minute per bucket. This means a storm of 401s does
  not block the alert budget for other problems.

## Error categories

`DimagIngestException::classifyMessage()` sorts incoming errors into four
categories:

| Category | Triggers (examples) |
|---|---|
| `auth_failed` | HTTP 401, "Access to DIMAG failed" |
| `permission_denied` | "Permission denied", "not writable" |
| `unreachable` | Timeout, connection refused, DNS errors |
| `unknown` | everything else |

The category appears in the mail subject and in the issue tracker entry (if the
feedback module is connected).

## Data model: `media_events`

Since v0.65.0, status events are stored in a dedicated table `media_events`
(append-only). Schema:

| Column | Content |
|---|---|
| `media_id` | FK to `media.id`, ON DELETE CASCADE |
| `event_type` | e.g. `dimag_upload`, `pdf_validation` |
| `status` | `ok` / `failed` / `info` |
| `category` | `dimag-ingest` / `pdf-validation` / nullable |
| `details` | JSON |
| `created_at` | Timestamp |

The table replaces the earlier `media.custom_properties.events[]` JSON blob,
which 5+ classes filled with differing schemas.

Helpers:

```php
MediumEvent::record($medium, $type, $status, $category, $details);
Media::ingestStatus(?string $category)  // → 'ok' | 'pending' | 'failed' | null
Media::latestIngestEvent(?string $category)  // → MediumEvent | null
```

`pending` is only returned for `category=dimag-ingest` if the file has
`original_location='inge'` but no events yet.

## Troubleshooting

| Symptom | Cause | Measure |
|---|---|---|
| All uploads are 🔴 with "401 Unauthorized" | DIMAG password rotated | Set the new password in the `.env`, restart the queue worker |
| Uploads stay 🟡 "waiting for DIMAG" | Queue worker is down | Check the supervisor: `supervisorctl status` |
| Badge missing entirely | Tenant is not a DIMAG tenant (`setting('cloud') !== 'inge'`) | As expected — the badge only appears with the inge cloud |
| Mail storm on repeated errors | The rate limit bucket does not take effect | Check the cache driver — the rate limit needs a working cache (Redis/DB, not `array`) |

## SIP status tab

In addition to the per-file status, since v0.65.0/v0.66.0 there is an admin tab
`/sip/status` under **SIP import → Status** (only with `cloud === 'inge'`),
which shows the current Inge URL and the token setup and offers a "Run
infrastructure check now" button. The same check is available as the command
`inge:check-infrastructure`.

## Related topics

- [Inge / DIMAG connection](inge.md) — basic configuration of the DIMAG cloud
- [SIP ingest (eCH-0160)](sip-ingest.md) — taking over SIP packages
- [Notifications](notifications.md) — if DIMAG events are additionally to be
  displayed as in-app notifications
