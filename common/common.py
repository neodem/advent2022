class Stack:
    data = []

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def print(self, index):
        print("stack {}".format(index))
        print(self.data)


class Queue:
    data = []

    def __init__(self):
        self.data = []

    def enque(self, value):
        self.data.append(value)

    def deque(self):
        return self.data.pop(0)

    def peek(self):
        return self.data(0)

    def size(self):
        return len(self.data)

    def as_list(self):
        return self.data


# will only allow a given size, when full, it will drop the oldest
class FixedList:
    data = Queue()
    max_size = 0

    def __init__(self, max_size):
        self.max_size = max_size
        self.data = Queue()

    def add(self, value):
        if self.data.size() == self.max_size:
            self.data.deque()
        self.data.enque(value)

    def get_list(self):
        return self.data.as_list()

    def size(self):
        return self.data.size()


class Point:
    x = 0
    y = 0
    name = ""

    def __init__(self, x, y, name=""):
        self.x = x
        self.y = y
        self.name = name

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __str__(self):
        return "[{},{}]".format(self.x, self.y)

    def copy(self):
        return Point(self.x, self.y, self.name)

    def display(self):
        return "{} is at [{},{}]".format(self.name, self.x, self.y)

    def move_point(self, direction):
        if direction == 'L':
            self.x = self.x - 1
        elif direction == 'R':
            self.x = self.x + 1
        elif direction == 'U':
            self.y = self.y + 1
        elif direction == 'D':
            self.y = self.y - 1

    def move_to(self, x, y):
        self.x = x
        self.y = y


def read_file_as_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines
