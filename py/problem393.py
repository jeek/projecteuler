from collections import defaultdict

import copy

size = 6

rowcount = []

for i in range(size):
    rowcount.append(defaultdict(int))

def count(original, empty, current, size):
    if current == size ** 2 + 1:
#        print "!!", current, empty
        currow = 0
        for i in empty:
            rowcount[currow][str(i)] += 1
            print rowcount[currow][str(i)], str(i)
            currow += 1
        for i in rowcount:
            print len(i)
        return 1
    total = 0
    original = copy.deepcopy(original)
    empty = copy.deepcopy(empty)
#    print original
#    print empty
    locationcol = (current - 1) % size
    locationrow = int((current - 1) / size)
#    print ("  " * current), current, locationrow, locationcol
    if current <= size ** 2:
        # count(original, empty, current + 1, size)
        if locationcol > 0 and empty[locationrow][locationcol - 1] == 0 and\
          empty[locationrow][locationcol] != (locationrow * size + locationcol - 1 + 1):
            temp = copy.deepcopy(empty)
            temp[locationrow][locationcol - 1] = current
            total += count(original, temp, current + 1, size)
        if locationrow > 0 and empty[locationrow - 1][locationcol] == 0 and\
          empty[locationrow][locationcol] != ((locationrow - 1) * size + locationcol + 1):
            temp = copy.deepcopy(empty)
            temp[locationrow - 1][locationcol] = current
            total += count(original, temp, current + 1, size)
        if locationcol < (size - 1) and empty[locationrow][locationcol + 1] == 0 and\
          empty[locationrow][locationcol] != (locationrow * size + locationcol + 1 + 1):
            temp = copy.deepcopy(empty)
            temp[locationrow][locationcol + 1] = current
            total += count(original, temp, current + 1, size)
        if locationrow < (size - 1) and empty[locationrow + 1][locationcol] == 0 and\
          empty[locationrow][locationcol] != ((locationrow + 1)* size + locationcol + 1):
            temp = copy.deepcopy(empty)
            temp[locationrow + 1][locationcol] = current
            total += count(original, temp, current + 1, size)
    return total

original = []
empty = []
counter = 0
for i in range(size):
    original.append([])
    empty.append([])
    for j in range(size):
        counter += 1
        original[i].append(counter)
        empty[i].append(0)

print ""
print count(original, empty, 1, size)
#for i in rowcount:
#    print len(i)
