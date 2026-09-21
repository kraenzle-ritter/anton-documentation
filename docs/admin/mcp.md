# KI-Assistenten (MCP)

Anton stellt den öffentlichen Katalog als **MCP-Server** bereit: Ein
KI-Assistent (Claude, ChatGPT, Copilot …) wird von der Benutzerin oder vom
Benutzer angebunden und recherchiert dann selbständig im Katalog. Wie das auf
der Seite der Benutzer:innen aussieht, beschreibt
[KI-Assistenten anbinden](../user/mcp.md).

Die Richtung ist umgekehrt zur [KI-Erschliessung](ai-cataloging.md): Anton ruft
kein Sprachmodell auf, braucht keinen Schlüssel und verursacht keine
Modellkosten. Der Assistent gehört der Person, die ihn anbindet.

## Aktivierung

Die Schnittstelle ist **standardmässig aus**. Zwei Einstellungen müssen gesetzt
sein:

1. **`mcp_enabled`** — der Schalter für die Schnittstelle. Unter
   **Einstellungen** für Admins änderbar. Die Einstellung entsteht mit
   `anton:update`; vorher ist sie in der Liste nicht zu finden.
2. **`public_access`** — der Katalog muss ohne Anmeldung zugänglich sein. Ist er
   es nicht, bleibt die Schnittstelle zu, auch wenn `mcp_enabled` gesetzt ist:
   Wer im Browser nichts sieht, soll über einen Assistenten nicht mehr sehen.

Solange eine der beiden fehlt, antwortet `/api/mcp` mit 404.

Prüfen lässt sich die Schnittstelle von der Kommandozeile aus:

```bash
curl -s -X POST https://archiv.example.ch/api/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

Die Antwort listet sechs Werkzeuge.

## Was ausgegeben wird

Die Schnittstelle ist **anonym** und zeigt ausschliesslich die öffentliche
Sicht — dieselbe Regel wie für Gäste im Browser, ohne eigene Rechteprüfung
daneben:

- Verzeichnungen im Status «Final» (oder ohne Status), deren Feld **Gesperrt**
  nicht gesetzt ist. Bei untergeordneten Datensätzen und Zählungen fehlen die
  gesperrten spurlos.
- Die Felder des **externen Detailformulars** — was die öffentliche Detailseite
  zeigt, gibt auch die Schnittstelle aus.
- Dokumente und deren Volltext nur bei abgelaufener
  [Schutzfrist](protection-periods.md) und nicht unbefristet gesperrten Medien.
- Keine privaten Akteur:innen.

Ein Konto hilft nicht weiter: Auch eine angemeldete Mitarbeiterin sieht über die
Schnittstelle nur die öffentliche Sicht. Zugriff auf interne Bestände über ein
Konto ist für einen späteren Ausbau vorgesehen.

!!! warning "Vor dem Einschalten"
    Ein Assistent fragt in Minuten ab, wofür ein Mensch Wochen bräuchte. Was
    heute nur theoretisch öffentlich ist — ein vergessener Entwurf im Status
    «Final», ein Textfeld im externen Formular, das intern gemeint war —
    wird damit tatsächlich gelesen. Vor dem Einschalten lohnt ein Blick auf die
    öffentliche Detailseite einiger Datensätze und auf die Felder des externen
    Detailformulars.

## Anfragen begrenzen

Pro Adresse sind **60 Anfragen pro Minute** zugelassen; darüber antwortet die
Schnittstelle mit 429. Eine Recherche braucht meist ein paar Dutzend Aufrufe.
Der Wert steht in `config/ratelimiting.php` unter `mcp`; `0` hebt die Grenze
auf.

## Betrieb hinter Anubis und Cookie-Sperre

Ein MCP-Client schickt einzelne Anfragen ohne Cookie und ohne Browser — genau
das Muster, das Anubis und die Cookie-Sperre abweisen. Der Pfad `/api/mcp` muss
deshalb an beiden vorbeigeführt werden, wie der OAI-Endpunkt. Sonst ist der
Schalter gesetzt und die Schnittstelle trotzdem unerreichbar.
