from memoize import Memoize
from gmpy import is_prime
from copy import deepcopy
from math import log10
def connected(x, max = -1):
    answers = set()
    intlen = 1 + int(log10(x))
    y = str(x)
    if x >= 10 and (x / 10 ** (intlen - 2)) % 10 != 0:
#        if y[1] != "0":
        answers.add(str(x % 10 ** (intlen - 1)))
    for i in range(len(y)):
        y = str(x)
        for j in range(10):
            if i != 0 or j != 0:
#                answers.add(y[:i] + str(j) + y[i + 1:])
                if i > 0:
                    answers.add(str((x % (10 ** (i)) + j * (10 ** i) + int(x / 10 ** (i + 1)) * (10 ** (i + 1)))))
#                    print x, (x % (10 ** (i)) + j * (10 ** i) + int(x / 10 ** (i + 1)) * (10 ** (i + 1)))
#                    pass
                else:
                    answers.add(str(int(x / 10) * 10 + j))
#                print x, answers
#    for i in deepcopy(answers):
#        if i[0] == "0":
#            answers.discard(i)
    answers = set([int(i) for i in answers])
    if max > 0:
        return [i for i in answers if i <= max and is_prime(i)]
    return [i for i in answers if is_prime(i)]

def related(x, max = -1):
    family = set(connected(x, max))
    queue = set(deepcopy(family))
    familysize = len(family)
    done = False
    while len(queue):
        i = queue.pop()
        for j in connected(i, max):
            if j < max:
                if megarelated(j):
                    return True
            if j == 2:
                return True
            if j <= max and j not in family:
                family.add(j)
                queue.add(j)
    if 2 in family:
        return True
    return False

def megarelated(x):
    if x >= 10 and str(x)[:2] == "10":
        return False
    return related(x, x)

connected = Memoize(connected)
related = Memoize(related)
megarelated = Memoize(megarelated)
            
answer = 0
print sum([i for i in xrange(2, 10 ** 3) if is_prime(i) and not megarelated(i)])
print sum([i for i in xrange(2, 10 ** 4) if is_prime(i) and not megarelated(i)])
print sum([i for i in xrange(2, 10 ** 7) if is_prime(i) and not megarelated(i)])
quit()
for i in xrange(2, 10 ** 4):
    if is_prime(i):
        if not megarelated(i):
            answer += i
print answer