import functions


def drop_sand(matrix, row_index, col_index, max_row):
    """

    :param matrix:
    :param row_index:
    :param col_index:
    :return:
    """
    matrix.set_value(row_index, col_index, 'o')
    while functions.can_move_down(matrix, row_index, col_index):
        new_position = functions.move_down_once(matrix, row_index, col_index)
        # clear last position
        matrix.set_value(row_index, col_index, '.')
        row_index = new_position[0]
        col_index = new_position[1]
        if row_index > max_row:
            return True

    return False


filename = 'input.dat'
[matrix, min_col, max_row] = functions.loadMatrix(filename)

# matrix.draw(col_min=min_col)

sand_counter = 0
off_edge = False
while functions.is_open(matrix, 0, 500) and not off_edge:
    off_edge = drop_sand(matrix, 0, 500, max_row)
    sand_counter += 1
    # print()
    # matrix.draw(col_min=min_col)

matrix.draw(col_min=min_col)
print()
print("num dropped before dropped off edge: {}".format(sand_counter - 1))
