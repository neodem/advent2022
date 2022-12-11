from common import Point


class Plot:
    overlays = []

    # origin values are down and right from the top left
    def __init__(self, width, height, org_down=None, org_right=None):
        self.width = width
        self.height = height
        if org_right is not None:
            self.x_offset = org_right
        else:
            self.x_offset = int(width / 2)

        if org_down is not None:
            self.y_offset = org_down
        else:
            self.y_offset = int(height / 2)

        self.display = [['.'] * self.width for i in range(self.height)]
        self.display[self.y_offset][self.x_offset] = '+'

    def reset_display(self):
        self.display = [['.'] * self.width for i in range(self.height)]
        self.display[self.y_offset][self.x_offset] = '+'

    def print_plot(self, spacing=0):
        self.reset_display()

        for location in self.overlays:
            row = self.y_offset - location.y
            col = location.x + self.x_offset
            self.display[row][col] = location.id

        for row in range(self.height):
            for col in range(self.width):
                print(self.display[row][col], end='')
                for i in range(spacing):
                    print(' ', end='')
            print()

    def add_location(self, location):
        self.overlays.append(location)

    def set_point(self, x, y, id):
        p = Point(x, y, "", id)
        self.overlays.append(p)
