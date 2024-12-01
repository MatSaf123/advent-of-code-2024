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

# Sort the lists in ascending order
list_a.sort()
list_b.sort()

# Go over the lists and compute distances between elements on the same indices.
# Compute the distances sum
assert len(list_a) == len(
    list_b), "Lists are not of the same length, this is not allowed"
sum_of_distances = 0
for pair in zip(list_a, list_b):
    a = pair[0]
    b = pair[1]

    if a > b:
        sum_of_distances += a - b
    else:
        sum_of_distances += b - a

# Print the result
print(sum_of_distances)
