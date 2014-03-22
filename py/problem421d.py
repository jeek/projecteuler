import gmpy
import random
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def mul(a, b):
    return a * b
primes = reduce(mul, [i for i in xrange(10 ** 8) if gmpy.is_prime(i)])
print primes
