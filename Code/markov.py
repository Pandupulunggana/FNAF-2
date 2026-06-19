from importlib import import_module

bobot = import_module("1_bobot")

OFFICE_STATE = 104

ROUTES: dict[str, list[int]] = {
    "Toy Bonnie":       [9, 3, 4, 2, 6, 102, 104],
    "Toy Chica":        [9, 7, 4, 101, 1, 5, 103, 104],
    "Toy Freddy":       [9, 10, 101, 104],
    "Withered Bonnie":  [8, 7, 101, 5, 104],
    "Withered Chica":   [8, 4, 2, 6, 104],
    "Withered Freddy":  [8, 7, 3, 101, 104],
    "Foxy":             [8, 101, 104],
    "Mangle":           [12, 11, 10, 7, 1, 2, 6, 101, 102, 104],
    "Balloon Boy":      [10, 5, 103, 104],
    "Puppet":           [11, 104],
}


def build_markov_chain(route: list[int], ai_level: int, dt: float = 1000.0
                        ) -> dict[int, dict[int, float]]:
    w = bobot.transition_weight(ai_level, dt)
    chain: dict[int, dict[int, float]] = {}

    for idx, state in enumerate(route):
        if state == OFFICE_STATE:
            chain[state] = {OFFICE_STATE: 1.0}
            continue

        next_state = route[idx + 1]
        chain[state] = {
            next_state: w,
            state: 1.0 - w,
        }

    return chain