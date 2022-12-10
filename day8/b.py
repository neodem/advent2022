import common
from classes import Matrix


def score_to_left(row, col, matrix, size):
    score = 0;
    for col_index in range(col - 1, -1, -1):
        score = score + 1
        val = matrix.get_value(row, col_index)
        if val >= size:
            break

    return score


def score_to_right(row, col, matrix, size):
    score = 0;
    for col_index in range(col + 1, matrix.get_num_cols()):
        score = score + 1
        val = matrix.get_value(row, col_index)
        if val >= size:
            break

    return score


def score_to_top(row, col, matrix, size):
    score = 0;
    for row_index in range(row - 1, -1, -1):
        score = score + 1
        val = matrix.get_value(row_index, col)
        if val >= size:
            break

    return score


def score_to_bottom(row, col, matrix, size):
    score = 0;
    for row_index in range(row + 1, matrix.get_num_cols()):
        score = score + 1
        val = matrix.get_value(row_index, col)
        if val >= size:
            break

    return score


def calculate_score(row_index, col_index, matrix):
    size = matrix.get_value(row_index, col_index)
    left = score_to_left(row_index, col_index, matrix, size)
    right = score_to_right(row_index, col_index, matrix, size)
    top = score_to_top(row_index, col_index, matrix, size)
    bottom = score_to_bottom(row_index, col_index, matrix, size)

    if left == right == top == bottom == 0:
        return 0

    if left == 0:
        left = 1

    if right == 0:
        right = 1

    if top == 0:
        top = 1

    if bottom == 0:
        bottom = 1

    return left * right * top * bottom


filename = "input.dat"
lines = common.read_file_as_lines(filename)
matrix = Matrix(lines)

highest_scenic_score = 0
for row_index in range(matrix.get_num_rows()):
    for col_index in range(matrix.get_num_cols()):
        scenic_score = calculate_score(row_index, col_index, matrix)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

print("highest scenic score: {}".format(highest_scenic_score))
