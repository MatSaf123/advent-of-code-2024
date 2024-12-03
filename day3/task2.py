
import re

split_pattern = r"(do\(\)|don't\(\))"
mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'


sum = 0
with open('input.txt', 'r') as f:
    line = f.read()

    # Split by using "do()" and "don't()" as delimiters,
    # capture delimiters in the parts as well by using groups
    parts = re.split(split_pattern, line)

    should_compute = True
    for p in parts:
        if p == "don't()":
            should_compute = False
            continue
        elif p == "do()":
            should_compute = True
            continue
        else:
            if should_compute:
                matches = re.findall(mul_pattern, p)
                for a, b in [(int(m[0]), int(m[1])) for m in matches]:
                    sum += a*b

print(sum)
