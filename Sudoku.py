import networkx as nx
import matplotlib.pyplot as plt
import sys

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
        un_Sudoku.nodes[(9 * (ordonnee - 1)) + abscisse - 1]["Color"] = valeur
    



"""      
definition de gloutonSimple(g)

S = liste des sommets de g

pour tout x de S
  pc = première couleur non utilisée par les voisins de x
  colorer le sommet x avec pc
fin pour tout

retourner la liste des couleurs de g"""

def glouton_naif(g) :
    S = [sommet for sommet in g.nodes()]
    couleurs_disponibles = list(g.nodes[sommet]["Color"] for sommet in g.nodes() if g.nodes[sommet]["Color"] != 0)

    for sommet in S :
        couleurs_des_voisins = []

        for voisin in nx.neighbors(g, sommet) :
            if g.nodes[voisin]["Color"] != 0 :
                couleurs_des_voisins.append(g.nodes[voisin]["Color"])
    
        for couleur_inutilisable in couleurs_des_voisins :
            couleurs_disponibles.remove(couleur_inutilisable)

        pc = couleurs_disponibles[0]
        g.nodes[sommet]["Color"] = pc

        couleurs_disponibles = list(g.nodes[sommet]["Color"] for sommet in g.nodes() if g.nodes[sommet]["Color"] != 0)
    
    for sommet in S :
        for voisin in nx.neighbors(g, sommet) :
            if g.nodes[sommet]["Color"] == g.nodes[voisin]["Color"] :
                glouton_naif(g)


        
        

    



if __name__ == "__main__":
    Sudoku = Sudoku_full_zero()
    apply_input(Sudoku, sys.argv[1])
    glouton_naif(Sudoku)
    


    couleur = nx.get_node_attributes(Sudoku, "Color")
    nx.draw(Sudoku, labels = couleur)
    plt.show()