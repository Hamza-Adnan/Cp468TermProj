import random
from typing import List
from city import City

def inversion(route: List[City]) -> None:
    a, b = sorted(random.sample(range(len(route)), 2))
    route[a:b+1] = reversed(route[a:b+1])

def swap(route: List[City]) -> None:
    a, b = random.sample(range(len(route)), 2)
    route[a], route[b] = route[b], route[a]

MUTATIONS = {"inversion": inversion, "swap": swap}
