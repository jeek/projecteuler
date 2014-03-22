import gmpy

x = 0
done = 0
while done == 0:
    if gmpy.is_square(8 * x ** 2 - 8 * x + 1):
        if 1.0/2*(gmpy.sqrt(8 * x ** 2 - 8 * x + 1) + 1) == int(1.0/2*(gmpy.sqrt(8 * x ** 2 - 8 * x + 1) + 1)):
            print x,int(1.0/2*(gmpy.sqrt(8 * x ** 2 - 8 * x + 1) + 1))
            if x + int(1.0/2*(gmpy.sqrt(8 * x ** 2 - 8 * x + 1) + 1)) > 10 ** 12:
                done = 1
    x += 1