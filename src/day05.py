import re

def part1():
    f = open("../resources/day05.txt").read().split("\n\n")
    first_half, second_half = f[0], f[1]

    stacks = first_half.splitlines()
    stacks.pop()
    list_of_towers = []
    tower1 = []
    tower2 = []
    tower3 = []
    tower4 = []
    tower5 = []
    tower6 = []
    tower7 = []
    tower8 = []
    tower9 = []
    list_of_towers.append(tower1)
    list_of_towers.append(tower2)
    list_of_towers.append(tower3)
    list_of_towers.append(tower4)
    list_of_towers.append(tower5)
    list_of_towers.append(tower6)
    list_of_towers.append(tower7)
    list_of_towers.append(tower8)
    list_of_towers.append(tower9)

    for line in stacks:
        for i in range(len(line)):
            if i % 4 == 1 and line[i] != " ":
                list_of_towers[i // 4].append(line[i])

    instructions = second_half.splitlines()
    coordinates = []
    for line in instructions:
        line = re.sub("[^ | 0-9]", "", line)
        line = line.strip()
        a = line.split()
        coordinates.append(a)
    for line in coordinates:
        for i in range(int(line[0])):
            crate = list_of_towers[int(line[1])-1].pop(0)
            list_of_towers[int(line[2])-1].insert(0, crate)
    for tower in list_of_towers:
        print(tower[0], end="")

def part2():
    f = open("../resources/day05.txt").read().split("\n\n")
    first_half, second_half = f[0], f[1]
    stacks = first_half.splitlines()
    stacks.pop()
    list_of_towers = []
    tower1 = []
    tower2 = []
    tower3 = []
    tower4 = []
    tower5 = []
    tower6 = []
    tower7 = []
    tower8 = []
    tower9 = []
    list_of_towers.append(tower1)
    list_of_towers.append(tower2)
    list_of_towers.append(tower3)
    list_of_towers.append(tower4)
    list_of_towers.append(tower5)
    list_of_towers.append(tower6)
    list_of_towers.append(tower7)
    list_of_towers.append(tower8)
    list_of_towers.append(tower9)

    for line in stacks:
        for i in range(len(line)):
            if i % 4 == 1 and line[i] != " ":
                list_of_towers[i // 4].append(line[i])

    instructions = second_half.splitlines()
    coordinates = []
    for line in instructions:
        line = re.sub("[^ | 0-9]", "", line)
        line = line.strip()
        a = line.split()
        coordinates.append(a)
    for line in coordinates:
        crates = []
        for i in range(int(line[0])):
            crates.append(list_of_towers[int(line[1]) - 1].pop(0))
        for i in range(int(line[0])):
            list_of_towers[int(line[2]) - 1].insert(0, crates.pop())
    print()
    for tower in list_of_towers:
        print(tower[0], end="")


if __name__ == '__main__':
    part1()
    part2()

