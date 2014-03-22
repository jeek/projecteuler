import math
a = 1
b = 1
count = 2
size = 100000000

while(count < size):
    (a, b) = (b, a + b)
    i = 2
    while b % (i ** 2) != 0 and i ** 2 < b and i <= count:
        i += 1
    if b % (i ** 2) != 0:
        count += 1
        print count, b%(10**16),(b * 10) / 10 ** int((math.log(b)/math.log(10))), int((math.log(b)/math.log(10)))
print b