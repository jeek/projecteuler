import math

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

smallx = 1 - math.cos(math.radians(72))
bigx = smallx - math.cos(math.radians(144))
smally = math.sin(math.radians(72)) - math.sin(math.radians(144))
bigy = math.sin(math.radians(72))
biggery = math.sin(math.radians(144)) - math.sin(math.radians(216))
print smallx, bigx, smally, bigy, biggery

def solve(x, y, dir, left):
    if left == 0:
        if abs(x) < 10 ** -5 and abs(y) < 10 ** -5 and dir == 0:
            return 1
        return 0
    if dir == 0:
        return solve(x - smallx, y + bigy   , 4, left - 1) + solve(x + smallx, y + bigy   , 1, left - 1)
    if dir == 1:
        return solve(x + smallx, y + bigy   , 0, left - 1) + solve(x + bigx  , y - smally , 2, left - 1)
    if dir == 2:
        return solve(x + bigx  , y - smally , 1, left - 1) + solve(x         , y - biggery, 3, left - 1)
    if dir == 3:
        return solve(x         , y - biggery, 2, left - 1) + solve(x - bigx  , y - smally , 4, left - 1)
    if dir == 4:
        return solve(x - bigx  , y - smally , 3, left - 1) + solve(x - smallx, y + bigy   , 0, left - 1) 
    return 0

solve = Memoize(solve)

for i in range(0, 71, 5):
    print i, solve(0, 0, 0, i)