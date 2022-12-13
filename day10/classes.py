from enum import Enum


class Command_Type(Enum):
    """
    command name and cycles to execute
    """
    NOOP = 1
    ADDX = 2


class Command:
    command_type = Command_Type.NOOP
    command_param = 0

    def __init__(self, command_string):
        if command_string == "noop":
            self.command_type = Command_Type.NOOP
        else:
            tokens = command_string.split(' ')
            if tokens[0] == "addx":
                self.command_type = Command_Type.ADDX
                self.command_param = int(tokens[1])

    def __str__(self):
        return "{} {}".format(self.command_type, self.command_param)


class CPU:
    current_command = None
    clock_cycle = 0
    register = 1
    in_command = False

    def set_command(self, command):
        self.current_command = command
        self.clock_cycle = 0
        self.in_command = True

    def cycle_clock(self):
        self.clock_cycle = self.clock_cycle + 1
        if self.current_command.command_type == Command_Type.ADDX and self.clock_cycle % 2 == 0:
            self.register = self.register + self.current_command.command_param
            self.in_command = False
        if self.current_command.command_type == Command_Type.NOOP:
            self.in_command = False

    def report(self):
        if self.current_command.command_type == Command_Type.ADDX and self.clock_cycle == 0:
            return "begin executing {}".format(self.current_command)
        if self.current_command.command_type == Command_Type.NOOP and self.clock_cycle == 0:
            return "executing {}".format(self.current_command)
        if self.current_command.command_type == Command_Type.ADDX and self.clock_cycle == 2:
            return "finish executing {} (Register X is now {})".format(self.current_command, self.register)

    def get_register(self):
        return self.register

    def ready(self):
        return not self.in_command


class CRT:
    pixels = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = [[' '] * self.width for i in range(self.height)]

    def draw_pixel(self, position, character):
        row_index = position // self.width
        col_index = position - (row_index * self.width)
        self.display[row_index][col_index] = character

    def get_row_string(self, position):
        row_index = position // self.width
        return ''.join(self.display[row_index])

    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self.display[row][col], end='')
            print()
