def divisors(x):
    return sorted(list(set([i for i in range(1, 1 + int(x ** .5)) if x % i == 0] + [x / i for i in range(2, 1 + int(x ** .5)) if x % i == 0])))
