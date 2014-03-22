primesieve = range(2, 5000)
primes = []

while (len(primesieve) > 0):
    current = primesieve.pop(0)
    primes.append(current)
    primesieve = [x for x in primesieve if x % current != 0]

print primes

def match(total, a, b, c):
    aa = 0
    while a * aa <= total:
        bb = 0
        while a * aa + b * bb <= total:
            cc = 0
            while a * aa + b * bb + c * cc <= total:
                if a * aa + b * bb + c * cc == total:
                    print total,aa,bb,cc
                    return True
                cc += 1
            bb += 1
        aa += 1
    return False

def solve(a, b, c):
    total = 300
    while (match(total, a, b, c) == True):
        total -= 1
    return total

print solve(14, 22, 77)