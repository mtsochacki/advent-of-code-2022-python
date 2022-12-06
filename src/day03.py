def part1(compartments):
    priority_sum = 0
    for rucksack in compartments:
        p1 = rucksack[:len(rucksack) // 2]
        p2 = rucksack[len(rucksack) // 2:]
        item = list(set(p1) & set(p2))[0]
        priority_sum += ord(item) - 96 if item.islower() else ord(item) - 38
    return priority_sum


def part2(compartments):
    priority_sum = 0
    for elf1, elf2, elf3 in zip(compartments[::3], compartments[1::3], compartments[2::3]):
        item = list(set(elf1) & set(elf2) & set(elf3))[0]
        priority_sum += ord(item) - 96 if item.islower() else ord(item) - 38
    return priority_sum


if __name__ == '__main__':
    list_of_compartments = open("resources/day03.txt").read().splitlines()
    print(part1(list_of_compartments))
    print(part2(list_of_compartments))
