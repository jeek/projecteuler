upperlimit = 1000000

primes = range(2, upperlimit)

i = 0
while primes[i] ** 2 <= upperlimit:
    primes = primes[:i + 1] + [j for j in primes[i + 1:] if j % primes[i] != 0]
    print primes[i]
    i += 1
for j in primes[i:]:
    print j