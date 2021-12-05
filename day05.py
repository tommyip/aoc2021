from collections import defaultdict
from utils import read_input


def process(line):
    lhs, rhs = [pair.split(',') for pair in line.split(' -> ')]
    return (int(lhs[0]), int(lhs[1])), (int(rhs[0]), int(rhs[1]))


lines = read_input(process)


def count_points(diagonal: bool) -> int:
    counter = defaultdict(int)
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            ylo, yhi = min(y1, y2), max(y1, y2)
            for y in range(ylo, yhi + 1):
                counter[(x1, y)] += 1
        elif y1 == y2:
            xlo, xhi = min(x1, x2), max(x1, x2)
            for x in range(xlo, xhi + 1):
                counter[(x, y1)] += 1
        elif diagonal:
            xlo, ylo = (x1, y1) if x1 < x2 else (x2, y2)
            flip_y = -1 if (x1 < x2) != (y1 < y2) else 1
            for i in range(abs(x1 - x2) + 1):
                counter[(xlo + i, ylo + i * flip_y)] += 1

    return sum(1 for v in counter.values() if v >= 2)


print('Part 1:', count_points(False))
print('Part 2:', count_points(True))
