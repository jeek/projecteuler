import math
import string
import re

def isprime(x):
    return 1 == len(primefactors(x))

def primefactors(x):
    """Return prime factors of x"""
    answer = []
    i = 2
    while (i <= x):
        while (x % i == 0):
            answer.append(i)
            x /= i
        i += 1
    return answer

def gcd(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    return a

def B(n):
    k = 1
    if (gcd(n,10) == 1):
        k = 1
        times = 1
        while (int (n*k/times) != 0):
            while ((n * k / times) % 10 != 1):
                k += times
            times *= 10
        return k

def A(n):
    answer = 1
    while (answer % n != 0):
        answer *= 10
        answer += 1
    return len(str(answer))

n = 2
nn = 1
count = 0
sum = 0
while (count < 25):
    if (gcd(n,10) == 1 and not isprime(n)):
#    if (gcd(n,10) == 1):
        nn = A(n)
        if ((n - 1) % nn == 0):
            print n,nn
            sum += n
            count += 1
    n += 1
print sum