import numpy as np
import matplotlib.pyplot as plt
from importlib import import_module

matrix_mod = import_module("3_matrix")

TARGETS = ["Foxy", "Mangle", "Toy Bonnie"]
AI_LEVEL = 10

for name in TARGETS:
    P, states = matrix_mod.build_transition_matrix(name, AI_LEVEL)
    n = len(states)

    fig, ax = plt.subplots(figsize=(0.9 * n + 2, 0.9 * n + 1))
    ax.axis("off")

    cell_text = [[f"{val:.3f}" for val in row] for row in P]
    table = ax.table(
        cellText=cell_text,
        rowLabels=[str(s) for s in states],
        colLabels=[str(s) for s in states],
        cellLoc="center",
        loc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.6)

    for (row, col), cell in table.get_celld().items():
        if row == 0 or col == -1:
            cell.set_facecolor("#1C2951")
            cell.set_text_props(color="white", fontweight="bold")
        else:
            value = P[row - 1, col]
            if value > 0:
                cell.set_facecolor("#F4D9D9" if value < 1 else "#E74C3C")

    ax.set_title(f"Matriks Transisi P — {name} (AI Level = {AI_LEVEL})", fontsize=12, pad=20)
    plt.savefig(f"matrix_{name.lower().replace(' ', '_')}.png", dpi=300, bbox_inches="tight")
    plt.show()