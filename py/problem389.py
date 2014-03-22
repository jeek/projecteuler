from collections import defaultdict

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

def dice(number, sides):
    dice = []
    dice.append(defaultdict(int))
    for i in range(1, sides + 1):
        dice[0][i] += 1
    for i in range(1, number):
        dice.append(defaultdict(int))
        for j in dice[-2]:
            for k in range(1, sides + 1):
                dice[-1][j+k] += dice[-2][j]
        dice.pop(0)
    return dice[-1]
        
dice = Memoize(dice)

total = defaultdict(int)
overalltotal = 0

for t in sorted(dice(1, 4)):
    for c in sorted(dice(t, 6)):
        for o in sorted(dice(c, 8)):
            for d in sorted(dice(o, 12)):
                for i in sorted(dice(d, 20)):
                    total[i] += dice(t,6)[c] * dice(c, 8)[o] * dice(o, 12)[d] * dice(d, 20)[i]
                    overalltotal += dice(t,6)[c] * dice(c, 8)[o] * dice(o, 12)[d] * dice(d, 20)[i]                    
                print t,c,o,d,i,overalltotal
import pickle

pickle.dump(total, "done.txt")
