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
import time

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
        try:
            chris = np.loadtxt('initsols/'+self.instance+'CHRISTOFIDES.txt',dtype=int,delimiter='-')
            chris = [int(i) for i in chris]
        except:
            chris = None
        try:
            pca = np.loadtxt('initsols/'+self.instance+'PCA.txt',dtype=int,delimiter='-')
            pca = [int(i) for i in pca]
        except:
            pca = None
        try:
            savings = np.loadtxt('initsols/' +self.instance+ 'SAVINGS.txt',dtype=int,delimiter='-')
            savings = [int(i) for i in savings]
        except:
            savings = None
        lis = [chris,pca,savings]
        pop = [i for i in lis if i != None]
        for i in range(pop_size - len(pop)  + 1):
            pop.append(random.sample(a, len(a)))
        return pop

    def mutate_position(self,position, n):
        idx1, idx2 = random.sample(range(n), 2)
        new_position = position.copy()
        new_position[idx1], new_position[idx2] = new_position[idx2], new_position[idx1]
        return new_position

    def discrete_pso(self, population_size):
        fitness_function = self.custom_fitness_function
        population = self.generate_initial_population(population_size)
        personal_best = population.copy()
        personal_best_fitness = [fitness_function(p) for p in personal_best]
        global_best = min(personal_best, key=fitness_function)
        global_best_fitness = fitness_function(global_best)
        for i in range(20):
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
            print("Global best:", global_best)
            print("Global best fitness:", global_best_fitness)

        return global_best_fitness
    
if __name__ == '__main__':
    # Run memetic algorithm
    #np.random.seed(random.randint(0,1000))
    n = 10  # Length of the list
    DOE = np.loadtxt('Tiguchi\PSODOE.txt',delimiter=',')
    PPSO = PSO('A1')
    for index,i in enumerate(DOE):
        for j in range(5):
            print(i)
            firs = time.time()
            best_solution = PPSO.discrete_pso(int(i[0]))
            with open('Tiguchi\PSOAns.txt','a') as f:
                #write best solution to f and go to next line
                f.write(str(time.time() - firs)+","+ str(index)+"," + str(best_solution)+'\n')