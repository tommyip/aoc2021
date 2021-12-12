from utils import read_input
from collections import defaultdict

paths = read_input(lambda line: line.split('-'))

m = defaultdict(list)
for path in paths:
    m[path[0]].append(path[1])
    m[path[1]].append(path[0])


def is_small(node):
    return 'a' <= node[0] <= 'z'


small_caves = [cave for cave in m.keys() if is_small(
    cave) and cave not in ['start', 'end']]


routes1 = 0


def search_part1(node, small_visited: set):
    global routes1
    if node in small_visited:
        return
    next_sv = small_visited.union({node}) if is_small(node) else small_visited
    if node == 'end':
        routes1 += 1
        return
    neighbors = m[node]
    for neighbor in neighbors:
        search_part1(neighbor, next_sv)


# Using Python's immutable strings as a hack for the lack of immutable
# list.
routes2 = set()


def search_part2(node, small_visited, small_cave, history):
    global routes2
    history += ',' + node
    if node == 'end':
        routes2.add(history)
        return
    if node == small_cave:
        small_cave = None
    else:
        if node in small_visited:
            return
        small_visited = small_visited.union(
            {node}) if is_small(node) else small_visited

    neighbors = m[node]
    for neighbor in neighbors:
        search_part2(neighbor, small_visited, small_cave, history)


search_part1('start', set())

print('Part 1:', routes1)

for small_cave in small_caves:
    search_part2('start', set(), small_cave, '')

print('Part 2:', len(routes2))
