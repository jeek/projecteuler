total = 0
queue = [1]
while (len(queue)>0):
    i = queue.pop()
    if (i ^ (2*i) ^ (3*i) == 0):
        total += 1
        if (2 * i <= 2 ** 30):
            queue.append(2*i)
        if (2 * i + 1 <= 2 ** 30):
            queue.append(2*i + 1)
print total
