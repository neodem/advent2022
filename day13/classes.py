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
            print("== Pair {} == : ".format(self.index))

        self.right_order = self.compare(self.input1, self.input2, logging=logging)
        print("== Pair {} == : {}".format(self.index, self.right_order))

    def compare(self, left, right, logging=False):
        """

        :param left: a list
        :param right: a list
        :param logging:
        :return: True if lists are "in order"
        """
        # return true if in order, false if not

        indent = 0
        keep_processing = True
        while keep_processing:
            if logging:
                spaces = " ".join([' ' for _ in range(indent)])
                print("{}- Compare: {} vs {}".format(spaces, left, right))

            # empty left list and right list is in order
            if len(left) == 0 and len(right) == 0:
                if logging:
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Both lists are empty returning true".format(spaces))
                return True

            # empty left list and right list with values is in order
            if len(left) == 0 and len(right) > 0:
                if logging:
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Left side ran out of items, so inputs are in the right order".format(spaces))
                return True

            # empty right list and left list with values is not in order
            if len(right) == 0 and len(left) > 0:
                if logging:
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Right side ran out of items, so inputs are not in the right order".format(spaces))
                return False

            left_val = left.pop(0)
            right_val = right.pop(0)

            if type(left_val) is int and type(right_val) is int:
                if right_val > left_val:
                    if logging:
                        indent += 2
                        spaces = " ".join([' ' for _ in range(indent)])
                        print("{}- Left side is smaller, so inputs are in the right order".format(spaces))
                    return True

                if right_val < left_val:
                    if logging:
                        indent += 2
                        spaces = " ".join([' ' for _ in range(indent)])
                        print("{}- Right side is smaller, so inputs are not in the right order".format(spaces))
                    return False

            if type(left_val) is int or type(right_val) is int:
                if type(left_val) is int:
                    left_val = [left_val]
                    if logging:
                        indent += 2
                        spaces = " ".join([' ' for _ in range(indent)])
                        print("{}- Mixed types; convert left to {} and retry comparison".format(spaces, left_val))

                right_val = [right_val]
                if logging:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Mixed types; convert right to {} and retry comparison".format(spaces, right_val))

            indent += 2




        #
        #
        #
        #
        #
        # # if left and right are single value integers, we have a potential result
        #
        #
        #     return True
        #
        # # if we are here, both aren't int.. if one is a int, the other is a list, we make it into a list
        # # and try again
        #
        #
        # # if we are here, both left and right are lists we compare them and return result
        # if type(left) is list and type(right) is list:
        #
        #     if len(left) == 0 and len(right) > 0:
        #         if logging:
        #             spaces = " ".join([' ' for _ in range(indent)])
        #             print("{}- Left side ran out of items, so inputs are in the right order".format(spaces))
        #         return True
        #
        #     if len(right) == 0 and len(left) > 0:
        #         if logging:
        #             spaces = " ".join([' ' for _ in range(indent)])
        #             print("{}- Right side ran out of items, so inputs are not in the right order".format(spaces))
        #         return False
        #
        #     # we have at least one element in each list
        #     while len(left) > 0:
        #         left_val = left.pop(0)
        #         right_val = right.pop(0)
        #
        #         result = self.compare(left_val, right_val, indent=indent, logging=logging)
        #         if not result:
        #             return False
        #
        #     return True

    # def compare(self, left, right, indent=0, logging=False):
    #     # return true if in order, false if not
    #     if logging:
    #         spaces = " ".join([' ' for _ in range(indent)])
    #         print("{}- Compare: {} vs {}".format(spaces, left, right))
    #
    #     # if left and right are single value integers, we have our result
    #     if type(left) is int and type(right) is int:
    #         if right > left:
    #             if logging:
    #                 indent += 2
    #                 spaces = " ".join([' ' for _ in range(indent)])
    #                 print("{}- Left side is smaller, so inputs are in the right order".format(spaces))
    #             return True
    #
    #         if right < left:
    #             if logging:
    #                 indent += 2
    #                 spaces = " ".join([' ' for _ in range(indent)])
    #                 print("{}- Right side is smaller, so inputs are not in the right order".format(spaces))
    #             return False
    #
    #         return True
    #
    #     # if we are here, both aren't int.. if one is a int, the other is a list, we make it into a list
    #     # and try again
    #     if type(left) is int or type(right) is int:
    #         if type(left) is int:
    #             new_left = [left]
    #             if logging:
    #                 indent += 2
    #                 spaces = " ".join([' ' for _ in range(indent)])
    #                 print("{}- Mixed types; convert left to {} and retry comparison".format(spaces, new_left))
    #             return self.compare(new_left, right, indent=indent, logging=logging)
    #
    #         new_right = [right]
    #         if logging:
    #             indent += 2
    #             spaces = " ".join([' ' for _ in range(indent)])
    #             print("{}- Mixed types; convert right to {} and retry comparison".format(spaces, new_right))
    #         return self.compare(left, new_right, indent=indent, logging=logging)
    #
    #     # if we are here, both left and right are lists we compare them and return result
    #     if type(left) is list and type(right) is list:
    #
    #         if len(left) == 0 and len(right) > 0:
    #             if logging:
    #                 spaces = " ".join([' ' for _ in range(indent)])
    #                 print("{}- Left side ran out of items, so inputs are in the right order".format(spaces))
    #             return True
    #
    #         if len(right) == 0 and len(left) > 0:
    #             if logging:
    #                 spaces = " ".join([' ' for _ in range(indent)])
    #                 print("{}- Right side ran out of items, so inputs are not in the right order".format(spaces))
    #             return False
    #
    #         # we have at least one element in each list
    #         while len(left) > 0:
    #             left_val = left.pop(0)
    #             right_val = right.pop(0)
    #
    #             result = self.compare(left_val, right_val, indent=indent, logging=logging)
    #             if not result:
    #                 return False
    #
    #         return True
