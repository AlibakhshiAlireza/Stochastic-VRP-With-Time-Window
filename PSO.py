import numpy as np
import random
from utils import *
from reader import *
from phasetypes import *
import sys
sys.path.append('butools2/Python')
sys.path.append('MPMAVRPMain/butools2/Python')
from butools.ph import *
from butools.fitting import *
import matplotlib.pyplot as plt
from initpop import *

class PSO(object):
    def __init__(self,instance):
        self.instance = instance
        self.nurses,self.patients,self.TW = reader(self.instance)
        self.Costmat = matcord(rcord(self.instance))
    
    def custom_fitness_function(self,x):
        a = Split(self.instance,permutation=x)
        return a[2]

    def generate_initial_population(self,pop_size):
        a = list(range(1,self.patients+1))
        pop = []
        for i in range(pop_size - len(pop)  + 1):
            pop.append(random.sample(a, len(a)))
        return pop

    def mutate_position(self,position, n):
        idx1, idx2 = random.sample(range(n), 2)
        new_position = position.copy()
        new_position[idx1], new_position[idx2] = new_position[idx2], new_position[idx1]
        return new_position

    def discrete_pso(self, population_size, max_iter):
        Gen = []
        BG = []
        BO = []
        BS = []
        MP = []
        fitness_function = self.custom_fitness_function
        population = self.generate_initial_population(population_size)
        personal_best = population.copy()
        personal_best_fitness = [fitness_function(p) for p in personal_best]
        global_best = min(personal_best, key=fitness_function)
        global_best_fitness = fitness_function(global_best)

        for _ in range(max_iter):
            for i in range(population_size):
                new_position = self.mutate_position(population[i], n)
                new_fitness = fitness_function(new_position)

                if new_fitness < personal_best_fitness[i]:
                    personal_best[i] = new_position
                    personal_best_fitness[i] = new_fitness

                    if new_fitness < global_best_fitness:
                        global_best = new_position
                        global_best_fitness = new_fitness

                # Update population with probability 0.5
                if random.random() < 0.5:
                    population[i] = new_position
        Gen.append(_)
        BG.append(global_best_fitness)
        BO.append(global_best)
        BS.append(personal_best_fitness)
        MP.append(sum(personal_best_fitness)/len(personal_best_fitness))
        print("Iteration:", _)
        print("Global best:", global_best)
        print("Global best fitness:", global_best_fitness)

        return global_best, global_best_fitness

# Parameters
n = 10  # Length of the list
population_size = 25
max_iter = 20
PS1 = PSO('A1')
# Perform the optimization using discrete PSO
optimal_permutation, min_fitness = PS1.discrete_pso(population_size, max_iter)

print("Optimal permutation:", optimal_permutation)
print("Minimum fitness:", min_fitness)
