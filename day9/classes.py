class Plot:
    locations = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = [['.'] * width for i in range(height)]
        self.x_offset = int(width / 2)
        self.y_offset = int(height / 2)
        self.display[self.y_offset][self.x_offset] = '+'

    def reset_display(self):
        self.display = [['.'] * self.width for i in range(self.height)]
        self.display[self.y_offset][self.x_offset] = '+'

    def print_plot(self, spacing=0):
        self.reset_display()

        for location in self.locations:
            self.set_point_from_location(location)

        for row in range(self.height):
            for col in range(self.width):
                print(self.display[row][col], end='')
                for i in range(spacing):
                    print(' ', end='')
            print()

    def add_location(self, location):
        self.locations.append(location)

    def set_point_from_location(self, location):
        row = self.y_offset - location.y
        col = location.x + self.x_offset
        self.display[row][col] = location.id

    def set_point(self, x, y, id):
        row = self.y_offset - y
        col = x + self.x_offset
        self.display[row][col] = id

    def reset_point(self, x, y):
        row = y + self.y_offset
        col = x + self.x_offset
        self.display[row][col] = '.'
