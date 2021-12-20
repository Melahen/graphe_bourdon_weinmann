import networkx as nx
import matplotlib.pyplot as plt
import sys


def init_map(un_input) :
    resaux_antennes = nx.Graph()
    with open(un_input, "r") as input :
        les_connexions = []
        for line in input.readlines() :
            deux_antennes_connectees = line.strip().split(" ")
            les_connexions.append((deux_antennes_connectees[0], deux_antennes_connectees[1]))


    resaux_antennes.add_edges_from(les_connexions)
    return resaux_antennes


if __name__ == "__main__":
    Antennes = init_map(sys.argv[1])
    nx.draw(Antennes, with_labels=True, font_size = 11)
    plt.show()