import common
from common import Matrix


def visible_from_left(row, col, matrix, size):
    for col_index in range(col - 1, -1, -1):
        val = matrix.get_value(row, col_index)
        if val is None:
            return True
        if val >= size:
            return False
    return True


def visible_from_right(row, col, matrix, size):
    for col_index in range(col + 1, matrix.get_num_cols()):
        val = matrix.get_value(row, col_index)
        if val is None:
            return True
        if val >= size:
            return False
    return True


def visible_from_top(row, col, matrix, size):
    for row_index in range(row - 1, -1, -1):
        val = matrix.get_value(row_index, col)
        if val is None:
            return True
        if val >= size:
            return False
    return True


def visible_from_bottom(row, col, matrix, size):
    for row_index in range(row + 1, matrix.get_num_cols()):
        val = matrix.get_value(row_index, col)
        if val is None:
            return True
        if val >= size:
            return False
    return True


filename = "input.dat"
lines = common.read_file_as_lines(filename)
matrix = Matrix(lines)

visible_count = 0
for row_index in range(matrix.get_num_rows()):
    for col_index in range(matrix.get_num_cols()):
        size = matrix.get_value(row_index, col_index)
        visible = False
        # (possible to be smart about the order of vv depending on where the cell is in the matrix)
        if visible_from_left(row_index, col_index, matrix, size):
            visible = True
        elif visible_from_right(row_index, col_index, matrix, size):
            visible = True
        elif visible_from_top(row_index, col_index, matrix, size):
            visible = True
        elif visible_from_bottom(row_index, col_index, matrix, size):
            visible = True

        if visible:
            visible_count = visible_count + 1

print("visible: {}".format(visible_count))
