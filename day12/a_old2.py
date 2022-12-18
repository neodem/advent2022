import sys

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
    return Node(index, value, 'e')


def get_next_hops(node, matrix):
    index = node.index
    paths = []

    right = matrix.get_right(index)
    if right is not None and node.can_step_to(right):
        paths.append(right)

    left = matrix.get_left(index)
    if left is not None and node.can_step_to(left):
        paths.append(left)

    up = matrix.get_above(index)
    if up is not None and node.can_step_to(up):
        paths.append(up)

    down = matrix.get_below(index)
    if down is not None and node.can_step_to(down):
        paths.append(down)

    return paths


def find_best_path_to_end(node, matrix, visited=[]):
    best_path = []
    visited.append(node)

    if node.value != 'E':
        best_path_len = sys.maxsize
        forward_paths = get_next_hops(node, matrix)
        for next_path_node in forward_paths:
            if not visited.__contains__(next_path_node):
                candidate_path = find_best_path_to_end(next_path_node, matrix, visited)
                if 0 < len(candidate_path) < best_path_len:
                    best_path.extend(candidate_path)
    else:
        best_path = visited

    if len(best_path) > 0:
        node.best_path_to_end = best_path

    return best_path


lines = common.read_file_as_lines("baby.dat")
matrix = IndexedMatrix(lines, create_data_function)

nodes = matrix.data

start_node = find_node(nodes, 'S')
find_best_path_to_end(start_node, matrix)

functions.print_node_paths(nodes)

# print("best distance : {}".format(start_node.distance_to_end))
# 746 is too high
