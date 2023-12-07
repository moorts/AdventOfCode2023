from functools import reduce,cmp_to_key
from collections import Counter

from enum import Enum

cards = "AKQJT98765432"
cards2 = "AKQT98765432J"

def value(card, part2=False):
    if part2:
        return len(cards2) - cards2.index(card)

    return len(cards) - cards.index(card)

class Type(Enum):
    FIVE = 6
    FOUR = 5
    FULL_HOUSE = 4
    THREE = 3
    TWO_PAIRS = 2
    PAIR = 1
    HIGH_CARD = 0

def type(hand, part2=False):
    counter = Counter(hand)

    keys = counter.keys()
    values = counter.values()

    match len(counter):
        case 1:
            return Type.FIVE
        case 2:
            if part2 and "J" in keys:
                return Type.FIVE

            if 4 in values:
                return Type.FOUR

            return Type.FULL_HOUSE
        case 3:
            if part2 and "J" in keys:
                if counter["J"] == 2 or 3 in values:
                    return Type.FOUR
                return Type.FULL_HOUSE
            if 3 in values:
                return Type.THREE
            return Type.TWO_PAIRS
        case 4:
            if part2 and "J" in keys:
                return Type.THREE
            return Type.PAIR
        case _:
            if part2 and "J" in keys:
                return Type.PAIR
            return Type.HIGH_CARD

def compare(game1, game2, part2=False):
    hand1 = game1[0]
    hand2 = game2[0]
    if type(hand1, part2) == type(hand2, part2):
        for c1, c2 in zip(hand1, hand2):
            if value(c1, part2) < value(c2, part2):
                return -1
            if value(c1, part2) > value(c2, part2):
                return 1
        return 0
    return 1 if type(hand1, part2).value > type(hand2, part2).value else -1

def part1(games):
    games = sorted(games, key=cmp_to_key(compare))
    scores = [games[i][1] * (i + 1) for i in range(len(games))]
    return sum(scores)

def part2(games):
    games = sorted(games, key=cmp_to_key(lambda x, y: compare(x, y, True)))
    scores = [games[i][1] * (i + 1) for i in range(len(games))]
    return sum(scores)

with open("./data") as f:
    data = f.read()
    lines = data.splitlines()
    games = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]
    print(part1(games))
    print(part2(games))
