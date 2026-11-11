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
    U -.->|PUSH, chiffré| Z["Sauvegarde supplémentaire (offre complète), autre fournisseur"]
    
    %% Surveillance
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

## Caractéristiques de sécurité

- **Stockage local des données** : toutes les données sont conservées en Suisse ; l'offre complète Archive numérique ajoute une sauvegarde en Allemagne (en Suisse sur demande)
- **Sauvegardes à plusieurs niveaux** : 
    - sauvegardes horaires des métadonnées (heures de bureau)
    - sauvegardes complètes quotidiennes (métadonnées + numérisations)
- **Répartition géographique** : deux serveurs de sauvegarde sur deux sites à Zurich ; avec les données de production et la sauvegarde locale sur le SERVEUR ANTON, quatre copies sur trois sites. Les deux sites zurichois partagent les mêmes risques régionaux ; la sauvegarde supplémentaire de l'offre complète ajoute un lieu indépendant de ceux-ci
- **Mise en miroir** : les deux serveurs de sauvegarde fonctionnent en RAID 1 ; cela protège contre la panne d'un disque, mais ne constitue pas une copie supplémentaire
- **Chiffrement** : toutes les sauvegardes sont stockées et transmises chiffrées
- **Sauvegardes en mode pull** : les serveurs de sauvegarde vont chercher les données (pas de push)
    - protection contre une compromission du serveur de production
- **Sauvegarde supplémentaire** (avec l'[offre complète Archive numérique](longterm_archives.md#offre-de-base-et-offre-complete)) : chaque nuit, une sauvegarde supplémentaire avec un autre logiciel (restic) vers un stockage objet chez un autre fournisseur. Le serveur de production la chiffre avant qu'elle ne le quitte et l'écrit lui-même ; en contrepartie, aucun état de sauvegarde ne peut être effacé ni écrasé pendant 30 jours. En exploitation de test depuis novembre 2026
- **Surveillance continue** : serveur de surveillance distinct
- **Notification proactive** : alertes par courriel en cas de problème
