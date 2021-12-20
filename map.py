import networkx as nx
import matplotlib.pyplot as plt
import sys
import algorithms


def init_map(un_input) :
    map = nx.Graph()
    with open(un_input, "r") as input :
        les_connexions = []
        for line in input.readlines() :
            deux_pays_frontaliers = line.strip().split(" ")
            les_connexions.append((deux_pays_frontaliers[0], deux_pays_frontaliers[1]))


    map.add_edges_from(les_connexions)

    for sommet in map.nodes :
        map.nodes[sommet]["Color"] = 0


    return map


if __name__ == "__main__":
    Carte = init_map(sys.argv[1])
    algorithms.glouton(Carte)



    couleur = nx.get_node_attributes(Carte, "Color")
    nx.draw(Carte, with_labels=True, font_size = 8, labels = couleur)
    plt.show()