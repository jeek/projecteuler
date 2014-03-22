def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

count = 0
for q in xrange(0, 10**8 + 1):
    print q, count
    for p in xrange(1, q / 100 + 1):
        if gcd(p, q) == 1:
            count += 1
print count
