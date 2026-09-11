# Nachrichten (Notifications)

Anton verfügt über ein internes Nachrichten-System, mit dem Admins Mitteilungen an die Benutzer:innen einer Installation senden können. Nachrichten erscheinen als Badge (Glocke mit Zähler) in der Navigationsleiste und können von den Benutzer:innen eingesehen und als gelesen markiert werden.

## Übersicht

- **Admins** können Nachrichten über die Web-Oberfläche verfassen und versenden
- **k & r** kann Nachrichten über die CLI an alle Installationen verteilen (via Ansible)
- **Benutzer:innen** sehen ungelesene Nachrichten als Badge in der Navigation
- Nachrichten können an **alle User**, nur an **Editors & Admins** oder nur an **Admins** gerichtet werden
- Titel und Text sind **mehrsprachig** (pro konfigurierter Locale)

## Drei Stufen

Nicht jede Nachricht muss sich melden. Anton unterscheidet:

| Stufe | Wo | Meldet sich |
|---|---|---|
| **Mitteilung** (`announcement`) | Liste und Badge | ja — zählt als ungelesen |
| **Bericht** (`report`) | nur in der Liste | nein |
| **Changelog** | `/changelog` | nein — englisch, technisch, nur Admins |

Der Grund ist gemessen: zwischen v0.54.0 und v0.88.0 hat Anton 34 Release-Mitteilungen verschickt, eine alle 3,6 Tage. So viele Meldungen sind kein Nachrichtenkanal mehr, sondern Grundrauschen — und darin geht die eine Mitteilung unter, die wirklich gelesen werden muss.

Seither entsteht pro Release ein **Bericht**: er steht in der Liste, damit nachvollziehbar bleibt, was sich geändert hat, erzeugt aber kein Badge. Was sich meldet, ist der **Digest**, der mehrere Berichte zusammenfasst — geschrieben, wenn genug zusammengekommen ist, ohne festen Takt. Dazu die einzelne Mitteilung, die es wirklich wert ist.

Eine von Hand verfasste Nachricht (Web-Oberfläche, `notification:send`) ist immer eine Mitteilung.

## Release-Berichte

```bash
php artisan notification:release --env=besenval
```

Liest `documentation/anton_news_v{version}.md` der ausgerollten Version und legt daraus den Bericht an: Titel «Anton v0.93.0 — was neu ist», Text aus dem Einleitungsabsatz plus Verweise auf die Release-Notes und das Changelog.

`anton:update` ruft den Befehl beim Ausrollen selbst — von Hand nötig ist er nur zum Nachholen. Gibt es keine News-Datei zur Version, entsteht nichts; das ist der Normalfall eines Patch-Releases. Gesucht wird dann noch die Datei des zugehörigen Minors, damit eine Installation, die erst bei v0.94.2 aktualisiert, den Bericht zu v0.94.0 nicht verpasst.

| Option | Beschreibung |
|---|---|
| `--release=` | Version, Vorgabe: die ausgerollte. Nicht `--version` — das gehört Artisan |
| `--dry-run` | Nur zeigen, was entstehen würde |
| `--env=` | Ziel-Installation (Slug) |
| `--all` | Über alle Installationen |

## Digest

```bash
php artisan notification:digest --intro-file=digest.md --env=besenval
```

Sammelt die Berichte der Installation, die neuer sind als der letzte Digest, und legt eine Mitteilung mit der Liste an. Der einleitende Absatz kommt von Hand: was eine Reihe von Releases für ein Archiv bedeutet, steht in keiner Datei, aus der man es zusammensetzen könnte.

Gebaut wird pro Installation aus deren eigenen Berichten — ein Archiv, das Releases übersprungen hat, bekommt nur, was es betrifft.

| Option | Beschreibung |
|---|---|
| `--since=` | Version, ab der zusammengefasst wird (ausschliesslich). Vorgabe: der letzte Digest |
| `--intro=` / `--intro-file=` | Einleitender Absatz (Pflicht) |
| `--audience=` | `all` (Default), `editors`, `admins` |
| `--dry-run` | Nur zeigen, was entstehen würde |
| `--force` | Auch anlegen, wenn zu dieser Version schon ein Digest vorliegt |
| `--env=` / `--all` | Ziel-Installation oder alle |

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
php artisan notification:send --title="Neue Version" --body="Neue Features." --all
```

### Mehrsprachig

Titel und Text können als JSON übergeben werden:

```bash
php artisan notification:send \
  --title='{"de":"Neue Version","fr":"Nouvelle version"}' \
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

- Tabelle `notifications`: id, title (JSON), body (JSON), sender_id, source (local/system), audience (all/editors/admins), level (announcement/report), version
- Tabelle `notification_user`: Pivot für Gelesen-Status pro User (notification_id, user_id, read_at)
- Nachrichten ohne Pivot-Eintrag für einen User gelten als ungelesen (lazy tracking)
