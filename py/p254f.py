from copy import deepcopy as copy

i = 10

split = {}
split[0] = []
split[1] = []
split[2] = [11]
split[3] = [21, 12]
split[4] = [31, 22, 13]
split[5] = [41, 32, 23, 14]
split[6] = [51, 42, 33, 24, 15]
split[7] = [61, 52, 43, 34, 25, 16]
split[8] = [71, 62, 53, 44, 35, 26, 17]
split[9] = [81, 72, 63, 54, 45, 36, 27, 18]

def splitnum(i):
    current = [int(j) for j in str(i)]
    for j in range(len(current)):
        for k in split[current[j]]:
            temp = copy(current)
            temp.pop(j)
            temp.insert(j, k)
#            print temp
            while len(temp) > 1:
                temp.append(str(temp.pop(-2)) + str(temp.pop(-1)))
            yield int([str(l) for l in temp][0])

queue = set()

for i in splitnum(69999999999999999):
    queue.add(i)

while(len(queue)):
    current = min(queue)
    queue.remove(current)
    print current, len(queue)
    for i in splitnum(current):
        queue.add(i)