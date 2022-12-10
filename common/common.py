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


def read_file_as_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines