def look_from_left(list_of_trees):
    set = {(0, 0)}
    for y in range(len(list_of_trees)):
        tallest_tree = -1
        for x in range(len(list_of_trees[y])):
            if int(list_of_trees[y][x]) > tallest_tree:
                set.add((x, y))
                tallest_tree = int(list_of_trees[y][x])
    return set


def look_from_right(list_of_trees):
    set = {(0, 0)}
    for y in range(len(list_of_trees)):
        tallest_tree = -1
        for x in range(len(list_of_trees[y]) - 1, -1, -1):
            if int(list_of_trees[y][x]) > tallest_tree:
                set.add((x, y))
                tallest_tree = int(list_of_trees[y][x])
    return set


def look_from_top(list_of_trees):
    set = {(0, 0)}
    for x in range(len(list_of_trees[0])):
        tallest_tree = -1
        for y in range(len(list_of_trees[x])):
            if int(list_of_trees[y][x]) > tallest_tree:
                set.add((x, y))
                tallest_tree = int(list_of_trees[y][x])
    return set


def look_from_bot(list_of_trees):
    set = {(0, 0)}
    for x in range(len(list_of_trees[0])):
        tallest_tree = -1
        for y in range(len(list_of_trees[x]) - 1, -1, -1):
            if int(list_of_trees[y][x]) > tallest_tree:
                set.add((x, y))
                tallest_tree = int(list_of_trees[y][x])
    return set


def part1():
    list_of_tree_lines = open("/Users/mateusz/PycharmProjects/advent-of-code-2022-python/resources/day08.txt",
                              "r").read().splitlines()
    a = look_from_left(list_of_tree_lines)
    b = look_from_right(list_of_tree_lines)
    c = look_from_top(list_of_tree_lines)
    d = look_from_bot(list_of_tree_lines)
    e = a.union(b.union(c.union(d)))
    print(len(e))


def tree_score(x, y, list_of_tree_lines):
    score = 1
    tmp_score = 0
    for z in range(x + 1, len(list_of_tree_lines), 1):
        if list_of_tree_lines[y][z] < list_of_tree_lines[y][x]:
            tmp_score += 1
        else:
            tmp_score += 1
            break
    if tmp_score != 0:
        score = score * tmp_score
    tmp_score = 0
    for z in range(x - 1, -1, -1):
        if list_of_tree_lines[y][z] < list_of_tree_lines[y][x]:
            tmp_score += 1
        else:
            tmp_score += 1
            break
    if tmp_score != 0:
        score = score * tmp_score
    tmp_score = 0
    for z in range(y - 1, -1, -1):
        if list_of_tree_lines[z][x] < list_of_tree_lines[y][x]:
            tmp_score += 1
        else:
            tmp_score += 1
            break
    if tmp_score != 0:
        score = score * tmp_score
    tmp_score = 0
    for z in range(y + 1, len(list_of_tree_lines), 1):
        if list_of_tree_lines[z][x] < list_of_tree_lines[y][x]:
            tmp_score += 1
        else:
            tmp_score += 1
            break
    if tmp_score != 0:
        score = score * tmp_score
    return score


def part2():
    list_of_tree_lines = open("/Users/mateusz/PycharmProjects/advent-of-code-2022-python/resources/day08.txt",
                              "r").read().splitlines()
    high_score = 0
    for y in range(len(list_of_tree_lines)):
        for x in range(len(list_of_tree_lines[0])):
            score = tree_score(x, y, list_of_tree_lines)
            if high_score < score:
                high_score = score
    print(high_score)


if __name__ == '__main__':
    part1()
    part2()
