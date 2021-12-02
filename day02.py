from utils import read_input


def preprocess(line):
    cmd, x = line.split(' ')
    return cmd, int(x)


course = read_input(preprocess)

pos, depth = 0, 0
for cmd, x in course:
    if cmd == 'forward':
        pos += x
    elif cmd == 'up':
        depth -= x
    elif cmd == 'down':
        depth += x
print('Part 1:', pos * depth)

pos_2, depth_2, aim = 0, 0, 0
for cmd, x in course:
    if cmd == 'down':
        aim += x
    elif cmd == 'up':
        aim -= x
    elif cmd == 'forward':
        pos_2 += x
        depth_2 += aim * x
print('Part 2:', pos_2 * depth_2)
