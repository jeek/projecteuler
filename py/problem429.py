def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)

def gcd(i, j):
    while j != 0:
        (i, j) = (j, i % j)
    return i

def udivisors(n):
    answer = 0
    d = 1
    while d < n + 1:
        if n % d == 0 and gcd(d, n/d) == 1:
            answer += d ** 2
        d += 1
    return answer

fac = 1
for i in range(1, 33):
    fac *= i
    print i, fac, udivisors(fac)
