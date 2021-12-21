import networkx as nx
import matplotlib.pyplot as plt
import sys
import algorithms


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
    Antennes = init_gsm(sys.argv[1])
    algorithms.glouton(Antennes)

    couleur = nx.get_node_attributes(Antennes, "Color")
    nx.draw(Antennes, with_labels=True, font_size = 11, labels = couleur)
    plt.show()