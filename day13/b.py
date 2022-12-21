import functions
import common
import copy
from functools import cmp_to_key


def num_scanner(str):
    """
    strip the first part of the string until we get a number or end
    :param str:
    :return:
    """
    for index in range(len(str)):
        char = str[index]
        if '0' <= char <= '9':
            return ''.join(str[index:])

    return ''


def get_number(str):
    """
    for a given string return the first number seen before the first comma or '] or end of string
    also, remove it from the string
    eg. "345,233" will return 345
    eg. "345]" will return 345
    eg. "345" will return 345
    :param token: a string
    :return: [the new string and an integer for the number found]
    """
    number_register = []

    index = 0
    while len(str) > 0:
        char = str[index]
        if '0' <= char <= '9':
            number_register.append(char)
            str = str[index + 1:]
            index = -1
        elif char == ',' or char == ']':
            break

        index += 1

    if len(number_register) > 0:
        number = ''.join(number_register)
        return [str, int(number)]

    return [str, None]


# scan the string, return all numbers as a list, disregard all brackets
def parse_string_to_list_of_numbers(some_string):
    result = []
    s = num_scanner(some_string)
    while s != '':
        get_number_result = get_number(s)
        result.append(get_number_result[1])
        s = num_scanner(get_number_result[0])

    return result


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

data = [parse_string_to_list_of_numbers("[[2]]"), parse_string_to_list_of_numbers("[[6]]")]
lines = common.read_file_as_lines(filename)
for line in lines:
    if len(line) > 0:
        data.append(parse_string_to_list_of_numbers(line))

data = sorted(data, key=cmp_to_key(comparator))

index2 = 0
index6 = 0
index = 1
for data_packet in data:
    if data_packet == [2]:
        index2 = index
    if data_packet == [6]:
        index6 = index
    index += 1

print("decoder key: {}".format(index2 * index6))
