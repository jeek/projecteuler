from memoize import Memoize

def recur(x, y):
    if x == 0 or y == 0:
        return 1
    if x > y:
        return recur(y, x)
    return ((recur(x - 1, y) + recur(x, y - 1)) % 7)

recur = Memoize(recur)

answer = 0
for j in xrange(10 ** 9):
    for i in xrange(j+1):
        if recur(j - i, i) != 0:
            answer += 1
#        print j, i, recur(j - i, i)
    print j, answer
print answer

