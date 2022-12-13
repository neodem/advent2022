import common
import re


class Monkey:
    old = False

    def __init__(self, monkey_id, starting_items, operator, operand, test, test_true, test_false):
        self.monkey_id = monkey_id
        self.items = [int(x) for x in starting_items.split(",")]
        self.operator = operator
        self.operand = self.parse_operand(operand)
        self.test = test
        self.test_true = test_true
        self.test_false = test_false

    def parse_operand(self, operand):
        if operand == "old":
            self.old = True
            return 0
        return int(operand)


monkey_regex = r"Monkey\s(\d+)"
starting_items_regex = r"\s?Starting\sitems:\s(.*)"
operation_regex = r"\s?Operation: new = old (.)\s(.*)"
test_regex = r"\s?Test: divisible by\s(.*)"
true_regex = r"\s?If true: throw to monkey (\d+)"
false_regex = r"\s?If false: throw to monkey (\d+)"


def ingest_monkey_data(lines):
    data = {}

    index = 0
    while index < len(lines):

        line = lines[index]

        # read lines until we encounter a "monkey" line
        re_search = re.search(monkey_regex, line)
        if re_search is not None:
            monkey_id = int(re_search.group(1))
            starting_items = re.search(starting_items_regex, lines[index + 1]).group(1)

            ops = re.search(operation_regex, lines[index + 2])
            operator = ops.group(1)
            operand = ops.group(2)

            test = int(re.search(test_regex, lines[index + 3]).group(1))
            test_true = int(re.search(true_regex, lines[index + 4]).group(1))
            test_false = int(re.search(false_regex, lines[index + 5]).group(1))

            monkey = Monkey(monkey_id, starting_items, operator, operand, test, test_true, test_false)
            data[monkey_id] = monkey

        index = index + 1

    return data


filename = "test.dat"
lines = common.read_file_as_lines(filename)
monkeys = ingest_monkey_data(lines)


def process_monkey(monkey_id, monkeys):
    pass


def display_monkeys(monkeys):
    for index in range(len(monkeys)):
        m = monkeys[index]
        print("Monkey {}: {}".format(m.monkey_id, m.items))


def process_round(monkeys, round_num):
    print("round {}".format(round_num))
    print()
    for index in range(len(monkeys)):
        process_monkey(index, monkeys)

    display_monkeys(monkeys)
    print()


for index in range(2):
    process_round(monkeys, index)
