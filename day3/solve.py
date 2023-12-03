from collections import defaultdict

def neighbors(y, x, n):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            ny = y + dy
            nx = x + dx
            if 0 < ny < n and 0 < nx < n:
                yield (ny, nx)

def solve(schematic):
    n = len(schematic)
    m = len(schematic[0])
    assert n == m

    gears = defaultdict(list)

    part1 = 0
    part2 = 0
    for y in range(n):
        x = 0
        while x < n:
            part_num = False
            value = 0
            adj_gear = None
            while x < n and schematic[y][x].isdigit():
                value *= 10
                value += int(schematic[y][x])

                for ny, nx in neighbors(y, x, n):
                    if schematic[ny][nx] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                        part_num = True
                        if schematic[ny][nx] == "*":
                            adj_gear = (ny, nx)

                x += 1
            x += 1
            if part_num:
                part1 += value
                if adj_gear is not None:
                    gears[adj_gear].append(value)
    for l in gears.values():
        if len(l) == 2:
            part2 += l[0] * l[1]
    return part1, part2




with open("./data") as f:
    data = f.read()
    lines = data.splitlines()

    print(solve(lines))

