def calculate_sums_of_calories(list_of_elf_inventories):
    sums_of_calories = []
    for elf_inventory in list_of_elf_inventories:
        sums_of_calories.append(sum([int(snack) for snack in elf_inventory.split()]))
    sums_of_calories.sort()
    return sums_of_calories


if __name__ == '__main__':
    source_file = open("resources/day01.txt", "r").read().split("\n\n")
    print(calculate_sums_of_calories(source_file)[-1:])
    print(sum(calculate_sums_of_calories(source_file)[-3:]))
