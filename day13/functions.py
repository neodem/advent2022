import common

def parse_list(token):
    """
    parse the string into a list of tokens separated by commas
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


def parse_string_to_lists(token):
    result = []

    if common.is_list(token):
        for element in parse_list(token):
            r = parse_string_to_lists(element)
            result.append(r)

    if common.is_number(token):
        number = common.get_number(token)
        return number

    return result


def compare(left, right, indent=0, logging=False):
    """

    :param left:
    :param right:
    :param indent:
    :return: -1 for not in right order, 1 if in right order, 0 for same
    """

    if logging:
        spaces = " ".join([' ' for _ in range(indent)])
        print("{}- Compare: {} vs {}".format(spaces, left, right))

    result = 0
    while result == 0:

        if type(left) is int and type(right) is int:
            if right > left:
                if logging:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Left side is smaller, so inputs are in the right order".format(spaces))
                return 1

            if right < left:
                if logging:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Right side is smaller, so inputs are not in the right order".format(spaces))
                return -1
            return 0

        elif type(left) is int or type(right) is int:
            if type(left) is int:
                left = [left]
                if logging:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Mixed types; convert left to {} and retry comparison".format(spaces, left))
            else:
                right = [right]
                if logging:
                    indent += 2
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Mixed types; convert right to {} and retry comparison".format(spaces, right))

            result = compare(left, right, indent=indent, logging=logging)

        elif type(left) is list and type(right) is list:
            if len(left) == 0 and len(right) == 0:
                return 0

            if len(left) == 0:
                if logging:
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Left side ran out of items, so inputs are in the right order".format(spaces))
                return 1

            if len(right) == 0:
                if logging:
                    spaces = " ".join([' ' for _ in range(indent)])
                    print("{}- Right side ran out of items, so inputs are not in the right order".format(spaces))
                return -1

            left_val = left.pop(0)
            right_val = right.pop(0)

            result = compare(left_val, right_val, indent=indent + 2, logging=logging)

    return result
