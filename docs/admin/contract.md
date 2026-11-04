# Vertrag

Unter **Administration › Benutzer und Ausleihen › Vertrag** steht, was das Archiv gebucht hat, was es belegt und was es bestellt hat (seit v0.118.0, anton#805). Die Seite ist für die Gesamtverantwortung: Sehen und bestellen können nur Konten mit der Befugnis **Vertrag und Ansprechpersonen**, alle anderen sehen sie auch im Menü nicht.

## Was die Seite zeigt

- **Abo:** Stufe, seit wann, Laufzeit und Kündigung, Betrieb (Anton as a Service, eigener Server, DIMAG), dazu das nächste Abo mit Speicher und Preis.
- **Speicher:** gebucht und belegt. Gezählt werden die Master und die [behaltenen Fassungen](preservation.md#behaltene-originale), aus der Datenbank. Daneben steht das ganze Verzeichnis, wie es Anton nachts misst, mit Ansichtsbildern und Zwischenspeicher.
- **Module und Pakete:** je mit Stand (inbegriffen, gebucht, buchbar) und Preis.
- **Bestellungen** und **Nutzungsauszüge**.

Die Vertragsdaten pflegt Kränzle & Ritter in anton-ansible; Anton liest sie nur. Ohne hinterlegte Daten zeigt die Seite nur den Speicher.

## Bestellen

Buchen, Kündigen, eine Speicherstufe und der Wechsel zum nächsten Abo gehen als [Bestätigung per Mail](contacts.md#bestatigung-per-mail) an die Ansprechpersonen für die Gesamtverantwortung. Die Bestellung gilt, sobald eine von ihnen bestätigt; die Mail nennt Modul, Preis und den Hinweis auf die Bedingungen der Offerte. Kränzle & Ritter richtet danach ein, was bestellt ist, und führt die Vertragsdaten nach. Bis dahin steht das Modul als «bestellt».

Das Paket **Technische Betreuung** bucht man nicht hier, sondern mit dem [Erhaltungsauftrag](preservation-mandate.md) «Technische Betreuung»: Die Seite zeigt seinen Stand und verweist dorthin. Die Bestätigung des Auftrags gilt zugleich als Bestellung des Pakets, der Widerruf als Kündigung; die Gesamtverantwortung bestätigt also nur einmal.

Eine Speicherstufe nennt den Speicher insgesamt und den Preis insgesamt pro Jahr, wie ihn die Preisliste hat. Die Seite teilt ihn in Abo und Speicherpaket auf, zum Beispiel «500 GB Speicher insgesamt – CHF 7’500.– pro Jahr (Abo CHF 5’000.–, Speicherpaket CHF 2’500.–)».

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
  "plan": {"key": "standard", "label": {"de": "Standard"}, "since": "2024-01-01", "yearly": 3000,
           "term": {"de": "jährlich, Kündigung drei Monate vor Ablauf"}},
  "plans": [{"key": "basic", "label": "Basic", "gb": 5, "yearly": 1000},
            {"key": "standard", "label": "Standard", "gb": 50, "yearly": 3000},
            {"key": "pro", "label": "Pro", "gb": 250, "yearly": 5000}],
  "operating_model": "A",
  "show_prices": true,
  "storage": {"booked_gb": 50, "tiers": [{"gb": 100, "yearly": 4800}, {"gb": 500, "yearly": 7500}]},
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
| `plan.yearly` | Preis des Abos pro Jahr; damit teilt die Seite den Preis einer Speicherstufe in Abo und Speicherpaket auf |
| `plans` | die Abos in ihrer Reihenfolge, je mit `gb` und `yearly`; die Seite bietet das Abo nach dem jetzigen an |
| `storage.tiers` | bestellbare Speicherstufen: `gb` ist der Speicher insgesamt, `yearly` der Preis insgesamt pro Jahr nach der Preisliste (`anton_preise.xlsx`) |
| `technical_care` | der Posten, an dem der [Erhaltungsauftrag](preservation-mandate.md) «Technische Betreuung» hängt |
