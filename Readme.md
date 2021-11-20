Kévin Bourdon et Maximilien Weinmann

## Modélisation

### ce qui est modélisé par les sommets
Pour le Sudoku : les sommets représentent les cases du Sudoku, cases qui détiendront une valeur entre 1 et 9 inclus

De manière générale, les sommets représenteront un valeur de l'application

### ce qui est modélisé par les arcs ou les arêtes

Les arrêtes désignent littéralement le voisinage :

Pour le Sudoku : les arêtes indiquent qu'une valeur est sur la même ligne, colonne ou bloc qu'une autre valeur


### les ́eventuelles informations complémentaires que vous jugerez nécessaires à ajouter au graphe


### vous expliquerez ce qu'on cherche à réaliser dans le graphe, et en quoi cela permet de répondre au problème de l'application

La question qui se pose du point de vue d'un sommet est : ai-je un voisin comme moi ? 

(case Sudoku : ai-je un voisin qui à la même valeur que moi?
case Map : ai-je un voisin de même couleur que moi ?
case Gsm : ai-je un voisin de même fréquence que moi ?)

Dans le graphe on cherche à faire un sorte que chacun des sommets n'a aucun voisin comme lui même


Car si chaque voisin de tel sommet est différent de ce tel sommet, alors le graphe est résolu, c'est à dire que tous les sommets ont une valeur attribuée qui correspond aux objectifs de l'application.


Pour le cas du Sudoku, bien que ce soit envisageable, à notre stade pour les autres cas aussi :
On cherche aussi à faire en sorte qu'avec un graphe initial aux sommets incomplets(sans valeur), un seul graphe final aux sommets complets soit possible

Le Sudoku étant connu, on sait que au moins 17 sommets sont à donner, mais ce n'est pas parce qu'il y a 17 sommets donnés, que le Sudoku peut être résolu