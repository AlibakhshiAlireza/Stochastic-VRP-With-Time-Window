import random
from phase import *
from phasetypes import *
from reader import *
from random import shuffle
from utils import *
import sys
sys.path.append('butools2/Python')
sys.path.append('MPMAVRPMain/butools2/Python')
from butools.ph import *
from butools.fitting import *
import time
import math
nurses,patients,TW = reader('A7')
Costmat = matcord(rcord('A7'))
# Placeholder functions for fitness function and initial population
def fitness(solution):
    a = Split('A7',permutation=solution)
    return a[2]

def initial_population(pop_size):
    a = list(range(1,patients+1))
    pop = []
    for i in range(pop_size + 1):
        pop.append(random.sample(a, len(a)))
    return pop

# Order Crossover (OX) function
def ox(parent1, parent2):
    size = len(parent1)
    a = random.randint(0, size-1)
    b = random.randint(a, size-1)
    child = [-1] * size
    for i in range(a, b+1):
        child[i] = parent1[i]
    remaining = [item for item in parent2 if item not in child]
    j = 0
    for i in range(size):
        if child[i] == -1:
            child[i] = remaining[j]
            j += 1
    return child

# Tournament selection function
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    best = None
    best_fitness = None
    for individual in tournament:
        fitness_val = fitness(individual)
        if best is None or fitness_val < best_fitness:
            best = individual
            best_fitness = fitness_val
    return best

# OR-opt operator
def or_opt(solution):
    n = len(solution)
    i, j = sorted(random.sample(range(n), 2))
    k, l = sorted(random.sample(range(n), 2))
    if i == k or j == l:
        return None
    if j < k:
        i, j, k, l = k, l, i, j
    new_solution = solution[:i] + solution[j:k+1] + solution[i:j] + solution[k+1:]
    return new_solution

# 2-opt operator
def two_opt(solution):
    n = len(solution)
    i, j = sorted(random.sample(range(n), 2))
    if i == 0 and j == n-1:
        return None
    if i > j:
        i, j = j, i
    new_solution = solution[:i] + list(reversed(solution[i:j+1])) + solution[j+1:]
    return new_solution


def local_search(solution):
    neighborhoods = [or_opt, two_opt]
    current_solution = solution
    moves_left = 3 # set the maximum number of movements to 3
    while moves_left > 0:
        best_neighbor = None
        best_fitness = fitness(current_solution)
        for neighborhood in neighborhoods:
            neighbor = neighborhood(current_solution)
            if neighbor is None:
                continue
            neighbor_fitness = fitness(neighbor)
            if neighbor_fitness < best_fitness:
                best_neighbor = neighbor
                best_fitness = neighbor_fitness
        if best_neighbor is not None:
            current_solution = best_neighbor
            moves_left -= 1 # decrement the number of moves left
        else:
            break
    return current_solution # return the best solution found with up to 3 cities



# Memetic algorithm with variable neighborhood search
def memetic_algorithm(pop_size, num_generations, local_search_prob, crossover_prob, mutation_prob, tournament_size):
    # Generate initial population
    population = initial_population(pop_size)

    for generation in range(num_generations):
        # Evaluate fitness of population
        fitness_scores = [fitness(solution) for solution in population]

        # Sort population by fitness in descending order
        population_fitness = list(zip(population, fitness_scores))
        population_fitness.sort(key=lambda x: x[1], reverse=True)
        population = [p[0] for p in population_fitness]

        # Apply local search to a subset of the population
        for i in range(int(local_search_prob * pop_size)):
            population[i] = local_search(population[i])

        # Apply crossover using OX operator to a subset of the population
        for i in range(int(crossover_prob * pop_size)):
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            offspring = ox(parent1, parent2)
            population.append(offspring)

        # Remove least fit individuals from population
        num_to_remove = len(population) - pop_size
        if num_to_remove > 0:
            population_fitness = list(zip(population, fitness_scores))
            population_fitness.sort(key=lambda x: x[1],reverse=True)
            population = [p[0] for p in population_fitness[num_to_remove:]]

    # Return best solution
    fitness_scores = [fitness(solution) for solution in population]
    population_fitness = list(zip(population, fitness_scores))
    population_fitness.sort(key=lambda x: x[1])
    return population_fitness[0][0] , population_fitness[0][1]

# Run memetic algorithm
start_time = time.time()
best_solution = memetic_algorithm(pop_size=10, num_generations=2, local_search_prob=0.1, crossover_prob=0.8, mutation_prob=0.1, tournament_size=2)
print('Best solution: %s' % best_solution[0])
print('Best solution fitness: %s' % best_solution[1])