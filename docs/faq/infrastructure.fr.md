# Schéma de l'infrastructure serveur d'Anton

```mermaid
---
config:
  theme: redux
  layout: elk
---
flowchart TB
    subgraph prod[" "]
        U["SERVEUR ANTON"]
        UB[Sauvegarde locale chiffrée]
    end

    A["Serveur de sauvegarde 1 (RAID 1)"]
    L["Serveur de sauvegarde 2 (RAID 1)"]
    G[Monitoring]
    E[Alertes par courriel]
    %% Liaisons de sauvegarde
    U --> UB
    UB -->|PULL| A
    UB -->|PULL| L
    
    %% Surveillance
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

## Caractéristiques de sécurité

- **Stockage local des données** : toutes les données sont conservées en Suisse
- **Sauvegardes à plusieurs niveaux** : 
    - sauvegardes horaires des métadonnées (heures de bureau)
    - sauvegardes complètes quotidiennes (métadonnées + numérisations)
- **Répartition géographique** : deux serveurs de sauvegarde sur deux sites différents en Suisse
- **Mise en miroir** : les deux serveurs de sauvegarde fonctionnent en RAID 1, chaque sauvegarde existe donc en double ; au total une redondance sextuple des données
- **Chiffrement** : toutes les sauvegardes sont stockées et transmises chiffrées
- **Sauvegardes en mode pull** : les serveurs de sauvegarde vont chercher les données (pas de push)
    - protection contre une compromission du serveur de production
- **Surveillance continue** : serveur de surveillance distinct
- **Notification proactive** : alertes par courriel en cas de problème
