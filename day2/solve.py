def check(draw):
    available = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for color, k in draw.items():
        if k > available[color]:
            return False
    return True

def part1(games):
    res = 0
    for i in range(len(games)):
        if all([check(draw) for draw in games[i]]):
            res += i + 1
    return res

def power(game):
    return max(game, key=lambda x: 0 if not "red" in x else x["red"])["red"] * max(game, key=lambda x: 0 if not "blue" in x else x["blue"])["blue"] * max(game, key=lambda x: 0 if not "green" in x else x["green"])["green"]
 
def part2(games):
    return sum(map(power, games))

def canonicalize(draw):
    out = dict()
    for s in draw:
        k, color = s.split(" ")
        out[color] = int(k)
    return out


def parse(line):
    _, game = line.split(": ")
    draws = game.split("; ")
    draws = [draw.split(", ") for draw in draws]
    draws = [canonicalize(draw) for draw in draws]

    return draws



#with open("./test") as f:
with open("./data") as f:
    data = f.read()
    lines = data.splitlines()

    games = [parse(line) for line in lines]

    print(part1(games))
    print(part2(games))
