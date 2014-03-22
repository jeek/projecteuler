def divisors(x):
    """Return the divisors of x"""
    if (x == 1):
        return [1]
    i = 1
    answer = []
    while (i * i <= x):
        if (x % i == 0):
            answer.append(i)
            answer.append(x / i)
        i += 1
    if (len(answer)<=1):
        return [1]
    if (answer[-1] == answer[-2]):
        answer.pop()
    return sorted(answer)

def gcd(i, j):
    while j > 0:
        (i, j) = (j, i % j)
    return i

def primitivetriples():
    m = 1
    while (m > 0):
        n = 1
        while (m > n):
            if (gcd(m, n) == 1) and (m - n) % 2 == 1:
                yield([m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2],[m,n])
            n += 1
        m += 1

c = 2
trigen = primitivetriples()
from collections import defaultdict

primtriangles = [trigen.next()[0]]
done = 0
maxcount = 1
maxc = 1
lastc = 1
factors = defaultdict(int)
factors[3] = 1
factors[4] = 1

while not done:
    while c > primtriangles[-1][0] or c > primtriangles[-1][1]:
        i = trigen.next()
        factors[i[0][0]] += 1
        factors[i[0][1]] += 1
        while i[1][0] - i[1][1] != 1:
            primtriangles.append(i[0])
            i = trigen.next()
            factors[i[0][0]] += 1
            factors[i[0][1]] += 1
        primtriangles.append(i[0])
    count = 0
    while 1 < len(primtriangles):
        primtriangles.pop(0)
#    print c,factors
    for i in divisors(c):
        count += factors[i]
        i+= 1
    if count > maxcount:
        lastc = maxc
        maxc = c
        maxcount = count
        print maxc,maxcount,c,count,c*1.0/count,count**2.0/c
    if count == 47547:
        print c,count
        done = 1
    c += 1
    