# ---------------------------------------------------------------------------
# main.py  —  now includes elapsed‑time reporting
# ---------------------------------------------------------------------------
import sys
import matplotlib.pyplot as plt
from utils import parse_params, parse_cities, timer          # <- timer imported
from ga import GeneticAlgorithm
from city import total_distance


# ---------- plotting helper (unchanged except for docstring tweak) ----------
def plot_curve(values, title, y_label, out_png, *, color=None):
    """
    Display (if possible) and save a single curve to 'out_png'.
    Pass color="red" etc. to override the default line colour.
    """
    if not values:
        return

    plt.figure()
    plt.plot(range(1, len(values) + 1), values, color=color)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel(y_label)
    plt.tight_layout()

    try:               # on GUI‑less backends this will error → skip
        plt.show(block=False)
    except Exception:
        pass

    plt.savefig(out_png)
    print(f"[+] Saved {out_png}")
# ---------------------------------------------------------------------------


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage:  python main.py  config.txt")

    # ---------- 1. Load config ----------
    p = parse_params(sys.argv[1])
    if "city_coords" not in p:
        sys.exit("Config must contain a 'city_coords =' line")

    # ---------- 2. Build GA ----------
    cities = parse_cities(p["city_coords"])
    ga     = GeneticAlgorithm(cities, p)

    # ---------- 3. Run GA with timer ----------
    with timer() as t:                     # <-- start stopwatch
        best = ga.evolve()                 #     run evolutionary loop
    elapsed_sec = t.dt                     # <-- seconds elapsed

    # ---------- 4. Convergence plots ----------
    if p.get("enable_convergence_plot", "true").lower() == "true":

        # Distance curve
        plot_curve(
            ga.history,
            "GA Convergence (distance)",
            "Distance",
            p.get("distance_png", "convergence_distance.png")
        )

        # Fitness curve (red line)
        fitness_history = [1.0 / d if d else 0 for d in ga.history]
        plot_curve(
            fitness_history,
            "GA Convergence (fitness)",
            "Fitness",
            p.get("fitness_png", "convergence_fitness.png"),
            color="red"
        )

    # ---------- 5. Final summary ----------
    print("\n=== Best tour ===")
    print(" -> ".join([c.name for c in best] + [best[0].name]))
    print(f"Distance : {total_distance(best):.3f}")
    print(f"Elapsed  : {elapsed_sec:.2f} seconds")        # <-- timer output


if __name__ == "__main__":
    main()
