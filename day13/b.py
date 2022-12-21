import functions
import common
import copy
from functools import cmp_to_key


def parse_string_to_list_of_numbers(some_string):
    result = []

    tokens = functions.parse_list(some_string)

    for token in tokens:
        if common.is_number(token):
            number = common.get_number(token)
            result.append(number)

    return result


def parse_string_to_lists(token):
    result = []

    if common.is_list(token):
        for element in parse_list(token):
            r = parse_string_to_lists(element)
            result.append(r)

    if common.is_number(token):
        number = common.get_number(token)
        return number

    return result


def comparator(left, right):
    result = functions.compare(left, right)
    return result


filename = 'test.dat'
index = 1
logging = True
divider2 = [[2]]
divider6 = [[6]]

data = []
data.append(parse_string_to_list_of_numbers("[[2]]"))
data.append(parse_string_to_list_of_numbers("[[6]]"))
lines = common.read_file_as_lines(filename)
for line in lines:
    if len(line) > 0:
        data.append(parse_string_to_list_of_numbers(line))

data = sorted(data, key=cmp_to_key(comparator))

index2 = 0
index6 = 0
index = 1
for data_packet in data:
    if data_packet == divider2:
        index2 = index
    if data_packet == divider6:
        index6 = index
    index += 1

print("decoder key: {}".format(index2 * index6))
