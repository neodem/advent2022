calorie_count = []
elf_total = 0

with open("../day2/rps.dat") as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            elf_total = elf_total + int(line)
        else:
            calorie_count.append(elf_total)
            elf_total = 0

calorie_count.sort(reverse=True)

calorie_index = 0
for elf in calorie_count:
    print(calorie_count[calorie_index])
    calorie_index += 1

calorie_max = calorie_count[0] + calorie_count[1] + calorie_count[2]

print("max calories top 3 = {}".format(calorie_max))
