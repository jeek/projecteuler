from memoize import Memoize

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def g(n):
    if n == 4:
        return 13
    return g(n - 1) + gcd(n, g(n - 1))

g = Memoize(g)
last = 13
temp = 13
i = 5
while i <= 10 ** 15:
    temp = last + gcd(i, last)
    print i, temp
    last = temp
    i += 1
