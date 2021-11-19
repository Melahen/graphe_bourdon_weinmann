import networkx as nx
import matplotlib.pyplot as plt

les_numeros = []
for x in range(81) :
    les_numeros.append((x, 0))

G = nx.Graph()
G.add_nodes_from(les_numeros)

#G.add_edges_from([(1, 2), ])
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()