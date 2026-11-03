# Vertrag

Unter **Administration › Benutzer und Ausleihen › Vertrag** steht, was das Archiv gebucht hat, was es belegt und was es bestellt hat (seit v0.118.0, anton#805). Alle Admins sehen die Seite; bestellen können Konten mit der Befugnis **Vertrag und Ansprechpersonen**.

## Was die Seite zeigt

- **Abo:** Stufe, seit wann, Laufzeit und Kündigung, Betrieb (Anton as a Service, eigener Server, DIMAG).
- **Speicher:** gebucht und belegt. Gezählt werden die Master und die [behaltenen Fassungen](preservation.md#behaltene-originale), aus der Datenbank. Daneben steht das ganze Verzeichnis, wie es Anton nachts misst, mit Ansichtsbildern und Zwischenspeicher.
- **Module und Pakete:** je mit Stand (inbegriffen, gebucht, buchbar) und Preis.
- **Bestellungen** und **Nutzungsauszüge**.

Die Vertragsdaten pflegt Kränzle & Ritter in anton-ansible; Anton liest sie nur. Ohne hinterlegte Daten zeigt die Seite nur den Speicher.

## Bestellen

Buchen, Kündigen und eine Speicherstufe gehen als [Bestätigung per Mail](contacts.md#bestatigung-per-mail) an die Ansprechpersonen für die Gesamtverantwortung. Die Bestellung gilt, sobald eine von ihnen bestätigt; die Mail nennt Modul, Preis und den Hinweis auf die Bedingungen der Offerte. Kränzle & Ritter richtet danach ein, was bestellt ist, und führt die Vertragsdaten nach. Bis dahin steht das Modul als «bestellt».

## Nutzungsauszug

Jeden Monat hält Anton einen Nutzungsauszug fest: belegter und gebuchter Speicher, Zahl der Medien und Konten, Kosten der [KI-Erschliessung](ai-cataloging.md) im Monat, Abo und was in Kraft war. Ein Monat wird einmal geschrieben und danach nicht mehr geändert. Die Auszüge stehen auf der Seite und lassen sich als CSV herunterladen; die Buchhaltung von Kränzle & Ritter holt sie über `GET /api/usage-statements`.

```bash
php artisan contract:usage-statement --env=<slug>                 # Vormonat
php artisan contract:usage-statement --env=<slug> --month=2026-10
```

## Für den Betrieb: die Vertragsdatei

anton-ansible legt die Daten je Installation als `customers/<slug>/contract.json` ab (anderer Ort: `CONTRACT_FILE`). Bezeichnungen und Beschreibungen sind ein Text oder je Sprache angegeben. Eine Datei, die nicht dem Schema entspricht, gilt als nicht vorhanden; das Protokoll nennt den Grund.

```json
{
  "schema": 1,
  "updated": "2026-11-03",
  "plan": {"key": "pro", "label": {"de": "Pro"}, "since": "2024-01-01",
           "term": {"de": "jährlich, Kündigung drei Monate vor Ablauf"}},
  "operating_model": "A",
  "show_prices": true,
  "storage": {"booked_gb": 50, "tiers": [{"gb": 100, "yearly": 300}]},
  "items": [
    {"key": "oai", "label": "OAI-PMH", "status": "included", "bookable": true, "price": {"yearly": 500}},
    {"key": "sru", "label": "Archives Online", "status": "available", "bookable": true, "price": {"once": 2500, "yearly": 500}},
    {"key": "technical_care", "label": "Technische Betreuung", "status": "active", "since": "2026-11-03", "bookable": true}
  ]
}
```

| Feld | Bedeutung |
|---|---|
| `status` | `included` (im Grundangebot oder im Abo), `active` (gebucht), `available` (buchbar) |
| `bookable` | ob sich der Posten auf der Seite buchen oder kündigen lässt |
| `price.once`, `price.yearly` | CHF; ohne Angabe «nach Offerte» |
| `storage.booked_gb` | gebuchter Speicher; ohne Datei gilt die Einstellung `maximum_storage` |
| `technical_care` | der Posten, an dem der [Erhaltungsauftrag](preservation-mandate.md) «Technische Betreuung» hängt |
