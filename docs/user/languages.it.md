# Configurazione delle lingue in Anton

## Panoramica

Anton supporta contenuti multilingue (DE, EN, FR e IT) per diversi campi (titolo, campi di testo, parole chiave ecc.). Questo documento descrive le impostazioni disponibili e fornisce raccomandazioni per la configurazione.

## Tipi di lingua

In Anton esistono due concetti distinti di «lingua»:

1. **Lingua dell'interfaccia** (`app.locale`): la lingua dell'interfaccia utente (menu, etichette, messaggi)
2. **Lingue dei contenuti** (`locales`): le lingue nelle quali possono essere registrati i dati archivistici

## Impostazione di sistema: `locales`

| Proprietà | Valore |
|------------|------|
| Tipo | Array |
| Scope | `localisation` |
| Esempio | `["de", "en", "fr"]` |

Definisce quali lingue sono disponibili per i campi traducibili.

**Importante:** la **prima lingua dell'array è la lingua principale** e viene utilizzata come ripiego quando per un'altra lingua non esiste alcun valore.

**Campi traducibili:**
- Titolo (AntonObject)
- Campi di testo (Note)
- Parole chiave (name, use_for)
- Luoghi (description)

## Impostazione utente: `show_all_locales_in_edit_forms`

| Proprietà | Valore |
|------------|------|
| Tipo | Booleano |
| Valore predefinito | `false` |
| Posizione | Profilo → Impostazioni → Modifica |

**Se attivata (`true`):**
- Nei formulari di modifica vengono visualizzati **campi di inserimento separati per ogni lingua configurata**
- Esempio: titolo (DE), titolo (EN), titolo (FR)

**Se disattivata (`false`):**
- Viene visualizzato **un solo campo** (per la lingua corrente dell'interfaccia)
- I valori già inseriti in altre lingue vengono mostrati a titolo informativo, ma non sono modificabili

## Lingua durante l'importazione

Un'importazione possiede una propria **lingua dei contenuti**, indipendente dalla lingua dell'interfaccia. Essa determina in quale lingua vengono scritti titoli, campi di testo e dati di autorità di nuova creazione — e in quale lingua Anton cerca attori, attrici e luoghi esistenti.

Fino alla v0.86.x l'importazione seguiva la lingua dell'interfaccia; chi aveva impostato l'inglese creava titoli inglesi con testo tedesco. Dalla **v0.87.0** la lingua viene scelta consapevolmente ed è visibile prima dell'esecuzione.

I campi traducibili possono essere indirizzati nell'importazione anche **per lingua** — `title_de`, `title_fr`, `scopecontent_it`. In questo modo si possono importare titoli multilingue e la tabella di aggiornamento di un archivio multilingue esce e rientra senza perdite.

Entrambi gli aspetti sono descritti in dettaglio in [Importazione → Lingua dei contenuti dell'importazione](import.md#lingua-dei-contenuti-dellimportazione).

## Comportamento di ripiego

Se per la lingua corrente non esiste alcun valore:
1. Anton utilizza il valore della **prima lingua** di `setting('locales')`
2. Se nemmeno lì è presente qualcosa: ricerca nelle ulteriori lingue configurate

Nella vista di dettaglio, a chi descrive viene indicato da quale lingua proviene il valore (ad es. «Titolo (DE)»).

## Raccomandazione: una lingua per campo

**La nostra raccomandazione è di salvare una sola lingua per campo** (`show_all_locales_in_edit_forms = false`).

### Motivi

1. **Coerenza**: se i titoli vengono registrati in più lingue, tutte le traduzioni devono essere mantenute. Quando l'originale cambia, le traduzioni spesso non vengono aggiornate.

2. **Standard archivistici**: nella pratica archivistica i documenti vengono normalmente descritti nella lingua originale, non tradotti.

3. **Ricercabilità**: la ricerca full text (colonna `full_text`) contiene tutte le versioni linguistiche. Ciò può produrre risultati confusi.

4. **Onere di manutenzione**: la gestione di dati multilingue richiede risorse notevolmente maggiori.

### Quando il multilinguismo ha senso

- Archivi con pubblico internazionale (ad es. raccolte scientifiche)
- Fondi con documenti in lingue diverse, in cui il titolo viene registrato nella lingua originale
- Istituzioni con un obbligo legale di multilinguismo

## Esempi di configurazione

### Archivio monolingue 

```php
// Setting: locales
["de"]
```
```php
// UserSettings
show_all_locales_in_edit_forms: false
```

### Archivio bilingue (DE/FR)

```php
// Setting: locales
["de", "fr"]
```
```php
// UserSettings (secondo le esigenze)
show_all_locales_in_edit_forms: false  // Raccomandato
```

### Archivio internazionale

```php
// Setting: locales
["en", "de", "fr", "it"]
```
```php
// UserSettings (per chi traduce)
show_all_locales_in_edit_forms: true
```
