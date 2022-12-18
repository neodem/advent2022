from classes import Graph
import functions
import common
from common import IndexedMatrix
from classes import Node


def create_data_function(index, value):
    return Node(index, value)


lines = common.read_file_as_lines("input.dat")
matrix = IndexedMatrix(lines, create_data_function)

nodes = matrix.data


def get_next_hops(node, matrix):
    index = node.index
    paths = {}

    right = matrix.get_right(index)
    if right is not None and node.can_step_to(right):
        paths[right] = 1

    left = matrix.get_left(index)
    if left is not None and node.can_step_to(left):
        paths[left] = 1

    up = matrix.get_above(index)
    if up is not None and node.can_step_to(up):
        paths[up] = 1

    down = matrix.get_below(index)
    if down is not None and node.can_step_to(down):
        paths[down] = 1

    return paths

def find_node(nodes, val):
    for node in nodes:
        if node.value == val:
            return node
    return None


init_graph = {}
for node in nodes:
    init_graph[node] = get_next_hops(node, matrix)

graph = Graph(nodes, init_graph)

start_node = find_node(nodes, 'S')
end_node = find_node(nodes, 'E')

previous_nodes, shortest_path = functions.dijkstra_algorithm(graph=graph, start_node=start_node)

result = shortest_path[end_node]
print(result)

# functions.print_result_d(previous_nodes, shortest_path, start_node=start_node, target_node=end_node)
