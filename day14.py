import sys
from collections import Counter, defaultdict

lines = sys.stdin.read().rstrip()
template, rules_str = lines.split('\n\n')
rules = {}
for rule_str in rules_str.split('\n'):
    lhs, rhs = rule_str.split(' -> ')
    rules[lhs] = rhs


def solve(steps):
    pair_count = defaultdict(int)
    for lhs in rules.keys():
        pair_count[lhs] = 1 if lhs in template else 0

    for _ in range(steps):
        next_pair_count = defaultdict(int)
        for pair, count in pair_count.items():
            insert = rules[pair]
            next_pair_count[pair[0] + insert] += count
            next_pair_count[insert + pair[1]] += count
        pair_count = next_pair_count

    count = defaultdict(int)
    for pair, pc in pair_count.items():
        count[pair[0]] += pc
    count[template[-1]] += 1

    counter = Counter(count)
    common = counter.most_common()
    return common[0][1] - common[-1][1]


print('Part 1:', solve(10))
print('Part 2:', solve(40))
