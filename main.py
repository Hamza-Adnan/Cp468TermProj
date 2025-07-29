import sys
import matplotlib.pyplot as plt

from utils import parse_params, parse_cities
from ga import GeneticAlgorithm
from city import total_distance


# --------------- plotting helper ---------------
def plot_curve(values, title, y_label, out_png, *, color=None):
    """
    Display (if possible) and save a single curve.

    `color` is optional; pass e.g. color="red" to override the default.
    """
    if not values:
        return

    plt.figure()
    plt.plot(range(1, len(values) + 1), values, color=color)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel(y_label)
    plt.tight_layout()

    try:             # pop up a window when GUI backend is present
        plt.show(block=False)
    except Exception:
        pass

    plt.savefig(out_png)
    print(f"[+] Saved {out_png}")
# ----------------------------------------------


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage:  python main.py  config.txt")

    p = parse_params(sys.argv[1])
    if "city_coords" not in p:
        sys.exit("Config must contain a 'city_coords =' line")

    cities = parse_cities(p["city_coords"])
    ga     = GeneticAlgorithm(cities, p)

    # ------------- run GA -------------
    best = ga.evolve()

    # ------------- plots --------------
    if p.get("enable_convergence_plot", "true").lower() == "true":

        # 1) Distance curve (default Matplotlib color)
        plot_curve(
            ga.history,
            "GA Convergence (distance)",
            "Distance",
            p.get("distance_png", "convergence_distance.png")
        )

        # 2) Fitness curve (red line)
        fitness_history = [1.0 / d if d else 0 for d in ga.history]
        plot_curve(
            fitness_history,
            "GA Convergence (fitness)",
            "Fitness",
            p.get("fitness_png", "convergence_fitness.png"),
            color="red"                         # <‑‑‑ red line
        )

    # ------------- summary -------------
    print("\n=== Best tour ===")
    print(" -> ".join([c.name for c in best] + [best[0].name]))
    print(f"Distance : {total_distance(best):.3f}")


if __name__ == "__main__":
    main()
