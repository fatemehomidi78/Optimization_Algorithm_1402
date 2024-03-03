import random
import numpy as np
import matplotlib.pyplot as plt

# Define problem parameters
num_generations = 100
population_size = 12
mutation_rate = 0.01
max_x1 = 4
max_x2 = 6
elitism_count = 2  # Choose how many individuals to carry over to the next generation

def generate_random_individual():
    x1 = random.uniform(0, max_x1)
    x2 = random.uniform(0, max_x2)
    return [x1, x2]

def fitness(x1, x2):
    return 3*x1**2 + 5*x2**2

def apply_constraints(x1, x2):
    x1 = min(x1, max_x1)
    x2 = min(x2, max_x2)
    if 3*x1 + 2*x2 > 18:
        excess = 3*x1 + 2*x2 - 18
        x1 -= excess / 3
        x2 -= excess / 2
    return x1, x2

def crossover(parent1, parent2):
    beta = random.uniform(-0.1, 1.1)  # Use beta method for crossover point
    child1 = [beta * p1 + (1 - beta) * p2 for p1, p2 in zip(parent1, parent2)]
    child2 = [beta * p2 + (1 - beta) * p1 for p1, p2 in zip(parent1, parent2)]
    return child1, child2

def mutate(individual):
    mutated = individual[:]
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = random.uniform(0, max_x1) if i == 0 else random.uniform(0, max_x2)
    return mutated

# Generate initial population
population = [generate_random_individual() for _ in range(population_size)]

# Initialize a list to store best fitness values
best_fitness_values = []

# Initialize a list to store elite individuals
elite_individuals = []

# Main loop
for generation in range(num_generations):
    # Evaluate fitness and apply constraints
    evaluated_population = []
    for individual in population:
        x1, x2 = apply_constraints(*individual)
        evaluated_population.append((individual, fitness(x1, x2)))

    # Sort by fitness
    evaluated_population.sort(key=lambda x: x[1], reverse=True)

    # Get the best solution
    best_individual = evaluated_population[0]
    best_x1, best_x2 = apply_constraints(*best_individual[0])

    # Store the best fitness value
    best_fitness_values.append(fitness(best_x1, best_x2))

    # Store elite individuals
    elite_individuals.extend([apply_constraints(*individual[0]) for individual in evaluated_population[:elitism_count]])

    # Select parents
    parents = [evaluated_population[i][0] for i in range(min(population_size//2, len(evaluated_population)))]

    # Apply crossover
    children = []
    for i in range(0, len(parents), 2):
        if i + 1 < len(parents) and random.random() < 0.8:  # Crossover rate
            child1, child2 = crossover(parents[i], parents[i+1])
            children.extend([child1, child2])
        else:
            children.extend([parents[i]])

    # Apply mutation
    population = [mutate(child) for child in children]

    # Add elite individuals to the population
    population.extend(elite_individuals)
    elite_individuals = []
    # Print top 100 individuals and their fitness values every 10 generations
    if generation % 10 == 0:
        print(f"Generation {generation}:")
        for i in range(min(100, len(evaluated_population))):
            ind = evaluated_population[i]
            x1, x2 = apply_constraints(*ind[0])
            print(f"Chromosome {i+1}: x1 = {x1:.4f}, x2 = {x2:.4f}, Fitness = {ind[1]:.4f}")
# Plot convergence
plt.plot(range(num_generations), best_fitness_values)
plt.xlabel('Generation')
plt.ylabel('Best Fitness Value')
plt.title('Convergence of Genetic Algorithm')
plt.show()

print(f"Best solution found: x1 = {best_x1}, x2 = {best_x2}, z = {fitness(best_x1, best_x2)}")
