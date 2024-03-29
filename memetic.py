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
class MA(object):
    def __init__(self,instance):
        self.instance = instance
        self.nurses,self.patients,self.TW = reader(self.instance)
        self.Costmat = matcord(rcord(self.instance))
# Placeholder functions for fitness function and initial population
    def fitness(self,solution):
        a = Split(self.instance,permutation=solution)
        return a[2]

    def initial_population(self,pop_size):
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

    # Order Crossover (OX) function
    def ox(self,parent1, parent2):
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
    def tournament_selection(self,population, tournament_size):
        tournament = random.sample(population, tournament_size)
        best = None
        best_fitness = None
        for individual in tournament:
            fitness_val = self.fitness(individual)
            if best is None or fitness_val < best_fitness:
                best = individual
                best_fitness = fitness_val
        return best

    # OR-opt operator
    def or_opt(self,solution):
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
    def two_opt(self,solution):
        n = len(solution)
        i, j = sorted(random.sample(range(n), 2))
        if i == 0 and j == n-1:
            return None
        if i > j:
            i, j = j, i
        new_solution = solution[:i] + list(reversed(solution[i:j+1])) + solution[j+1:]
        return new_solution

    import random

    def scramble_mutation(self,solution, mutation_rate):
        # Copy the original solution
        mutated_solution = solution.copy()

        # Determine the subset of genes to scramble
        subset_size = int(len(solution) * mutation_rate)
        start_index = random.randint(0, len(solution) - subset_size)
        end_index = start_index + subset_size

        # Scramble the subset of genes
        subset = mutated_solution[start_index:end_index]
        random.shuffle(subset)

        # Update the mutated solution with the scrambled subset
        mutated_solution[start_index:end_index] = subset

        return mutated_solution


    def local_search(self,solution):
        neighborhoods = [self.or_opt, self.two_opt]
        shuffle(neighborhoods)
        current_solution = solution
        moves_left = 10 # set the maximum number of movements to 10
        while moves_left > 0:
            best_neighbor = None
            best_fitness = self.fitness(current_solution)
            for neighborhood in neighborhoods:
                neighbor = neighborhood(current_solution)
                if neighbor is None:
                    continue
                neighbor_fitness = self.fitness(neighbor)
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
    def memetic_algorithm(self,pop_size, num_generations, local_search_prob, crossover_prob,mut_prob, tournament_size):
        Gen = []
        BG = []
        BO = []
        BS = []
        MP = []
        # Generate initial population
        population = self.initial_population(pop_size)

        for generation in range(num_generations):
            # Evaluate fitness of population
            fitness_scores = [self.fitness(solution) for solution in population]

            # Sort population by fitness in descending order
            population_fitness = list(zip(population, fitness_scores))
            population_fitness.sort(key=lambda x: x[1], reverse=True)
            population = [p[0] for p in population_fitness]

            shuffle(population)
            # Apply crossover using OX operator to a subset of the population
            for i in range(int(crossover_prob * pop_size)):
                parent1 = self.tournament_selection(population, tournament_size)
                parent2 = self.tournament_selection(population, tournament_size)
                offspring = self.ox(parent1, parent2)
                population.append(offspring)
            #apply mutation
            for i in range(int(mut_prob * pop_size)):
                parent = self.tournament_selection(population, tournament_size)
                offspring = self.scramble_mutation(parent, 0.6)
                population.append(offspring)
            
            # Apply local search to a subset of the population
            for i in range(int(local_search_prob * pop_size)):
                population[i] = self.local_search(population[i])
            population = [x for i,x in enumerate(population) if x not in population[:i]]
            #Remove least fit individuals from population
            num_to_remove = len(population) - pop_size
            print(len(population))
            if num_to_remove > 0:
                fitness_scores = [self.fitness(solution) for solution in population]
                population_fitness = list(zip(population, fitness_scores))
                population_fitness.sort(key=lambda x: x[1],reverse=True)
                population = [p[0] for p in population_fitness[num_to_remove:]]
            print('Generation %s: %s' % (generation, population_fitness[-1][1]))
            Gen.append(generation)
            BG.append(population_fitness[-1][1])
            #get mean of population fitness
            MP.append(sum(fitness_scores)/len(fitness_scores))
            if BO == []:
                BO.append(population_fitness[-1][1])
                BS.append(population_fitness[-1][0])
            else:
                if population_fitness[-1][1] < BO[-1]:
                    BO.append(population_fitness[-1][1])
                    BS.append(population_fitness[-1][0])
                else:
                    BO.append(BO[-1])
                    BS.append(BS[-1])

        # Return best solution
        fitness_scores = [self.fitness(solution) for solution in population]
        population_fitness = list(zip(population, fitness_scores))
        population_fitness.sort(key=lambda x: x[1])
        return Gen , BG , BO , BS , MP

if __name__ == '__main__':
    # Run memetic algorithm
    #np.random.seed(random.randint(0,1000))
    ins = ['C1','C2','C3','C4','C5','C6','C7']
    for i in ins:
        print(i)
        mma = MA(i)
        best_solution = mma.memetic_algorithm(pop_size=15, num_generations=20, local_search_prob=0.1, crossover_prob=0.6,mut_prob=0.3,tournament_size=4)
        print('Best solution: %s' % best_solution[3][-1])
        print('Best solution fitness: %s' % best_solution[2][-1])
        with open('Soloutions\\'+mma.instance+'.txt','w') as f:
            for item in best_solution:
                f.write(",".join(str(x) for x in item) + "\n")