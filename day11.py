from utils import read_input

lines = read_input(lambda line: [int(x) for x in line])

n = len(lines)

neighbors = [(-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0),
             (-1, 1), (0, 1), (1, 1)]

n_flashed = 0
step = 0
while True:
    flashed = set()
    to_flash = []
    for j in range(n):
        for i in range(n):
            lines[j][i] += 1
            if lines[j][i] > 9:
                to_flash.append((i, j))
    while len(to_flash) > 0:
        next_to_flash = []
        for (i, j) in to_flash:
            if (i, j) in flashed:
                continue
            flashed.add((i, j))
            for (dx, dy) in neighbors:
                u, v = i + dx, j + dy
                if 0 <= u < n and 0 <= v < n:
                    lines[v][u] += 1
                    if lines[v][u] > 9:
                        next_to_flash.append((u, v))
        to_flash = next_to_flash
    for (i, j) in flashed:
        lines[j][i] = 0

    step += 1
    n_flashed += len(flashed)

    if step == 100:
        print('Part 1:', n_flashed)

    if len(flashed) == n * n:
        print('Part 2:', step)
        break
