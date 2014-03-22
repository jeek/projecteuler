from collections import defaultdict

numbers = [1]
queue = [x for x in range(500000, 1000001)]

i = 0
while i < len(numbers):
    print numbers[i], queue[0]
    try:
        queue.remove(numbers[i])
    except:
        pass
    if i * 2 <= 1000000:
        numbers.append(i * 2)
    if (i - 1) % 3 == 0 and i > 3:
        numbers.append((i - 1) / 3)
    i += 1
print queue[:100]