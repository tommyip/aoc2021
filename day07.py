import sys
import numpy as np

pos = np.array([int(x)
               for x in sys.stdin.read().strip().split(',')])

part1 = np.sum(np.abs(pos - np.median(pos)), dtype=np.int_)

print('Part 1:', part1)

max_align = np.max(pos)
best_align = (None, 0)
for align in range(max_align + 1):
    distances = np.abs(pos - align)
    cost = np.sum((distances * (distances + 1)) / 2, dtype=np.int_)
    if best_align[0] is None or cost < best_align[1]:
        best_align = (align, cost)

print('Part 2', best_align[1])
