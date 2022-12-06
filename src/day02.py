def part1(strategy_guide):
    score = 0
    results = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    }
    for line in strategy_guide:
        score += results[line]
    return score


def part2(strategy_guide):
    score = 0
    results = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }
    for line in strategy_guide:
        score += results[line]
    return score


if __name__ == '__main__':
    lines = open("resources/day02.txt", "r").read().split("\n")
    print(part1(lines))
    print(part2(lines))
