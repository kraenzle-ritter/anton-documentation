# Contract

Under **Administration › Users and loans › Contract** the archive sees what it has booked, what it uses and what it ordered (since v0.118.0, anton#805). The page is for the overall responsibility: only accounts holding **Contract and contacts** see it and order there; everyone else does not see it in the menu either.

## What the page shows

- **Plan:** tier, since when, term and notice, operation (Anton as a Service, own server, DIMAG), and the next plan with its storage and price.
- **Storage:** booked and in use. Counted are the masters and the [kept versions](preservation.md#behaltene-originale), from the database. Beside it stands the whole directory as Anton measures it at night, with derivatives and caches.
- **Modules and packages:** each with its status (included, booked, available) and price.
- **Orders** and **usage statements**.

Kränzle & Ritter keeps the contract data in anton-ansible; Anton only reads them. Without data on file the page shows the storage only.

## Ordering

Booking, cancelling, a storage tier and the switch to the next plan go as a [confirmation by mail](contacts.md#confirmation-by-mail) to the contact persons for the overall responsibility. The order holds once one of them confirms; the mail names the module, the price and refers to the terms of the offer. Kränzle & Ritter then sets up what was ordered and updates the contract data. Until then the module shows as «ordered».

The package **Technical care** is not booked here but with the [preservation mandate](preservation-mandate.md) «Technical care»: the page shows its state and links there. Confirming the mandate counts as ordering the package, revoking it as cancelling; the overall responsibility confirms once.

A storage tier names the storage in all and its price in all per year, as the price list has it. The page splits it into plan and storage package, for instance «500 GB storage in all – CHF 7’500.– per year (plan CHF 5’000.–, storage package CHF 2’500.–)».

## Usage statement

Every month Anton records a usage statement: storage in use and booked, number of media and accounts, the month's cost of [AI cataloguing](ai-cataloging.md), the plan and what was in force. A month is written once and not changed afterwards. The statements are on the page and can be downloaded as CSV; the accounts of Kränzle & Ritter fetch them over `GET /api/usage-statements`.

```bash
php artisan contract:usage-statement --env=<slug>                 # previous month
php artisan contract:usage-statement --env=<slug> --month=2026-10
```

## For operations: the contract file

anton-ansible places the data per installation as `customers/<slug>/contract.json` (elsewhere: `CONTRACT_FILE`). Labels and descriptions are a text or given per locale. A file that does not match the schema counts as missing; the log names the reason.

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

| Field | Meaning |
|---|---|
| `status` | `included` (in the base offer or the plan), `active` (booked), `available` (can be booked) |
| `bookable` | whether the item can be booked or cancelled on the page |
| `price.once`, `price.yearly` | CHF; without, «as offered» |
| `storage.booked_gb` | booked storage; without a file the setting `maximum_storage` applies |
| `plan.yearly` | the plan's price per year; with it the page splits a storage tier's price into plan and storage package |
| `plans` | the plans in their order, each with `gb` and `yearly`; the page offers the one after the current plan |
| `storage.tiers` | storage tiers that can be ordered: `gb` is the storage in all, `yearly` its price in all per year from the price list (`anton_preise.xlsx`) |
| `technical_care` | the item the [preservation mandate](preservation-mandate.md) «Technical care» depends on |
