import common
import functions

pairs = functions.read_file_to_pairs('test.dat')

for pair in pairs:
    pair.compute()
