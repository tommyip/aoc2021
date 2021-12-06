import sys
from collections import Counter

line = [int(x) for x in sys.stdin.read().strip().split(',')]


def simulate_fast(line, days):
    counter = Counter(line)
    m = [counter.get(i, 0) for i in range(9)]
    for _day in range(days):
        n_reset = m[0]
        for i in range(8):
            m[i] = m[i+1]
        m[6] += n_reset
        m[8] = n_reset
    return sum(m)


print('Part 1:', simulate_fast(line, 80))
print('Part 2:', simulate_fast(line, 256))
