primes = range(2, 100001)
i = 0
while i < len(primes) and primes[i] * primes[i] <= primes[-1]:
    primes[i + 1:] = [j for j in primes[i+1:] if j % primes[i] != 0]
    i += 1

def mul(a, b):
    return a * b

def rad(x):
    if x == 1:
        return 1
    answer = []
    i = 0
    while x > 1 and primes[i] * primes[i] <= x:
        while x % primes[i] == 0:
            answer.append(primes[i])
            x /= primes[i]
        i += 1
    if x > 1:
        answer.append(x)
    return reduce(mul, list(set(answer)))

answer = [(rad(i), i) for i in xrange(1, 100001)]
answer.sort()
print answer[9999]