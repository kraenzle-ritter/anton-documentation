# Recherche instantanée

La recherche instantanée (`/search-v2`) est une recherche en temps réel : les
résultats apparaissent dès la frappe, peuvent être filtrés via une barre
latérale et sont présentés sous forme de liste mixte d'objets **et** de texte
intégral de PDF, triée par pertinence.

!!! info "Fonction Pro"
    La recherche instantanée est réservée à la clientèle Pro et fonctionne en
    parallèle de la [recherche plein texte](search.md) classique. Ce qui est
    interrogé et la manière dont la recherche se comporte en principe (débuts de
    mots, combinaison ET, vue interne) y est décrit et vaut également ici.

## Rechercher

Saisir le terme recherché en haut — la liste de résultats se met à jour
immédiatement. Chaque résultat indique :

- un marqueur de type (**objet** avec son type, ou **PDF** pour un résultat
  plein texte dans un document),
- le niveau de description et le chemin (fonds → série → …),
- un extrait de texte mis en évidence à l'endroit trouvé,
- une image de prévisualisation, si elle existe.

Si le champ est vide, une liste de parcours des notices les plus récentes
s'affiche (si cette option est activée), de sorte que la page n'est jamais vide.

## Filtrer (barre latérale)

La barre latérale propose des facettes assorties du nombre de résultats. Selon
le service, sont disponibles :

- **niveau de description**, **type d'objet**, **médias** (avec/sans)
- **acteur·trice·s**, **mots-clés**, **lieux** — avec un champ de recherche
  permettant de restreindre rapidement lorsqu'il y a beaucoup de valeurs
- **période** — un curseur à deux poignées (de/à) ; les valeurs peuvent aussi
  être saisies directement

Plusieurs valeurs au sein d'une même facette agissent comme un
«&nbsp;ou&nbsp;», des facettes différentes comme un «&nbsp;et&nbsp;».
**Réinitialiser les filtres** vide la sélection.

!!! note "Seules les facettes utiles"
    Les facettes pour lesquelles un service ne tient aucune valeur (p. ex.
    aucun lieu) sont automatiquement masquées.

## Trier

Via le menu de tri : **pertinence** (par défaut), **date (les plus récentes
d'abord)** ou **date (les plus anciennes d'abord)**.

## Partager et lier

L'état complet de la recherche figure dans la barre d'adresse — terme recherché,
filtres, période et tri. L'URL peut être **enregistrée ou partagée** et rétablit
la recherche avec ses filtres.

## Autres aides

- L'**autocomplétion** dans la barre de navigation propose des résultats dès la
  frappe.
- **«&nbsp;Vouliez-vous dire …&nbsp;?&nbsp;»** propose une orthographe corrigée
  lorsqu'il y a peu ou pas de résultats.
- Les **dernières recherches** sont proposées localement dans le navigateur.

## Visibilité

Comme dans la recherche classique, vous ne voyez que ce que vous êtes autorisé·e
à voir. Les contenus de PDF bloqués (sous embargo) n'apparaissent pas dans la
recherche publique, même si les données descriptives correspondent au terme
recherché.
