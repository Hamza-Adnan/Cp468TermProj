import random
from tournament_selection import tournament_selection
from uniform_crossover import uniform_crossover
from swap_mutation import swap_mutation
import math

def compute_total_distance(chromosome, city_coords):
    """
    Calculate the total distance of the tour represented by the chromosome.
    Uses Euclidean distance (sqrt((x2 - x1)^2 + (y2 - y1)^2))
    """
  
    total_distance = 0.0
    num_cities = len(chromosome)
    
    for i in range(num_cities):
        city_a = city_coords[chromosome[i]]
        city_b = city_coords[chromosome[(i + 1) % num_cities]]  
        
        # Euclidean distance, sqrt((x2 - x1)^2 + (y2 - y1)^2)
        dist = math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)
        total_distance += dist
        
    return total_distance

def initialize_population(city_map, population_size):
    cities = list(range(len(city_map)))
    population = []
  
    for _ in range(population_size):
        # Create a random permutation of cities for each individual
        c = random.sample(cities, len(cities))
        population.append(c)
      
    return population

def fitness_function(population, city_map):
    fitnesses = []
  
    for chromosome in population:
        distance = compute_total_distance(chromosome, city_map)
        fitnesses.append(distance)
    return fitnesses

def select_parents(population, fitnesses):
    return tournament_selection(population, fitnesses)

def generate_new_population(population, city_map, mutation_rate):
    fitnesses = fitness_function(population, city_map)
    new_population = []

  # UNFINISHED

    return new_population

def genetic_algorithm(city_map, population_size, mutation_rate, generations):
#UNFINISHED
