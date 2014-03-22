import math
i = 2
total = 0
while i <= 10 ** 6:
    seen = set()
    j = 999999999
    while j > 0 and pow(i, j, 10 ** 9) != j:
        j -= 1
    total += j
    print i, j, total
    i += 1
