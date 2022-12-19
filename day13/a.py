import functions

pairs = functions.read_file_to_pairs('test_cases.dat')

right_order_index_sum = 0

for pair in pairs:
    pair.compute(logging=True)
    print()
    if pair.right_order:
        right_order_index_sum += pair.index

print("sum: {}".format(right_order_index_sum))
