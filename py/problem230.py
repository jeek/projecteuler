def F(a,b):
    yield a
    yield b
    while (1):
        c = int(str(a) + str(b))
        yield c
        a = b
        b = c

def D(a,b,c):
    i = 0
    for i in F(a,b):
        if len(str(i)) >= c:
            i = str(i)
            return int(i[c-1])

print D(1415926535, 8979323846, 35)
total = 0
for n in range(18):
    total += (10 ** n) * D(1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679, 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196,(127+19*n)*(7**n))
    print n,total
print total
