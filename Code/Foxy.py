import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from importlib import import_module

abs_mod = import_module("4_absorption_time")

TARGET = "Foxy"
AI_LEVEL = 10
HIGHLIGHT_COLOR = "#E63946"
FADE_COLOR = "#7D7D7D"

NODE_LABELS = {
    1: "CAM 01", 2: "CAM 02", 3: "CAM 03", 4: "CAM 04",
    5: "CAM 05", 6: "CAM 06", 7: "CAM 07", 8: "CAM 08",
    9: "CAM 09", 10: "CAM 10", 11: "CAM 11", 12: "CAM 12",
    101: "Hallway", 102: "R.Vent", 103: "L.Vent", 104: "Office"
}

MOVEMENTS = {
    "Toy Bonnie": [(9, 3), (3, 4), (4, 2), (2, 6), (6, 102), (102, 104)],
    "Toy Chica": [(9, 7), (7, 4), (4, 101), (101, 1), (1, 5), (5, 103), (103, 104)],
    "Toy Freddy": [(9, 10), (10, 101), (101, 104)],
    "Withered Bonnie": [(8, 7), (7, 101), (101, 5), (5, 104)],
    "Withered Chica": [(8, 4), (4, 2), (2, 6), (6, 104)],
    "Withered Freddy": [(8, 7), (7, 3), (3, 101), (101, 104)],
    "Foxy": [(8, 101), (101, 104)],
    "Mangle": [(12, 11), (11, 10), (10, 7), (7, 1), (1, 2), (2, 6), (6, 101), (101, 102), (102, 104)],
    "Balloon Boy": [(10, 5), (5, 103), (103, 104)],
    "Puppet": [(11, 104)],
}

POS = {
    8: (0, 4.5), 7: (2, 4.5), 9: (5, 5),
    3: (0, 3), 4: (2, 3), 10: (5, 3.5),
    1: (0, 1.5), 2: (2, 1.5), 11: (5, 2),
    5: (0, 0), 6: (5, 0),
    101: (2.5, -0.2), 103: (1.2, -0.8), 102: (3.8, -0.8),
    104: (2.5, -2), 12: (5, -1)
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
    G, POS, node_color=node_colors, node_size=node_sizes,
    edgecolors="white", linewidths=2, ax=ax
)

nx.draw_networkx_labels(
    G, POS, labels=NODE_LABELS, font_size=8,
    font_color="white", font_weight="bold", ax=ax
)

for character, edges in MOVEMENTS.items():
    is_target = character == TARGET
    nx.draw_networkx_edges(
        G, POS, edgelist=edges,
        edge_color=HIGHLIGHT_COLOR if is_target else FADE_COLOR,
        width=3.2 if is_target else 1.2,
        alpha=1.0 if is_target else 0.25,
        arrows=True,
        arrowstyle="-|>",
        arrowsize=26 if is_target else 14,
        min_source_margin=25,
        min_target_margin=25,
        connectionstyle="arc3,rad=0.08",
        ax=ax
    )

markov_mod = import_module("2_markov")
chain = markov_mod.build_markov_chain(TARGET, AI_LEVEL)

edge_prob_labels = {}
for src, dst in MOVEMENTS[TARGET]:
    p = chain[src][dst]
    edge_prob_labels[(src, dst, 0)] = f"p={p:.3f}"

nx.draw_networkx_edge_labels(
    G, POS, edge_labels=edge_prob_labels,
    font_size=8, font_color=HIGHLIGHT_COLOR, ax=ax,
    bbox=dict(facecolor="white", edgecolor="none", alpha=0.7, pad=0.5)
)

times = abs_mod.expected_absorption_time(TARGET, AI_LEVEL)
for state, t in times.items():
    x, y = POS[state]
    ax.text(
        x, y + 0.35, f"{t/1000:.1f}s",
        color=HIGHLIGHT_COLOR, fontsize=9, fontweight="bold",
        ha="center", va="bottom"
    )

legend_elements = [
    Line2D([0], [0], color=HIGHLIGHT_COLOR, lw=3, label=TARGET),
    Line2D([0], [0], color=FADE_COLOR, lw=1.5, label="Animatronik lain"),
    mpatches.Patch(facecolor="#1C2951", edgecolor="white", label="Camera Room"),
    mpatches.Patch(facecolor="#2C3E50", edgecolor="white", label="Hallway / Vent"),
    mpatches.Patch(facecolor="#E74C3C", edgecolor="white", label="Office"),
]

ax.legend(
    handles=legend_elements, loc="center left", bbox_to_anchor=(1.02, 0.5),
    fontsize=9, title=f"AI Level = {AI_LEVEL}", framealpha=1
)

plt.subplots_adjust(right=0.78)
ax.set_title(f"Jalur Pergerakan {TARGET} dan Expected Absorption Time", color="black", fontsize=13)
ax.axis("off")
plt.savefig("graph_foxy.png", dpi=600, bbox_inches="tight")
plt.show()