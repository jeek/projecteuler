def gcd(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    return a

def rep(n):
    return (10 ** n - 1)/9
    
n = 1000000
k = 1
max = 0
while (k <= 1000000):
    if (gcd(n, 10) == 1):
        k = 1
        temp = rep(k)
        while (rep(k) % n != 0):
            k += 1
#        if k > max:
#            max = k
#            print n, max
        print n, k
    n += 1