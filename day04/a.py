def is_fully_in(test, target):
    test_range = set(test)
    target_range = set(target)
    return test_range.issubset(target_range)


def overlap_found(range0, range1):
    return is_fully_in(range0, range1) or is_fully_in(range1, range0)


def make_range(string_range):
    tokens = string_range.split('-')
    num0 = int(tokens[0])
    num1 = int(tokens[1])
    range_list = [*range(num0, num1), num1]
    return range_list


total = 0
with open("input.dat") as file:
    for line in file:
        line = line.strip()
        ranges = line.split(',')
        actual_range0 = make_range(ranges[0])
        actual_range1 = make_range(ranges[1])
        overlap = overlap_found(actual_range0, actual_range1)
        if overlap:
            total = total + 1
        print("first {}, second {}, overlap: {}, total_score: {}".format(actual_range0, actual_range1, overlap, total))

print("total: {}".format(total))
