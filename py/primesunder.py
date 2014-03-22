def primesunder(x):
    primes = range(x)

    primes[1] = 0

    i = 0
    while i < len(primes):
        if primes[i] > 0:
            j = i * i
            while j < len(primes):
                primes[j] = 0
                j += i
        i += 1
    return [i for i in primes if i != 0]
