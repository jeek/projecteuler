from memoize import Memoize
divisors = lambda x: [i for i in range(1, x) if x % i == 0]
#amicable = lambda x: True if x != sum(divisors(x)) and x == sum(divisors(sum(divisors(x)))) else False
print sum(i for i in xrange(10000) if i != sum(j for j in xrange(1, i) if i % j == 0) and i == sum(l for l in xrange(1, sum(k for k in xrange(1, i) if i % k == 0)) if sum(k for k in xrange(1, i) if i % k == 0) % l == 0))
