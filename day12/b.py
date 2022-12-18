from classes import Graph
import functions
import common
from common import IndexedMatrix
from classes import Node
import sys


def create_data_function(index, value):
    return Node(index, value)


lines = common.read_file_as_lines("input.dat")
matrix = IndexedMatrix(lines, create_data_function)

nodes = matrix.data

init_graph = {}
for node in nodes:
    init_graph[node] = functions.get_next_hops(node, matrix)

graph = Graph(nodes, init_graph)

start_node = functions.find_node(nodes, 'S')
a_nodes = functions.find_nodes_with_value(nodes, 'a')
end_node = functions.find_node(nodes, 'E')

best_start = None
best_distance = sys.maxsize
for a_node in a_nodes:
    previous_nodes, shortest_path = functions.dijkstra_algorithm(graph=graph, start_node=a_node)
    distance = shortest_path[end_node]
    if distance < best_distance:
        best_distance = distance
        best_start = a_node


print(best_distance)
