import common
from common import IndexedMatrix
from classes import Node
import functions


def find_node(nodes, val):
    for node in nodes:
        if node.value == val:
            return node
    return None


def create_data_function(index, value):
    return Node(index, value)


def load_nodes(matrix):
    nodes = []
    for index in range(matrix.max_index()):
        node = matrix.get_by_index(index)

        if node.value != 'E':
            right = matrix.get_right(index)
            if right is not None and node.can_step_to(right):
                node.add_connection(right)

            left = matrix.get_left(index)
            if left is not None and node.can_step_to(left):
                node.add_connection(left)

            up = matrix.get_above(index)
            if up is not None and node.can_step_to(up):
                node.add_connection(up)

            down = matrix.get_below(index)
            if down is not None and node.can_step_to(down):
                node.add_connection(down)

        nodes.append(node)
    return nodes


def print_nodes():
    for node in nodes:
        node.print_full()


lines = common.read_file_as_lines("test.dat")
matrix = IndexedMatrix(lines, create_data_function)
# matrix.draw_matrix()

nodes = load_nodes(matrix)

print_nodes()

# end_node = find_node(nodes, 'E')
# set_back_distances(end_node, 1)

start_node = find_node(nodes, 'S')
functions.find_best_path_to_end(start_node)

functions.print_node_paths(nodes)

# print("best distance : {}".format(start_node.distance_to_end))
# 746 is too high
