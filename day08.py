from utils import read_input
from collections import Counter


def process(line):
    lhs, rhs = line.split(' | ')
    return lhs.split(' '), rhs.split(' ')


lines = read_input(process)

m = {
    'abcdefg': 0,
    'ab': 1,
    'acdfg': 2,
    'abcdf': 3,
    'abef': 4,
    'bcdef': 5,
    'bcdefg': 6,
    'abd': 7,
    'abcdeg': 8,
    'abdef': 9
}

part1 = 0
part2 = 0


def is1478(n):
    return n in [2, 4, 3, 7]


#          0  1  2  3  4  5  6  7  8  9
lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for lhs, rhs in lines:
    part1 += sum(is1478(len(x)) for x in rhs)

    def find(n):
        return [set(x) for x in lhs if len(x) == n][0]

    d1 = find(2)
    d4 = find(4)
    d7 = find(3)
    d8 = find(7)

    def deduce069(x):
        if len(x.intersection(d4)) == 4:
            return 9
        if len(x.intersection(d7)) == 2:
            return 6
        return 0

    def deduce235(x):
        if len(x.intersection(d1)) == 2:
            return 3
        if len(x.intersection(d4)) == 2:
            return 2
        return 5

    def decode(digit):
        n = len(digit)
        if n == 2:
            return 1
        elif n == 4:
            return 4
        elif n == 3:
            return 7
        elif n == 7:
            return 8
        elif n == 6:  # 0, 6, 9
            s = set(digit)
            return deduce069(s)
        elif n == 5:  # 2, 3, 5
            s = set(digit)
            return deduce235(s)
    n = decode(rhs[0]) * 1000 + decode(rhs[1]) * 100 + \
        decode(rhs[2]) * 10 + decode(rhs[3])
    part2 += n

print('Part 1:', part1)
print('Part 2:', part2)
