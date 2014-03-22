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

total = 0
queue = []
for i in range(1, 10**8+1):
    factors = divisors(i)
    factors.pop(0)
#    print i, factors
    queue.append(factors)
    maxlen = 0
    alreadydone = dict()
    while(len(queue) > 0):
        current = queue.pop(0)
#        print current,queue
#        if len(current) > maxlen:
        if 1 == 1:
            good = 1
            j = 0
            while j < len(current):
                k = j + 1
                while k < len(current):
                    if current[k] % current[j] == 0:
                        good = 0
                        clone = current[:]
                        clone.pop(0)
                        if not alreadydone.has_key(str(clone)):
                            alreadydone[str(clone)] = 1
                            queue.append(clone)
                        clone = current[:]
                        clone.pop(-1)
                        if not alreadydone.has_key(str(clone)):
                            alreadydone[str(clone)] = 1
                            queue.append(clone)
                    k += 1
                j += 1
            if good == 1:
                queue = []
                total += len(current)
                print i,total,(total*1.0/i),current
                maxlen = len(current)
