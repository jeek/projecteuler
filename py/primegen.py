def primegen():
    yield 2
    primes = [2]
    i = 3
    while True:
        isprime = True
        for j in primes:
            if i % j == 0:
                isprime = False
        if isprime:
            yield i
            primes.append(i)
        i += 1
