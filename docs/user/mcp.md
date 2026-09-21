# KI-Assistenten anbinden (MCP)

Ein KI-Assistent wie Claude oder ChatGPT kann direkt im öffentlichen Katalog
eines Archivs recherchieren: Bestände überblicken, suchen, Datensätze lesen, im
Bestandsbaum navigieren und aus den Volltexten der Digitalisate zitieren. Die
Verbindung läuft über das **Model Context Protocol (MCP)**, einen offenen
Standard, den die gängigen Assistenten unterstützen.

Der Assistent antwortet dann nicht mehr aus dem, was er beim Training
aufgeschnappt hat, sondern aus dem Katalog — mit Signatur und Link zu jedem
Datensatz, auf den er sich stützt.

!!! note "Nur wo das Archiv es eingeschaltet hat"
    Die Schnittstelle ist pro Archiv freizuschalten und steht nur Archiven mit
    öffentlichem Katalog zur Verfügung. Antwortet die Adresse mit «Not Found»,
    ist sie dort nicht in Betrieb.

## Was der Assistent sieht

Genau das, was ohne Anmeldung auch im Browser sichtbar ist: Verzeichnungen im
Status «Final», die nicht [gesperrt](access.md) sind. Die Dokumente und ihr
Volltext nur, wenn die Schutzfrist abgelaufen ist. Private Akteur:innen,
interne Textfelder und gesperrte Medien bleiben aussen vor.

Eine Anmeldung gibt es nicht und braucht es nicht — auch wer bei Anton ein Konto
hat, sieht über die Schnittstelle nur die öffentliche Sicht.

!!! warning "Was der Assistent liest, liest sein Anbieter mit"
    Alles, was die Schnittstelle zurückgibt, geht an den Anbieter des
    Assistenten (Anthropic, OpenAI, Microsoft …). Das sind ausschliesslich
    öffentliche Daten — aber es ist gut, es zu wissen.

## Adresse

```
https://<Adresse des Archivs>/api/mcp
```

Also zum Beispiel `https://archiv.example.ch/api/mcp`.

## Einrichten

### Claude (claude.ai und Claude Desktop)

**Einstellungen → Connectors → Custom Connector hinzufügen**, einen Namen
vergeben (etwa den Archivnamen) und die Adresse eintragen. Eine
Authentifizierung ist nicht einzurichten. Ob eigene Connectors zur Verfügung
stehen, hängt vom Abo ab.

### Claude Code

```bash
claude mcp add --transport http archiv https://archiv.example.ch/api/mcp
```

### ChatGPT, Microsoft Copilot und andere

Jeder Assistent, der entfernte MCP-Server über «Streamable HTTP» und ohne
Anmeldung einbinden kann, funktioniert. Wo die Einstellung liegt, ist je nach
Produkt und Abo verschieden; massgeblich ist die Anleitung des Anbieters.

## Was der Assistent damit tun kann

| Werkzeug | Zweck |
|---|---|
| `holdings_overview` | Welche Bestände gibt es? Archive, Bestandsgruppen und Bestände mit Signatur, Titel und Datierung |
| `search_records` | Suche in den Verzeichnungen — Titel, Textfelder, Akteur:innen, Orte, Schlagwörter |
| `search_media_texts` | Suche in den Volltexten der Digitalisate; liefert Textstellen rund um den Treffer |
| `read_record` | Ein Datensatz mit allen öffentlichen Feldern, verknüpften Normdaten und Dokumenten; den Volltext seitenweise |
| `navigate_tree` | Übergeordnete und untergeordnete Datensätze, Nachbarn |
| `lookup_authority` | Akteur:innen, Orte und Schlagwörter mit Normdatenverweisen (GND, Wikidata …) und den verknüpften Datensätzen |

Der Assistent wählt die Werkzeuge selbst. Man fragt einfach:

- «Was enthält das Archiv?»
- «Was hat die Maurmer Post über die Gründung des FC Maur berichtet? Zitiere die Stellen.»
- «Welche Unterlagen gibt es zum Bau des Schulhauses, und wo stehen sie im Bestand?»

## Grenzen

- **Suchbegriffe unter drei Buchstaben** findet der Index schlecht. Abkürzungen
  am besten als Phrase und zusammen mit einem längeren Wort suchen lassen.
- **Texterkennung (OCR) ist nicht fehlerfrei.** Findet ein Wort nichts, hilft
  oft ein Wortanfang mit `*` oder eine andere Schreibweise.
- **Nur Lesen.** Bestellen, Ändern oder Anlegen geht über die Schnittstelle
  nicht.
- **Anzahl Anfragen:** 60 pro Minute und Adresse. Eine Recherche braucht
  meist ein paar Dutzend.

Die Antworten des Assistenten bleiben seine eigenen. Was zählt, ist der
verlinkte Datensatz — im Zweifel dort nachsehen.
