def gcd(a,b):
    while (b):
        (a, b) = (b, a % b)
    return a
def l(x):
    for i in [k for k in xrange(x - 2, 0, -1) if gcd(k, x) == 1]:
        if (i * i) % x == 1:
            return i
print sum([l(j) for j in range(3, 2 * 10 ** 7 + 1)])