import common


def is_unique(packet):
    packet_set = set(packet)
    return len(packet_set) == len(packet)


def find_start(line):
    index = 0
    data = common.FixedList(packet_size)
    for char in line:
        data.add(char)
        index = index + 1
        if data.size() == packet_size:
            packet = data.get_list();
            if is_unique(packet):
                return index;


filename = "input.dat"
packet_size = 14

lines = []
with open(filename) as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    print("{} \n::: {}".format(line, find_start(line)))
