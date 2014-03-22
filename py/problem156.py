total = [0 for i in range(10)]
i = 1
while i:
    k = i
    printit = 0
    while k > 0:
        if k % 10 != 0:
            total[k % 10] += 1
        k /= 10
    for j in range(1, 10):
        if total[j] == i:
            total[0] += i
            printit = 1
    if printit:
        print i, total    
    i += 1