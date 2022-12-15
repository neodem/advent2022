import common
from common import Matrix
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
        print("{} can connect to: {}, back paths to: {}".format(self.__str__(), self.f_paths, self.b_paths))

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
        if not self.f_paths.__contains__(node):
            self.b_paths.add(node)

    def add_connection(self, node):
        if not self.b_paths.__contains__(node):
            self.f_paths.add(node)


class IndexedMatrix:
    data = []
    num_cols = 0
    num_rows = 0

    def __init__(self, lines):
        index = 0
        for line in lines:
            self.num_rows += 1
            chars = [char for char in line]
            self.num_cols = len(chars)
            for char in chars:
                node = Node(index, char)
                self.data.append(node)
                index += 1

    def max_index(self):
        return self.num_cols * self.num_rows

    def get_by_index(self, index):
        return self.data[index]

    def get_by_row_col(self, row, col):
        if row >= self.num_rows:
            return None
        if col >= self.num_cols:
            return None
        if row < 0 or col < 0:
            return None

        index = row * self.num_cols + col
        return self.get_by_index(index)

    def get_row_from_index(self, index):
        return index // self.num_cols

    def get_col_from_index(self, index):
        r = self.get_row_from_index(index)
        return index - (r * self.num_cols)

    def get_right(self, index):
        r = self.get_row_from_index(index)
        c = self.get_col_from_index(index)
        return self.get_by_row_col(r, c + 1)

    def get_left(self, index):
        r = self.get_row_from_index(index)
        c = self.get_col_from_index(index)
        return self.get_by_row_col(r, c - 1)

    def get_above(self, index):
        r = self.get_row_from_index(index)
        c = self.get_col_from_index(index)
        return self.get_by_row_col(r - 1, c)

    def get_below(self, index):
        r = self.get_row_from_index(index)
        c = self.get_col_from_index(index)
        return self.get_by_row_col(r + 1, c)

    def draw_matrix(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                node = self.get_by_row_col(r, c)
                print(node.value, end='')
            print()
        print()


lines = common.read_file_as_lines("test.dat")
m = IndexedMatrix(lines)
m.draw_matrix()

nodes = []
for index in range(m.max_index()):
    node = m.get_by_index(index)

    if node.value != 'E':
        right = m.get_right(index)
        if right is not None and node.can_step(right):
            node.add_connection(right)
            right.add_back_connection(node)

        left = m.get_left(index)
        if left is not None and node.can_step(left):
            node.add_connection(left)
            left.add_back_connection(node)

        up = m.get_above(index)
        if up is not None and node.can_step(up):
            node.add_connection(up)
            up.add_back_connection(node)

        down = m.get_below(index)
        if down is not None and node.can_step(down):
            node.add_connection(down)
            down.add_back_connection(node)

    nodes.append(node)

for node in nodes:
    node.print_full()


def find_node(nodes, val):
    for node in nodes:
        if node.value == val:
            return node
    return None


start_node = find_node(nodes, 'S')
end_node = find_node(nodes, 'E')


def set_back_distances(node, distance):
    back_nodes = node.b_paths
    if back_nodes is not None and len(back_nodes) > 0:
        for back_node in back_nodes:
            back_node.set_path_to_end(node, distance)
            set_back_distances(back_node, distance + 1)


set_back_distances(end_node, 1)

print("best distance : {}".format(start_node.distance_to_end))
