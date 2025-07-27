import sys
from utils import parse_params, parse_cities, timer
from ga import GeneticAlgorithm
from city import total_distance

def main():
    if len(sys.argv)!=2:
        sys.exit("Usage: python main.py config.txt")
    p = parse_params(sys.argv[1])
    if "city_coords" not in p:
        sys.exit("config must include 'city_coords =' line")
    cities = parse_cities(p["city_coords"])
    ga = GeneticAlgorithm(cities, p)
    with timer() as t:
        best = ga.evolve()
    print("\n=== Best tour ===")
    print(" -> ".join([c.name for c in best] + [best[0].name]))
    print(f"Distance : {total_distance(best):.3f}")
    print(f"Elapsed  : {t.dt:.2f}s")

if __name__ == "__main__":
    main()
