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

# bit criteria : oxygen generator rating
oxygen_rating = None
lines_left = lines
for i in range(w):
    lines_next = []
    count = 0
    for line in lines_left:
        if line[i] == '1':
            count += 1
    if count >= (len(lines_left) - count):
        for line in lines_left:
            if line[i] == '1':
                lines_next.append(line)
    else:
        for line in lines_left:
            if line[i] == '0':
                lines_next.append(line)
    lines_left = lines_next
    if len(lines_left) == 1:
        oxygen_rating = lines_left[0]
        break
else:
    raise Exception('Oxygen rating not found')

# bit criteria : CO2 scrubber rating
co2_rating = None
lines_left = lines
for i in range(w):
    lines_next = []
    count = 0
    for line in lines_left:
        if line[i] == '1':
            count += 1
    if count < (len(lines_left) - count):
        for line in lines_left:
            if line[i] == '1':
                lines_next.append(line)
    else:
        for line in lines_left:
            if line[i] == '0':
                lines_next.append(line)
    lines_left = lines_next
    if len(lines_left) == 1:
        co2_rating = lines_left[0]
        break
else:
    raise Exception(' rating not found')
print(oxygen_rating, co2_rating)


def s2d(s):
    x = 0
    for i, bit in enumerate(reversed(s)):
        if bit == '1':
            x += 2 ** i
    return x


print('Part 2:', s2d(oxygen_rating) * s2d(co2_rating))
