import numpy as np
from importlib import import_module

matrix_mod = import_module("3_matrix")


def fundamental_matrix(Q: np.ndarray) -> np.ndarray:
    n = Q.shape[0]
    I = np.eye(n)
    return np.linalg.inv(I - Q)


def expected_steps(N: np.ndarray) -> np.ndarray:
    ones = np.ones((N.shape[0], 1))
    return N @ ones


def expected_absorption_time(route: list[int], ai_level: int, dt: float = 1000.0
                              ) -> dict[int, float]:
    P, states = matrix_mod.build_transition_matrix(route, ai_level, dt)
    Q, R, transient_states = matrix_mod.partition_QR(P, states)

    N = fundamental_matrix(Q)
    t_steps = expected_steps(N)
    t_time = t_steps.flatten() * dt

    return dict(zip(transient_states, t_time))