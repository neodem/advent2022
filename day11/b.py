import common
import functions

DEBUG = False


def handle_item(item, monkey_id, monkeys):
    m = monkeys[monkey_id]
    worry_level = m.inspect(item)
    mod = worry_level % m.test
    test_result = "is not"
    if mod == 0:
        test_result = "is"
        throw_to = m.test_true
    else:
        throw_to = m.test_false

    if DEBUG:
        print("  Monkey inspects an item with a worry level of {}.".format(item))
        print("    Worry level {} {} to {}.".format(m.get_operation_string(), m.get_operand_string(), worry_level))
        print("    Monkey gets bored with item.")
        print("    Current worry level {} divisible by {}.".format(test_result, m.test))
        print("    Item with worry level {} is thrown to monkey {}.".format(worry_level, throw_to))

    monkeys[throw_to].add_item(worry_level)


def process_monkey(monkey_id, monkeys):
    m = monkeys[monkey_id]
    if DEBUG:
        print("Monkey {}:".format(m.monkey_id))

    items = m.items

    while not items.is_empty():
        item = items.deque()
        handle_item(item, monkey_id, monkeys)


def display_monkeys(monkeys, round_number):
    print()
    print("results from round {}".format(round_number))
    for index in range(len(monkeys)):
        m = monkeys[index]
        print("Monkey {}: {}".format(m.monkey_id, m.items.as_list()))


def process_round(monkeys, round_num):
    if DEBUG:
        print("round {}".format(round_num))
        print()

    for index in range(len(monkeys)):
        process_monkey(index, monkeys)

    if DEBUG:
        display_monkeys(monkeys, round_num)
        print()


def display_inspection_counts(round_number, monkeys):
    print("== After round {} ==".format(round_number))
    inspections = []
    for monkey in monkeys.values():
        i = monkey.inspect_count
        inspections.append(i)
        print("Monkey {} inspected items {} times.".format(monkey.monkey_id, i))

    return inspections


num_rounds = 20
filename = "test.dat"
lines = common.read_file_as_lines(filename)
monkeys = functions.ingest_monkey_data(lines)

round_displays = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for index in range(num_rounds):
    round_number = index + 1
    process_round(monkeys, round_number)
    if round_displays.__contains__(round_number):
        display_inspection_counts(round_number, monkeys)

# inspections.sort(reverse=True)
# print("inspection_counts: {}".format(inspections))
#
# mb = inspections[0] * inspections[1]
#
# print("monkey business: {}".format(mb))
