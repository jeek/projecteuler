import gmpy
primes = [i for i in xrange(2, 10 ** 8) if gmpy.is_prime(i)]

i = 10 ** 11
def s(n, m):
    test = n ** 15 + 1
    factors = set()
    for j in [n + 1, n ** 2 - n + 1, n ** 4 - n ** 3 + n ** 2 - n + 1, n ** 8 + n ** 7 - n ** 5 - n ** 4 - n ** 3 + n + 1]:
        k = 0
        while k < len(primes) and primes[k] <= j and primes[k] <= m:
            if j % primes[k] == 0:
                factors.add(primes[k])
                while j % primes[k] == 0:
                    j /= primes[k]
            k += 1
    return sum(factors)

i = 1
total = 0
while i <= 10 ** 11:
    temp = s(i, 10 ** 8)
    total += temp
    print i, temp, total
    i += 1