import random
import operator

# test values
n = 200

# divisble by ...
mod = 23


def reduce_worry(worry_level, mod):
    return worry_level - ((worry_level // mod) * mod)


def test(worry_level, mod):
    return worry_level % mod == 0


worry_levels = []

for i in range(n):
    worry_levels.append(random.randint(1, 200))

print("worry      reduced      test")
print("----------------------------")
for worry_level in worry_levels:
    reduced = reduce_worry(worry_level, mod)
    w_test = test(worry_level, mod)
    r_test = test(reduced, mod)
    all_passed = w_test and r_test
    one_passed = operator.xor(w_test, r_test)

    if w_test:
        print("{}          {}         {}    {}".format(worry_level, reduced, all_passed, one_passed))
