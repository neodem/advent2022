def find_overlap(half1, half2):
    common_chars = list(set(half1) & set(half2))
    return common_chars[0]


def calc_priority(overlap):
    ascii = ord(overlap)

    if ascii > 96:
        return ascii - 96

    return ascii - 38


total = 0
with open("sacks.dat") as file:
    for line in file:
        line = line.strip()
        line_len = len(line)
        if line_len > 0:
            half1 = line[0:line_len // 2]
            half2 = line[line_len // 2:]
            overlap = find_overlap(half1, half2)
            priority = calc_priority(overlap)
            total = total + priority

            print("first {}, second {}, overlap: {}, priority: {}, total_score: {}".format(half1, half2, overlap,
                                                                                           priority, total))


print("total: {}".format(total))
