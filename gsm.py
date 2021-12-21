import networkx as nx
import matplotlib.pyplot as plt
import sys
import algorithms
import time


def init_gsm(un_input) :
    resaux_antennes = nx.Graph()
    with open(un_input, "r") as input :
        les_connexions = []
        for line in input.readlines() :
            deux_antennes_connectees = line.strip().split(" ")
            les_connexions.append((deux_antennes_connectees[0], deux_antennes_connectees[1]))


    resaux_antennes.add_edges_from(les_connexions)
    for sommet in resaux_antennes.nodes :
        resaux_antennes.nodes[sommet]["Color"] = 0

    return resaux_antennes


if __name__ == "__main__":
    Antennes = init_gsm(sys.argv[2])

    start = time.time()

    algorithms.glouton(Antennes)

    end = time.time()
    print("L'algorithme a pris : ", round((end - start), 6), "s")

    fichier = open(sys.argv[4], "w") 
    fichier.write("")
    fichier.close()
    fichier = open(sys.argv[4], "a") 

    les_noeuds = [int(x) for x in Antennes.nodes]
    les_noeuds.sort()
    for sommet in les_noeuds :
        fichier.write(str(sommet) + " " + str(Antennes.nodes[str(sommet)]["Color"]) + "\n" )
    fichier.close()

    couleur = nx.get_node_attributes(Antennes, "Color")
    nx.draw(Antennes, with_labels=True, font_size = 11, labels = couleur)
    plt.show()