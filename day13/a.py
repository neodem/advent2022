import functions

pairs = functions.read_file_to_pairs('mini.dat')

right_order_index_sum = 0

for pair in pairs:
    pair.compute()
    if pair.right_order:
        right_order_index_sum += pair.index

print("sum: {}".format(right_order_index_sum))
