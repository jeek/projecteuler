def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
def lcm(a, b):
    return a * b / gcd(a, b)

def A(n):
    total = 0
    i = 1
    while i <= n:
        total += lcm(n, i)
        i += 1
    return total / n
def S(n):
    i = 1
    total = 0
    while i <= n:
        total += A(i)
        total %= 999999017
#        print i, total
        i += 1
    return total

print A(10)
print S(100)
for i in range(1, 101):
    print i, S(i)
print (S(99999999019) % 999999017)