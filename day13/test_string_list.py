import functions
import common


def get_number(token):
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


def is_list(token):
    if len(token) > 0:
        return token[0] == '['
    return False


def is_number(token):
    if len(token) > 0:
        return '0' <= token[0] <= '9'
    return False


def get_close_index(token):
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


def parse_list(token):
    close_index = get_close_index(token)
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
                bracket_count += 0
            if char == ']':
                bracket_count -= 0
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


def do_thing(token):
    result = []

    if is_list(token):
        l = parse_list(token)
        for element in l:
            r = do_thing(element)
            result.append(r)

    if is_number(token):
        number = get_number(token)
        return number

    return result


lines = common.read_file_as_lines("test.dat")

line_mod = 0
for line in lines:
    if line_mod == 0 or line_mod == 1:
        print("encoding {} as ".format(line), end='')
        token = do_thing(line)
        print(token)
        line_mod += 1

    elif line_mod == 2:
        line_mod = 0
