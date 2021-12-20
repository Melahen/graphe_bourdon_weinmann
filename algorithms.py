import networkx as nx
import matplotlib.pyplot as plt
from numpy import number

"""
G = nx.Graph()


# Proposer un premier algorithme naïf, qui permettra de résoudre le problème lorsqu’on ne met pas de
# contraintes sur le nombre d’éléments permettant de resoudre le probleme

# Algo naïf :
# On donne à chaque sommet une "couleur" différente
# Ainsi on s'assure qu'aucun sommet n'a la même couleur
couleur = 0
for sommet in G.nodes() :
    sommet["color"] = couleur
    couleur += 1"""
    
# Ce genre de solution n'est pas réaliste, on ne va pas remplir le Sudoku avec 81 numéros

# Objectif, resoudre le graphe avec le moins de couleurs possibles 
# Algo poussé :

'''définition de glouton(g)

S = liste ordonnée des sommets, suivant la valeur décroissante de leur degré.

pour tout x de S
  pc = première couleur non utilisée par les voisins de x
  colorer le sommet x avec pc
fin pour tout

retourner la liste des couleurs de g'''




def glouton(graphe) :
    dico = {}
    for sommet in graphe.nodes() :
        dico[sommet] = graphe.degree[sommet]
    liste_sommet_par_degree_decreasing = sorted(dico.keys(), key = dico.get, reverse = True)

    liste_sommets_colorees = []
    couleur_actuelle = 1
    sommet_actuel = 0

    while len(liste_sommets_colorees) < graphe.number_of_nodes() :
        voisins_colored = False

        for voisin in nx.neighbors(graphe, liste_sommet_par_degree_decreasing[sommet_actuel]) :
            if graphe.nodes[voisin]["Color"] == couleur_actuelle :
                voisins_colored = True
                break
        
        if not voisins_colored :
            graphe.nodes[liste_sommet_par_degree_decreasing[sommet_actuel]]["Color"] = couleur_actuelle
            liste_sommets_colorees.append(liste_sommet_par_degree_decreasing[sommet_actuel])


        sommet_actuel += 1
        
        if sommet_actuel == len(liste_sommet_par_degree_decreasing) :
            sommet_actuel = 0
            couleur_actuelle += 1
            for sommet_colored in liste_sommets_colorees :
                if sommet_colored in liste_sommet_par_degree_decreasing :
                    liste_sommet_par_degree_decreasing.remove(sommet_colored)







# on peut modifier glouton pour qu'il prenne en fonction de la liste decroissante des degre
        
            
