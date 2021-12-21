import networkx as nx
import matplotlib.pyplot as plt
import sys
import algorithms
import copy

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
    




"""
def solveur_naif(g) :

    liste_tous_sommets = [sommet for sommet in g.nodes()]
    dico_chaque_sommet = {}
    for sommet in liste_tous_sommets :

        if g.nodes[sommet]["Color"] == 0 :
        
            for sommet_encore in liste_tous_sommets :
                listes_toutes_couleurs_possible = set([g.nodes[sommet]["Color"] for sommet in g.nodes() if g.nodes[sommet]["Color"] != 0])

                for voisin in nx.neighbors(g, sommet_encore) :
                    listes_toutes_couleurs_possible.discard(g.nodes[voisin]["Color"])
                dico_chaque_sommet[sommet_encore] = listes_toutes_couleurs_possible

                if len(dico_chaque_sommet[sommet_encore]) == 1 :
                    g.nodes[sommet_encore]["Color"] = list(dico_chaque_sommet[sommet_encore])[0]



            les_valeurs = []
            for clef in list(dico_chaque_sommet.keys()) :
                les_valeurs.append([clef, dico_chaque_sommet[clef]])
            les_valeurs_rangees = []
            for couple in les_valeurs :
                if not les_valeurs_rangees : 
                    les_valeurs_rangees.append(couple)
                else :
                    if len(couple[1]) < len(les_valeurs_rangees[0][1]) :
                        les_valeurs_rangees.insert(0, couple)
            

            g.nodes[les_valeurs_rangees[0][0]]["Color"] = list(les_valeurs_rangees[0][1])[0]

"""
    

def is_possible(graphe, sommet, couleur_a_verifier) :
    for voisin in nx.neighbors(graphe, sommet) :
        if graphe.nodes[voisin]["Color"] == couleur_a_verifier :
            return False
    return True

def solveSudokHelper(graphe, sommet) :
    
    if (sommet + 1) == len(graphe) :
        if graphe.nodes[sommet]["Color"] != 0 :
            print()
            for node in graphe.nodes :
                print(graphe.nodes[node]["Color"], end=" ")
        else :
            for pigment in range(1, 10) :
                if is_possible(graphe, sommet, pigment) :
                    graphe.nodes[sommet]["Color"] = pigment
                    print()
                    for node in graphe.nodes :
                        print(graphe.nodes[node]["Color"], end=" ")
                    graphe.nodes[sommet]["Color"] = 0
        print()
        
        return graphe
    
    if sommet > 80 :
        graphe = solveSudokHelper(graphe, (sommet % 9) + 1)
        return graphe

    if graphe.nodes[sommet]["Color"] == 0 :
        for pigment in range(1, 10) :
            if is_possible(graphe, sommet, pigment) :
                graphe.nodes[sommet]["Color"] = pigment
                graphe = solveSudokHelper(graphe, sommet + 9)
                if sudokuChecker(graphe) :
                    return graphe
                graphe.nodes[sommet]["Color"] = 0
    
    else :
        graphe = solveSudokHelper(graphe, sommet + 9)
    
    return graphe


def solveSudoku(graphe, sommet) :
    solveSudokHelper(graphe, sommet)



def sudokuChecker(graphe) :
    for sommet in graphe.nodes :
        for voisin in nx.neighbors(graphe, sommet) :
            if graphe.nodes[voisin]["Color"] == graphe.nodes[sommet]["Color"] :
                return False
    return True


if __name__ == "__main__":
    Sudoku = Sudoku_full_zero()
    apply_input(Sudoku, sys.argv[1])
    #solveur_naif(Sudoku)
    #algorithms.glouton(Sudoku)
    temoin = 0
    solveSudoku(Sudoku, 0)
    
    


    couleur = nx.get_node_attributes(Sudoku, "Color")
    nx.draw(Sudoku, labels = couleur)
    plt.show()