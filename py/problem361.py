import math

import copy
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

def T(n):
    if n == 0:
       return 0
    if n % 2 == 0:
        return T(n / 2)
    return 1 - T((n - 1) / 2)

#T = Memoize(T)

def TT(x, y):
    i = x
    total = 0
    while i <= y:
        if T(i) == 1:
            total += 1
        total *= 2
        i += 1
    return total / 2

answers = []
for i in xrange(0, 10 ** 9):
    for j in range(0, i + 1):
        temp = TT(j, i)
        if answers.count(temp) < 1:
            answers.append(temp)
    answers.sort()
#    j = 0
#    while j + 1 < len(answers):
#        if answers[j] == answers[j + 1]:
#            answers.pop(j)
#        j += 1
    lol = len(answers)
    print i, lol,
    for j in range(1, len(str(lol))):
        print sorted(answers)[10 ** j],
    print
    if i > 5:
        lol2 = math.log(answers[-1]) / math.log(2)
        for j in range(0, lol2):
#            print 2 ** j, 2 ** (j + 1), " | ",
            print "|", j, len([x for x in answers if x >= 2 ** j and x < 2 **(j + 1)]),
        print
