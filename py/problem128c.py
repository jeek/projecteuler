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

primesieve = range(2, 5)

primelist = [2, 3]
primeslist = dict()
primeslist[2] = 1
primeslist[3] = 1
#while(len(primesieve) > 0):
#    last = primesieve.pop(0)
#    primelist.append(last)
#    primeslist[last] = 1
#    primesieve = [x for x in primesieve if x % last != 0]

def isprime(x):
    x = abs(x)
    i = primelist[-1]
    while (primelist[-1] < x):
        i += 2
        flag = True
        j = 0
        while j < len(primelist):
            if i % primelist[j] == 0:
                flag = False
                j = len(primelist)
            j += 1
        if flag == True:
            primelist.append(i)
            primeslist[i] = 1
    return primeslist.has_key(x)

i = 0

def plane(x, y):
    if x == 0:
        if y == -2:
            return 5
        if y == 0:
            return 1
        if y == 2:
            return 2
        return plane(0, y - 2) + 6 * y / 2 - 6
    if x == -1:
        if y == -1:
            return 4
        return plane(x + 1, y + 1) + 1
    if x == 1:
        if y == -1:
            return 6
        return plane(x - 1, y + 3) - 1
    if x == 2:
        if y == 0:
            return 17
        return plane(x - 1, y + 1) - 1

plane = Memoize(plane)

answers = []
row = 0
while(len(answers) < 2000):
    x = 0
    y = row * 2
    primes = []
#    if (isprime(plane(x, y) - plane(x, y + 2))):
#        primes.append(abs(plane(x, y) - plane(x, y + 2)))
#    if (isprime(plane(x, y) - plane(x, y - 2))):
#        primes.append(abs(plane(x, y) - plane(x, y - 2)))
    if (isprime(plane(x, y) - plane(x - 1, y + 1))):
        primes.append(abs(plane(x, y) - plane(x - 1, y + 1)))
#    if (isprime(plane(x, y) - plane(x - 1, y - 1))):
#        primes.append(abs(plane(x, y) - plane(x - 1, y - 1)))
    if (isprime(plane(x, y) - plane(x + 1, y + 1))):
        primes.append(abs(plane(x, y) - plane(x + 1, y + 1)))
    if (isprime(plane(x, y) - plane(x + 1, y - 1))):
        primes.append(abs(plane(x, y) - plane(x + 1, y - 1)))
    if len(primes) == 3:
        answers.append(plane(x, y))
        print len(answers), plane(x, y), [x, y], primes
    x += 1
    y += 1
    primes = []
#    if (isprime(plane(x, y) - plane(x, y + 2))):
#        primes.append(abs(plane(x, y) - plane(x, y + 2)))
#    if (isprime(plane(x, y) - plane(x, y - 2))):
#        primes.append(abs(plane(x, y) - plane(x, y - 2)))
    if (isprime(plane(x, y) - plane(x - 1, y + 1))):
        primes.append(abs(plane(x, y) - plane(x - 1, y + 1)))
    if (isprime(plane(x, y) - plane(x - 1, y - 1))):
        primes.append(abs(plane(x, y) - plane(x - 1, y - 1)))
    if (isprime(plane(x, y) - plane(x + 1, y + 1))):
        primes.append(abs(plane(x, y) - plane(x + 1, y + 1)))
    if (isprime(plane(x, y) - plane(x + 1, y - 1))):
        primes.append(abs(plane(x, y) - plane(x + 1, y - 1)))
    if len(primes) == 3:
        answers.append(plane(x, y))
        print len(answers), plane(x, y), [x, y], primes
    row += 1

