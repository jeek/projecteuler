total = 0
for i in range(2, 10**6):
    j = 10 ** 9
    done = False
    while j > 0 and not done:
        if pow(i, j, 10 ** 9) == j:
            done = True
        j -= 1
    total += j
    print i, j, total
        