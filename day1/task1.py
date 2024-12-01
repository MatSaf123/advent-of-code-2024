import re

pattern = r'(\d+)\s+(\d+)'

# Read the input file into two lists
list_a = []
list_b = []
with open("input.txt", "r") as f:
    for row in f:
        groups = re.findall(pattern, row)
        assert len(groups) == 1, "More than one group found, this is not allowed"
        group = groups[0]
        list_a.append(int(group[0]))
        list_b.append(int(group[1]))

# Sort the lists
list_a.sort()
list_b.sort()

# Go over the list and compute distances.
# We could save them into a list but lets count the sum already
sum = 0
for pair in zip(list_a, list_b):
    a = pair[0]
    b = pair[1]

    if a > b:
        sum += a - b
    else:
        sum += b - a

# Print the sum
print(sum)
