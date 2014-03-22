import math
import string
import re

def gcd(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    return a

n = 1
done = 0
def A(n):
    k = 1
    if (gcd(n,10) == 1):
        k = 1
        times = 1
        while (int (n*k/times) != 0):
            while ((n * k / times) % 10 != 1):
                k += times
            times *= 10
        return k

nn = 1
while (math.log(nn)/math.log(10) < 10):
    if (gcd(n,10) == 1):
        nn = A(n)
        print n,A(n)
    n += 1