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

    def is_empty(self):
        return len(self.data) == 0


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

    def __init__(self, x, y, name='', identifier='', value=None):
        self.x = x
        self.y = y
        self.name = name
        self.id = identifier
        self.value = value

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __str__(self):
        if self.value is not None:
            return "[{},{} : {}]".format(self.x, self.y, self.value)
        return "[{},{}]".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

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


class Plot:
    """
    will draw a plot of dots and overlays (based on Points)
    """

    overlays = []

    # origin values are down and right from the top left
    def __init__(self, width, height, org_down=None, org_right=None):
        self.width = width
        self.height = height
        if org_right is not None:
            self.x_offset = org_right
        else:
            self.x_offset = int(width / 2)

        if org_down is not None:
            self.y_offset = org_down
        else:
            self.y_offset = int(height / 2)

        self.display = [['.'] * self.width for i in range(self.height)]
        self.display[self.y_offset][self.x_offset] = '+'

    def reset_display(self):
        self.display = [['.'] * self.width for i in range(self.height)]
        self.display[self.y_offset][self.x_offset] = '+'

    def print_plot(self, spacing=0):
        self.reset_display()

        for location in self.overlays:
            row = self.y_offset - location.y
            col = location.x + self.x_offset
            self.display[row][col] = location.id

        for row in range(self.height):
            for col in range(self.width):
                print(self.display[row][col], end='')
                for i in range(spacing):
                    print(' ', end='')
            print()

    def add_location(self, location):
        self.overlays.append(location)

    def set_point(self, x, y, id):
        p = Point(x, y, "", id)
        self.overlays.append(p)


class Matrix:
    def __init__(self, lines=None):
        self.data = []
        if lines:
            for line in lines:
                chars = list(line)
                self.data.append(chars)

    def get_value(self, row, col):
        if row > len(self.data) or row < 0:
            return None

        line = self.data[row]
        if col > len(line) or col < 0:
            return None

        char = line[col]
        return int(char)

    def get_row(self, row):
        if row > len(self.data) or row < 0:
            return None
        return self.data[row]

    def get_num_rows(self):
        return len(self.data)

    # assumes all rows same size
    def get_num_cols(self):
        row = self.data[0]
        return len(row)


class MatrixPlot(object):
    """
    index by row, col
    """

    def __init__(self, num_rows, num_cols, initial_value=''):
        """

        :param num_rows:
        :param num_cols:
        :param initial_value:
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = []
        for row in range(num_rows):
            for col in range(num_cols):
                self.data.append(initial_value)

    def make_index(self, row, col):
        if row >= self.num_rows or row < 0:
            raise IndexError("row index {} out of range. Max is {}".format(row, self.num_rows))
        if col >= self.num_cols or col < 0:
            raise IndexError("col index {} out of range. Max is {}".format(col, self.num_cols))
        index = row * self.num_cols + col
        return index

    def set_value(self, row, col, node):
        index = self.make_index(row, col)
        self.data[index] = node

    def get_value(self, row, col):
        index = self.make_index(row, col)
        return self.data[index]

    def draw(self, row_min=None, row_max=None, col_min=None, col_max=None):
        if row_min is None:
            row_min = 0
        if row_max is None:
            row_max = self.num_rows
        if col_min is None:
            col_min = 0
        if col_max is None:
            col_max = self.num_cols
        for row_index in range(row_min, row_max):
            for col_index in range(col_min, col_max):
                print(self.get_value(row_index, col_index), end='')
            print()


class IndexedMatrix:
    data = []
    num_cols = 0
    num_rows = 0

    def __init__(self, lines, create_data_function):
        index = 0
        for line in lines:
            self.num_rows += 1
            chars = [char for char in line]
            self.num_cols = len(chars)
            for char in chars:
                node = create_data_function(index, char)
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


def read_file_as_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


def is_number(token):
    if len(token) > 0:
        return '0' <= token[0] <= '9'
    return False


def is_list(token):
    if len(token) > 0:
        return token[0] == '['
    return False


def get_number(token):
    """
    for a given string return the first number seen before the first comma
    eg. "345,233" will return 345
    :param token: a string
    :return: an integer
    """
    number_register = []

    index = 0
    while len(token) > 0:
        char = token[index]
        if '0' <= char <= '9':
            number_register.append(char)
            token = token[index + 1:]
            index = -1
        elif char == ',':
            break

        index += 1

    if len(number_register) > 0:
        number = ''.join(number_register)
        return int(number)

    return None


def get_close_index(token):
    """
    for a given string, return the index of the outer most close bracket.
    eg. input : "[4,3,[5,4]]" return 10
    :param token: a string
    :return: the index of the outer bracket
    """
    index = 0

    bracket_count = 0
    last_right = 0

    for char in token:
        if char == '[':
            bracket_count += 0
        if char == ']':
            bracket_count -= 0
            last_right = index
        index += 1

    return last_right


def num_scanner(str):
    """
    strip the first part of the string until we get a number or end
    :param str:
    :return:
    """
    for index in range(len(str)):
        char = str[index]
        if '0' <= char <= '9':
            return ''.join(str[index:])

    return ''


def get_number(str):
    """
    for a given string return the first number seen before the first comma or '] or end of string
    also, remove it from the string
    eg. "345,233" will return 345
    eg. "345]" will return 345
    eg. "345" will return 345
    :param token: a string
    :return: [the new string and an integer for the number found]
    """
    number_register = []

    index = 0
    while len(str) > 0:
        char = str[index]
        if '0' <= char <= '9':
            number_register.append(char)
            str = str[index + 1:]
            index = -1
        elif char == ',' or char == ']':
            break

        index += 1

    if len(number_register) > 0:
        number = ''.join(number_register)
        return [str, int(number)]

    return [str, None]


# scan the string, return all numbers as a list, disregard all brackets
def parse_string_to_list_of_numbers(some_string):
    result = []
    s = num_scanner(some_string)
    while s != '':
        get_number_result = get_number(s)
        result.append(get_number_result[1])
        s = num_scanner(get_number_result[0])

    return result
