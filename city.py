from math import hypot
from typing import List

class City:
    def __init__(self, name: str, x: float, y: float):
        self.name, self.x, self.y = name, x, y

    def dist(self, other: "City") -> float:
        return hypot(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return self.name

# handy one‑liner for closed‑tour distance
def total_distance(route: List["City"]) -> float:
    return sum(route[i].dist(route[(i + 1) % len(route)])
               for i in range(len(route)))
