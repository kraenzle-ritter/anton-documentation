# Media

All'importazione di media Anton crea normalmente una copia di consultazione. Questa è ottimizzata per l'uso sul web. Se non sono bloccati per altri motivi, gli utenti esterni hanno accesso solo a questa versione web.

## Formati dei media

In linea di principio è consigliabile utilizzare come formati di partenza il minor numero possibile di formati diversi. Ciò rende la gestione e la manutenzione a lungo termine più chiare e più semplici. Esistono inoltre formati di file più adatti all'archiviazione di altri. Su questo tema forniscono informazioni numerosi archivi pubblici e servizi specializzati nella conservazione digitale a lungo termine.

Per i seguenti formati Anton produce copie di consultazione; un'estensione è facilmente implementabile in qualsiasi momento all'occorrenza. L'importazione di altri formati è possibile, ma dovrebbe se possibile essere testata. Alcuni formati non vengono convertiti (ad es. DOCX, XLSX, TXT, ZIP).

### Foto  
- TIFF  
- JPEG2000  
- PNG  
- JPEG

### Documenti  
- PDF/A
- PDF

### Video
- MP4  
- Quicktime

### Audio
- WAF  
- MPEG  
- MP3  

## Metadati tecnici (AV)

Al caricamento Anton legge automaticamente le proprietà tecniche tramite
`ffprobe` e le mostra nella scheda dei media della pagina di dettaglio: durata,
risoluzione, codec, bitrate, frequenza di campionamento, rapporto d'aspetto —
nella misura in cui hanno senso per il file in questione. Per le fotografie viene
mostrata solo la dimensione dell'immagine, per l'audio nessuna risoluzione e così
via.

I valori vengono forniti anche nell'esportazione RDF (profilo Memobase) come
proprietà EBUcore, vedi [Esportazione RDF](../admin/download-rdf.md). Per i media
più vecchi già presenti i campi possono essere completati a posteriori tramite
backfill — vedi
[`media:extract-av-metadata`](../admin/console-commands.md#mediaextract-av-metadata).


## Modificare l'ordine dei media

Dalla **v0.87.0** l'ordine dei media di un'unità di descrizione può essere
modificato senza doverli eliminare e caricare di nuovo.

Nella **scheda dei media** dell'unità di descrizione ogni media dispone di una
coppia di frecce (↑ ↓). Un clic sposta il media di una posizione all'interno
della propria raccolta. Per il primo e per l'ultimo media la rispettiva freccia
è disattivata.

L'ordine vale per la visualizzazione nel catalogo, nella galleria e nel
visualizzatore — è lo stesso ordine attribuito al momento del caricamento.

Immagini e documenti vengono ordinati separatamente: un'immagine non può
scambiare il proprio posto con un documento.

Il riordino è una modifica visibile e viene registrato di conseguenza sulla
scheda (data di modifica, persona che ha modificato, protocollo delle modifiche).
Richiede la stessa autorizzazione necessaria per eliminare un media.


## Mettere a disposizione i media originali
Per mettere a disposizione della clientela i media originali si apre la scheda dei media in un'unità di descrizione:

![Scheda dei media](images/transfer-ordner-1.png)
 
Lì fare clic sul pulsante «Copia il master nella cartella di trasferimento».

![Copia il master nella cartella di trasferimento](images/transfer-ordner-2.png)

Copiare il link facendo clic su «Copia il link negli appunti».

![Copia il master nella cartella di trasferimento](images/transfer-ordner-3.png)

Inviare il link alla persona interessata per e-mail. Il link è valido una settimana, dopodiché il file copiato viene eliminato automaticamente.
