import random


def uniform_crossover(par1, par2):
    """
    Performs uniform crossover by picking each city from either
    parent at random, but we’re modifying it to not repeat a 
    city as its a permutation.
    Inputs:
        2 parent lists as input
        par1 (list): First parent
        par2 (list): Second parent
    Returns:
        list: returns a list of Offspring tour which is a 
        permutation of cities
    """
    par1_length = len(par1)
    stores_mask = [random.randint(0, 1) for _ in range(par1_length)]
    index_par2 = 0
    offsprg = [None] * par1_length
    visited_set = set()
    # This loop will copy genes from first parent where mask is 1
    for i in range(par1_length):
        if (1 == stores_mask[i]):
            visited_set.add(par1[i])
            offsprg[i] = par1[i]
    # This loop will fill the remaining positions with second parents unused cities in order
    for j in range(par1_length):
        if (offsprg[j] is None):
            while (par2[index_par2] in visited_set):
                index_par2 = index_par2+1
            visited_set.add(par2[index_par2])
            offsprg[j] = par2[index_par2]
            index_par2 = index_par2 + 1
    return offsprg
