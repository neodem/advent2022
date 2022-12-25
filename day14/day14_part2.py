import functions


def drop_sand(matrix, row_index, col_index):
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


filename = 'input.dat'
[matrix, min_col, max_col, max_row] = functions.loadMatrix(filename)

# add floor
for col_index in range(matrix.num_cols):
    matrix.set_value(max_row + 2, col_index, '#')

# matrix.draw(col_min=min_col-2)

sand_counter = 0
while functions.is_open(matrix, 0, 500):
    drop_sand(matrix, 0, 500)
    sand_counter += 1

matrix.draw()
print()
print("num dropped before we filled up: {}".format(sand_counter))
