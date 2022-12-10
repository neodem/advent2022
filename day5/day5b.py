import common

filename = 'input.dat'

stacks = []  # each of these will be a stack of chars
commands = []  # each of these will be a command


# line is numbers broken up by 3 spaces
def parse_num_stacks(line):
    tokens = line.split('   ')
    return len(tokens)


def parse_letter(token):
    if token == "   ":
        return None
    if len(token) > 0:
        return token[1]
    return None


def load_line_into_stacks(stacks, num_stacks, line):
    for stack_number in range(num_stacks):
        offset = 4 * stack_number
        token = line[0 + offset:3 + offset]
        letter = parse_letter(token)
        if letter:
            stacks[stack_number + 1].push(letter)


def read_stacks(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line)
            if line == '\n':
                break

    num_stacks_line = len(lines) - 2
    num_stacks = parse_num_stacks(lines[num_stacks_line])

    # stacks are an array of Stack objects. This ints that
    stacks = [None]
    for index in range(num_stacks):
        stacks.append(common.Stack())

    for line_number in range(num_stacks_line - 1, -1, -1):
        load_line_into_stacks(stacks, num_stacks, lines[line_number])

    return stacks


def read_raw_commands(filename):
    lines = []
    line_index = 0
    commands_start_at = 0
    with open(filename) as file:
        for line in file:
            line_index = line_index + 1
            line = line.strip()
            lines.append(line)
            if len(line) == 0:
                commands_start_at = line_index

    return lines[commands_start_at:]


def parse_commands(raw_commands):
    converted = []
    tokens = []
    for command in raw_commands:
        raw_command = command.split(' ')
        tokens.append(int(raw_command[1]))
        tokens.append(int(raw_command[3]))
        tokens.append(int(raw_command[5]))
        converted.append([*tokens])
        tokens.clear()

    return converted


def print_stacks(stacks):
    index = 0
    for stack in stacks:
        if stack:
            stack.print(index)
        index = index + 1


def process_command(stacks, command):
    print_stacks(stacks)
    print("move {} from {} to {}".format(command[0], command[1], command[2]))
    really_process_the_command(command, stacks)
    print_stacks(stacks)
    print('\n')
    return stacks


def really_process_the_command(command, stacks):
    grab = common.Stack()
    for index in range(command[0]):
        cargo = stacks[command[1]].pop()
        grab.push(cargo)

    for index in range(command[0]):
        stacks[command[2]].push(grab.pop())


stacks = read_stacks(filename)
commands = parse_commands(read_raw_commands(filename))
for command in commands:
    stacks = process_command(stacks, command)

result = ""
for stack in stacks:
    if stack:
        result = result + stack.peek()

print(result)
