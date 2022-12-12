import common
from classes import CPU
import functions

filename = "test_b.dat"
commands = common.read_file_as_lines(filename)
cycle_count = 1
cpu = CPU()
ss = {}


def do_cycle():
    global cycle_count
    cycle_count = cycle_count + 1
    cpu.cycle_clock()
    if functions.record_data(cycle_count):
        ss[cycle_count] = cycle_count * cpu.get_register()
    print("advance clock | cycle: {}, register={}, signal_strength={}".format(cycle_count,
                                                                              cpu.register,
                                                                              cycle_count * cpu.get_register()))


while True:
    command = functions.fetch_command(commands)
    if command is not None:
        print("set command to {} | cycle: {}, register={}, signal_strength={}".format(command, cycle_count,
                                                                                      cpu.register,
                                                                                      cycle_count * cpu.get_register()))
        cpu.set_command(command)

        while not cpu.ready():
            do_cycle()

    else:
        break

print("-----------------------------------")
print("cycle_count: {}".format(cycle_count))
print("ss: {}".format(ss))

sum = 0
for item in ss.values():
    sum = sum + item

print("sum: {}".format(sum))
