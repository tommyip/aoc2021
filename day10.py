from utils import read_input

lines = read_input(lambda x: x)

error_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_map = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

error_score = 0
completion_scores = []
for line in lines:
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            if stack == []:
                error_score += error_map[c]
                break
            else:
                top = stack.pop()
                if (top, c) not in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
                    error_score += error_map[c]
                    break
    else:
        completion_score = 0
        if len(stack) > 0:
            for c in reversed(stack):
                completion_score = completion_score * \
                    5 + completion_map[c]
        completion_scores.append(completion_score)

print('Part 1:', error_score)

completion_scores.sort()
print('Part 2:', completion_scores[len(completion_scores)//2])
