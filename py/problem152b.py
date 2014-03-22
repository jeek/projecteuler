import copy
import random

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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return a * b / gcd(a, b)
i = 1
for j in range(2, 35):
    i = lcm(i,j * j)
print i

result = i / 2
result2 = sum([(result * 2 / (x ** 2)) for x in range(2,36)]) - result
def solve(goal, range):
    range = eval(range)
#    print goal, len(range)
    if goal == 0:
        return 1
    if goal < 0:
        return 0
    if goal > sum(range):
        return 0
    if len(range) == 0:
        return 0
    first = range.pop(int(random.random()*len(range)))
    if goal - first >= 0:
        return solve(goal, str(range)) + solve(goal - first, str(range))
    return solve(goal, str(range))


#solve = Memoize(solve)

print solve(result2, str([(result * 2 / (x ** 2)) for x in range(2,36)]))
