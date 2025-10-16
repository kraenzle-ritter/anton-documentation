# Anton Server Infrastruktur Diagramm

```mermaid
---
config:
  theme: redux
  layout: elk
---
flowchart TB
    subgraph prod[" "]
        U["ANTON-SERVER"]
        UB[Verschlüsseltes lokales Backup]
    end

    A[Backup-Server 1]
    L[Backup-Server 2]
    G[Monitoring]
    E[Email Fehlermeldungen]
    %% Backup-Verbindungen
    U --> UB
    UB -->|PULL| A
    UB -->|PULL| L
    
    %% Überwachung
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

## Sicherheitsmerkmale

- **Lokale Datenspeicherung**: Alle Daten werden in der Schweiz gespeichert
- **Mehrstufige Backups**: 
    - Stündliche Metadaten-Backups (Geschäftszeiten)
    - Tägliche Vollbackups (Metadaten + Digitalisate)
- **Geografische Verteilung**: Backup-Server an verschiedenen Standorten in der Schweiz
- **Verschlüsselung**: Alle Backups verschlüsselt gespeichert und übertragen
- **Pull-basierte Backups**: Backup-Server holen Daten ab (kein Push)
    - Schutz vor Kompromittierung des Produktionsservers
- **Kontinuierliche Überwachung**: Separater Überwachungsserver 
- **Proaktive Benachrichtigung**: Email-Alerts bei Problemen
