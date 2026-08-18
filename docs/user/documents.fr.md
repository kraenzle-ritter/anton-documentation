# Documents

Le module «&nbsp;Documents&nbsp;» offre un accès propre à certains PDF — par
exemple des rapports d'activité ou des publications qu'un service souhaite
proposer spécifiquement à la lecture. C'est une vitrine à côté de la
[recherche](search.md), et non une voie supplémentaire vers le plan de
classement.

La vue d'ensemble se trouve sous `/documents` et peut être liée depuis le site
web du service. Les documents y apparaissent classés par groupes, chaque groupe
accompagné d'un bref texte explicatif.

!!! note "Configuration nécessaire"
    Le module n'affiche quelque chose que s'il est configuré — voir
    [Configurer les documents](../admin/documents.md). Sans configuration,
    l'appel renvoie à la page d'accueil.

## Ce que la description doit fournir

Dans le module, **un document correspond à une unité de description**. Qui
souhaite l'utiliser décrit donc les PDF individuellement et non regroupés dans un
dossier.

## La visionneuse

À l'ouverture d'un document, le contenu du champ **forme et contenu** apparaît à
gauche, le PDF à droite.

Une table des matières peut simplement être écrite sous forme de liste dans le
champ de texte :

```markdown
Sommaire :
- Premier chapitre (p. 5)
- Deuxième chapitre (p. 17)
```

### Lorsque les numéros de page ne correspondent pas

Les numéros de page imprimés diffèrent souvent des pages du PDF — un rapport
comportant une page de titre et une préface peut commencer sa page 5 à la page 17
du PDF. Pour que le saut atteigne malgré tout le bon endroit, la page PDF peut
être indiquée en commentaire après l'entrée :

```markdown
Sommaire :
- Premier chapitre (p. 5) <!-- 17 -->
- Deuxième chapitre (p. 17) <!-- 29 -->
```

C'est toujours le numéro de page imprimé qui s'affiche ; le saut mène à la page
PDF indiquée dans le commentaire. Pour les lecteur·trice·s, le commentaire reste
invisible.
