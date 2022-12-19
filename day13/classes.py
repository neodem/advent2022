import common


class Pair(object):
    index = None
    input1 = None
    input2 = None
    right_order = False

    @staticmethod
    def parse_list(token):
        """
        parse the string into a list of tokens seperated by commas
        :param token:
        :return:
        """
        close_index = common.get_close_index(token)
        clean_string = token[1:close_index]
        token_register = []
        if len(clean_string) > 0:
            # only process commas when out of brackets
            in_brackets = False
            bracket_count = 0
            buffer = []

            for char in clean_string:
                buffer.append(char)
                if char == '[':
                    in_brackets = True
                    bracket_count += 1
                if char == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        in_brackets = False
                if char == "," and not in_brackets:
                    buffer.pop()  # remove comma
                    # end of token
                    buffer_string = ''.join(buffer)
                    token_register.append(buffer_string)
                    buffer = []

            if len(buffer) > 0:
                buffer_string = ''.join(buffer)
                token_register.append(buffer_string)

        return token_register

    def parse_string_to_lists(self, token):
        result = []

        if common.is_list(token):
            for element in self.parse_list(token):
                r = self.parse_string_to_lists(element)
                result.append(r)

        if common.is_number(token):
            number = common.get_number(token)
            return number

        return result

    def __init__(self, index):
        self.index = index

    def set_line1(self, line):
        self.input1 = self.parse_string_to_lists(line)

    def set_line2(self, line):
        self.input2 = self.parse_string_to_lists(line)

    def compute(self, logging=False):
        if logging:
            print("== Pair {} ==".format(self.index))

        result = self.compare(self.input1, self.input2, logging=logging)
        if result >= 0:
            self.right_order = True
        else:
            self.right_order = False

    def compare(self, left, right, indent=0, logging=False, original=True):
        if logging:
            spaces = " ".join([' ' for _ in range(indent)])
            print("{}- Compare: {} vs {}".format(spaces, left, right))

        # return -1 if left is greater, +1 if right is greater, 0 if the same

        # if left and right are single value integers, we have our result
        if type(left) is int and type(right) is int:
            result = right - left

            if logging:
                if result > 0:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Left side is smaller, so inputs are in the right order".format(spaces))
                if result < 0:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Right side is smaller, so inputs are not in the right order".format(spaces))

            return result

        # if we are here, both aren't int.. if one is a int, the other is a list
        if type(left) is int or type(right) is int:
            if type(left) is int:
                new_left = [left]
                if logging:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Mixed types; convert left to {} and retry comparison".format(spaces, new_left))
                return self.compare(new_left, right, indent=indent, logging=logging, original=False)

            new_right = [right]
            if logging:
                indent += 2
                spaces = " ".join([' ' for _ in range(indent)])
                print("{}- Mixed types; convert right to {} and retry comparison".format(spaces, new_right))
            return self.compare(left, new_right, indent=indent, logging=logging, original=False)

        # if we are here, both left and right are lists we iterate and compare values
        # type(left) is list and type(right) is list:
        while len(left) > 0:
            if len(right) == 0:
                # right has run out of items
                if logging:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Right side ran out of items, so inputs are not in the right order".format(spaces))
                return -1
            left_val = left.pop(0)
            right_val = right.pop(0)
            result = self.compare(left_val, right_val, indent=indent + 2, logging=logging, original=False)
            if result != 0:
                return result

        if original:
            indent += 2
            spaces = " ".join([' ' for _ in range(indent)])
            print("{}- Left side ran out of items, so inputs are not in the right order".format(spaces))

        return 0
