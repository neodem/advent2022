
class File:
    name = ""
    size = 0

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def get_size(self):
        return self.size

    def display(self, indent):
        spaces = ' ' * indent
        print("{}- {} (file, size={})".format(spaces, self.name, self.size))


class Dir:
    name = ""
    parent = None
    files = []
    dirs = []

    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.dirs = []
        self.parent = parent

    def has_children(self):
        return len(self.dirs) > 0

    def goto(self, dest):
        if self.dirs:
            for dir in self.dirs:
                if dir.name == dest:
                    return dir
        else:
            return self

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, dir):
        self.dirs.append(dir)

    def get_total_size(self):
        size = 0

        if self.files:
            for file in self.files:
                size = size + file.get_size()
        if self.dirs:
            for dir in self.dirs:
                size = size + dir.get_total_size()

        return size

    def display(self, indent=0):
        spaces = ' ' * indent
        print("{}- {} (dir, size={})".format(spaces, self.name, self.get_total_size()))

        if self.files:
            for file in self.files:
                file.display(indent + 2)
        if self.dirs:
            for dir in self.dirs:
                dir.display(indent + 2)
