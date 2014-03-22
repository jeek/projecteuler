import gmpy

n = 10 ** 10
total = 0

b = 2
while b <= n:
    c = 2
    dd = b ** 2 + c ** 2 + b ** 2 * c ** 2
    while ((c < b) and (gmpy.sqrt(dd))/2 <= n):
        if (gmpy.is_square(dd) and (gmpy.sqrt(dd)) % 2 == 0):
            total += (gmpy.sqrt(dd)) / 2
            print total,b,c
        c += 2
        dd = b ** 2 + c ** 2 + b ** 2 * c ** 2
    b += 2
