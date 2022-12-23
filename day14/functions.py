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

    # find matrix size
    max_row = 0
    max_col = 0
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

    num_rows = max_row + 2
    num_cols = max_col + 2

    matrix = MatrixPlot(num_rows, num_cols, initial_value='.')

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

    return [matrix, min_col, max_row]


def is_open(matrix, row_index, col_index):
    """
    return if a given point is open. in bounds and == '.'

    :param matrix:
    :param row_index:
    :param col_index:
    :return:
    """

    try:
        value = matrix.get_value(row_index, col_index)
    except IndexError:
        # we are out of bounds
        return True

    return value == '.'


def can_move_down(matrix, row_index, col_index):
    """
    can we move down, else left, else right?
    :param matrix:
    :param row_index:
    :param col_index:
    :return:
    """

    # check one down
    down = is_open(matrix, row_index + 1, col_index)

    if not down:
        left = is_open(matrix, row_index + 1, col_index - 1)

        if not left:
            return is_open(matrix, row_index + 1, col_index + 1)

    return True


def move_down_once(matrix, row_index, col_index):
    new_row = row_index + 1
    new_col = col_index

    if not is_open(matrix, new_row, new_col):
        new_col -= 1
        if not is_open(matrix, new_row, new_col):
            new_col += 2

    matrix.set_value(new_row, new_col, 'o')
    return [new_row, new_col]
