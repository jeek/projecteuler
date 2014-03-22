#from tempfile import mkdtemp
#cachedir = mkdtemp()
#from joblib import Memory
#memory = Memory(cachedir=cachedir, verbose=0)

import sys
sys.setrecursionlimit(1000000000)
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

import gmpy

def admissible(x, y):
    if x == 0 or y == 0:
        return True
    if gmpy.is_square(x) and gmpy.is_square(y) and gmpy.is_square(x+y):
        return False
    return True

#@memory.cache
def score(x, y, max):
#    print x, y, max
    if x > y:
        return score(y, x, max)
    if not admissible(x, y):
        print x, y
        return 0
    if x == max or y == max:
        return 1
    if x == max:
        return score(x, y + 1, max)
    if y == max:
        return score(x + 1, y, max)
    return (score(x, y + 1, max) + score(x + 1, y, max)) % 1000000007

score = Memoize(score)

def P(max):
    return score(0, 0, max)
size = 16
for i in range(size, -1, -1):
    for j in range(size, -1, -1):
        score(i, j, size)
    print i, i, score(i, i, size)
  
print (P(size) % 1000000007)
