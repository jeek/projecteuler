r = ((10 ** (10 ** 9)) - 1) / 9

i = 2
while r > 1:
    while r % i == 0 and r > 1:
        print i
        r /= i
    i += 1
