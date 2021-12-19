import networkx as nx
import matplotlib.pyplot as plt
import sys


def Sudoku_full_zero() :
    un_Sudoku = nx.sudoku_graph()
    for node in nx.nodes(un_Sudoku) :
        un_Sudoku.nodes[node]["Color"] = 0
    return un_Sudoku

def apply_input(un_Sudoku) :
    toutes_les_lignes = []
    with open("input_Sudoku/Sudoku_simple.txt", "r") as input :
        for ligne in input.readlines() :
            toutes_les_lignes.append(ligne.strip())
    for commande in toutes_les_lignes :
        abscisse = int(commande[0])
        ordonnee = int(commande[2])
        valeur = int(commande [4])
        un_Sudoku.nodes[(9 * (ordonnee - 1)) + abscisse - 1]["Color"] = valeur
    







if __name__ == "__main__":
    Sudoku = Sudoku_full_zero()
    apply_input(Sudoku)
    


    couleur = nx.get_node_attributes(Sudoku, "Color")
    nx.draw(Sudoku, labels = couleur)
    plt.show()