answers = []
i = 1

while i ** 2 < 10 ** 8:
    total = 0
    j = i
    while total < 10 ** 8:
        total += j ** 2
        if total != i ** 2:
            answers.append(total)
        j += 1
    i += 1
print sum([i for i in set(answers) if str(i) == str(i)[::-1]])
