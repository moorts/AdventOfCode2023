def parse(s):
    digits = []
    for i in range(len(s)):
        if s[i].isdigit():
            digits.append(int(s[i]))
        for j, prefix in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if s[i:].startswith(prefix):
                digits.append(j + 1)
    return 10*digits[0] + digits[-1]


def filter(s):
    out = ""
    for c in s:
        if c.isdigit():
            out += c
    return out

with open("./data") as f:
    data = f.read()
    lines = data.splitlines()
    lines = [parse(line) for line in lines]

    print(sum(lines))
