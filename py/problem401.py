import gmpy

def divisors(x):
    if gmpy.is_prime(x):
        return 1 + x ** 2
    j = 1
    total = 0
    while j ** 2 < x:
        if x % j == 0:
            total += j ** 2
            total += (x / j) ** 2
        j += 1
    if j ** 2 == x:
        total += j ** 2
    return total
        
total = 0

x = 1
while x <= 10 ** 15:
    total += divisors(x)
    total %= 10 ** 9
    print x, total
    x += 1