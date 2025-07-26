import random
from typing import List
from city import City

def order_xo(p1: List[City], p2: List[City]) -> List[City]:
    size = len(p1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[a:b+1] = p1[a:b+1]
    fill = [c for c in p2 if c not in child]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = fill[idx]; idx += 1
    return child

def uniform_xo(p1: List[City], p2: List[City]) -> List[City]:
    size = len(p1)
    mask = [random.randint(0,1) for _ in range(size)]
    child, chosen = [None]*size, set()
    for i, bit in enumerate(mask):
        if bit:
            child[i] = p1[i]; chosen.add(p1[i])
    fill = [c for c in p2 if c not in chosen]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = fill[idx]; idx += 1
    return child

CROSSOVERS = {"order": order_xo, "uniform": uniform_xo}
