from collections import defaultdict

def neighbors(y, x, n):
    l = []
    if y > 0:
        l.append((y - 1, x))
        if x < n - 1:
            l.append((y - 1, x + 1))
        if x > 0:
            l.append((y - 1, x - 1))
    if y < n - 1:
        l.append((y + 1, x))
        if x < n - 1:
            l.append((y + 1, x + 1))
        if x > 0:
            l.append((y + 1, x - 1))
    if x > 0:
        l.append((y, x - 1))
    if x < n - 1:
        l.append((y, x + 1))
    return l

def part1(schematic):
    n = len(schematic)
    m = len(schematic[0])
    assert n == m

    out = 0
    for y in range(n):
        x = 0
        while x < n:
            part_num = False
            value = 0
            while x < n and schematic[y][x].isdigit():
                value *= 10
                value += int(schematic[y][x])

                if not part_num:
                    for ny, nx in neighbors(y, x, n):
                        if schematic[ny][nx] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                            part_num = True
                x += 1
            x += 1
            if part_num:
                out += value
    return out

def part2(schematic):
    n = len(schematic)
    m = len(schematic[0])
    assert n == m

    gears = defaultdict(list)

    out = 0
    for y in range(n):
        x = 0
        while x < n:
            part_num = False
            value = 0
            adj_gear = None
            while x < n and schematic[y][x].isdigit():
                value *= 10
                value += int(schematic[y][x])

                if not part_num:
                    for ny, nx in neighbors(y, x, n):
                        if schematic[ny][nx] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                            part_num = True
                            if schematic[ny][nx] == "*":
                                adj_gear = (ny, nx)

                x += 1
            x += 1
            if part_num and adj_gear is not None:
                gears[adj_gear].append(value)
    for l in gears.values():
        if len(l) == 2:
            out += l[0] * l[1]
    return out






with open("./data") as f:
    data = f.read()
    lines = data.splitlines()

    print(part1(lines))
    print(part2(lines))

