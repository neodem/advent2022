
class Node:
    # index is the space in maze
    index = None

    # value is the value of the space
    value = None

    best_path_to_end = None

    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.f_paths = set()

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
        print("{} can move to: {}".format(self.__str__(), self.f_paths))

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

    def add_connection(self, node):
        self.f_paths.add(node)