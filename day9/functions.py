import math


def distance(point0, point1):
    dx = (point1.x - point0.x) ** 2
    dy = (point1.y - point0.y) ** 2
    return math.sqrt(dx + dy)


def touching(loc0, loc1):
    return distance(loc0, loc1) < 2


# move a link relative to the previous one. Return the updated location of the link (may not have moved)
def move_link(previous_link, link_loc):
    if touching(previous_link, link_loc):
        print("link {} is touching link {}".format(link_loc.name, previous_link.name))

    # if our dir is 2 then we are in the same col/row and need to move towards the other
    # if x same, move Up/Down, if y same, move Right/Left
    elif distance(previous_link, link_loc) == 2:
        temp_loc = link_loc.copy()

        if previous_link.x == link_loc.x:
            link_loc.move_point("U" if previous_link.y - link_loc.y > 0 else "D")
        else:
            link_loc.move_point("R" if previous_link.x - link_loc.x > 0 else "L")

        print("move {}: {}, {} moves from {} to {}".format(link_loc.name, previous_link.display(), link_loc.name,
                                                           temp_loc, link_loc))
        return link_loc

    # diagonal
    else:
        temp_loc = link_loc.copy()
        link_loc.move_point("R" if previous_link.x - link_loc.x > 0 else "L")
        link_loc.move_point("U" if previous_link.y - link_loc.y > 0 else "D")
        print("move {}: {}, {} moves from {} to {}".format(link_loc.name, previous_link.display(), link_loc.name,
                                                           temp_loc, link_loc))
    return link_loc


# width/height are relative to origin at center
def draw_plot(width, height):
    display = [['.' * width] * height]

    # draw dots
    for row in range(height):
        print(display[row])
