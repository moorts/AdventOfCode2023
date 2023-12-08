from math import lcm

def day1(instrs, network):
    n = len(instrs)
    node = "AAA"
    steps = 0
    while node != "ZZZ":
        node = network[node][instrs[steps % n]]
        steps += 1
    return steps

def day2(instrs, network):
    state = []
    n = len(instrs)
    steps = 0
    for node in network.keys():
        if node[-1] == 'A':
            state.append(node)

    factors = []
    for i in range(len(state)):
        new_state = [None] * len(state)
        start = state[i]
        dists = []
        while len(dists) < 2:
            state[i] = network[state[i]][instrs[steps % n]]
            if state[i][-1] == 'Z':
                dists.append(steps)
            steps += 1
        factors.append(dists[1] - dists[0])
    return lcm(*factors)

    


with open('./data') as f:
    data = f.read()
    instrs, maps = data.split("\n\n")

    instrs = list(map(lambda c: 0 if c == 'L' else 1, instrs))

    network = {}
    for line in maps.splitlines():
        start, leftright = line.split(" = ")
        left, right = leftright[1:-1].split(", ")
        network[start] = (left, right)

    print(day1(instrs, network))
    print(day2(instrs, network))
