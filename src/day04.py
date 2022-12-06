def part1(assignments):
    result = 0
    for pair in assignments:
        elf1, elf2 = pair.split(",")
        a1, a2 = elf1.split("-")
        b1, b2 = elf2.split("-")
        if (int(a1) >= int(b1) and int(a2) <= int(b2)) or (int(b1) >= int(a1) and int(b2) <= int(a2)):
            result += 1
    return result


def part2(assignments):
    result = len(assignments)
    for pair in assignments:
        elf1, elf2 = pair.split(",")
        a1, a2 = elf1.split("-")
        b1, b2 = elf2.split("-")
        if int(a2) < int(b1) or int(a1) > int(b2):
            result -= 1
    return result


if __name__ == '__main__':
    pair_assignments = open("resources/day04.txt", "r").read().splitlines()
    print(part1(pair_assignments))
    print(part2(pair_assignments))
