
calorie_count = []
elf_total = 0

with open("calories.dat") as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            elf_total = elf_total + int(line)
        else:
            calorie_count.append(elf_total)
            elf_total = 0

calorie_max = 0
calorie_index = 0
for elf in calorie_count:
    if calorie_count[calorie_index] > calorie_max:
        calorie_max = calorie_count[calorie_index]
    print("elf {} has {} total calories".format(calorie_index, calorie_count[calorie_index]))
    calorie_index += 1

print("max calories = {}".format(calorie_max))
