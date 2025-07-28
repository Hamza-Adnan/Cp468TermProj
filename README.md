# CP468: Genetic Algorithm for the Traveling Salesman Problem (TSP)

This project uses a **Genetic Algorithm (GA)** to find good routes for the Traveling Salesman Problem. The goal is to find the shortest possible path that visits every city exactly once and returns to the starting point.

---

## What It Does

The algorithm starts with a bunch of random routes and gradually improves them over many generations by:

- **Selecting parents** using tournament selection — picking the best among random groups.  
- **Combining parents** with crossover operators (like `order` or `uniform`) to create children routes.  
- **Mutating children** randomly to explore new possibilities (using `inversion` or `swap`).  
- **Preserving the best routes** each generation with elitism to make sure progress is kept.

By repeating these steps, the GA searches for routes with shorter total distances.

---

## Project Files

- **city.py**: Defines the `City` class and methods to calculate distances between cities.  
- **config.txt**: Where you list the cities and adjust all the GA settings.  
- **crossover.py**: Contains crossover functions to mix two parent routes into a child route.  
- **mutation.py**: Contains mutation functions that slightly change routes to maintain diversity.  
- **selection.py**: Implements tournament selection to choose parents for breeding.  
- **ga.py**: The core GA engine — runs generations, applies selection, crossover, mutation, and elitism.  
- **main.py**: Entry point script that loads configuration, runs the GA, and prints results.  
- **utils.py**: Helper functions for reading configs, parsing cities, and timing the process.

---

## How to Run

1. **Edit `config.txt` to set up your cities and tweak the GA parameters:**

   - **Define your cities:**  
     List all the cities you want the algorithm to visit. For each city, write its name and the coordinates separated by a colon, and separate different cities with semicolons (`;`).  
     *Example:*  
     ```
     city_coords = C1:81,14; C2:3,94; C3:35,31; C4:28,17; C5:94,13
     ```

   - **Adjust the GA settings:**  
     Here’s what each setting does and how changing it might affect the run:

     - **`population_size`**  
       Number of routes in each generation. More routes mean the GA can explore more options, usually leading to better solutions, but it also makes the program run slower.  
       *Example:* `600`

     - **`num_generations`**  
       How many rounds of evolution the algorithm runs. Running more generations gives the GA more chances to improve routes but takes longer to finish.  
       *Example:* `2000`

     - **`children_per_generation`**  
       How many new routes get created each generation. Larger numbers add variety but increase computation time.  
       *Example:* `300`

     - **`tournament_size`**  
       How many candidates compete when picking parents. Bigger tournament sizes increase selection pressure (favoring better parents), speeding up improvement but possibly reducing diversity.  
       *Example:* `7`

     - **`crossover`**  
       How two parent routes combine into a child. `order` preserves city order (generally better for TSP), while `uniform` picks cities randomly from parents.  
       *Example:* `order`

     - **`mutation`**  
       How children get randomly tweaked. `inversion` reverses a chunk of the route, while `swap` exchanges two cities. Mutation helps avoid getting stuck in poor solutions.  
       *Example:* `inversion`

     - **`mutation_rate`**  
       Probability (0 to 1) that any given child gets mutated. Higher rates mean more random changes — good for exploring new solutions but can disrupt good routes if too high.  
       *Example:* `0.30`

     - **`elitism`**  
       Number of the best routes carried unchanged to the next generation. Protects top solutions but too many reduce variety.  
       *Example:* `1`

     - **`seed` (optional)**  
       Random seed to reproduce the same results on multiple runs. Handy for debugging or comparing changes.  
       *Example:* `42`

   Just write each line like `parameter_name = value` without any quotes or extra spaces.

2. Run the program with this command:

```bash
python main.py config.txt