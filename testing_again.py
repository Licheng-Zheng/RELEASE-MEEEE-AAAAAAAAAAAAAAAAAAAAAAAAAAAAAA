import random
from deap import base, creator, tools, algorithms
import numpy as np
import matplotlib.pyplot as plt

# Define the fitness function
def eval_function(individual):
    return (individual[0]**2,)

# Create the toolbox with the right parameters
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -10, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_function)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)
    population = toolbox.population(n=300)
    ngen = 40
    cxpb = 0.5
    mutpb = 0.2

    # Run the algorithm
    algorithms.eaSimple(population, toolbox, cxpb, mutpb, ngen, stats=None, halloffame=None, verbose=True)

    # Print the best individual
    best_ind = tools.selBest(population, 1)[0]
    print(f'Best individual: {best_ind}, Fitness: {best_ind.fitness.values[0]}')

if __name__ == "__main__":
    main()

