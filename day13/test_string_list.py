import functions


def single_balanced(line):
    lefts = line.count('[')
    rights = line.count(']')

    return lefts == rights and lefts == 1


def number_only(line):
    lefts = line.count('[')
    rights = line.count(']')

    return lefts == rights and lefts == 0


def split_line(line):
    # will break a line into tokens (either numbers or additional lists)

    # had I had more time I could certainly make this a lot more efficient and elegant. but I don't have time

    tokens = []

    number_register = []
    in_array = False
    number_index = 0
    left_index = 0
    index = 0
    while len(line) > 0:
        char = line[index]
        if char == '[':
            number_register = []
            number_index = 0
            left_index = index
            in_array = True
        elif char == ']':
            # token complete
            token = line[left_index:index + 1]
            tokens.append(token)
            line = line[index + 1:-1]
            index = -1
            in_array = False
        elif '0' <= char <= '9' and not in_array:
            number_register.append(char)
            line = line[index + 1:-1]
        elif char == ',':
            if len(number_register) > 0 and not in_array:
                number = ''.join(number_register)
                tokens.append(number)
                line = line[number_index + 1:-1]
                number_register = []
                number_index = 0
                index = -1

        index += 1

    if len(number_register) > 0 and not in_array:
        number = ''.join(number_register)
        tokens.append(number)

    return tokens


def encode_input(line):
    if single_balanced(line):
        return line[1:-1].split(',')

    if number_only(line):
        return line

    tokens = split_line(line)

    result = []

    for token in tokens:
        result.append(encode_input(token))

    return result


pairs = functions.read_file_to_pairs('test.dat')
for pair in pairs:
    left = encode_input(pair.input1)
    right = encode_input(pair.input2)
    print(left)
    print(right)
