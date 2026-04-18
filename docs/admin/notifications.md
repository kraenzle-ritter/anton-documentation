# Nachrichten (Notifications)

Anton verfügt über ein internes Nachrichten-System, mit dem Admins Mitteilungen an die Benutzer:innen einer Installation senden können. Nachrichten erscheinen als Badge (Glocke mit Zähler) in der Navigationsleiste und können von den Benutzer:innen eingesehen und als gelesen markiert werden.

## Übersicht

- **Admins** können Nachrichten über die Web-Oberfläche verfassen und versenden
- **k & r** kann Nachrichten über die CLI an alle Installationen verteilen (via Ansible)
- **Benutzer:innen** sehen ungelesene Nachrichten als Badge in der Navigation
- Nachrichten können an **alle User**, nur an **Editors & Admins** oder nur an **Admins** gerichtet werden
- Titel und Text sind **mehrsprachig** (pro konfigurierter Locale)

## Nachrichten verfassen (Admin)

Unter **Admin > Info > Notifications** (oder direkt `/admin/notifications`) sehen Admins eine Liste aller Nachrichten der Installation.

Mit **Neue Nachricht** (`/admin/notifications/create`) kann eine Nachricht verfasst werden:

- **Titel** (Pflichtfeld, pro Sprache): Kurzer Betreff, der in der Liste und im Badge-Kontext angezeigt wird
- **Text** (optional, pro Sprache): Ausführlicher Inhalt, unterstützt Markdown
- **Adressaten**: Wer die Nachricht sehen kann:
    - *Alle User* — alle angemeldeten Benutzer:innen
    - *Editors & Admins* — nur Editors und Admins
    - *Nur Admins* — nur Admins

Hat die Installation mehrere Sprachen konfiguriert (`locales`), erscheint pro Sprache ein Titel- und ein Textfeld.

## Nachrichten lesen (User)

Alle angemeldeten Benutzer:innen sehen in der Navigation ein **Glocken-Symbol**. Gibt es ungelesene Nachrichten, erscheint ein roter Badge mit der Anzahl.

Unter `/notifications` werden alle Nachrichten aufgelistet (neueste zuerst). Ungelesene Nachrichten sind visuell hervorgehoben (fetter Titel, farbiger Rand). Einzelne Nachrichten können als gelesen markiert werden, oder alle auf einmal mit **Alle als gelesen markieren**.

Beim Öffnen einer Nachricht wird sie automatisch als gelesen markiert. Der Text wird als Markdown gerendert.

## Nachrichten über die CLI verteilen

Für die Verteilung von Nachrichten an mehrere Installationen (z.B. Update-Hinweise, Wartungsankündigungen) steht der Befehl `notification:send` zur Verfügung:

### Einzelne Installation

```bash
php artisan notification:send --title="Wartung am 20.4." --body="Details folgen." --env=besenval
```

### Alle Installationen

```bash
php artisan notification:send --title="Update v0.54" --body="Neue Features." --all
```

### Mehrsprachig

Titel und Text können als JSON übergeben werden:

```bash
php artisan notification:send \
  --title='{"de":"Update v0.54","fr":"Mise à jour v0.54"}' \
  --body='{"de":"Neue Features verfügbar.","fr":"Nouvelles fonctions disponibles."}' \
  --all
```

### Text aus Datei

```bash
php artisan notification:send --title="Wartungsarbeiten" --file=notification.md --env=besenval
```

### Adressaten einschränken

```bash
php artisan notification:send --title="Intern" --audience=editors --env=besenval
```

Mögliche Werte für `--audience`: `all` (Default), `editors`, `admins`.

### Optionen

| Option | Beschreibung |
|---|---|
| `--title=` | Titel (Pflicht). String oder JSON für mehrsprachig |
| `--body=` | Text (optional). String oder JSON |
| `--file=` | Text aus Markdown-Datei lesen |
| `--audience=` | Adressaten: `all`, `editors`, `admins` (Default: `all`) |
| `--env=` | Ziel-Installation (Slug) |
| `--all` | An alle Installationen senden |

### Integration mit Ansible

Der Befehl kann in Ansible-Playbooks oder als Schritt in `anton:update` eingebunden werden, um Nachrichten beim Deployment automatisch zu verteilen.

## Datenmodell

- Tabelle `notifications`: id, title (JSON), body (JSON), sender_id, source (local/system), audience (all/editors/admins)
- Tabelle `notification_user`: Pivot für Gelesen-Status pro User (notification_id, user_id, read_at)
- Nachrichten ohne Pivot-Eintrag für einen User gelten als ungelesen (lazy tracking)
