def S():
    i = 0
    answer = 0
    while (1):
        temp = i
        while temp > 0:
            if temp % 2 == 1:
                answer += 1
            temp = int(temp/2)
        yield answer
        i += 1
for i in S():
    print i
