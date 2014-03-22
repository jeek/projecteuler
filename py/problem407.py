total = 0
for n in range(1, 10 ** 7 + 1):
    a = n - 1
    while a ** 2 % n != a % n:
        a -= 1
    total += a
    print n, a, total
            