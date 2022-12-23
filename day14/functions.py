import sys
import common
from common import MatrixPlot
from common import Point


def point_from_token(token):
    coords = token.split(',')
    return Point(int(coords[1]), int(coords[0]))


def break_line_into_segs(line):
    """
    break a formatted line into segments made up of 2 Point objects
    :param line: ex. '503,4 -> 502,4 -> 502,9 -> 494,9'
    :return: [[[503,4], [502,4]], [[502,4], [502,9]], [[502,9], [494,9]]
    """
    tokens = line.split('->')
    tokens = [i.strip() for i in tokens]

    segments = []

    while len(tokens) > 1:
        t1 = point_from_token(tokens.pop(0))
        t2 = point_from_token(tokens[0])
        pair = [t1, t2]
        segments.append(pair)

    return segments


def loadMatrix(filename):
    """

    :param filename:
    :return:
    """
    lines = common.read_file_as_lines(filename)

    all_segs = []
    for line in lines:
        # break into segments
        segs = break_line_into_segs(line)
        # collect all segments
        all_segs = all_segs + segs

    # find matrix size and convert points
    max_row = 0
    max_col = 0
    min_row = 0
    min_col = sys.maxsize
    for seg in all_segs:
        for point in seg:
            row = point.x
            col = point.y

            if row > max_row:
                max_row = row
            if col > max_col:
                max_col = col
            if col < min_col:
                min_col = col

    rows = max_row - min_row + 1
    cols = max_col - min_col + 1

    matrix = MatrixPlot(rows, cols, row_offset=min_row, col_offset=min_col, initial_value='.')

    # add segments to matrix
    for seg in all_segs:
        from_point = seg[0]
        to_point = seg[1]

        # x is row, y is col
        if from_point.x == to_point.x:
            # same row
            row_index = from_point.x

            col_start = min(from_point.y, to_point.y)
            col_end = abs(from_point.y - to_point.y) + col_start + 1

            for col_index in range(col_start, col_end):
                matrix.set_value(row_index, col_index, '#')

        elif from_point.y == to_point.y:
            # same col
            col_index = from_point.y

            row_start = min(from_point.x, to_point.x)
            row_end = abs(from_point.x - to_point.x) + row_start + 1

            for row_index in range(row_start, row_end):
                matrix.set_value(row_index, col_index, '#')

    return matrix
