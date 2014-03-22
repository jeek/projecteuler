from collections import defaultdict

def G(x):
    yield x
    k = 2
    while x > 0:
        xx = x
        based = []
        while xx > 0:
            based.append(xx % k)
            xx = int(xx / k)
        k += 1
#        print based
        xxx = sum([based[x] * k ** x for x in range(len(based))])
        x = xxx - 1
        if x != 0:
            yield x

counted = defaultdict(int)
for j in range(1, 16):
    for i in G(j):
#        print j, i
        counted[j] += 1
    print j, counted[j] % 10 ** 9
print sum(counted.values())
