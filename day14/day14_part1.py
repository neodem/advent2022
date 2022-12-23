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


def move_down_once(matrix, row_index, col_index):
    new_row = row_index + 1
    new_col = col_index

    if not is_open(matrix, new_row, new_col):
        new_col -= 1
        if not is_open(matrix, new_row, new_col):
            new_col += 2

    matrix.set_value(new_row, new_col, 'o')
    return [new_row, new_col]


def drop_sand(matrix, row_index, col_index, max_row):
    """

    :param matrix:
    :param row_index:
    :param col_index:
    :return:
    """
    matrix.set_value(row_index, col_index, 'o')
    while can_move_down(matrix, row_index, col_index):
        new_position = move_down_once(matrix, row_index, col_index)
        # clear last position
        matrix.set_value(row_index, col_index, '.')
        row_index = new_position[0]
        col_index = new_position[1]
        if row_index > max_row:
            return True

    return False


filename = 'test.dat'
[matrix, max_row] = functions.loadMatrix(filename)

matrix.draw(0, 10, 490, 504)

sand_counter = 0
off_edge = False
while is_open(matrix, 0, 500) and not off_edge:
    off_edge = drop_sand(matrix, 0, 500, max_row)
    sand_counter += 1
    print()
    matrix.draw(0, 10, 490, 504)

print()
print("sand dropped before edge: {}".format(sand_counter - 1))
