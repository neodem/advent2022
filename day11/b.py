import common
import functions




def handle_item(item, monkey_id, monkeys):
    m = monkeys[monkey_id]
    print("  Monkey inspects an item with a worry level of {}.".format(item))
    new_level = m.inspect(item)
    print("    Worry level {} {} to {}.".format(m.get_operation_string(), m.get_operand_string(), new_level))
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


def display_monkeys(monkeys, round_number):
    print()
    print("results from round {}".format(round_number))
    for index in range(len(monkeys)):
        m = monkeys[index]
        print("Monkey {}: {}".format(m.monkey_id, m.items.as_list()))


def process_round(monkeys, round_num):
    print("round {}".format(round_num))
    print()
    for index in range(len(monkeys)):
        process_monkey(index, monkeys)

    display_monkeys(monkeys, round_num)
    print()


filename = "input.dat"
lines = common.read_file_as_lines(filename)
monkeys = functions.ingest_monkey_data(lines)
for index in range(20):
    process_round(monkeys, index + 1)

inspections = []
for monkey in monkeys.values():
    i = monkey.inspect_count
    inspections.append(i)
    print("Monkey {} inspected items {} times".format(monkey.monkey_id, i))

inspections.sort(reverse=True)
print("inspection_counts: {}".format(inspections))

mb = inspections[0] * inspections[1]

print("monkey business: {}".format(mb))
