import functions


def tota_lte(dir, max):
    sub_dirs = functions.get_all_dirs(dir)
    total = 0
    for sub_dir in sub_dirs:
        if sub_dir.get_total_size() <= max:
            total = total + sub_dir.get_total_size()

    return total


filename = "input.dat"
root = functions.load_tree_from_file(filename)
total_lte_100 = tota_lte(root, 100000)
print("total of dirs lte 100k: {}".format(total_lte_100))
