# Notifications

Anton has an internal notification system with which admins can send messages to the users of an installation. Notifications appear as a badge (bell with a counter) in the navigation bar and can be viewed by users and marked as read.

## Overview

- **Admins** can compose and send notifications via the web interface
- **k & r** can distribute notifications to all installations via the CLI (using Ansible)
- **Users** see unread notifications as a badge in the navigation
- Notifications can be addressed to **all users**, only to **editors & admins** or only to **admins**
- Title and text are **multilingual** (per configured locale)

## Three tiers

Not every message has to announce itself. Anton distinguishes:

| Tier | Where | Announces itself |
|---|---|---|
| **Announcement** (`announcement`) | list and badge | yes — counts as unread |
| **Report** (`report`) | list only | no |
| **Changelog** | `/changelog` | no — English, technical, admins only |

The reason is measured: between v0.54.0 and v0.88.0 Anton sent 34 release notifications, one every 3.6 days. That many messages are no longer a channel but background noise — and the one message that really has to be read drowns in it.

Since then every release produces a **report**: it sits in the list, so that what changed stays on record, but it raises no badge. What announces itself is the **digest**, which gathers several reports — written when enough has accumulated, with no fixed cadence. Alongside it, the single message that is genuinely worth it.

A notification written by hand (web interface, `notification:send`) is always an announcement.

## Release reports

```bash
php artisan notification:release --env=besenval
```

Reads `documentation/anton_news_v{version}.md` for the deployed version and builds the report from it: title «Anton v0.93.0 — what is new», text from the opening paragraph plus links to the release notes and the changelog.

`anton:update` calls the command itself on deploy — by hand it is only needed to catch up. Where there is no news file for the version nothing is created; that is the normal case for a patch release. The minor's file is then looked up as well, so an installation that only updates at v0.94.2 does not miss the v0.94.0 report.

| Option | Description |
|---|---|
| `--release=` | Version, default: the deployed one. Not `--version` — that one belongs to Artisan |
| `--dry-run` | Only show what would be created |
| `--env=` | Target installation (slug) |
| `--all` | Across all installations |

## Digest

```bash
php artisan notification:digest --intro-file=digest.md --env=besenval
```

Gathers the installation's reports newer than the last digest and creates one announcement listing them. The opening paragraph is written by hand: what a run of releases means for an archive stands in no file to assemble it from.

It is built per installation from that installation's own reports — an archive that skipped releases is only told what concerns it.

| Option | Description |
|---|---|
| `--since=` | Version to summarise from (exclusive). Default: the last digest |
| `--intro=` / `--intro-file=` | Opening paragraph (mandatory) |
| `--audience=` | `all` (default), `editors`, `admins` |
| `--dry-run` | Only show what would be created |
| `--force` | Create even when a digest already exists for this version |
| `--env=` / `--all` | Target installation or all |

## Composing notifications (admin)

Under **Admin > Info > Notifications** (or directly `/admin/notifications`), admins see a list of all notifications of the installation.

With **New notification** (`/admin/notifications/create`) a notification can be composed:

- **Title** (mandatory, per language): short subject displayed in the list and in the badge context
- **Text** (optional, per language): detailed content, supports Markdown
- **Recipients**: who can see the notification:
    - *All users* — all logged-in users
    - *Editors & admins* — editors and admins only
    - *Admins only* — admins only

If the installation has several languages configured (`locales`), a title and a text field appear per language.

## Reading notifications (user)

All logged-in users see a **bell icon** in the navigation. If there are unread notifications, a red badge with the number appears.

Under `/notifications`, all notifications are listed (newest first). Unread notifications are highlighted visually (bold title, coloured border). Individual notifications can be marked as read, or all at once with **Mark all as read**.

When a notification is opened, it is automatically marked as read. The text is rendered as Markdown.

## Distributing notifications via the CLI

For distributing notifications to several installations (update notices, maintenance announcements, for example), the command `notification:send` is available:

### Single installation

```bash
php artisan notification:send --title="Wartung am 20.4." --body="Details folgen." --env=besenval
```

### All installations

```bash
php artisan notification:send --title="Neue Version" --body="Neue Features." --all
```

### Multilingual

Title and text can be passed as JSON:

```bash
php artisan notification:send \
  --title='{"de":"Neue Version","fr":"Nouvelle version"}' \
  --body='{"de":"Neue Features verfügbar.","fr":"Nouvelles fonctions disponibles."}' \
  --all
```

### Text from a file

```bash
php artisan notification:send --title="Wartungsarbeiten" --file=notification.md --env=besenval
```

### Restricting the recipients

```bash
php artisan notification:send --title="Intern" --audience=editors --env=besenval
```

Possible values for `--audience`: `all` (default), `editors`, `admins`.

### Options

| Option | Description |
|---|---|
| `--title=` | Title (mandatory). String or JSON for multilingual |
| `--body=` | Text (optional). String or JSON |
| `--file=` | Read the text from a Markdown file |
| `--audience=` | Recipients: `all`, `editors`, `admins` (default: `all`) |
| `--env=` | Target installation (slug) |
| `--all` | Send to all installations |

### Integration with Ansible

The command can be included in Ansible playbooks or as a step in `anton:update`, in order to distribute notifications automatically on deployment.

## Data model

- Table `notifications`: id, title (JSON), body (JSON), sender_id, source (local/system), audience (all/editors/admins), level (announcement/report), version
- Table `notification_user`: pivot for the read status per user (notification_id, user_id, read_at)
- Notifications without a pivot entry for a user count as unread (lazy tracking)
