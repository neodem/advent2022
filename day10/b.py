import common
from classes import CPU
from classes import CRT
from classes import Command_Type
import functions

filename = "test_b.dat"
commands = common.read_file_as_lines(filename)
cycle_count = 1
cpu = CPU()
crt = CRT(40, 6)
ss = {}


def determine_character(location, mid_sprite):
    if location == mid_sprite:
        return '#'
    if location == mid_sprite - 1:
        return '#'
    if location == mid_sprite + 1:
        return '#'
    return '.'


def sprite_position_string(location):
    row = ['.'] * 40
    row[location] = '#'
    row[location + 1] = '#'
    row[location - 1] = '#'
    return ''.join(row)


def draw_crt(cycle_count):
    position = cycle_count - 1
    print("During cycle  {}: CRT draws pixel in position {}".format(cycle_count, position))
    char = determine_character(cycle_count, cpu.register)
    crt.draw_pixel(position, char)
    print("Current CRT row: {}".format(crt.get_row_string(position)))


def do_cycle():
    global cycle_count

    if cpu.current_command.command_type == Command_Type.ADDX:
        if cycle_count % 2:
            print("Start cycle   {}: {}".format(cycle_count, cpu.report()))

    draw_crt(cycle_count)
    cpu.cycle_clock()

    if cpu.current_command.command_type == Command_Type.ADDX:
        if not cycle_count % 2:
            print("End of cycle  {}: {}".format(cycle_count, cpu.report()))
            print("Sprite position: {}".format(sprite_position_string(cpu.get_register())))

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
print("ss: {}".format(ss))

sum = 0
for item in ss.values():
    sum = sum + item

print("sum: {}".format(sum))

print()
crt.draw()
