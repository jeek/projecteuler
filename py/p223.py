from gmpy import is_square

count = 0
a = 1
while a <= 25000000:
    b = a
    while a + b + b <= 25000000: 
        if is_square(a * a + b * b - 1):
            c = int((a * a + b * b - 1) ** .5)
            if a * a + b * b == c * c + 1:
                pass
            else:
                c += 1
            if a + b + c <= 25000000:
                if a * a + b * b == c * c + 1:
                    count += 1
#                    print a, b, c, count
        b = b + 1
    print a, count
    a = a + 1