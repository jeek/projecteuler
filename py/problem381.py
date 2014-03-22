
def facmod(x, p):
    answer = 1
    i = 1
    while i <= x and answer != 0:
        answer = (answer * i) % p
        i += 1
    return answer

def S(p):
    return sum([facmod(p - i, p) for i in range(1, 6)])

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


total = 0
for i in xrange(5, 10 ** 8):
    if is_prime(i):
        total += S(i) % i
        print i, total

print total
