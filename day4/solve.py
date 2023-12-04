def part1(cards):
    score = 0
    for left, right in cards:
        if len(intersection := left & right) > 0:
            score += pow(2, len(intersection) - 1)
    return score

def part2(cards):
    copies = []
    matches = dict()
    for i, (left, right) in enumerate(cards):
        matches[i] = []
        if len(intersection := left & right) > 0:
            matches[i] = [i + j + 1 for j in range(len(intersection))]
            copies.extend(matches[i])

    score = len(cards)
    while len(copies) > 0:
        i = copies.pop()
        left, right = cards[i]
        score += 1
        copies.extend(matches[i])
    return score


with open("./data") as f:
    data = f.read()
    lines = [line.split(": ")[1] for line in data.splitlines()]

    cards = []
    for line in lines:
        left, right = line.split(" | ")
        left = set(map(int, filter(lambda x: x != '', left.split(" "))))
        right = set(map(int, filter(lambda x: x != '', right.split(" "))))
        cards.append((left, right))

    print(part1(cards))
    print(part2(cards))
