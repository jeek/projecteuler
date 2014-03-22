import shelve
import sys
sys.setrecursionlimit(1000000)
import copy
m = 5
n = 3

class Memoize: # stolen from http://code.activestate.com/recipes/52201/
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
#        self.memo = shelve.open("412.txt")
        if not self.memo.has_key(str(args)):
            self.memo[str(args)] = self.fn(*args)
        answer = copy.deepcopy(self.memo[str(args)])
#        self.memo.close()
        return answer
depth = 0

def queue(current, m, n):
    global depth
    depth += 1
    print depth, m, n
    answer = 0
    done = True
    for i in range(m - n):
        if current[i] != m:
            done = False
    for i in range(m - n, m):
        if current[i] != m - n:
            done = False
    if done == True:
        depth -= 1
        return 1
    if current[0] < m:
        current[0] += 1
        answer += queue(current, m, n)
        current[0] -= 1
    for i in range(m - n, m)[::-1]:
        if current[i] < current[i - 1] and current[i] < (m - n):
            current[i] += 1
            answer += queue(current, m, n)
            current[i] -= 1
    for i in range(1, m - n)[::-1]:
        if current[i] < current[i - 1]:
            current[i] += 1
            answer += queue(current, m, n)
            current[i] -= 1
    depth -= 1
    print current, m, n, answer
    return answer
queue = Memoize(queue)

current = [m for i in range(m - n)] + [(m - n) for i in range(n)]
temp = 0
index = 0
while(sum(current) > 0):
    print queue(current, m, n), temp, index
    temp = max(current)
    index = len(current) - 1
#    while current[index] != temp:
#        index -= 1
    current[index] -= 1
print queue([0 for i in range(m)], m, n)
