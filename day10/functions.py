from classes import Command

command_index = 0
next_record_marker = 20


def fetch_command(commands):
    global command_index
    if command_index == len(commands):
        return None

    command_string = commands[command_index]
    command = Command(command_string)
    command_index = command_index + 1
    return command


def record_data(cycle_count):
    global next_record_marker
    if 220 >= next_record_marker == cycle_count:
        next_record_marker = next_record_marker + 40
        return True
    return False
