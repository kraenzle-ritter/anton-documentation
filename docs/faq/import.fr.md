# Import

## Migration depuis une autre base de données

La migration d'une base de données vers une nouvelle base représente toujours un effort relativement important. Les données doivent être mappées, en partie préparées et/ou retravaillées, et le cas échéant corrigées. Une migration rend en même temps visibles les faiblesses des données et permet de les homogénéiser. En ce sens, une migration de base de données est l'occasion d'améliorer la qualité des données.

La stratégie de migration la plus appropriée doit être déterminée au cas par cas. Nous avons mené à bien les approches suivantes avec Anton :

1. Export de l'ancienne base de données vers des fichiers Excel – import Excel dans Anton  
2. Export de l'ancienne base de données vers des fichiers EAD – import EAD dans Anton  
3. Reprise directe des données depuis l'ancienne base de données  

Pour les méthodes 2 et 3, des scripts doivent être programmés et/ou adaptés.

## Import depuis Excel

Anton dispose d'un import Excel élaboré et bien documenté. Les campagnes de description importantes portant sur un même niveau de description sont elles aussi souvent réalisées dans Excel. Le fichier Excel est ensuite validé et les données importées dans Anton.

L'import Excel permet également d'importer des objets numériques (photographies, documents, etc.).

## Import depuis un SIP (eCH-0160)

Anton prend en charge l'import de paquets SIP au format eCH-0160. Il est ainsi possible de reprendre dans Anton des fonds gérés dans d'autres systèmes. Voir aussi [Import SIP dans Anton](../user/sip.md).

## Arborescences de fichiers

Un import existe pour les arborescences de fichiers. Anton reconstitue la hiérarchie de l'arborescence. Chaque fichier devient une pièce. Cet import n'est pour l'instant pas encore disponible depuis le navigateur.
