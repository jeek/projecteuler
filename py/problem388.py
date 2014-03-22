max = 1

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

count = 0
for a in range(max + 1):
    for b in range(a + 1):
        if gcd(a, b) == 1 or a == 0 or b == 0:
            for c in range(b + 1):
                if (gcd(a, c) == 1 and gcd(b, c) == 1) or c == 0:
                    count += 1
                    print count, a, b, c