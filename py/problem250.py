import gmpy

import operator as op
#def gmpy.comb(n, r):
#    r = min(r, n-r)
#    if r == 0: return n
#    num = reduce(op.mul, xrange(n, n-r, -1))
#    denom = reduce(op.mul, xrange(1, r+1))
#    return num//denom

array = []
for i in xrange(1,250251):
    array.append(pow(i,i,250))
last = [0] * 250251
for i in range(len(array)):
    next = last[:]
    for j in range(250251):
#        print "?",i
        next[(j + array[i]) % 250] += (last[i] + array[i]) % (10 * 16)
    print i, next[0]
    last = next[:]
print last[0] - 1 , "!"

        