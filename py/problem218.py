def gcd(a,b):
   while b != 0:
       (a, b) = (b, a % b)
   return a
c = 0

def gcdcheck(a,b):
    if gcd(a,b) == 1:
        return True
    return False

count = 0

while c ** 2 <= 10 ** 16:
    a = 1
    for a in [x for x in range(1, (c**2)/2) if gcd(x, (c**2)) == 1]:
#    while a < c:
        b = int((c ** 4 - a ** 2) ** .5)
        if (gcd(a,b) == 1 and gcd(b,c**2) == 1 and a < b and a ** 2 + b ** 2 == c ** 4 and (a * b / 2.0) % 84 != 0):
            count += 1
            print count,"|",a,b,c**2
        a += 1    
    c += 1