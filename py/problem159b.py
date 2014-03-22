import subprocess
import copy

total = 0
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


def calcdrs(i):
    if i % 9 == 0:
        return 9
    return i % 9

calcdrs = Memoize(calcdrs)

for k in range(2, 1000000):
    queue = set([str(subprocess.Popen(['factor',str(k)], stdout = subprocess.PIPE).communicate()[0][:-1].split(" ")[1:])])
    processed = set()
    while len(queue - processed) > 0:
        current = eval((queue - processed).pop())
        processed.add(str(current))
        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                temp = copy.deepcopy(current)
                tempprod = int(temp.pop(j))
                tempprod *= int(temp.pop(i))
                temp.append(str(tempprod))
                queue.add(str(sorted(temp)))
    maxdrs = 0
    for i in processed:
        thestring = ""
        drs = 0
        for j in eval(i):
            drs += calcdrs(int(j))
        if drs > maxdrs:
            maxdrs = drs
            answer = i
    total += maxdrs
#    if k % 1000 == 999:
    print k, total, maxdrs, answer
