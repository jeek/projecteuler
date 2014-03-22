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
queue = []
while True:
    i += 1
    for i in range(100):
        queue.append(recur(10 ** 7, 100))
    queue.sort()
    while len(queue) > 10000:
        queue.pop(0)
        queue.pop()
    print sum(queue) * 1.0 / len(queue)

print total * 1.0 / 100000000