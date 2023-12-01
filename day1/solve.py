def part1(lines):
    return sum(map(parse1, lines))

def part2(lines):
    return sum(map(parse2, lines))

def parse1(s):
    l = list(map(int, filter(str.isdigit, s)))
    return 10*l[0] + l[-1]

def parse2(s):
    digits = []
    for i in range(len(s)):
        if s[i].isdigit():
            digits.append(int(s[i]))
        for j, prefix in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if s[i:].startswith(prefix):
                digits.append(j + 1)
    return 10*digits[0] + digits[-1]


with open("./data") as f:
    data = f.read()
    lines = data.splitlines()

    print(part1(lines))
    print(part2(lines))
