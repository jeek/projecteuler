from gmpy import is_prime

numbers = range(1, 100001)

def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

primes = [x for x in range(1, 2**25 + 1) if is_prime(x)]

print primes
