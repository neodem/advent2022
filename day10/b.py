import common
from classes import CPU
from classes import CRT
from classes import Command_Type
import functions

CRT_WIDTH = 40
CRT_HEIGHT = 6
filename = "test_b.dat"
commands = common.read_file_as_lines(filename)
cycle_count = 1
cpu = CPU()
crt = CRT(CRT_WIDTH, CRT_HEIGHT)


def determine_character(location, mid_sprite):
    row_location = location % CRT_WIDTH

    if row_location == mid_sprite:
        return '#'
    if row_location == mid_sprite - 1:
        return '#'
    if row_location == mid_sprite + 1:
        return '#'
    return '.'


def sprite_position_string(location):
    row = ['.'] * CRT_WIDTH
    row[location] = '#'
    row[location + 1] = '#'
    row[location - 1] = '#'
    return ''.join(row)


def draw_crt(cycle_count):
    position = cycle_count - 1
    print("During cycle  {}: CRT draws pixel in position {}".format(cycle_count, position))
    char = determine_character(position, cpu.register)
    crt.draw_pixel(position, char)
    print("Current CRT row: {}".format(crt.get_row_string(position)))


in_addx = False


def do_cycle():
    global cycle_count, in_addx

    if cpu.current_command.command_type == Command_Type.ADDX:
        if not in_addx:
            print("Start cycle   {}: {}".format(cycle_count, cpu.report()))
            in_addx = True
        else:
            in_addx = False

    if cpu.current_command.command_type == Command_Type.NOOP:
        print("Start cycle   {}: {}".format(cycle_count, cpu.report()))

    draw_crt(cycle_count)
    cpu.cycle_clock()

    if cpu.current_command.command_type == Command_Type.ADDX:
        if not in_addx:
            print("End of cycle  {}: {}".format(cycle_count, cpu.report()))
            print("Sprite position: {}".format(sprite_position_string(cpu.get_register())))

    if cpu.current_command.command_type == Command_Type.NOOP:
        print("End of cycle  {}: {}".format(cycle_count, cpu.report()))

    cycle_count = cycle_count + 1
    print()


print("Sprite position: {}".format(sprite_position_string(cpu.get_register())))
print()
while True:
    command = functions.fetch_command(commands)
    if command is not None:
        cpu.set_command(command)

        while not cpu.ready():
            do_cycle()

    else:
        break

print("-----------------------------------")
print("cycle_count: {}".format(cycle_count))
print()
crt.draw()
