from common import Point


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


def touching(loc0, loc1):
    if loc0 == loc1:
        return True

    if steps_apart(loc0, loc1, 1):
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


# move a link relative to the previous one. Return the updated location of the link (may not have moved)
def move_link(previous_link, link_loc, direction):
    if touching(previous_link, link_loc):
        print("link {} is touching link {}".format(link_loc.name, previous_link.name))

    elif steps_apart(previous_link, link_loc, 2):
        temp_loc = link_loc.copy()
        link_loc.move_point(direction)
        print("move {}: {}, {} moves from {} to {}".format(link_loc.name, previous_link.display(), link_loc.name,
                                                                          temp_loc, link_loc))
        return link_loc

    else:
        temp_loc = link_loc.copy()
        link_loc.move_point(direction)
        dir2 = calc_dir2(link_loc, previous_link, direction)
        link_loc.move_point(dir2)
        print("move {}: {}, {} moves from {} to {}".format(link_loc.name, previous_link.display(), link_loc.name,
                                                           temp_loc, link_loc))
    return link_loc
