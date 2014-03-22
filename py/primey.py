upperlimit = 100000000

def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

primes = range(2, upperlimit)

i = 0

while i < len(primes) and primes[i] * primes[i] <= upperlimit:
    primes[i:] = [j for j in primes[i:] if j <= primes[i] or gcd(j, primes[i]) == 1]
    print primes[i]
    i += 1

print primes