# Anton server infrastructure diagram

```mermaid
---
config:
  theme: redux
  layout: elk
---
flowchart TB
    subgraph prod[" "]
        U["ANTON SERVER"]
        UB[Encrypted local backup]
    end

    A["Backup server 1 (RAID 1)"]
    L["Backup server 2 (RAID 1)"]
    G[Monitoring]
    E[Email error alerts]
    %% Backup connections
    U --> UB
    UB -->|PULL| A
    UB -->|PULL| L
    
    %% Monitoring
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

## Security features

- **Local data storage**: all data is stored in Switzerland
- **Multi-level backups**: 
    - Hourly metadata backups (business hours)
    - Daily full backups (metadata + digitised objects)
- **Geographical distribution**: two backup servers at two locations in Zurich; with the production data and the local backup on the ANTON SERVER, four copies at three locations. The two Zurich locations share the regional risks; there is no further, independent location for now
- **Mirroring**: both backup servers run as RAID 1; this protects against the failure of a disk but is not a further copy
- **Encryption**: all backups are stored and transmitted encrypted
- **Pull-based backups**: the backup servers fetch the data (no push)
    - protection against compromise of the production server
- **Continuous monitoring**: separate monitoring server
- **Proactive notification**: email alerts in case of problems
