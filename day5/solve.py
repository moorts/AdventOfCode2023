def apply(mapping, seed):
    for dst, src, length in mapping:
        dist = seed - src
        if 0 <= dist < length:
            return dst + dist
    return seed

def apply_range(mapping, seed, seed_length):
    for i, (dst, src, length) in enumerate(mapping):
        dist = seed - src
        if 0 <= dist < length:
            return dst + dist, min(length - dist, seed_length)

        if seed < src:
            return seed, abs(dist)

    return seed, seed_length





def part1(seeds, maps):
    state = seeds
    for mapping in maps:
        state = [apply(mapping, seed) for seed in state]
    return min(state)

def part2(seeds, maps):
    maps = [sorted(mapping, key=lambda x: x[1]) for mapping in maps]
    seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

    out = None

    for start, length in seeds:
        state = [[start, length]]
        for mapping in maps:
            new_state = []
            for start, length in state:
                increment = 0
                while increment < length:
                    new_start, new_length = apply_range(mapping, start + increment, length - increment)
                    increment += new_length
                    new_state.append([new_start, new_length])
            state = new_state
        min_location = min(state, key=lambda x: x[0])[0]
        if out is not None:
            out = min(out, min_location)
        else:
            out = min_location
    return out




def parse_map(lines):
    return [list(map(int, line.split(" "))) for line in lines]

with open("./data") as f:
    data = f.read()
    paragraphs = data.split("\n\n")

    seeds = paragraphs[0]
    seeds = [int(seed) for seed in seeds.removeprefix("seeds: ").split(" ")]
    maps = paragraphs[1:]
    maps = [parse_map(paragraph.strip().split(":\n")[1].split("\n")) for paragraph in maps]
    
    print(part1(seeds, maps))
    print(part2(seeds, maps))
