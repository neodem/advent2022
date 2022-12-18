from classes import Graph
import functions
import common
from common import IndexedMatrix
from classes import Node


def create_data_function(index, value):
    return Node(index, value)


lines = common.read_file_as_lines("test.dat")
matrix = IndexedMatrix(lines, create_data_function)

nodes = matrix.data

init_graph = {}
for node in nodes:
    init_graph[node] = functions.get_next_hops(node, matrix)

graph = Graph(nodes, init_graph)

start_node = functions.find_node(nodes, 'S')
end_node = functions.find_node(nodes, 'E')

previous_nodes, shortest_path = functions.dijkstra_algorithm(graph=graph, start_node=start_node)

result = shortest_path[end_node]
print(result)

# functions.print_result_d(previous_nodes, shortest_path, start_node=start_node, target_node=end_node)
