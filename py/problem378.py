def T(n):
    return n * (n + 1) / 2

def divisors(n):
    return [i for i in xrange(1, n + 1) if n % i == 0]

def numdivisors(n):
    return len(divisors(n))

def dT(n):
    return numdivisors(T(n))

print dT(7)

b = 1
while b:
    a = 1
    while a < b:
        if dT(a) < dT(b):
            print a, b
        a += 1
    b += 1