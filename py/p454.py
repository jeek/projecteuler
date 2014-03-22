upperlimit = 10 ** 12
#upperlimit = 1000
x = 1
count = 0
while x <= upperlimit:
#for x in xrange(1, upperlimit + 1):
    z = x
    while z % 2 == 0:
        z /= 2
    y = x + 1
    while y <= x * x and y <= upperlimit:
#    for y in xrange(x + 1, upperlimit + 1):
        if (x * y) % (x + y) == 0:
            count += 1
            print count, x, y, (x + y), (x * y)
        y += 1
    x += 1