# Schema dell'infrastruttura server di Anton

```mermaid
---
config:
  theme: redux
  layout: elk
---
flowchart TB
    subgraph prod[" "]
        U["SERVER ANTON"]
        UB[Backup locale cifrato]
    end

    A["Server di backup 1 (RAID 1)"]
    L["Server di backup 2 (RAID 1)"]
    G[Monitoraggio]
    E[Avvisi di errore via e-mail]
    %% Collegamenti di backup
    U --> UB
    UB -->|PULL| A
    UB -->|PULL| L
    
    %% Sorveglianza
    G -.-> U
    G -.-> A
    G -.-> L
    G --> E
    
    %% Styling
    classDef production fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    classDef backup fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef monitoring fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef notification fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef main fill:#e1f5fe,stroke:#01579b,stroke-width:4px,font-size:16px,font-weight:bold
    
    class UB production
    class A,L backup
    class G monitoring
    class E notification
    class U main
```

## Caratteristiche di sicurezza

- **Memorizzazione locale dei dati**: tutti i dati sono conservati in Svizzera
- **Backup a più livelli**: 
    - backup orari dei metadati (orari lavorativi)
    - backup completi giornalieri (metadati + digitalizzazioni)
- **Distribuzione geografica**: due server di backup in due ubicazioni diverse in Svizzera
- **Mirroring**: entrambi i server di backup funzionano in RAID 1, ogni salvataggio è quindi presente in doppia copia; complessivamente una ridondanza sestupla dei dati
- **Cifratura**: tutti i backup vengono conservati e trasmessi in forma cifrata
- **Backup basati su pull**: sono i server di backup a prelevare i dati (nessun push)
    - protezione da una compromissione del server di produzione
- **Sorveglianza continua**: server di sorveglianza separato
- **Notifica proattiva**: avvisi via e-mail in caso di problemi
