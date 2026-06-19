import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

NODE_LABELS = {
    1: "CAM 01",
    2: "CAM 02",
    3: "CAM 03",
    4: "CAM 04",
    5: "CAM 05",
    6: "CAM 06",
    7: "CAM 07",
    8: "CAM 08",
    9: "CAM 09",
    10: "CAM 10",
    11: "CAM 11",
    12: "CAM 12",
    101: "Hallway",
    102: "R.Vent",
    103: "L.Vent",
    104: "Office"
}

MOVEMENTS = {
    "Toy Bonnie": [
        (9, 3), (3, 4), (4, 2), (2, 6), (6, 102), (102, 104)
    ],
    "Toy Chica": [
        (9, 7), (7, 4), (4, 101), (101, 1), (1, 5), (5, 103), (103, 104)
    ],
    "Toy Freddy": [
        (9, 10), (10, 101), (101, 104)
    ],
   
    "Withered Bonnie": [
        (8, 7), (7, 101), (101, 1), (1, 5), (5, 104)
    ],
    "Withered Chica": [
        (8, 4), (4, 2), (2, 6), (6, 104)
    ],
    "Withered Freddy": [
        (8, 7), (7, 3), (3, 101), (101, 104)
    ],
    "Foxy": [
        (8, 101), (101, 104)
    ],
    "Mangle": [
        (12, 11),
        (11, 10),
        (10, 7),
        (7, 1),
        (1, 2),
        (2, 6),
        (6, 102),
        (102, 104)
    ],
   
    "Balloon Boy": [
        (10, 5), (5, 103), (103, 104)
    ],
    "Puppet": [
        (11, 104)
    ]
}

COLORS = {
    "Toy Bonnie": "#7C5CBF",
    "Toy Chica": "#E8AC2A",
    "Toy Freddy": "#8B4513",
    "Withered Bonnie": "#4A90D9",
    "Withered Chica": "#E87A2A",
    "Withered Freddy": "#6B4226",
    "Foxy": "#D44E2A",
    "Mangle": "#C25A8A",
    "Balloon Boy": "#3AABCC",
    "Puppet": "#000000"
}

POS = {
    8: (0, 4.5),
    7: (2, 4.5),
    9: (5, 5),
    3: (0, 3),
    4: (2, 3),
    10: (5, 3.5),
    1: (0, 1.5),
    2: (2, 1.5),
    11: (5, 2),
    5: (0, 0),
    6: (5, 0),
    101: (2.5, -0.2),
    103: (1.2, -0.8),
    102: (3.8, -0.8),
    104: (2.5, -2),
    12: (5, -1)
}

G = nx.MultiDiGraph()
for character, edges in MOVEMENTS.items():
    for src, dst in edges:
        G.add_edge(src, dst, character=character)

fig, ax = plt.subplots(figsize=(14, 10))

node_colors = []
node_sizes = []
for node in G.nodes():
    if node == 104:
        node_colors.append("#E74C3C")
        node_sizes.append(2200)
    elif node in (101, 102, 103):
        node_colors.append("#2C3E50")
        node_sizes.append(1800)
    else:
        node_colors.append("#1C2951")
        node_sizes.append(1800)

nx.draw_networkx_nodes(
    G,
    POS,
    node_color=node_colors,
    node_size=node_sizes,
    edgecolors="white",
    linewidths=2,
    ax=ax
)

nx.draw_networkx_labels(
    G,
    POS,
    labels=NODE_LABELS,
    font_size=8,
    font_color="white",
    font_weight="bold",
    ax=ax
)

for character, color in COLORS.items():
    nx.draw_networkx_edges(
        G,
        POS,
        edgelist=MOVEMENTS[character],
        edge_color=color,
        width=2.5,
        arrows=True,
        arrowstyle="-|>",
        arrowsize=24,
        min_source_margin=25,
        min_target_margin=25,
        connectionstyle="arc3,rad=0.08",
        ax=ax
    )

legend_elements = [
    Line2D(
        [0], [0],
        color=color,
        lw=2.5,
        label=name
    )
    for name, color in COLORS.items()
]
legend_elements.extend([
    mpatches.Patch(
        facecolor="#1C2951",
        edgecolor="white",
        label="Camera Room"
    ),
    mpatches.Patch(
        facecolor="#2C3E50",
        edgecolor="white",
        label="Hallway / Vent"
    ),
    mpatches.Patch(
        facecolor="#E74C3C",
        edgecolor="white",
        label="Office"
    )
])

ax.legend(
    handles=legend_elements,
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    fontsize=8,
    title="Animatronics",
    framealpha=1
)

plt.subplots_adjust(right=0.78)
ax.axis("off")
plt.savefig(
    "fnaf2_animatronic_graph.png",
    dpi=600,
    bbox_inches="tight"
)
plt.show()