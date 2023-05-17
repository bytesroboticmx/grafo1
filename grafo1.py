import matplotlib
matplotlib.use('TkAgg')

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Agregar 9 nodos al grafo
G.add_nodes_from(range(1, 10))

# Agregar 14 aristas al grafo
edges = [
    (1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 4),
    (3, 6), (4, 7), (5, 6), (5, 8), (6, 7), (6, 9),
    (8, 9), (9, 7)
]
G.add_edges_from(edges)

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show(block=True)
