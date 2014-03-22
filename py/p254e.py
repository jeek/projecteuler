from collections import deque
import heapq
from copy import deepcopy as copy

upperlimit = 150

def splitnum(i):
    answer = []
    while i > 0:
        answer.insert(0, i % 10)
        i /= 10
    return answer

def sumnum(i):
    answer = 0
    while i:
        answer += i % 10
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

fac = [1]

for i in xrange(1, 10):
   fac.append(fac[-1] * i)

queue = [(i, sum([fac[j] for j in splitnum(i)]), sumnum((sum([fac[j] for j in splitnum(i)])))) for i in queue]

heapq.heapify(queue)

def numlen(x):
    if x == 0:
        return 1
    return len(splitnum(x))

lefttodo = set(range(1, upperlimit + 1))

answer = 0
while len(lefttodo) > 0 and min(lefttodo) < 64:
    (i, sf, sg) = heapq.heappop(queue)
    if sg in lefttodo:
        answer += sumnum((i))
        print i, sf, sg, answer
        lefttodo.remove(sg)
    heapq.heappush(queue, (i * 10 + 9, sf + fac[9], sumnum((sf + fac[9]))))

while len(lefttodo) > 0:
    current = min(lefttodo)
    j = min(lefttodo)
    lefttodo.remove(j)
    i = int("0" + "9" * int(j / 9))
    j -= 9 * int(j / 9)
    i = int(str(j) + str(i))
    answer += 9 * (i / fac[9])
    i %= fac[9]
    for j in range(8, 0, -1):
        answer += j * (i / fac[j])
        i %= fac[j]
    print current, i, answer
    