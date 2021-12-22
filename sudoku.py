import networkx as nx
import matplotlib.pyplot as plt
import sys
import algorithms
import time

def Sudoku_full_zero() :
    un_Sudoku = nx.sudoku_graph()
    for node in nx.nodes(un_Sudoku) :
        un_Sudoku.nodes[node]["Color"] = 0
    return un_Sudoku

def apply_input(un_Sudoku, un_input) :
    toutes_les_lignes = []
    with open(un_input, "r") as input :
        for ligne in input.readlines() :
            toutes_les_lignes.append(ligne.strip())
    for commande in toutes_les_lignes :
        abscisse = int(commande[0])
        ordonnee = int(commande[2])
        valeur = int(commande [4])
        un_Sudoku.nodes[(9 * (ordonnee - 1)) + (abscisse - 1)]["Color"] = valeur
    
    


if __name__ == "__main__":

    Sudoku = Sudoku_full_zero()
    apply_input(Sudoku, sys.argv[2])

    start = time.time()

    algorithms.solveSudokuHelper(Sudoku, 0)
    
    end = time.time()
    print("L'algorithme a pris : ", round((end - start), 6), "s")

    fichier = open(sys.argv[4], "w") 
    fichier.write("")
    fichier.close()
    if algorithms.sudokuChecker(Sudoku) :
        fichier = open(sys.argv[4], "a") 
        for sommet in Sudoku.nodes() :
            if sommet == 80 :
                fichier.write(str((sommet % 9) + 1)   + " " + str(int((sommet - sommet % 9) / 9) + 1)  + " " + str(Sudoku.nodes[sommet]["Color"]))

            else :
                fichier.write(str((sommet % 9) + 1)   + " " + str(int((sommet - sommet % 9) / 9) + 1)  + " " + str(Sudoku.nodes[sommet]["Color"]) + "\n")
        fichier.close()
    else :
        print("\n\nCe sudoku n'est pas réalisable, en tout cas pas avec notre algorithme\n\n")


    couleur = nx.get_node_attributes(Sudoku, "Color")
    nx.draw(Sudoku, labels = couleur)
    plt.show()