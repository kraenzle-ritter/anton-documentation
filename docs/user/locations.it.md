# Collocazioni

Una collocazione è il luogo fisico di conservazione dell'originale — magazzino,
deposito, locale, scaffale. Le collocazioni sono schede a sé stanti e si
gestiscono in **Admin → Collocazioni**.

!!! note "Non per il pubblico"
    La scheda di collocazione stessa è visibile esclusivamente all'utenza
    interna, a chi descrive e all'amministrazione, mai a persone esterne — dove
    si trovi un documento non riguarda il pubblico.

    Il **campo** «collocazione» di un'unità di descrizione è cosa distinta: le
    nuove installazioni vengono consegnate con il campo rimosso dai formulari
    pubblici (esterni), così che «Collocazione: …» non compaia nel catalogo
    pubblico. Le installazioni esistenti restano invariate — lì il campo va, se
    necessario, rimosso dai formulari esterni tramite i
    [formulari](../admin/forms.md).

## Registrare

La collocazione è volutamente essenziale e prevede solo quattro campi:

| Campo | Scopo |
|---|---|
| ID | assegnato automaticamente |
| Abbreviazione | forma breve, ad es. `M2` |
| Nome | in chiaro, ad es. «Magazzino 2, scaffale C» |
| Descrizione | testo libero |

Nessuna coordinata, nessun [dato di autorità](authorities.md). Dove si trova una collocazione nel magazzino, il suo livello, il posto superiore e la capacità, figura nel riquadro [Magazzino](#magazin) della sua pagina.

!!! note "Autorizzazione"
    Creare, modificare ed eliminare collocazioni presuppone il ruolo `editor`.
    L'utenza interna (`user_intern`) può consultarle — a differenza di attori,
    luoghi e parole chiave, le collocazioni non sono affatto pubbliche.

## Assegnare

Un'unità di descrizione viene assegnata alla collocazione nel campo
**collocazione**. Si trova nella sezione «documentazione collegata» ed è un
elenco di selezione.

Un'unità di descrizione ha al massimo **una** collocazione. Se il campo compaia
nella maschera dipende dal [set di formulari](forms.md) — per impostazione
predefinita lo recano unità archivistica, serie e unità documentaria, ma non
archivio e fondo.

!!! tip "Collocazione o dettaglio della collocazione?"
    Due campi dal nome simile non vanno confusi:

    - **Collocazione** — la scelta tra le collocazioni registrate, un vero e
      proprio collegamento. Su di essa si possono fare valutazioni.
    - **Collocazione (dettaglio)** — un campo di testo per indicazioni
      complementari, senza collegamento.

## Magazzino {#magazin}

Le collocazioni si possono strutturare in un magazzino: sala, scaffale, segmento, ripiano e scatola, o come l’archivio suddivide il proprio magazzino. Un archivio che non struttura le proprie collocazioni non nota nulla; un elenco piatto resta un elenco piatto.

**Definire i livelli.** In **Admin → Livelli del magazzino** l’amministrazione definisce i livelli, dall’alto in basso, con una denominazione per lingua. Un livello può essere contrassegnato come **contenitore**, ad esempio la scatola: un contenitore occupa tutta la sua capacità sul posto in cui si trova, pieno o vuoto. Un livello assegnato a dei posti non può essere eliminato.

**Creare posti.** La pagina di una collocazione contiene il riquadro **Magazzino** con percorso, livello, occupazione e livelli sottostanti. **Aggiungi un livello sottostante** crea una nuova collocazione al di sotto; Anton propone il livello successivo. **Modifica i dati del magazzino** permette di cambiare livello, posto superiore («Si trova in»), capacità in centimetri lineari e ordine. Un posto non può trovarsi in sé stesso né in uno dei propri livelli sottostanti.

**Percorso.** Ovunque una collocazione sia indicata compare il suo percorso, p. es. «Sala 1 › Scaffale 3 › Ripiano 4 › Scatola 17»: nell’unità di descrizione, nell’elenco di selezione della maschera e della modifica in blocco, nella mail d’ordine e nell’esportazione Excel completa.

**Occupazione.** Si conta l’estensione delle unità di descrizione assegnate al posto stesso, su tutti i livelli sottostanti: la loro estensione o, se non è registrata, l’estensione sottostante, come la mostra la pagina di dettaglio. Un fondo i cui fascicoli si trovano in scatole conta attraverso le scatole, non due volte. Un contenitore con capacità conta sul suo ripiano con tutta la capacità. Senza capacità Anton indica solo l’occupazione.

**Panoramica del magazzino.** In **Admin → Panoramica del magazzino** il magazzino appare come albero con l’occupazione e il numero di unità di descrizione per posto. La scheda **Posti liberi** elenca i posti con capacità in cui c’è ancora spazio, i più vuoti per primi, se si vuole di un solo livello e con un minimo.

**Assegnare in blocco.** Le unità di descrizione arrivano al loro posto tramite la modifica in blocco o la tabella Excel. La colonna `standort` accetta l’ID, la denominazione o il percorso, con `›`, `>` o `/` tra i livelli. Una denominazione portata da più posti, p. es. «Ripiano 4», viene respinta come ambigua invece di essere indovinata; un percorso inesistente non viene creato come nuova collocazione.

## Che cosa si trova in una collocazione

La pagina di dettaglio di una collocazione elenca le unità di descrizione assegnate a essa o a un posto sottostante: uno scaffale mostra anche ciò che si trova nelle sue scatole.

## Eliminare

Se a una collocazione sono ancora assegnate unità di descrizione, Anton rifiuta l’eliminazione e lo segnala. Le assegnazioni vanno prima rimosse. Allo stesso modo resta una collocazione sotto cui si trovano ancora dei posti; vanno prima eliminati o spostati.

## Segnature con collocazione

In alcuni archivi l'abbreviazione della collocazione entra a far parte della
[segnatura](identifiers.md). Se ciò è configurato, nella finestra «Creare nuove
schede» compare un campo di selezione aggiuntivo **collocazione**.

!!! note "Specifico dell'archivio"
    Questa funzione presuppone una formazione delle segnature programmata
    appositamente. Lo schema standard non utilizza la collocazione — lì il campo
    di selezione resterebbe senza effetto. Con Anton as a Service, k & r sa se
    la propria installazione disponga di una simile formazione delle segnature.
