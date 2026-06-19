T0 = 50_000
K_FACTOR = 157
MAX_AI_LEVEL = 20


def movement_time(ai_level: int) -> float:
    if not (0 <= ai_level <= MAX_AI_LEVEL):
        raise ValueError(f"AI Level harus 0..{MAX_AI_LEVEL}, didapat {ai_level}")
    return max(T0 - ai_level * K_FACTOR, 1.0)


def move_threshold_time(ai_level: int) -> float:
    if ai_level == 0:
        return float("inf")
    return movement_time(ai_level) / ai_level


def transition_weight(ai_level: int, dt: float = 1000.0) -> float:
    t_wait = move_threshold_time(ai_level)
    if t_wait == float("inf"):
        return 0.0
    return min(1.0, dt / t_wait)


def transition_weight_foxy(ai_level: int, dt: float = 1000.0) -> float:
    if ai_level == 0:
        return 0.0
    t_wait = movement_time(ai_level) / ((ai_level + 1) * 1.2)
    return min(1.0, dt / t_wait)


def transition_weight_balloon_boy_first(ai_level: int, dt: float = 1000.0) -> float:
    if ai_level == 0:
        return 0.0
    t_wait = (movement_time(ai_level) + 96_000) / ai_level
    return min(1.0, dt / t_wait)