#!/usr/bin/env python3

import random
import argparse

#
# Simple Differential Evolution algorithm to minimize Sphere Function
#

# Population individual
class Citizen:
    
    # Initialize object
    def __init__(self):
        self.members = list()
    
    # Randomize citizen members
    def randomize(self, dimension, minimum, maximum):
        for i in range(0, dimension):
            self.members.append(minimum + random.random() * (maximum - minimum))
        
    # Get fitness for this individual
    def evaluate(self):
        return sum([member**2 for member in self.members])
    
    # Convert to string
    def __str__(self):
        return "["+", ".join(['%.2f' % x for x in self.members])+"]"
    
# DifferentialEvolution algorithm
class DifferentialEvolution:
    
    def __init__(self, np, f, cr, d, minimum, maximum):
        self.np = np
        self.f = f
        self.cr = cr
        self.d = d
        self.minimum = minimum
        self.maximum = maximum
    
    # Mutation function
    def mutate(self, target, random1, random2, random3):
        mutation = Citizen()
        for i in range(0, self.d):
            member = random1.members[i] + self.f * (random2.members[i] - random3.members[i])
            mutation.members.append(member)
        return mutation
    
    # Crossover function
    def crossover(self, target, mutant):
        trial = Citizen()
        j = random.choice(range(0, self.d))
        for i in range(0, self.d):
            if random.random() <= self.cr or i == j:
                trial.members.append(mutant.members[i])
            else:
                trial.members.append(target.members[i])
        return trial
    
    # Evolution function
    def evolve(self, maxGeneration):
        
        generation = 0        
        population = list()
        
        # Phase 1: Initialization
        for i in range(0, self.np):
            citizen = Citizen()
            citizen.randomize(self.d, self.minimum, self.maximum)
            population.append(citizen)
        
        while generation < maxGeneration:
        
            mutants = list()
            trials = list()
        
            # Phase 2: Mutation
            for citizen in population:
                rest = list(population)
                rest.remove(citizen)
                other1 = random.choice(rest)
                other2 = random.choice(rest)
                other3 = random.choice(rest)
                mutant = self.mutate(citizen, other1, other2, other3)
                mutants.append(mutant)
            
            # Phase 3: Crossover
            for i in range(0, self.np):
                trial = self.crossover(population[i], mutants[i])
                trials.append(trial)
            
            # Phase 4: Selection
            for i in range(0, self.np):
                if trials[i].evaluate() <= population[i].evaluate():
                    population[i] = trials[i]
            
            print("Generation ", generation + 1, " done")
            generation = generation + 1
        
        
        # Return best result from last generation
        result = population[0]
        for citizen in population:
            if citizen.evaluate() < result.evaluate():
                result = citizen
        
        return result
        
        
# Main
def main():
    
    # Parse arguments
    parser = argparse.ArgumentParser(description='Differential Evolution algorithm to minimize the Sphere Function.')
    parser.add_argument('np', metavar='NP', type=int, help='population size')
    parser.add_argument('f', metavar='F', type=float, help='differential weight')
    parser.add_argument('cr', metavar='CR', type=float, help='crossover probability')
    parser.add_argument('d', metavar='D', type=int, help='problem dimension')
    parser.add_argument('minimum', metavar='MIN', type=float, help='minimum parameter value')
    parser.add_argument('maximum', metavar='MAX', type=float, help='maximum parameter value')
    parser.add_argument('generations', metavar='N_GENERATIONS', type=int, help='number of generations to evolve')
    args = parser.parse_args()
    
    # Set parameters for the algorithm
    de = DifferentialEvolution(args.np, args.f, args.cr, args.d, args.minimum, args.maximum)
    
    # Trigger evolution
    result = de.evolve(args.generations)
    
    # Print results
    print("Best individual: \n", result)
    print("Function value: \n", result.evaluate())

if __name__ == "__main__":
    main()