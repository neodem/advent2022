from common import MatrixPlot

# m = MatrixPlot(3, 3, initial_value='.')
#
# m.draw()
# print()
# m.set_value(0, 1, '*')
# m.draw()
# print()
# print(m.get_value(0, 1))

m = MatrixPlot(3, 3, row_offset=1, col_offset=1, initial_value='.')

m.draw()
print()
m.set_value(1, 1, '*')
m.draw()
print()
print(m.get_value(1, 1))
