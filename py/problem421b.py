import gmpy
from math import ceil
def fermfactor(N):
#    print N
    if N != 1:
        even = 1
        while N % 2 == 0:
            even *= 2
            N /= 2
        a = int(ceil(N ** .5))
        b2 = a ** 2 - N
        while not gmpy.is_square(b2) and a < N:
            a += 1
            b2 = a ** 2 - N
        while even % 2 == 0:
            yield 2
            even /= 2
        if gmpy.is_prime(a - int(b2 ** .5)):
            yield a - int(b2 ** .5)
        else:
            for i in fermfactor(a - int(b2 ** .5)):
                yield i
        if gmpy.is_prime(a + int(b2 ** .5)):
            yield a + int(b2 ** .5)
        else:
            for i in fermfactor(a + int(b2 ** .5)):
                yield i
def factor(N):
    if gmpy.is_prime(N):
        return [N]
    return sorted(list(set(fermfactor(N))))

total = 0
n = 1
while n <= 10 ** 11:
#for n in xrange(1, 10 ** 11):
    factors = set()
    for j in [n + 1, n ** 2 - n + 1, n ** 4 - n ** 3 + n ** 2 - n + 1, n ** 8 + n ** 7 - n ** 5 - n ** 4 - n ** 3 + n + 1]:
        for k in factor(j):
            factors.add(k)
#    print sorted(list(factors))
    total += sum(factors)
    print n, total
    n += 1