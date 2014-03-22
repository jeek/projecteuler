import fractions, functools

def lcm(a, b):
    return a * b // fractions.gcd(a, b)

mx = 80

s = [fractions.Fraction(0)]

ii = list(range(2, mx + 1))

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]

def maxprime(ii):
    for p in primes:
        for i in ii:
            if i % p == 0:
                return i

while ii:
    i = maxprime(ii)
    ii.remove(i)
    l = functools.reduce(lcm, ii, 2)
    s = [x for x in s + [x + fractions.Fraction(1, i ** 2) for x in s]
          if l ** 2 % x.denominator == 0]

print(sum(1 for x in s if x == fractions.Fraction(1, 2)))
