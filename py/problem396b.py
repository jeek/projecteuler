from collections import defaultdict

def G(x):
    count = 1
    k = 2
    while x > 0:
        xx = x
        based = []
        while xx > 0:
            based.append(xx % k)
            xx = int(xx / k)
        k += 1
#        print based
        xxx = sum([based[x] * k ** x for x in range(len(based))])
        x = xxx - 1
        if x > 0:
#            print based
            x -= based[0] - 1
            count += (based[0] + 1)
        else:
            return count, based
    return count

for j in range(1, 8):
    print j, G(j)
