import common
import functions
from common import Point
from common import Plot


def move_links(head_loc, link_locs):
    prev_loc = head_loc
    for link in link_locs:
        functions.move_link(prev_loc, link)
        prev_loc = link


head_location = Point(0, 0, "head", "H")
link_locations = [Point(0, 0, str(i + 1), str(i + 1)) for i in range(9)]
link_locations[8].name = "tail"
link_locations[8].id = "T"
tail_visits = set()

p = Plot(50, 50, 20, 20)
for link_location in link_locations:
    p.add_location(link_location)
p.add_location(head_location)

filename = "testb.dat"
commands = common.read_file_as_lines(filename)

print("START: {}, {}".format(head_location.display(), link_locations[8].display()))
p.print_plot(1)

for command in commands:
    print(command)
    command_tokens = command.split(' ')
    direc = command_tokens[0]
    distance = int(command_tokens[1])

    for index in range(distance):
        print("-")
        prev_head_loc = head_location.copy()
        head_location.move_point(direc)
        print("move {} {}: from {} to {}.".format(head_location.name, direc, prev_head_loc, head_location))
        move_links(head_location, link_locations)
        tail_visits.add(link_locations[8])
        # p.print_plot(1)
        print("unique tail visit count: {}".format(len(tail_visits)))

    print()
    p.print_plot(1)
