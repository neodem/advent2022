def find_overlap(lines):
    common_chars = list(set(lines[0]) & set(lines[1]) & set(lines[2]))
    return common_chars[0]


def calc_priority(overlap):
    ascii = ord(overlap)

    if ascii > 96:
        return ascii - 96

    return ascii - 38


total = 0
index = 0
lines = []
with open("sacks.dat") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
        index = index + 1
        if not index % 3:
            index = 0
            overlap = find_overlap(lines)
            lines.clear()
            priority = calc_priority(overlap)
            total = total + priority


print("total: {}".format(total))
