from collections import deque
import heapq
from copy import deepcopy as copy

upperlimit = 150

splitnum = lambda i: splitnum(i / 10) + [i % 10] if i >= 10 else [i]
def splitnum(i):
    answer = []
    while i > 0:
        answer.insert(0, i % 10)
        i /= 10
    return answer

queue = []
for i in range(1, 9):
    for k in copy(queue):
        for j in range(1, i + 1):
            queue.append(int(str(k) + (str(i) * j)))
    for j in range(1, i + 1):
        queue.append(int(str(i) * j))
queue.append(9)
queue.sort()

heapq.heapify(queue)

fac = [1]

for i in xrange(1, 10):
   fac.append(fac[-1] * i)

def numlen(x):
    if x == 0:
        return 1
    return len(splitnum(x))

lefttodo = set(range(1, upperlimit + 1))
answer = 0
i = 0
while len(lefttodo) > 0:
    i = heapq.heappop(queue)
    current = sum(splitnum(sum([fac[z] for z in splitnum(i)])))
    if current in lefttodo:
        lefttodo.remove(current)
        temp = i
        lastanswer = answer
        answer += sum(splitnum(temp))
        print i, sum([fac[z] for z in splitnum(i)]), current, (answer - lastanswer), answer, len(queue)
    heapq.heappush(queue, i * 10 + 9)
