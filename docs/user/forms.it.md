# Formulari e campi

Anton non impone uno schema di campi fisso. Quali campi abbia un'unità di
descrizione, in quale ordine compaiano e come si chiamino lo stabilisce ogni
archivio. Ciò spiega perché le maschere abbiano un aspetto diverso da archivio
ad archivio — e perché gli esempi di questa documentazione possano discostarsi
dalla propria installazione.

## Set di formulari

Un **set di formulari** raggruppa cinque formulari per la stessa cosa:

| Formulario | A che cosa serve |
|---|---|
| Interno — Modifica | La maschera di descrizione |
| Interno — Dettaglio | La vista di dettaglio per le persone autenticate |
| Interno — Elenco | L'elenco dei risultati per le persone autenticate |
| Esterno — Dettaglio | La vista di dettaglio per il pubblico |
| Esterno — Elenco | L'elenco dei risultati per il pubblico |

La separazione interno/esterno è il motivo per cui chi è esterno vede meno
dell'archivio stesso: un campo compare solo se figura nel rispettivo formulario.
Un formulario di modifica per il pubblico non esiste.

I set di formulari esistono non solo per le unità di descrizione, ma anche per
[attori e attrici](actors.md), [luoghi](places.md),
[parole chiave](keywords.md) e collocazioni.

## Quale set di formulari vale?

Anton decide in questo ordine:

1. Se nella scheda il campo **set di formulari** è compilato, vale quello.
2. Altrimenti vale il set di formulari che porta lo stesso nome del
   [livello di descrizione](hierarchy.md) — per un'unità archivistica, quindi,
   «file».
3. Altrimenti vale il set standard.

Il campo **set di formulari** si trova in cima alla maschera di descrizione e di
regola resta vuoto. È la via d'uscita per i casi particolari: se un fondo
contiene fotografie che richiedono campi diversi dal resto, per esse si può
creare un set di formulari proprio e assegnarlo in modo mirato.

## Campi

Un campo compare solo se figura nel formulario **e** ha un valore — i campi
vuoti vengono nascosti nella vista di dettaglio, non mostrati come riga vuota.
Nella maschera di modifica, invece, sono sempre visibili.

Lo stesso campo si comporta diversamente a seconda della vista: ciò che in
modifica è un campo di inserimento o un elenco di selezione, nella vista di
dettaglio compare come semplice testo.

Le **sezioni** su sfondo grigio suddividono la maschera. Non sono esse stesse
campi; una sezione senza campi visibili viene omessa del tutto.

## Testi di aiuto sui campi

A un campo può essere associato un testo di aiuto — la regola di descrizione
propria dell'archivio per quel campo. Se è presente, compare nella maschera di
modifica come una piccola indicazione direttamente sotto il campo di
inserimento.

Questa visualizzazione in linea può essere attivata e disattivata da ciascuna
persona nel proprio profilo; per impostazione predefinita è **disattivata**.
Indipendentemente da ciò, tutti i testi di aiuto sono consultabili insieme nella
pagina di aiuto **Anton Fields** dell'applicazione.

## Modificare

I set di formulari e i formulari si gestiscono in **Admin → Formulari** e
**Admin → Tipi di formulario**. Lì è possibile aggiungere, rimuovere,
riordinare e rinominare i campi per ciascun formulario — l'etichetta di un campo
può quindi essere diversa nella maschera di modifica rispetto alla vista di
dettaglio. Quali campi siano complessivamente disponibili è mostrato dalla
pagina di aiuto **Anton Fields** dell'applicazione.
