import numpy as np
from importlib import import_module

markov = import_module("2_markov")


def build_transition_matrix(route: list[int], ai_level: int, dt: float = 1000.0
                             ) -> tuple[np.ndarray, list[int]]:
    chain = markov.build_markov_chain(route, ai_level, dt)

    states = list(dict.fromkeys(route))
    n = len(states)
    index = {s: i for i, s in enumerate(states)}

    P = np.zeros((n, n))
    for state, transitions in chain.items():
        i = index[state]
        for target, prob in transitions.items():
            j = index[target]
            P[i, j] = prob

    return P, states


def partition_QR(P: np.ndarray, states: list[int], absorbing_state: int = 104
                  ) -> tuple[np.ndarray, np.ndarray, list[int]]:
    absorb_idx = states.index(absorbing_state)
    transient_idx = [i for i in range(len(states)) if i != absorb_idx]

    Q = P[np.ix_(transient_idx, transient_idx)]
    R = P[np.ix_(transient_idx, [absorb_idx])]
    transient_states = [states[i] for i in transient_idx]

    return Q, R, transient_states