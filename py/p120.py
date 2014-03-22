answer = 0

for a in xrange(3, 1001):
    answer += max([((a - 1) ** n + (a + 1) ** n) % a ** 2 for n in xrange(2 * a + 1)])
print answer
        