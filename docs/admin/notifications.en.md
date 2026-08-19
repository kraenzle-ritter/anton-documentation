# Notifications

Anton has an internal notification system with which admins can send messages to the users of an installation. Notifications appear as a badge (bell with a counter) in the navigation bar and can be viewed by users and marked as read.

## Overview

- **Admins** can compose and send notifications via the web interface
- **k & r** can distribute notifications to all installations via the CLI (using Ansible)
- **Users** see unread notifications as a badge in the navigation
- Notifications can be addressed to **all users**, only to **editors & admins** or only to **admins**
- Title and text are **multilingual** (per configured locale)

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
php artisan notification:send --title="Update v0.54" --body="Neue Features." --all
```

### Multilingual

Title and text can be passed as JSON:

```bash
php artisan notification:send \
  --title='{"de":"Update v0.54","fr":"Mise à jour v0.54"}' \
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

- Table `notifications`: id, title (JSON), body (JSON), sender_id, source (local/system), audience (all/editors/admins)
- Table `notification_user`: pivot for the read status per user (notification_id, user_id, read_at)
- Notifications without a pivot entry for a user count as unread (lazy tracking)
