import random

def recur(n, m):
    values = random.sample(range(1, n), m - 1)
    values.append(n)
    values.append(0)
    values.sort()
    answers = [values[x + 1] - values[x] for x in range(len(values) - 1)]
    answers.remove(min(answers))
    return min(answers)

total = 0
i = 0
while True:
    i += 1
    total += recur(10 ** 7, 100)
#    total += recur(8, 3)
    if i % 1000000 == 0:
        print i,(total * 1.0 / i)

print total * 1.0 / 100000000