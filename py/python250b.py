from collections import defaultdict

count = defaultdict(int)

for i in [(x ** x) % 250 for x in range(1, 251251)]:
    count[i] += 1

print count
