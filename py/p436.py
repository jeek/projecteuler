from random import randint

from copy import copy

for slices in range(1, 100):
    values = [i for i in range(1, slices + 1)]
 #   print values
    
    queue = [[]]
    
    winsa = 0
    winsb = 0
    count = 0
    while len(queue):
        current = queue.pop(0)
    #    current = queue.pop(randint(0, len(queue) - 1))
        count += 1
        if sum(current) <= 2 * slices:
            current.append(0)
            for i in values:
                current[-1] = i
                queue.append(copy(current))
        else:
            a = 0
            while sum(current[:a]) <= slices:
                a += 1
            a = current[a - 1]
            b = current[-1]
            if a > b:
                winsa += 1
            if b > a:
                winsb += 1
#            if winsa > 0 or winsb > 0:
#                print len(queue), winsb / (winsa + winsb + 1.0), a, b, winsa, winsb, count, current
    print slices, winsb / (winsa + winsb + 1.0), count