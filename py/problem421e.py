import gmpy

primes = [x for x in xrange(10 ** 8) if gmpy.is_prime(x)]

print "Primes Generated"

total = 0
i = 1
while i <= 10 ** 11:
    relevant = [x for x in primes if (i ** 15 + 1) % x == 0]
    total += sum(relevant)
    print relevant, i, total
    i += 1