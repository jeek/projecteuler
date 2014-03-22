from gmpy import is_prime

listofprimes = [2]
i = 3
done = False
while not done:
    if listofprimes[-1] <= i:
        listofprimes += [j for j in xrange(listofprimes[-1] + 1, i + 1) if is_prime(j)]
    while is_prime(i):
        i += 2
        if listofprimes[-1] <= i:
            listofprimes += [j for j in xrange(listofprimes[-1] + 1, i + 1) if is_prime(j)]
    j = 1
    good = False
    while not good and 2 * j * j <= i:
        if i - 2 * j * j in listofprimes:
            good = True
        j += 1
    if not good:
        print i
#        done = True
    i += 2