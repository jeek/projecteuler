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

def sqrt(x):
    i = 0
    while i ** 2 < x:
        i += 1
    if i ** 2 == x:
        return i

def area(a, b, c):
    s = (a + b + c)
    if s % 2 == 1:
        return
    s /= 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

b = 1
# for c in range(1, 1001):
total = 0
while (True):
    for a in range(1, b + 1):
        odd = (a + b) % 2
        for c in range(b + odd, a + b, 2):
            if area(a, b, c):
                if area(a, b, c) % (a + b + c) == 0 and (area(a, b, c) / (a + b + c) <= 1000):
                    total += a + b + c
                    print ((a+b+c)%16), total, a, b, c, area(a, b, c), (area(a, b, c) / (a + b + c))
    b += 1