fac = [1]

for i in range(1, 10):
    fac.append(fac[-1] * i)

print fac

for h in range(1, 151):
    i = int(str(h % 9) + str("9" * (h / 9)))
    print h, i, 
    answer = [0 for z in range(10)]
    for j in range(9, -1, -1):
        answer[j] += 1
        answer[j] = i / sum([fac[k] * answer[k] for k in range(10)])
        while sum([fac[k] * answer[k] for k in range(10)]) < i:
            answer[j] += 1
        while sum([fac[k] * answer[k] for k in range(10)]) > i:
            answer[j] -= 1
    print sum([k * answer[k] for k in range(1, 10)])