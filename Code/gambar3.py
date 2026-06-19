import networkx as nx
import matplotlib.pyplot as plt

MOVEMENTS = {
    "Toy Bonnie": [(9,3),(3,4),(4,2),(2,6),(6,102),(102,104)],
    "Toy Chica": [(9,7),(7,4),(4,101),(101,1),(1,5),(5,103),(103,104)],
    "Toy Freddy": [(9,10),(10,101),(101,104)],
    "Withered Bonnie": [(8,7),(7,101),(101,1),(1,5),(5,104)],
    "Withered Chica": [(8,4),(4,2),(2,6),(6,104)],
    "Withered Freddy": [(8,7),(7,3),(3,101),(101,104)],
    "Foxy": [(8,101),(101,104)],
    "Mangle": [(12,11),(11,10),(10,7),(7,1),(1,2),(2,6),(6,102),(102,104)],
    "Balloon Boy": [(10,5),(5,103),(103,104)],
    "Puppet": [(11,104)]
}

G = nx.MultiDiGraph()

for edges in MOVEMENTS.values():
    G.add_edges_from(edges)

POS = {
    8:(0,4.5), 7:(2,4.5),
    9:(5,5),
    3:(0,3), 4:(2,3),
    10:(5,3.5),
    1:(0,1.5), 2:(2,1.5),
    11:(5,2),
    5:(0,0), 6:(5,0),
    101:(2.5,-0.2),
    103:(1.2,-0.8),
    102:(3.8,-0.8),
    104:(2.5,-2),
    12:(5,-1)
}

nx.draw_networkx(
    G,
    pos=POS,
    with_labels=True,
    arrows=True
)

plt.show()