import functions

filename = 'test.dat'
matrix = functions.loadMatrix(filename)

matrix.draw()


def can_drop(matrix, row_index, col_index):
    try:
        value = matrix.get_value(row_index, col_index)
    except IndexError:
        # we are out of bounds
        return False

    if value == 'o' or value == '#':
        can_drop_left = can_drop(matrix, row_index + 1, col_index - 1)
        if not can_drop_left:
            can_drop_right = can_drop(matrix, row_index + 1, col_index + 1)

            if not can_drop_right:
                return False

        return True
    return True


def drop_sand_one_space(matrix, row_index, col_index):
    """
    drop sand into matrix one space down (if possible)
    :param matrix: can only hold : '.' : empty space, 'o': sand space, '#': block
    :return: True if we did the drop, False if we couldn't
    """
    if can_drop(matrix, row_index, col_index):
        value = matrix.get_value(row_index, col_index)
        if value == 'o' or value == '#':
            # there is something in our way

            # try down and left
            dropped = drop_sand_one_space(matrix, row_index + 1, col_index - 1)
            if not dropped:
                dropped = drop_sand_one_space(matrix, row_index + 1, col_index + 1)

                if not dropped:
                    # we can go no farther
                    return False

            return True

        matrix.set_value(row_index, col_index, '+')
        return True

    return False


row_index = 0
col_index = 500
sand_counter = 0
first = True
value = matrix.get_value(row_index, col_index)
while value == '.':
    while can_drop(matrix, row_index, col_index):
        if not first:
            matrix.set_value(row_index - 1, col_index, '.')
        drop_sand_one_space(matrix, row_index, col_index)
        row_index += 1
        first = False
    sand_counter += 1
    row_index = 0
    first = True
    print()
    matrix.draw()
    value = matrix.get_value(row_index, col_index)
