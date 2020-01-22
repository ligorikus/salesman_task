import random


def generate_graph(count_of_cities, min_distance=1, max_distance=100):
    graph = [0]*count_of_cities
    for i in range(count_of_cities):
        graph[i] = [0] * count_of_cities

    for i in range(count_of_cities):
        for j in range(count_of_cities):
            if i == j:
                continue
            distance = random.randint(min_distance, max_distance)
            graph[i][j] = distance
            graph[j][i] = distance

    return graph
