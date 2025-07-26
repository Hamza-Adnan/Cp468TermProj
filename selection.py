import random
from typing import List
from city import City, total_distance

def tournament(pop: List[List[City]], k: int) -> List[City]:
    """k‑way tournament selection (lower distance wins)."""
    return min(random.sample(pop, k), key=total_distance)
