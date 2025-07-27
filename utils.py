import random, math, time
from typing import List, Dict
from city import City, total_distance

def fitness(route: List[City]) -> float:
    return 1.0 / total_distance(route)

def parse_params(path: str) -> Dict[str, str]:
    params = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                k, v = [s.strip() for s in line.split("=", 1)]
                params[k.lower()] = v
    return params

def parse_cities(coord_string: str) -> List[City]:
    cities = []
    for token in coord_string.split(";"):
        name, coords = token.split(":")
        x, y = coords.split(",")
        cities.append(City(name.strip(), float(x), float(y)))
    return cities

def timer():
    """Simple context‑manager timer."""
    class _Timer:
        def __enter__(self): self.t0=time.time(); return self
        def __exit__(self, *exc): self.dt=time.time()-self.t0
    return _Timer()
