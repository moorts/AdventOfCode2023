def part1(cards):
    score = 0
    for left, right in cards:
        if len(intersection := left & right) > 0:
            score += pow(2, len(intersection) - 1)
    return score

def part2(cards):
    copies = [1] * len(cards)
    score = 0
    for i, (left, right) in enumerate(cards):
        card_score = len(left & right)
        for j in range(card_score):
            copies[i + j + 1] += copies[i]
        score += copies[i]

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
