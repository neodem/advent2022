from common import Queue

class Monkey:
    old = False
    inspect_count = 0

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

    def get_operand_string(self):
        if self.old:
            return "itself"
        return self.operand

    def get_operation_string(self):
        if self.operator == "*":
            return 'is multiplied by'
        if self.operator == "+":
            return 'increases by'

    def inspect(self, item):
        self.inspect_count = self.inspect_count + 1
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