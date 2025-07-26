import random

def tournament_selection(population, fitness_fn, tournament_size=5):
    """
    Selects the best chromosome from a random subset (tournament) of the population.
    requires; population, fitness function, tournament size
    """
    tournament = random.sample(population, tournament_size)
    best = min(tournament, key=fitness_fn)
    return best
