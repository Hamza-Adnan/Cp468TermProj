import random

def swap_mutation(chromosome):
    """
    Performs swap mutation on a given tour.
    Swaps two cities randomly.

    Takes a chromosome (a list which represents a permutation of city indices)
    in TSP papers, it's sometimes called a tour

    Returns 2 cities swapped
    """
    mutated = chromosome[:]
    i, j = random.sample(range(len(mutated)), 2)
    mutated[i], mutated[j] = mutated[j], mutated[i]
    return mutated
