Kévin Bourdon et Maximilien Weinmann

# Execution du code et visualisation de la coloration des graphes

###### Pour Sudoku, vous pouvez taper dans le terminal :
python3 sudoku.py -i input/sudoku_simple.txt -o output_sudoku.txt

ou bien 

python3 sudoku.py -i input/sudoku2.txt -o output_sudoku.txt

ou bien, pour tester le comportement en cas de sudoku irréalisable :

python3 sudoku.py -i input/sudoku_impossible.txt -o output_sudoku.txt


###### Pour la carte géographique, vous pouvez taper dans le terminal :
python3 map.py -i input/input_map.txt -o output_map.txt


###### Pour le réseaux GSM, vous pouvez taper dans le terminal :
python3 gsm.py -i input/input_gsm.txt -o output_gsm.txt

###### Output

Vous trouverez le résultat des résolutions sous forme textuelle dans les fichiers output_gsm.txt, output_map.txt et output_sudoku.txt

## Modélisation (Partie du 1er rendu)

De manière générale, nous utiliserons un algorithme de coloration.
On se servira de graphe non orienté et d'arêtes.

On désignera des valeurs numériques par le terme "couleurs" pour simplifier l'obtention et l'exploitation des résultats.

### ce qui est modélisé par les sommets
Ce qui compte, c'est que les sommets puissent se différencier, qu'on utilise differentes couleurs ou différents chiffres ne changent rien.

Pour le Sudoku : les sommets représentent les cases du Sudoku, cases qui détiendront une valeur entre 1 et 9 inclus (ces valeurs seront nos couleurs).

Pour la carte géographique : les sommets représentent des pays.

Pour les fréquences gsm : les sommets représentent une antenne.


### ce qui est modélisé par les arcs ou les arêtes


Les arrêtes désignent littéralement des adjacences entre sommet:

Pour le Sudoku : les arêtes indiquent qu'une valeur est sur la même ligne, colonne ou bloc qu'une autre valeur.

Pour la carte géographique : une arete indique que deux pays sont adjacents.

Pour le GSM : une arete représente une adjacence entre deux antennes.


### les ́eventuelles informations complémentaires que vous jugerez nécessaires à ajouter au graphe

Pour le cas du Sudoku :

Le Sudoku étant connu, on sait que au moins 17 sommets sont à donner, mais ce n'est pas parce qu'il y a 17 sommets donnés, que le Sudoku peut être résolu.

On fera donc des sudokus pré-remplis avec au moins 17 sommets.


### vous expliquerez ce qu'on cherche à réaliser dans le graphe, et en quoi cela permet de répondre au problème de l'application

La question qui se pose du point de vue d'un sommet est : ai-je un voisin comme moi ? 
Par voisin on veut dire sommet compris dans le voisinage d'un sommet.


Dans le graphe on cherche à faire un sorte que chacun des sommets n'a aucun voisin comme lui même.
On va créer des algorithmes qui rempliront nos graphes suivant ce principe.


Car si pour chaque sommet x du graphe, chaque sommet y adjacent à ce sommet x a une couleur différente de ce sommet x, notre objectif est atteint. Par exemple le sudoku est résolu, maintenant il reste à voir si 81 couleurs ont été utilisé ou bien 9 (ou plus).




### Enoncer clairement le problème posé, en dehors de nos applications spécifique :
Comment colorier un graphe avec le moins de couleurs possibles ?

Problème qui en découle :

Comment le faire le plus rapidement possible ?



## Algorithme (Partie du 2ème rendu)


### Qu'est ce qu'on entend par probleme difficile :

Les problèmes difficiles sont des problèmes ne pouvant pas être résolus en temps polynomial, mais en plus de temps encore.
Par opposition, les problemes "faciles" peuvent être résolus en temps polynomial.

Nous tenons nos propos de ces sites :

https://waytolearnx.com/2019/03/difference-entre-un-probleme-np-complet-et-np-difficile.html

https://www.gerad.ca/Sebastien.Le.Digabel/MTH8415/8_Complexite.pdf


### Qu'est ce qu'une heuristique
Ici dans le cadre du DM, et en theorie des graphes :

On appelle heuristique une méthode de résolution qui ne permet pas d'affirmer que le résultat obtenu est toujours optimal.

Plus formelement : 
une heuristique est un algorithme qui
fournit rapidement une solution réalisable (en temps polynomial), pas nécessairement optimale
pour un probleme d'optimisation NP-difficile.


Moins formelement :
Une heuristique est une maniere de trouver une solution, même si la résolution n'est pas optimale.


Nos sources :
https://www.techno-science.net/glossaire-definition/Heuristique.html
http://ressources.unit.eu/cours/EnsROtice/module_avance_thg_voo6/co/heurreslim.html


### Propositions d'algorithme

Vous trouverez nos algorithmes en python dans algorithms.py

Dans ce Readme, on exposera nos algorithmes en pseudocode

#### Proposer un premier algorithme naïf, qui permettra de résoudre le problème lorsqu’on ne met pas de
#### contraintes sur le nombre d’éléments permettant de resoudre le problème.
On peut proposer un algorithme naïf de ce type :

```
fonction algorithme_trop_naif(graphe) :
    couleur initialisée à zéro
    pour chaque sommet dans graphe :
        sommet[couleur] = couleur
        couleur++
```

Cet algorithme est très simple et rapide. Il est aussi inutile, alors nous ne le prendrons pas en considération.

On proposera un autre algorithme naïf plus intéressant, glouton, ou greedy :

```
fonction glouton_naif(graphe) :
    les_sommets = liste de tous les sommets de graphe (au début)
    liste_sommets_colorés = liste des sommets ayant une couleur 
    couleur actuelle = 0
    sommet_actuel = 0
    tant que taille(liste_sommets_colorés) < nombre de sommet dans graphe :
        Si sommet_actuel n'a aucun voisin de couleur couleur_actuelle :
            sommet_actuel prend couleur actuelle pour couleur
            sommet_actuel est ajouté a liste_sommet_colorés
        sommet_actuel est incrémenté de 1
        si sommet_actuel est le dernier de les_sommets :
            sommet_actuel reinitialisé à 0
            couleur_actuelle est incrémentée de 1 
            retirer à les_sommets les sommets qu'il a en commun avec liste_sommet_colorés
```





#### Proposer un second algorithme qui mettra en œuvre une heuristique dont l’objectif sera de tenter d’envisager les sommets dans un ordre plus habile.

Cet algorithme va traiter les sommets du graphe dans l'ordre décroissant de leur degré

```
fonction glouton_avancé(graphe) :
    les_sommets = liste de tous les sommets de graphe rangé par ordre décroissant de leur dégré 
    liste_sommets_colorés = liste des sommets ayant une couleur 
    couleur actuelle = 0
    sommet_actuel = 0
    tant que taille(liste_sommets_colorés) < nombre de sommet du graphe :
        Si sommet_actuel n'a aucun voisin de couleur couleur_actuelle :
            sommet_actuel prend couleur actuelle pour couleur
            sommet_actuel est ajouté a liste_sommet_colorés
        sommet_actuel est incrémenté de 1
        si sommet_actuel est le dernier de les_sommets :
            sommet_actuel reinitialisé à 0
            couleur_actuelle est incrémentée de 1 
            retirer à les_sommets les sommets qu'il a en commun avec liste_sommet_colorés
```

#### Discuter des limites de cet heuristique

Cet algorithme n'associe une couleur a un sommet qu'une seule fois, il se peut qu'il associe une couleur qui ne sera pas la meilleur,
dans ce cas, il continuera la resolution avec cette couleur qui n'etait pas le meilleur choix et ne se corrigera jamais.

Il terminera rapidement, mais ne trouvera pas toujours le nombre minimum de couleur.

Un algorithme de backtracking sera plus efficace pour sudoku, où 9 couleurs sont imposées.

On appelé solveSudokuHelper() notre algorithme de backtracking dans algorithm.py

Pseudocode pour backtracking :
```
def backtracking(graphe, sommet) :
    si sommet est le dernier du graphe :
        si sommet n'est pas coloré :
            donner une couleur possible à sommet
        return graphe

    si sommet est plus grand que le dernier sommet du graphe :
        backtracking(graphe, sommet%9 +1) # pour atteindre la colonne d'a coté
    
    si sommet n'est pas coloré :
        donner couleur possible à sommet 
        backtracking(graphe, sommet + 9) # pour atteindre la ligne d'en dessous
        si le graphe est valide :
            return graphe
        retirer couleur a sommet

    sinon :
        backtracking(graphe, sommet + 9)
    return graphe
```

Ici donner une couleur possible signifie boucler sur les couleurs et donner au sommet une couleur qui ne déroge pas
aux regles du sudoku.

Le graphe est valide si le sudoku est rempli sans voisin de même couleur.


Dans algorithms.py, nous avons ajouté à notre backtracking une condition qui vérifie que le Sudoku est résoluble,
afin d'éviter qu'il tourne en boucle dans le cas d'un Sudoku sans résolution.


Cet algorithme est plus lent car brute-force, néanmoins, en cas de soucis il reviendra en arrière et prendra un autre chemin, d'où son nom.

Aussi, si on ne l'arretait pas au premier sudoku résolu, cet algorithme est capable de trouver plusieurs solution, s'il y en a.



Source pour l'algorithme glouton :
https://www.codeproject.com/Articles/801268/A-Sudoku-Solver-using-Graph-Coloring

( la partie :


1. Select the vertex of maximum degree V.

2. Find the set of non-adjacent vertices to V.

3. From this set select the vertex Y of maximum common vertices with V.

4. Contract Y into V to be colored with the same color.

5. Remove Y from the set and repeat steps 3-5 until the list is empty.

6. Remove vertex V from the graph

7. Repeat steps 1-6 until the resulting graph has all contracted nodes adjacent to each other.

)



Source pour l'algorithme backtracking :
https://medium.com/swlh/sudoku-solver-using-backtracking-in-python-8b0879eb5c2d

(L'algo proposé par le site n'est pas adapté pour le DM, mais avec quelques modifications on peut arriver à nos fins, comme vous le verrez dans
algorithms.py)



## Résultats :

On a lancé plusieurs fois nos algorithmes pour prendre un résultat moyen.


##### BackTracking :
- Sudoku : 2.260145 s (sans vérification constante 0.201292 s, ce qui reste lent)


##### Glouton Avancé :
- Carte : 0.000427 s
- GSM : 0.000198 s
- Sudoku : 0.003618 s (en 11 couleurs néanmoins)

##### Glouton naif :
- Carte : 0.000534 s
- GSM : 0.000305 s
- Sudoku : 0.006193 s (en 11 couleurs par contre)


Pour ce qui est de remplir chaque graphe, notre proposition de glouton avancé est la meilleur, dans chaque cas, quand il s'agit de temps de résolution.

Pour une résolution correcte, nos gloutons ne sont bons que pour Gsm et Carte, pour ce qui est de Sudoku, on se sert d'un backtracking, qui est très lent.

Nous tenons à préciser que les inputs sont restés les mêmes, d'un algorithme à l'autre.

L'input de map et de gsm est disponible sur Discord, sur le serveur Formations Informatique Lille, dans le groupe s5_graphes.
Celui de map correspond à peu près à la carte de l'Europe.
Nous avons pris des sudokus à résoudre pour l'input de sudoku.


## Vérification

On considère un graphe terminé lorsque notre algorithme a attribué une couleur à chaque sommet du graphe

Chaque graphe est soumis à au moins une vérification : 


Une fonction sudokuChecker(graphe) vérifie que le graphe est composé de sommet sans voisin de même couleur, et qu'il n'y a pas de sommet sans couleur


#### Cas du Sudoku :
En cas de sudoku inrésoluble, un affichage apparait dans la console indiquant qu'on ne peut pas résoudre le sudoku, en tout cas pas avec notre algorithme

En cas de succès, en dehors de l'affichage networkx du graphe et du message de la mesure du temps, il n'y a rien.

#### Cas de GSM et de Carte :
Dans le cas où glouton ne réussit pas à terminer le graphe, ou s'il le termine en associant la même couleur à 2 sommets adjacents, un message d'echec est affiché

Si le graphe est terminé, sans voisin de même couleur, un message de succès sera affiché

Que ce soit en cas d'échec ou de succès, un message sera affiché, et sera la preuve que sudokuChecker a vérifié le graphe



## Section Travail à faire du PDF du DM :

Ici nous allons nous vérifier que nous avons fait ce qui est demandé dans la partie travail à faire du DM.

#### identifier le point commun entre ces problèmes et proposer une modélisation sous forme de graphes pour chacun d’entre eux

Nous avons identifié le point commun dans la partie   "vous expliquerez ce qu'on cherche à réaliser dans le graphe, et en quoi cela permet de répondre au problème de l'application"   de la partie Modélisation du Readme


On a proposé nos modélisations dans les fichiers map.py, gsm.py et sudoku.py

cette modélisation est expliqué dans la partie Modélisation de notre Readme

#### proposer des algorithmes pour résoudre le problème, en prouver la terminaison et la correction

On peut voir nos propositions dans la partie des propositions et la partie dicuter des limites de la partie Algorithme du Readme


On prouve leur terminaison dans la partie Vérification du Readme et la correction dans la partie Algorithme (2ème Rendu) du readme

#### implémenter ces algorithmes, les valider en les exécutant sur des instances des problèmes et en interprétant les solutions obtenues,

Dans les fichiers map.py, gsm.py, sudoku.py et algorithms.py, vous trouverez les algorithmes de résolution du problème
ainsi que leur mise en oeuvre, vous y verrez nos implémentations. 

Vous trouverez les indications d'éxécutions au début du Readme

Vous pouvez voir nos résultats et interprétation dans la partie Résultat du Readme


#### trouver une application, différente de celles citées ci-dessous, qui utilise la même modélisation.

Nous pensons à la création d'emploi du temps, un professeur ne peut pas enseigner plusieurs classe en même temps.
