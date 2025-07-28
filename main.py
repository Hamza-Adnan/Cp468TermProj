import sys
import matplotlib.pyplot as plt

from utils import parse_params, parse_cities
from ga import GeneticAlgorithm
from city import total_distance


def plot_convergence(history, out_png):
    """Show the convergence plot if a GUI is available; always save PNG."""
    if not history:
        return

    plt.figure()
    plt.plot(range(1, len(history) + 1), history)
    plt.title("GA Convergence")
    plt.xlabel("Generation")
    plt.ylabel("Best distance")
    plt.tight_layout()

    # Try to pop up a window (will fail gracefully on head‑less systems)
    try:
        plt.show(block=False)
    except Exception:
        pass

    plt.savefig(out_png)
    print(f"[+] Convergence curve saved to {out_png}")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage:  python main.py  config.txt")

    p = parse_params(sys.argv[1])
    if "city_coords" not in p:
        sys.exit("Config file must include a 'city_coords =' line")

    cities = parse_cities(p["city_coords"])
    ga     = GeneticAlgorithm(cities, p)

    # ---------- run GA ----------
    best = ga.evolve()

    # ---------- plot convergence ----------
    if p.get("enable_convergence_plot", "true").lower() == "true":
        out_png = p.get("convergence_png", "convergence.png")
        plot_convergence(ga.history, out_png)

    # ---------- final summary ----------
    print("\n=== Best tour ===")
    print(" -> ".join([c.name for c in best] + [best[0].name]))
    print(f"Distance : {total_distance(best):.3f}")


if __name__ == "__main__":
    main()
