# Connecter des assistants IA (MCP)

Un assistant IA comme Claude ou ChatGPT peut effectuer des recherches
directement dans le catalogue public d'un service d'archives : parcourir les
fonds, chercher, lire des notices, naviguer dans l'arborescence et citer le
texte intégral des documents numérisés. La connexion passe par le **Model
Context Protocol (MCP)**, un standard ouvert pris en charge par les assistants
courants.

L'assistant ne répond alors plus à partir de ce qu'il a retenu lors de son
entraînement, mais à partir du catalogue — avec la cote et le lien de chaque
notice sur laquelle il s'appuie.

!!! note "Seulement là où le service l'a activé"
    L'interface est activée service par service et n'est disponible que pour
    les services dont le catalogue est public. Si l'adresse répond «Not Found»,
    elle n'est pas en service.

## Ce que voit l'assistant

Exactement ce qui est visible sans connexion dans le navigateur : les notices
au statut «Final» qui ne sont pas [bloquées](access.md). Les documents et leur
texte intégral uniquement lorsque le délai de protection a expiré. Les acteurs
privés, les champs de texte internes et les médias bloqués sont exclus.

Il n'y a pas de connexion, et il n'en faut pas — même avec un compte Anton,
l'interface ne montre que la vue publique.

!!! warning "Ce que lit l'assistant, son fournisseur le lit aussi"
    Tout ce que renvoie l'interface est transmis au fournisseur de l'assistant
    (Anthropic, OpenAI, Microsoft …). Il s'agit exclusivement de données
    publiques — mais il est bon de le savoir.

## Adresse

```
https://<adresse du service>/api/mcp
```

Par exemple `https://archives.example.ch/api/mcp`.

## Configuration

### Claude (claude.ai et Claude Desktop)

**Paramètres → Connecteurs → Ajouter un connecteur personnalisé**, donner un
nom (celui du service, par exemple) et saisir l'adresse. Aucune
authentification n'est à configurer. La disponibilité des connecteurs
personnalisés dépend de l'abonnement.

### Claude Code

```bash
claude mcp add --transport http archives https://archives.example.ch/api/mcp
```

### ChatGPT, Microsoft Copilot et autres

Tout assistant capable de se connecter à un serveur MCP distant via
«Streamable HTTP» sans authentification convient. L'emplacement du réglage
varie selon le produit et l'abonnement ; les instructions du fournisseur font
foi.

## Ce que l'assistant peut en faire

| Outil | Fonction |
|---|---|
| `holdings_overview` | Que contient le service ? Archives, groupes de fonds et fonds avec cote, titre et date |
| `search_records` | Recherche dans les descriptions — titres, champs de texte, acteurs, lieux, mots-clés |
| `search_media_texts` | Recherche dans le texte intégral des documents numérisés ; renvoie des passages autour de chaque occurrence |
| `read_record` | Une notice avec tous ses champs publics, les données d'autorité liées et les documents ; le texte intégral page par page |
| `navigate_tree` | Notices supérieures et inférieures, voisines |
| `lookup_authority` | Acteurs, lieux et mots-clés avec renvois aux fichiers d'autorité (GND, Wikidata …) et les notices liées |

L'assistant choisit lui-même les outils. Il suffit de demander :

- «Que contient le service d'archives ?»
- «Qu'a rapporté la Maurmer Post sur la fondation du FC Maur ? Cite les passages.»
- «Quels documents concernent la construction de l'école, et où se trouvent-ils dans les fonds ?»

## Limites

- **Les termes de moins de trois lettres** sont mal indexés. Faire chercher les
  abréviations comme expression et avec un mot plus long.
- **La reconnaissance de texte (OCR) n'est pas sans erreurs.** Si un mot ne
  donne rien, un début de mot avec `*` ou une autre graphie aide souvent.
- **Lecture seule.** Commander, modifier ou créer n'est pas possible par
  l'interface.
- **Nombre de requêtes :** 60 par minute et par adresse. Une recherche en
  demande généralement quelques dizaines.

Les réponses de l'assistant restent les siennes. Ce qui compte, c'est la notice
liée — en cas de doute, s'y reporter.
