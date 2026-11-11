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

    A["Backup-Server 1 (RAID 1)"]
    L["Backup-Server 2 (RAID 1)"]
    G[Monitoring]
    E[Email Fehlermeldungen]
    %% Backup-Verbindungen
    U --> UB
    UB -->|PULL| A
    UB -->|PULL| L
    U -.->|PUSH, verschlüsselt| Z["Zusätzliche Sicherung (Vollausbau), anderer Anbieter"]
    
    %% Überwachung
    G -.-> U
    G -.-> A
    G -.-> L
    G --> E
    
    %% Styling
    classDef production fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    classDef backup fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef extra fill:#fff8e1,stroke:#e65100,stroke-width:2px,stroke-dasharray: 5 5
    classDef monitoring fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef notification fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef main fill:#e1f5fe,stroke:#01579b,stroke-width:4px,font-size:16px,font-weight:bold
    
    class UB production
    class A,L backup
    class Z extra
    class G monitoring
    class E notification
    class U main
```

## Sicherheitsmerkmale

- **Lokale Datenspeicherung**: Alle Daten werden in der Schweiz gespeichert; mit dem Vollausbau Digitales Archiv kommt eine Sicherung in Deutschland dazu (auf Anfrage in der Schweiz)
- **Mehrstufige Backups**: 
    - Stündliche Metadaten-Backups (Geschäftszeiten)
    - Tägliche Vollbackups (Metadaten + Digitalisate)
- **Geografische Verteilung**: Zwei Backup-Server an zwei Standorten in Zürich; mit den Produktionsdaten und dem lokalen Backup auf dem ANTON-SERVER vier Kopien an drei Standorten. Die beiden Zürcher Standorte teilen sich die regionalen Risiken; einen davon unabhängigen Ort bringt die Zusätzliche Sicherung des Vollausbaus
- **Spiegelung**: Beide Backup-Server laufen als RAID 1; das schützt vor dem Ausfall einer Platte, ist aber keine weitere Kopie
- **Verschlüsselung**: Alle Backups verschlüsselt gespeichert und übertragen
- **Pull-basierte Backups**: Backup-Server holen Daten ab (kein Push)
    - Schutz vor Kompromittierung des Produktionsservers
- **Zusätzliche Sicherung** (mit dem [Vollausbau Digitales Archiv](longterm_archives.md#grundangebot-und-vollausbau)): jede Nacht eine weitere Sicherung mit anderer Software (restic) in einen Objektspeicher bei einem anderen Anbieter. Der Produktivserver verschlüsselt sie, bevor sie ihn verlässt, und schreibt sie selbst; dafür lässt sich jeder Stand 30 Tage lang nicht löschen oder überschreiben. Seit November 2026 im Testbetrieb
- **Kontinuierliche Überwachung**: Separater Überwachungsserver 
- **Proaktive Benachrichtigung**: Email-Alerts bei Problemen
