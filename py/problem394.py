import random

cutoff = 1 / 2.0

total = 0.0
times = 0.0
for x in range(1000000):
    top = 1.0
    count = 0
    while top >= cutoff:
        count += 1
        top = min(cutoff, random.random()*top, random.random()*top)
    times += 1
    total += count
print count,times,total,total/times
