import random


def init_population(count_of_cities, count_of_chain):
    chains = list()
    for i in range(count_of_chain):
        chain = [int(j) for j in range(count_of_cities)]
        random.shuffle(chain)
        chains.append(chain)
    return chains


def chain_weight(graph, chain):
    weight = 0
    for i in range(len(chain)-1):
        weight += graph[chain[i]][chain[i+1]]
    return weight


def crossbreeding(chain1, chain2):
    chain_result = [-1]*len(chain1)
    used_cities = []
    crossbreeding_flag = False
    processing_city = None
    indexes = []

    while len(used_cities) < len(chain1):
        if processing_city is None:
            for city in chain1:
                if city not in used_cities:
                    processing_city = city
                    break
        index = chain1.index(processing_city)
        indexes.append(index)
        used_cities.append(processing_city)
        processing_city = chain2[index]
        if processing_city in used_cities:
            crossbreeding_flag = True
            processing_city = None
        if crossbreeding_flag:
            dominant = random.randint(0, 1)
            for index in indexes:
                if dominant == 0:
                    chain_result[index] = chain1[index]
                else:
                    chain_result[index] = chain2[index]
            crossbreeding_flag = False
            indexes = []
    return chain_result


def mutation(chain):
    current_index = random.randint(0, len(chain)-1)
    if current_index == len(chain)-1:
        next_index = 0
    else:
        next_index = current_index+1
    chain_result = [elem for elem in chain]
    chain_result[current_index] = chain[next_index]
    chain_result[next_index] = chain[current_index]
    return chain_result


def evolution(graph, count_of_chains):
    population = init_population(len(graph), count_of_chains)
    n = 0
    k = 100
    while True:
        population = sorted(population, key=lambda elem: chain_weight(graph, elem))
        print("Population: ", n)
        for chain in population:
            print(chain_weight(graph, chain), chain)
        if k == 100:
            input()
            k = 0
        population = next_population(population)
        n += 1
        k += 1


def next_population(population):
    new_population = list()
    new_population.append(population[0])
    new_population.append(
        crossbreeding(population[0], population[9])
    )
    new_population.append(
        crossbreeding(population[1], population[8])
    )
    new_population.append(
        crossbreeding(population[2], population[7])
    )
    new_population.append(
        crossbreeding(population[3], population[6])
    )
    new_population.append(
        crossbreeding(population[4], population[5])
    )
    new_population.append(
        mutation(population[0])
    )
    new_population.append(
        mutation(population[1])
    )
    new_population.append(
        mutation(population[2])
    )
    new_population.append(
        mutation(population[3])
    )
    return new_population
