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
    





def solveur_naif(g) :
    """
        On regarde le premier noeud sans couleur, et on lui attribue la premiere des couleurs disponibles.
        Si en partant de cette premiere attribution on tombe sur un noeud auquel on ne peut pas attribuer de couleurs
        alors on attribue la seconde couleur disponible au premier noeud et ainsi de suite jusqu'à ne plus avoir de
        noeud sans couleur

        Si pour le premier noeud, on rencontre pour chacune de ses couleurs disponibles un noeud sans couleur attribuable,
        on ne peut pas resoudre le sudoku
    
    """
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
            

            g.nodes[dico_chaque_sommet[les_valeurs_rangees[0][0]]] = list(les_valeurs_rangees[0][1])[0]






    


        
        

    



if __name__ == "__main__":
    Sudoku = Sudoku_full_zero()
    apply_input(Sudoku, sys.argv[1])
    solveur_naif(Sudoku)
    


    couleur = nx.get_node_attributes(Sudoku, "Color")
    nx.draw(Sudoku, labels = couleur)
    plt.show()