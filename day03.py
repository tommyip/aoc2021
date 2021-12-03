from utils import read_input

lines = read_input(lambda x: x)

n = len(lines)
w = len(lines[0])

counter = [0] * w
for line in lines:
    for i, bit in enumerate(line):
        counter[i] += 1 if bit == '1' else 0

gamma = epsilon = 0
for i, count in enumerate(reversed(counter)):
    if count > (n - count):
        gamma += 2 ** i
    else:
        epsilon += 2 ** i

print('Part 1:', gamma * epsilon)


def rating(lines, flip):
    lines_left = lines
    for i in range(w):
        count = sum([line[i] == '1' for line in lines_left])
        filter_bit = '01'[(int(count >= (len(lines_left) - count)) + flip) % 2]
        lines_left = [line for line in lines_left if line[i] == filter_bit]
        if len(lines_left) == 1:
            return lines_left[0]


oxygen_rating = rating(lines, 0)
co2_rating = rating(lines, 1)
print('Part 2:', int(oxygen_rating, 2) * int(co2_rating, 2))
