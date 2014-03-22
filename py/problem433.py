from memoize import Memoize

def E(x, y):
    if y == 0:
        return 0
    else:
        return 1 + E(y, x % y)

def S(n):
    if n == 1:
        return 1
    return S(n - 1) + sum([E(x, n) for x in range(1, n + 1)]) + sum([E(n, x) for x in range(1, n)])

S = Memoize(S)

print E(1, 1)
print E(10, 6)
print E(6, 10)

print S(1)
print S(10)
print S(100)
#for x in range(1, 5 * 10 ** 6):
#    print x, S(x)
#print S(5 * 10 ** 6)
for x in range(1, 51):
    for y in range(1, 51):
        print E(x, y),
    print sum([E(x, y) for y in range(1, 51)])