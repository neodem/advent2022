import functions
import common


def comp(index):
    if logging:
        print("== Pair {} == : ".format(index))
    result = functions.compare(left, right, logging=logging) != -1
    print("== Pair {} == : {}".format(index, result))
    print()
    if result:
        return index
    return 0


filename = 'input.dat'
line_mod = 0
left = None
right = None
right_order_index_sum = 0
index = 1
logging = True
lines = common.read_file_as_lines(filename)

for line in lines:
    if line_mod == 0:
        left = functions.parse_string_to_lists(line)
        line_mod = 1

    elif line_mod == 1:
        right = functions.parse_string_to_lists(line)
        line_mod = 2

    elif line_mod == 2:
        right_order_index_sum += comp(index)
        index += 1
        line_mod = 0

right_order_index_sum += comp(index)

print("sum: {}".format(right_order_index_sum))
