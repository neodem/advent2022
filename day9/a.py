import common
import functions
from classes import Plot
from common import Point

head_location = Point(0, 0, "head", "H")
tail_location = Point(0, 0, "tail", "T")
tail_visits = set()
p = Plot(15, 15, 2, 10)
p.add_location(tail_location)
p.add_location(head_location)

filename = "test.dat"
commands = common.read_file_as_lines(filename)

print("START: {}, {}".format(head_location.display(), tail_location.display()))
p.print_plot(1)
for command in commands:
    print("command: {}".format(command))
    command_tokens = command.split(' ')
    direc = command_tokens[0]
    distance = int(command_tokens[1])

    for index in range(distance):
        print("-")
        head_location.move_point(direc)
        print("move {}: {}, {}".format(head_location.name, head_location.display(), tail_location.display()))
        tail_location = functions.move_link(head_location, tail_location, direc)
        tail_visits.add(tail_location)
        print("unique tail visit count: {}".format(len(tail_visits)))

    p.print_plot(1)
    print()

