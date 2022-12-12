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
    buffer = None

    def set_command(self, command):
        self.current_command = command
        self.clock_cycle = 0
        self.in_command = True

    def cycle_clock(self):
        if self.buffer is not None:
            self.register = self.buffer

        self.clock_cycle = self.clock_cycle + 1
        if self.current_command.command_type == Command_Type.ADDX and self.clock_cycle % 2 == 0:
            self.buffer = self.register + self.current_command.command_param
            self.in_command = False
        if self.current_command.command_type == Command_Type.NOOP:
            self.in_command = False

    def ready(self):
        return not self.in_command
