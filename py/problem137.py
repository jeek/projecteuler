import gmpy

x = 1
count = 0
while (count < 15):
    if (gmpy.is_square((x+1)**2+4*x**2)):
        count += 1
        print count,x
    x += 1
