import common
from common import Point


def move_point(start_loc, direction):
    if direction == 'L':
        return Point(start_loc.x - 1, start_loc.y)
    if direction == 'R':
        return Point(start_loc.x + 1, start_loc.y)
    if direction == 'U':
        return Point(start_loc.x, start_loc.y + 1)
    if direction == 'D':
        return Point(start_loc.x, start_loc.y - 1)

    return None


def steps_apart(point0, point1, delta):
    # apart on x axis only
    if abs(point0.x - point1.x) == delta and point0.y == point1.y:
        return True

    # apart on y axis only
    if abs(point0.y - point1.y) == delta and point0.x == point1.x:
        return True

    # apart on x,y axis (diag)
    if abs(point0.x - point1.x) == delta and abs(point0.y - point1.y) == delta:
        return True

    return False


def touching():
    if head_location == tail_location:
        return True

    if steps_apart(head_location, tail_location, 1):
        return True

    return False


def calc_dir2(source, target, direction):
    if direction == 'U' or direction == 'D':
        # is target to right or left of source?
        if source.x < target.x:
            return 'R'
        return 'L'

    if direction == 'L' or direction == 'R':
        # is target above or below source?
        if source.y < target.y:
            return 'U'
        return 'D'


def move_tail(tail_loc, direction):
    if touching():
        print("tail is touching head")
        return tail_loc

    if steps_apart(head_location, tail_loc, 2):
        new_tail = move_point(tail_loc, direction)
        print("move tail: head is at {}, tail is at {}".format(head_location, new_tail))
        return new_tail

    tail_loc = move_point(tail_loc, direction)
    dir2 = calc_dir2(tail_loc, head_location, direction)
    new_tail = move_point(tail_loc, dir2)
    print("move tail: head is at {}, tail is at {}".format(head_location, new_tail))
    return new_tail


head_location = Point(0, 0)
tail_location = Point(0, 0)
tail_visits = set()

filename = "test.dat"
commands = common.read_file_as_lines(filename)

print("START: head is at {}, tail is at {}".format(head_location, tail_location))
for command in commands:
    print(command)
    command_tokens = command.split(' ')
    direc = command_tokens[0]
    distance = int(command_tokens[1])

    for index in range(distance):
        print("-")
        head_location = move_point(head_location, direc)
        print("move head: head is at {}, tail is at {}".format(head_location, tail_location))
        tail_location = move_tail(tail_location, direc)
        tail_visits.add(tail_location)
        print("unique tail visit count: {}".format(len(tail_visits)))
    print()

