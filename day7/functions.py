import common
from classes import File
from classes import Dir


def get_all_dirs(root):
    sub_dirs = [root]
    if root.has_children():
        for sub_dir in root.dirs:
            sub_sub_dirs = get_all_dirs(sub_dir)
            if len(sub_sub_dirs) > 0:
                sub_dirs = sub_dirs + sub_sub_dirs

    return sub_dirs


def load_tree(lines):
    root = Dir("/")
    current = root
    in_ls = False
    for line in lines:
        tokens = line.split(' ')
        if line.startswith('$'):
            in_ls = False
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    current = root
                elif tokens[2] == "..":
                    current = current.parent
                else:
                    current = current.goto(tokens[2])
            elif tokens[1] == "ls":
                in_ls = True
        else:
            if in_ls:
                if tokens[0] == "dir":
                    new_dir = Dir(tokens[1], current)
                    current.add_dir(new_dir)
                else:
                    new_file = File(tokens[1], tokens[0])
                    current.add_file(new_file)

    return root


def load_tree_from_file(filename):
    print("loading file " + filename)
    lines = common.read_file_as_lines(filename)
    print("loading tree...")
    root = load_tree(lines)
    root.display()
    print()
    return root
