Kévin Bourdon et Maximilien Weinmann

## Modélisation

De manière générale, nous utiliserons un algorithme de coloration, on ajoutera quelques détails pour chaque cas
On se servira d'un graphe non orienté et d'arretes

On appelera si possible, des valeurs numériques, des couleurs

### ce qui est modélisé par les sommets
Ce qui compte, c'est que les sommets puissent se différencier, qu'on utilise differentes couleurs ou différents chiffres ne changent rien.

Pour le Sudoku : les sommets représentent les cases du Sudoku, cases qui détiendront une valeur entre 1 et 9 inclus (ces valeurs seront nos couleurs)

Pour la carte géographique : les sommets représentent des pays, ils auront chacun une valeur numérique attribué

Pour les fréquences gsm : les sommets représentent une antenne, ils auront chacun une valeur numérique attribué


### ce qui est modélisé par les arcs ou les arêtes

Les arrêtes désignent littéralement des adjacences :

Pour le Sudoku : les arêtes indiquent qu'une valeur est sur la même ligne, colonne ou bloc qu'une autre valeur

Pour la carte géographique : une aretes indique que deux pays sont adjacents

Pour le GSM : une arrete représente une adjacence entre deux antennes


### les ́eventuelles informations complémentaires que vous jugerez nécessaires à ajouter au graphe

Pour le cas du Sudoku :

Le Sudoku étant connu, on sait que au moins 17 sommets sont à donner, mais ce n'est pas parce qu'il y a 17 sommets donnés, que le Sudoku peut être résolu
### vous expliquerez ce qu'on cherche à réaliser dans le graphe, et en quoi cela permet de répondre au problème de l'application

La question qui se pose du point de vue d'un sommet est : ai-je un voisin comme moi ? 
Par voisin on veut dire sommet compris dans le voisinage d'un sommet


Dans le graphe on cherche à faire un sorte que chacun des sommets n'a aucun voisin comme lui même


Car si pour chaque sommet x du graphe, chaque sommet y adjacent à ce sommet x a une couleur différente de ce sommet x, notre objectif est atteint (par exemple le sudoku est résolu, maintenant il reste à voir si 81 couleurs ont été utilisé ou bien 9)


### Algorithme
Vous trouverez ce qui concerne l'algorithme dans algorithme.txt