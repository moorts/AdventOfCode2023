import math

def part1(times, distances):
    out = 1
    for time, distance in zip(times, distances):
        # time(t0) = t0 * (time - t0) = - t0**2 + time*t0
        # extremal point: -2t0 + time = 0 => t0 = time / 2
        score = 0
        for t0 in range(time):
            d = t0 * (time - t0)
            if d > distance:
                score += 1
        out *= score
    return out

def part2(times, distances):
    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    # time(t0) = t0 * (time - t0) = - t0**2 + time*t0
    # extremal point: -2t0 + time = 0 => t0 = time / 2
    # time*t0 - t0**2 == distance
    # t0 = time/2 +- sqrt(time**2/4 - distance)

    def cost(t0):
        return t0 * (time - t0)
    score = 0
    t0 = time // 2 - int(math.sqrt(time**2 // 4 - distance))
    t1 = time // 2 + int(math.sqrt(time**2 // 4 - distance))
    assert(cost(t0 - 1) < distance)
    assert(cost(t0) > distance)
    assert(cost(t1) > distance)
    assert(cost(t1 + 2) < distance)

    return t1 - t0 + 2

with open("./data") as f:
    data = f.read().splitlines()
    times = list(map(int, data[0].removeprefix("Time:").strip().split()))
    distances = list(map(int, data[1].removeprefix("Distance:").strip().split()))

    print(part1(times, distances))
    print(part2(times, distances))
