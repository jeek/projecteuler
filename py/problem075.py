c = 1500000

while c > 0:
    b = c
    while b >= c / 2:
        a = int((c ** 2 - b ** 2) ** .5)
        if a ** 2 + b ** 2 == c ** 2 and a + b + c <= 1500000:
            print a, b, c
        b -= 1
    c -= 1