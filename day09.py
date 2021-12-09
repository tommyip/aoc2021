from utils import read_input
from queue import Queue

map = read_input(lambda line: [int(c) for c in line])

w = len(map[0])
h = len(map)

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def neighbor(x, y):
    o = []
    for (dx, dy) in d:
        i = x + dx
        j = y + dy
        if 0 <= i < w and 0 <= j < h:
            o.append((i, j))
    return o


low_points = []
risk_level = 0
for j in range(h):
    for i in range(w):
        this = map[j][i]
        neighbors = neighbor(i, j)
        for (u, v) in neighbors:
            if map[v][u] <= this:
                break
        else:
            low_points.append((i, j))
            risk_level += this + 1
print('Part 1:', risk_level)

sizes = []
for (u, v) in low_points:
    locs = set()
    queue = Queue()
    queue.put((u, v))
    while not queue.empty():
        loc = queue.get()
        locs.add(loc)
        neighbors = neighbor(*loc)
        for (i, j) in neighbors:
            if (i, j) not in locs and map[j][i] != 9:
                queue.put((i, j))
    sizes.append(len(locs))

sorted_size = sorted(sizes, reverse=True)
print('Part 2:', sorted_size[0] * sorted_size[1] * sorted_size[2])
