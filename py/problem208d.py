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

def solve(left, dir = 0, smallx = 0, bigx = 0, smally = 0, bigy = 0, debug = 0):
    if left == 0:
        if dir == 0 and smallx == 0 and bigx == 0 and smally == 0 and bigy == 0:
            return 1
        return 0
    if dir == 0:
        if left % 5 == 0 and smallx == 0 and bigx == 0 and smally == 0 and bigy == 0:
            debugstring = str(solve(left - 1, 1, smallx - 1, bigx, smally, bigy + 1)) + " " + str(solve(left - 1, 4, smallx + 1, bigx, smally, bigy + 1))
            return 2 * solve(left - 1, 1, smallx - 1, bigx, smally, bigy + 1)
            print left, dir, smallx, bigx, smally, bigy, "|", debugstring
        if debug == 1:
            debugstring = str(solve(left - 1, 1, smallx - 1, bigx, smally, bigy + 1, 1)) + " " + str(solve(left - 1, 4, smallx + 1, bigx, smally, bigy + 1, 1))
            print left, dir, smallx, bigx, smally, bigy, "|", debugstring
        return solve(left - 1, 1, smallx - 1, bigx, smally, bigy + 1) + solve(left - 1, 4, smallx + 1, bigx, smally, bigy + 1)
    if dir == 1:
        if debug == 1:
             debugstring = str(solve(left - 1, 2, smallx + 1, bigx, smally, bigy + 1, 1)) + " " + str(solve(left - 1, 0, smallx, bigx + 1, smally - 1, bigy, 1))
             print left, dir, smallx, bigx, smally, bigy, "|", debugstring
        return solve(left - 1, 2, smallx + 1, bigx, smally, bigy + 1) + solve(left - 1, 0, smallx, bigx + 1, smally - 1, bigy)
    if dir == 2:
        if debug == 1:
             debugstring = str(solve(left - 1, 3, smallx, bigx + 1, smally - 1, bigy, 1)) + " " + str(solve(left - 1, 1, smallx, bigx, smally + 2, bigy - 2, 1))
             print left, dir, smallx, bigx, smally, bigy, "|", debugstring
        return solve(left - 1, 3, smallx, bigx + 1, smally - 1, bigy) + solve(left - 1, 1, smallx, bigx, smally + 2, bigy - 2)
    if dir == 3:
        if debug == 1:
             debugstring = str(solve(left - 1, 4, smallx, bigx, smally + 2, bigy - 2, 1)) + " " + str(solve(left - 1, 2, smallx, bigx - 1, smally - 1, bigy, 1))
             print left, dir, smallx, bigx, smally, bigy, "|", debugstring
        return solve(left - 1, 4, smallx, bigx, smally + 2, bigy - 2) + solve(left - 1, 2, smallx, bigx - 1, smally - 1, bigy)
    if dir == 4:
        if debug == 1:
             debugstring = str(solve(left - 1, 0, smallx, bigx - 1, smally - 1, bigy, 1)) + " " + str(solve(left - 1, 3, smallx - 1, bigx, smally, bigy + 1, 1))
             print left, dir, smallx, bigx, smally, bigy, "|", debugstring
        return solve(left - 1, 0, smallx, bigx - 1, smally - 1, bigy) + solve(left - 1, 3, smallx - 1, bigx, smally, bigy + 1)

solve = Memoize(solve)

#for i in range(0, 71, 5):
#    print i, solve(i, 0, 0, 0, 0, 0)
print solve(70,0,0,0,0,0)