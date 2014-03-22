import gmpy

def lps(n):
    n = gmpy.sqrt(n)
    while not gmpy.is_prime(n):
        n -= 1
    return n

def ups(n):
    if gmpy.is_square(n):
        n = gmpy.sqrt(n)
    else:
        n = gmpy.sqrt(n) + 1
    while not gmpy.is_prime(n):
        n += 1
    return n

n = 999666333
#n = 1000
sum = 0
while n >= 4:
    if ((n % lps(n) == 0) != (n % ups(n) == 0)):
        sum += n
        print n,sum,lps(n),ups(n)
    if gmpy.is_square(n):
        print "!",n
    n -= 1
print sum