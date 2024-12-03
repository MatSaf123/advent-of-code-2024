import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

sum = 0
with open('input.txt', 'r') as f:
    line = f.read()

    matches = re.findall(pattern, line)

    for a, b in [(int(m[0]), int(m[1])) for m in matches]:
        sum += a*b

print(sum)
