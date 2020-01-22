import random
import genetic
import graph as graph_class

print("Input count of cities")
count_of_cities = int(input())
graph = graph_class.generate_graph(count_of_cities, 10, 1000)

genetic.evolution(graph, 10)

