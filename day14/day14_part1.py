import functions


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


def move_down(matrix, row_index, col_index):
    new_row = row_index + 1
    new_col = col_index

    if not is_open(matrix, new_row, new_col):
        new_col -= 1
        if not is_open(matrix, new_row, new_col):
            new_col += 2

    matrix.set_value(new_row, new_col, 'o')
    return [new_row, new_col]


def drop_sand(matrix, row_index, col_index):
    """

    :param matrix:
    :param row_index:
    :param col_index:
    :return:
    """
    matrix.set_value(row_index, col_index, 'o')
    while can_move_down(matrix, row_index, col_index):
        new_position = move_down(matrix, row_index, col_index)
        # clear last position
        matrix.set_value(row_index, col_index, '.')
        row_index = new_position[0]
        col_index = new_position[1]


filename = 'test.dat'
[matrix, min_col] = functions.loadMatrix(filename)

matrix.draw()

sand_counter = 0
while is_open(matrix, 0, 500):
    drop_sand(matrix, 0, 500)
    sand_counter += 1
    print()
    matrix.draw()

print()
print("sand dropped: {}".format(sand_counter))
