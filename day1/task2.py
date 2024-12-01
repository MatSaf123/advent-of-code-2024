from collections import Counter
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

# Count the occurrences of numbers in list_b
counter = Counter(list_b)

# Go over list_a and compute the similarity score
similarity_score = 0
for num in list_a:
    num_occurrences = counter.get(num, 0)
    similarity_score += num*num_occurrences

# Print the result
print(similarity_score)
