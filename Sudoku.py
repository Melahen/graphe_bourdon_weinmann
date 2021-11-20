import networkx as nx
import matplotlib.pyplot as plt

#On fait un graphe avec 81 sommets et zéros arrêtes
Sudoku = nx.empty_graph(81)
# On va connecter les sommets de même ligne
for ligne in range(0, 9) :
    # deb = 9 -> premier sommet de la deuxième ligne, deb = 8 étant le dernier sommet de la première ligne
    # On fait un sous graphe complet pour chaque ligne
    premier_sommet_ligne = ligne * 9
    for i in range(1, 9) :
        for j in range(i) :
            Sudoku.add_edge(premier_sommet_ligne + i, premier_sommet_ligne + j)


# On connecte maintenant les sommets de même colonne
for colonne in range(0, 9) :
    for i in range(1, 9) :
        for j in range(i) :
            Sudoku.add_edge(i * 9 + colonne, j * 9 + colonne)

# Les cases de sudoku sont aussi reliées en bloc de 9, il y a 9 blocs dans un jeu de sudoku
# Vous observerez la beauté de la présence de 9/3, 9 et 9*3 dans ce morceau de code
for saut_colonne in range(3) :
        for saut_ligne in range(3) :
            deplacement = 27 * saut_colonne+ 3 * saut_ligne
            for i in range(1,  9) :
                for j in range(i) :
                    u = deplacement + (i % 3) + 9 * (i // 3)
                    v = deplacement + (j % 3) + 9 * (j // 3)
                    Sudoku.add_edge(u, v)

            
            
nx.draw(Sudoku, with_labels=True, font_weight='bold')
plt.show()