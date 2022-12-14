import common
from common import Matrix


class Node:
    # index is the space in maze
    index = None

    # value is the value of the space
    value = None

    # this is the distance to the end (best case)
    distance_to_end = None

    # forward paths point to Nodes
    f_paths = []

    # backward paths point to Nodes
    b_paths = []

    def __init__(self, index, value):
        self.index = index
        self.value = value

    def gte(self, other_node):
        return ord(self.value) >= ord(other_node.value)

    def add_back_connection(self, node):
        self.b_paths.append(node)

    def add_connection(self, node):
        node.add_back_connection(self)
        self.f_paths.append(node)


# class Maze:
#
#     # both point to Node objects
#     start = None
#     end = None
#
#     def __init__(self, lines):

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
        return index % self.num_cols

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

start_node = None
for index in range(m.max_index()):
    node = m.get_by_index(index)
    if not start_node:
        start_node = node

    right = m.get_right(index)
    if node.gte(right):
        node.add_connection(right)

    left = m.get_left(index)
    if node.gte(left):
        node.add_connection(left)

    up = m.get_above(index)
    if node.gte(up):
        node.add_connection(up)

    down = m.get_below(index)
    if node.gte(down):
        node.add_connection(down)

print(m.get_by_index(0))
print(m.get_by_index(1))
print(m.get_by_index(8))
print(m.get_by_index(9))
