import common
from common import Queue
import re


class Monkey:
    old = False

    def __init__(self, monkey_id, starting_items, operator, operand, test, test_true, test_false):
        self.monkey_id = monkey_id
        self.items = self.add_starting_items([int(x) for x in starting_items.split(",")])
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

    def add_starting_items(self, starting_items):
        q = Queue()
        for item in starting_items:
            q.enque(item)
        return q

    def add_item(self, item):
        self.items.enque(item)

    def get_operation_string(self):
        if self.operator == "*":
            return 'is multiplied by'
        if self.operator == "+":
            return 'increases by'
        # if self.operator == "-":
        #     return 'decreases by'
        # if self.operator == "/":
        #     return 'is divided by'

    def inspect(self, item):
        if self.operator == "*":
            if self.old:
                return item * item
            else:
                return item * self.operand
        if self.operator == "+":
            if self.old:
                return item + item
            else:
                return item + self.operand


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


def handle_item(item, monkey_id, monkeys):
    m = monkeys[monkey_id]
    print("  Monkey inspects an item with a worry level of {}.".format(item))
    new_level = m.inspect(item)
    print("    Worry level {} {} to {}.".format(m.get_operation_string(), m.operand, new_level))
    bored_level = new_level // 3
    print("    Monkey gets bored with item. Worry level is divided by 3 to {}.".format(bored_level))
    mod = bored_level % m.test

    test_result = "is not"
    if mod == 0:
        test_result = "is"
        throw_to = m.test_true
    else:
        throw_to = m.test_false

    print("    Current worry level {} divisible by {}.".format(test_result, m.test))
    print("    Item with worry level {} is thrown to monkey {}.".format(bored_level, throw_to))

    monkeys[throw_to].add_item(bored_level)


def process_monkey(monkey_id, monkeys):
    m = monkeys[monkey_id]
    print("Monkey {}:".format(m.monkey_id))

    items = m.items

    while not items.is_empty():
        item = items.deque()
        handle_item(item, monkey_id, monkeys)


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
