from utils import read_input

depths = read_input(int)

count_1 = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        count_1 += 1

print('Part 1:', count_1)

count_2 = 0
for i in range(3, len(depths)):
    middle_sum = depths[i-1] + depths[i-2]
    cur = middle_sum + depths[i]
    prev = middle_sum + depths[i-3]
    if cur > prev:
        count_2 += 1

print('Part 2:', count_2)
