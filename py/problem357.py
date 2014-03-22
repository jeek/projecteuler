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

primelist = [2, 3]

primeslist = dict()

for i in primelist:
    primeslist[i] = 1

def isprime(x):
    x = abs(x)
    i = primelist[-1]
    while (primelist[-1] < x):
        i += 2
        flag = True
        j = 0
        while j < len(primelist):
            if i % primelist[j] == 0 or primelist[j] ** 2 > i:
                if i % primelist[j] == 0:
                    flag = False
                j = len(primelist)
            j += 1
        if flag == True:
            primelist.append(i)
            primeslist[i] = 1
    return primeslist.has_key(x)

print [x for x in xrange(2, 1000000000, 4) if isprime(x + 1)]