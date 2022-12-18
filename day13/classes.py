

class Pair(object):
    index = None
    input1 = None
    input2 = None
    right_order = False

    def __init__(self, index):
        self.index = index

    def string_to_list(self, line):
        return line[1:-1].split(',')

    def set_line1(self, line):
        self.input1 = line

    def set_line2(self, line):
        self.input2 = line

    def compute(self):
        print("compare: {} with {}. ".format(self.input1, self.input2), end='')
        result = self.compare(self.input1, self.input2)
        if result >= 0:
            self.right_order = True

        if self.right_order:
            print("right order")
        else:
            print("not right order")

    def compare(self, left, right):
        # return -1 if left is greater, +1 if right is greater, 0 if the same

        if type(left) is str and left[0] == '[':
            left = self.string_to_list(left)

        if type(right) is str and right[0] == '[':
            right = self.string_to_list(right)

        # if left and right are single value integers, we have our result
        if type(left) is str and type(right) is str:
            left_int = int(left)
            right_int = int(right)
            return right_int - left_int

        # if we are here, both aren't strings.. if one is a string, the other is a list
        if type(left) is str or type(right) is str:
            if type(left) is str:
                return self.compare([left], right)
            return self.compare(left, [right])

        # if we are here, both left and right are lists we iterate and compare values
        # type(left) is list and type(right) is list:
        while len(left) > 0:
            if len(right) == 0:
                # right has run out of items
                return -1
            left_val = left.pop(0)
            right_val = right.pop(0)
            result = self.compare(left_val, right_val)
            if result != 0:
                return result

        return 0