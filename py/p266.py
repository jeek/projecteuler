import gmpy

primes = [x for x in range(2,190) if gmpy.is_prime(x)]
total = 1
for i in primes:
    total *= i
array = []
answer = 0
lefttoworkwith = total
for i in primes:
    lefttoworkwith /= i
    for j in sorted(array):
        if i * j <= gmpy.sqrt(total):
            array.append(i * j)
            if i * j > answer:
                answer = i * j
                print i, j, i * j
    array.append(i)
    array = [x for x in array if x * lefttoworkwith >= answer]
print max(array)
