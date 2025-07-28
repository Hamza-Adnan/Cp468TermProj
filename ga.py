import random, copy
from typing import List, Dict
from city import City, total_distance
from selection import tournament
from crossover import CROSSOVERS
from mutation import MUTATIONS


class GeneticAlgorithm:
    """
    Core GA engine — now records best distance each generation in self.history.
    """

    def __init__(self, cities: List[City], p: Dict[str, str]):
        # ------------ GA hyper‑parameters ------------
        self.cities      = cities
        self.pop_size    = int(p.get("population_size", 200))
        self.generations = int(p.get("num_generations", 500))
        self.children    = int(p.get("children_per_generation", 100))
        self.tourn_k     = int(p.get("tournament_size", 5))
        self.mut_rate    = float(p.get("mutation_rate", 0.2))
        self.elitism     = int(p.get("elitism", 1))

        # ------------ Operators ------------
        self.xo_fn  = CROSSOVERS[p.get("crossover", "order").lower()]
        self.mut_fn = MUTATIONS[p.get("mutation", "inversion").lower()]

        # ------------ Optional RNG seed ------------
        if "seed" in p:
            random.seed(int(p["seed"]))

        # ------------ Initial population ------------
        self.population = [random.sample(cities, len(cities))
                           for _ in range(self.pop_size)]

        # ------------ Convergence trace ------------
        self.history: List[float] = []        # best distance after each generation

    # -------------------------------------------------

    def evolve(self) -> List[City]:
        """Run GA loop, return best tour found."""
        best = min(self.population, key=total_distance)

        for g in range(1, self.generations + 1):

            # ---- elitism ----
            new_pop = sorted(self.population, key=total_distance)[:self.elitism]

            # ---- breeding ----
            while len(new_pop) < self.pop_size:
                p1 = tournament(self.population, self.tourn_k)
                p2 = tournament(self.population, self.tourn_k)

                child = self.xo_fn(p1, p2)

                if random.random() < self.mut_rate:
                    self.mut_fn(child)

                new_pop.append(child)

            self.population = new_pop

            candidate = min(self.population, key=total_distance)
            if total_distance(candidate) < total_distance(best):
                best = copy.deepcopy(candidate)

            # ---- record convergence ----
            self.history.append(total_distance(best))

            if g == 1 or g % 50 == 0:
                print(f"Gen {g:4d}: best = {total_distance(best):.3f}")

        return best
