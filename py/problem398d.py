from operator import mul
 
def factorial(n):
    print "Factorial!", n
    return reduce(mul,range(1,n+1),1)

def binomial(n,k):
    return factorial(n) / (factorial(k) * factorial(n - k))

class Memoize: # stolen from http://code.activestate.com/recipes/52201/
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not self.memo.has_key(args):
            self.memo[args] = self.fn(*args)
        return self.memo[args]

factorial = Memoize(factorial)

def compCount(n, k, a):
    if k < 0:
        return 0
    if a > int(n / k):
        return 0
    if k > n:
        return 0
    return binomial(n - k * a + k - 1, k - 1)

total = 10 ** 7
parts = 100

#total = 8
#parts = 3

cAll = compCount(total, parts, 1)
print cAll

cRunning = cAll
cExp = 0
ci = 0
for i in range(1, int(total / parts) + 1):
    ci = cRunning - compCount(total, parts, i + 1)
    cRunning -= ci
    for j in range(i, 1 + int((total - i) / (parts - 1))):
        cj = ci - parts * compCount(total - i, parts - 1, j + 1)
        cExp += j * cj
        ci -= cj
        if ci == 0:
            break
    print cExp * 10000000000 / cAll
print cExp * 10000000000 / cAll
