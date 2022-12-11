import common
import functions
from common import Point

head_location = Point(0, 0, "head")
link_locations = [Point(0, 0, str(i + 1)) for i in range(9)]
link_locations[8].name = "tail"
tail_visits = set()

filename = "testb.dat"
commands = common.read_file_as_lines(filename)

print("START: {}, {}".format(head_location.display(), link_locations[8].display()))


def move_links(head_loc, link_locs, direc):
    prev_loc = head_loc
    index = 0
    for link in link_locs:
        functions.move_link(prev_loc, link, direc)
        prev_loc = link
        index = index + 1


for command in commands:
    print(command)
    command_tokens = command.split(' ')
    direc = command_tokens[0]
    distance = int(command_tokens[1])

    for index in range(distance):
        print("-")
        head_location.move_point(direc)
        print("move {}: {}, {}".format(head_location.name, head_location.display(), link_locations[8].display()))
        move_links(head_location, link_locations, direc)
        tail_visits.add(link_locations[8])
        print("unique tail visit count: {}".format(len(tail_visits)))
    print()
