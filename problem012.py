i = 0
j = 0
while len([k for k in range(1, int(j ** .5) + 1) if j % k == 0]) < 250:
    i += 1
    j += i

print j