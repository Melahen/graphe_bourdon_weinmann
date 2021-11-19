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
            Sudoku.add_edge(j * 9 + colonne, i * 9 + colonne)
            
            

            
            
nx.draw(Sudoku, with_labels=True, font_weight='bold')
plt.show()