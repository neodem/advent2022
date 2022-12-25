import functions


def find_smallest_to_free(root, min_to_free):
    sub_dirs = functions.get_all_dirs(root)
    smallest = root.get_total_size()
    for sub_dir in sub_dirs:
        sub_dir_size = sub_dir.get_total_size()
        if sub_dir_size >= min_to_free:
            if sub_dir_size < smallest:
                smallest = sub_dir_size

    return smallest


filename = "input.dat"
root = functions.load_tree_from_file(filename)

disk_size = 70000000
space_needed = 30000000
total_usage = root.get_total_size()
space_left = disk_size - total_usage
min_to_free = space_needed - space_left

print("disk_size: {}".format(disk_size))
print("space_needed: {}".format(space_needed))
print("total_usage: {}".format(total_usage))
print("space_left: {}".format(space_left))
print("min_to_free: {}".format(min_to_free))
print()

smallest_to_free = find_smallest_to_free(root, min_to_free)

print("smallest_to_free: {}".format(smallest_to_free))
