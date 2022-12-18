import functions
import common


def split_line(line):
    # will break a line into tokens (either numbers or additional lists)

    # had I had more time I could certainly make this a lot more efficient and elegant. but I don't have time

    tokens = []

    number_register = []
    in_array = False
    left_index = 0
    index = 0
    while len(line) > 0:
        char = line[index]
        if char == '[':
            number_register = []
            left_index = index
            in_array = True
        elif char == ']':
            # token complete
            token = line[left_index:index + 1]
            if token == "[]":
                tokens.append([])
            else:
                tokens.append(token)
            line = line[index + 1:-1]
            index = -1
            in_array = False
        elif '0' <= char <= '9' and not in_array:
            number_register.append(char)
            line = line[index + 1:]
            index = -1
        elif char == ',':
            if len(number_register) > 0 and not in_array:
                number = ''.join(number_register)
                tokens.append(number)
                number_register = []
                index = -1

        index += 1

    if len(number_register) > 0 and not in_array:
        number = ''.join(number_register)
        tokens.append(number)

    return tokens


def encode_line(line):
    lefts = line.count('[')
    rights = line.count(']')

    if lefts == rights and lefts == 1:
        return line[1:-1].split(',')

    if lefts == rights and lefts == 0:
        return line

    tokens = split_line(line)

    result = []

    for token in tokens:
        result.append(encode_line(token))

    return result


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


def get_list(token):
    left_index = 0
    index = 0
    while len(token) > 0:
        char = line[index]
        if char == '[':
            number_register = []
            left_index = index
            in_array = True
        elif char == ']':
            # token complete
            token = line[left_index:index + 1]
            if token == "[]":
                tokens.append([])
            else:
                tokens.append(token)
            line = line[index + 1:-1]
            index = -1
            in_array = False
        elif '0' <= char <= '9' and not in_array:
            number_register.append(char)
            line = line[index + 1:]
            index = -1
        elif char == ',':
            if len(number_register) > 0 and not in_array:
                number = ''.join(number_register)
                tokens.append(number)
                number_register = []
                index = -1


def process(token):
    # return a number or a list
    character = token[0]
    if '0' <= character <= '9':
        return get_number(token)
    if character == '[' :
        return get_list(token)


"""
[1,1,3,1,1]

read char
[ : in array = true
read umtil ], and process (recurs)

if number, read until comma and return up






1,1,3,1,1

if no brackets, make list of elements, elements are ints
l[1,1,3,1,1]


[[1],[2,3,4]]

strip outermost brackets
[1],[2,3,4]

token:
if [ then the stuff in beween until ]
if number then number


[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""







lines = common.read_file_as_lines("test.dat")

line_mod = 0
for line in lines:
    if line_mod == 0 or line_mod == 1:
        print("encoding {} as ".format(line), end='')
        left = encode_line(line)
        print(left)
        line_mod += 1

    elif line_mod == 2:
        line_mod = 0
