
from collections import defaultdict


f = (1, 4)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for f in [(1, x) for x in range(1,10)]:
    flips = defaultdict(defaultdict)
    cash = (1, 1)
    flips[0] = {cash: 1}
#    print flips
    i = 1
    while i <= 1000:
#        print i
        flips[i] = defaultdict(int)
        for j in flips[i - 1]:
#        print "!", flips
#        print j, flips[i - 1][j], "!"

            top = j[0] * f[1] + j[0] * 2 * j[1] * f[0]
            bottom = j[1] * f[1]
    #        print "||| ",top,bottom
            temp = gcd(top, bottom)
            top /= temp
            bottom /= temp
            flips[i][(top, bottom)] += flips[i - 1][j]

            top = j[0] * f[1] - j[0] * j[1] * f[0]
            bottom = j[1] * f[1]
            temp = gcd(top, bottom)
            top /= temp
            bottom /= temp
            flips[i][(top, bottom)] += flips[i - 1][j]
        i += 1
    num = 0
    dem = 0
    for i in flips[1000]:
#        print i
        dem += flips[1000][i]
        if i[0] / i[1] >= 1000000000:
            num += flips[1000][i]
    print f, num * 10 ** 15 / dem