import common
from common import MatrixPlot
import sys

filename = 'input.dat'
lines = common.read_file_as_lines(filename)


def break_line_into_segs(line):
    """
    break a formatted line into segments
    :param line: ex. '503,4 -> 502,4 -> 502,9 -> 494,9'
    :return: [[[503,4], [502,4]], [[502,4], [502,9]], [[502,9], [494,9]]
    """
    tokens = line.split('->')
    tokens = [i.strip() for i in tokens]

    segments = []

    while len(tokens) > 1:
        t1 = tokens.pop(0)
        pair = [t1, tokens[0]]
        segments.append(pair)

    return segments


all_segs = []
for line in lines:
    # break into segments
    segs = break_line_into_segs(line)
    # collect all segments
    all_segs = all_segs + segs

# find matrix size and convert points
clean_segs = []
max_row = 0
max_col = 0
min_row = sys.maxsize
min_col = sys.maxsize
for seg in all_segs:
    for point in seg:
        p = point.split(',')

        row = int(p[0])
        col = int(p[1])

        if row > max_row:
            max_row = row
        if row < min_row:
            min_row = row
        if col > max_col:
            max_col = col
        if col < min_col:
            min_col = col

matrix = MatrixPlot(2, 2, '.')


print(all_segs)
