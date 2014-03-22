i = 10
while i < 10 ** 100:
    j = int(str(i)[1:] + str(i)[0])
    if i % j == 0:
        print i, j
    i += 1