import gmpy

n = 1
count = 0
while n < 50000000:
    if gmpy.is_prime(2 * n ** 2 - 1):
        count += 1
    n += 1
print count