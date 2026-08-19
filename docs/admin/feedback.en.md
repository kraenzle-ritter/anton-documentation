# Feedback form

Since **v0.55.0**, admins and superusers can send feedback to the development
team directly from within Anton. Every message automatically ends up as an issue
in Anton's GitHub repository, together with technical context.

Since **v0.58.0** the form runs on the same upload pipeline as Anton's other
input masks (with drag and drop / Cmd-V for screenshots).

## How it is used

A **«Feedback»** link is visible in the footer for admins and superusers.
Clicking it opens `/feedback`. The form has:

- **Title** — brief summary
- **Description** — Markdown allowed, running text
- **Screenshots** (optional) — drag and drop them into the form or paste them
  with **Cmd-V / Ctrl-V** anywhere on the page. The upload runs in the
  background as soon as the file is there.

After submission, Anton creates a GitHub issue in the
[`kraenzle-ritter/anton`](https://github.com/kraenzle-ritter/anton) repository.
The issue contains:

- title and description from the form
- the email address of the sending user (since v0.58.0; previously a manual SSH
  lookup was needed)
- the path called in Anton
- the Anton version (tag)
- the tenant slug
- technical context (browser, screen size, optional)

## Activation per tenant

By default the form is **switched off**. Three settings:

| Setting | Value | Meaning |
|---|---|---|
| `feedback_enabled` | `true`/`false` | Activates the form for the tenant |
| `feedback_roles` | Array of roles | Which roles see the link in the footer (e.g. `['admin', 'superuser']`) |
| `feedback_github_repo` | `owner/repo` | Target repository, default `kraenzle-ritter/anton` |

Additionally, per Anton installation **(env, not per tenant)**:

- `FEEDBACK_GITHUB_PAT` — personal access token with the `issues: write` scope
  on the target repo. A bot account is recommended, so that issues verifiably
  come from a clearly identifiable sender account.

## Screenshot configuration

Since v0.58.0, the upload constraints are configurable per tenant in the
database, without a code change:

- **Permitted file types** (default: `image/png`, `image/jpeg`, `image/webp`)
- **Maximum number** per feedback entry
- **Maximum size** per file

The former tenant-wide «screenshots off» switch (for intranet hosts such as ZH)
now runs on the same database mechanism as well — the old
`feedback_screenshots_enabled` setting is obsolete.

## Known peculiarities

- **The Windows Snipping Tool** triggered two identical images per issue before
  v0.58.0 (double paste). Since v0.58.0 the form responds to paste events with
  only one upload.
- **Attachments on GitHub** — all images are uploaded directly into the issue
  (not linked externally), so that they are still accessible years later.

## PAT rotation

GitHub PATs expire after one year. The current rotation is recorded in the
internal calendar; see the memory note `reference_feedback_bot_account`
(internal).

If the PAT expires, issue creation fails silently and the feedback only remains
in the Anton database — no loss, but no GitHub issue. An admin audit
(`/admin/feedback/pending`) shows the entries that got stuck.

## Related topics

- [Notifications](notifications.md) — if feedback replies are to flow back into
  the Anton UI as notifications (a separate feature)
- [API authentication](../api/authentication.md) — if custom tools are to send
  feedback via the API instead of through the UI form
