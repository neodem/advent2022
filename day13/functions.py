from classes import Pair
import common


def read_file_to_pairs(filename):
    lines = common.read_file_as_lines(filename)
    pairs = []
    pair_index = 1
    current_pair = Pair(pair_index)
    line_mod = 0
    for line in lines:
        if line_mod == 0:
            current_pair.set_line1(line)
            line_mod = 1

        elif line_mod == 1:
            current_pair.set_line2(line)
            line_mod = 2

        elif line_mod == 2:
            pairs.append(current_pair)
            pair_index += 1
            current_pair = Pair(pair_index)
            line_mod = 0

    return pairs
