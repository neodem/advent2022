import functions
import common
import copy
from functools import cmp_to_key


def comparator(left, right):
    result = functions.compare(copy.deepcopy(left), copy.deepcopy(right))

    if result == 1:
        return -1

    if result == -1:
        return 1

    return 0


filename = 'input.dat'
index = 1
logging = True

data = [functions.parse_string_to_lists("[[2]]"), functions.parse_string_to_lists("[[6]]")]
lines = common.read_file_as_lines(filename)
for line in lines:
    if len(line) > 0:
        data.append(functions.parse_string_to_lists(line))

data = sorted(data, key=cmp_to_key(comparator))

index2 = 0
index6 = 0
index = 1
for data_packet in data:
    if data_packet == [[2]]:
        index2 = index
    if data_packet == [[6]]:
        index6 = index
    index += 1

print("decoder key: {}".format(index2 * index6))
