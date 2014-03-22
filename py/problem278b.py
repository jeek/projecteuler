from collections import defaultdict

primesieve = range(2, 5000)
primes = []

while (len(primesieve) > 0):
    current = primesieve.pop(0)
    primes.append(current)
    primesieve = [x for x in primesieve if x % current != 0]

def solve(a, b, c):
    if a == 2:
        return b - 2
    listt = defaultdict(int)
    if solveb(a, b) < c:
        return solveb(a, b)
    listt[0] = 1
    listt[a] = 1
    listt[b] = 1
    listt[c] = 1
    counter = 0
    i = 0
    while counter < a * b * c:
        if listt[i - a] == 1 or listt[i - b] == 1 or listt[i - c] == 1:
            listt[i] = 1
            counter += 1
        else:
            counter = 0
        i += 1
    i = max(listt.keys())
    while listt[i] == 1:
        i -= 1
    return i

def solveb(a, b):
    listt = defaultdict(int)
    listt[0] = 1
    listt[a] = 1
    listt[b] = 1
    counter = 0
    i = 0
    while counter < a * b:
        if listt[i - a] == 1 or listt[i - b] == 1:
            listt[i] = 1
            counter += 1
        else:
            counter = 0
        i += 1
    i = max(listt.keys())
    while listt[i] == 1:
        i -= 1
    return i

finaltotal = 0
for a in primes:
    for b in primes:
        for c in primes:
             if a < b and b < c:
                 answer = solve(a,b,c)
                 print a,b,c,answer
                 finaltotal += answer

print finaltotal


    