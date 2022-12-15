import common
from common import IndexedMatrix
import sys


class Node:
    # index is the space in maze
    index = None

    # value is the value of the space
    value = None

    # this is the distance to the end (best case)
    distance_to_end = sys.maxsize

    # this is the path to take to the end (best case)
    next_node_to_end = None

    # forward paths point to Nodes
    f_paths = None

    # backward paths point to Nodes
    b_paths = None

    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.f_paths = set()
        self.b_paths = set()

    def __hash__(self):
        return self.index

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.index == other.index
        return NotImplemented

    def __str__(self):
        return "[{}.{}]".format(self.index, self.value)

    def __repr__(self):
        return "[{}.{}]".format(self.index, self.value)

    def print_full(self):
        print("{} can move to: {}, back paths from: {}".format(self.__str__(), self.f_paths, self.b_paths))

    def set_path_to_end(self, next_node, distance):
        if distance < self.distance_to_end:
            self.distance_to_end = distance
            self.next_node_to_end = next_node

    def get_clean_value(self):
        if self.value == 'S':
            return 'a'

        if self.value == 'E':
            return 'z'

        return self.value

    # return True if the self node can proceed forward to the other node
    def can_step_to(self, other_node):
        # we can step to an equal
        # or one greater
        # or any less

        our_level = ord(self.get_clean_value())
        their_level = ord(other_node.get_clean_value())

        if our_level == their_level:
            return True

        if our_level > their_level:
            return True

        if our_level + 1 == their_level:
            return True

    # return True if the self node is a "back" node of the other node. This means the other node can step to this node
    def is_a_back_of(self, other_node):
        return other_node.can_step_to(self)

    def add_back_connection(self, node):
        # if not self.f_paths.__contains__(node):
        self.b_paths.add(node)

    def add_connection(self, node):
        # if not self.b_paths.__contains__(node):
        self.f_paths.add(node)


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
                if right.is_a_back_of(node):
                    right.add_back_connection(node)

            left = matrix.get_left(index)
            if left is not None and node.can_step_to(left):
                node.add_connection(left)
                if left.is_a_back_of(node):
                    left.add_back_connection(node)

            up = matrix.get_above(index)
            if up is not None and node.can_step_to(up):
                node.add_connection(up)
                if up.is_a_back_of(node):
                    up.add_back_connection(node)

            down = matrix.get_below(index)
            if down is not None and node.can_step_to(down):
                node.add_connection(down)
                if down.is_a_back_of(node):
                    down.add_back_connection(node)

        nodes.append(node)
    return nodes


def print_nodes():
    for node in nodes:
        node.print_full()


def set_back_distances(node, distance, passed_nodes=set()):
    back_nodes = node.b_paths
    if back_nodes is not None and len(back_nodes) > 0:
        for back_node in back_nodes:
            if not passed_nodes.__contains__(back_node):
                passed_nodes.add(back_node)
                back_node.set_path_to_end(node, distance)
                set_back_distances(back_node, distance + 1, passed_nodes)


lines = common.read_file_as_lines("test.dat")
matrix = IndexedMatrix(lines, create_data_function)
# matrix.draw_matrix()

nodes = load_nodes(matrix)

print_nodes()

end_node = find_node(nodes, 'E')
set_back_distances(end_node, 1)

start_node = find_node(nodes, 'S')
print("best distance : {}".format(start_node.distance_to_end))
