import functions


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


pairs = functions.read_file_to_pairs('test.dat')
for pair in pairs:
    print("encoding {} ".format(pair.input1), end='')
    left = encode_line(pair.input1)
    print(left)

    print("encoding {} ".format(pair.input2), end='')
    right = encode_line(pair.input2)
    print(right)
