import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


# Proposer un premier algorithme naïf, qui permettra de résoudre le problème lorsqu’on ne met pas de
# contraintes sur le nombre d’éléments permettant de resoudre le probleme

# Algo naïf :
# On donne à chaque sommet une "couleur" différente
# Ainsi on s'assure qu'aucun sommet n'a la même couleur
couleur = 0
for sommet in G.neighbors() :
    sommet["color"] = couleur
    couleur += 1
    
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
    all_couleurs = []
    color_count = 0
    for sommet in graphe.nodes() :
        all_couleurs.append(color_count)
        color_count += 1
    
    
    for sommet in graphe.nodes() :
        couleurs_presentes = []
        for color in sommet.neighbors() :
            couleurs_presentes.append(color)
        for used in couleurs_presentes :
            all_couleurs.remove(used)
        couleur_pour_le_sommet = all_couleurs[0]
        sommet['color'] = couleur_pour_le_sommet
        for used in couleurs_presentes :
            all_couleurs.append(used)
        all_couleurs = sorted(all_couleurs)
        
# on peut modifier glouton pour qu'il prenne en fonction de la liste decroissante des degre
        
            
