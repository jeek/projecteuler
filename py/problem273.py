import gmpy

print [x for x in range(2,150) if gmpy.is_prime(x) and (x - 1) % 4 == 0]