from Queue import PriorityQueue

c = 0
queue = PriorityQueue()

def score(element, layer):
    if layer == 1:
        return element[0] * element[1] * element[2]
    layer -= 1
    return 4 * (element[0] + element[1] + element[2] + layer - 2) * (layer - 1) + 2 * element[0] * element[1] + 2 * element[1] * element[2] + 2 * element[0] * element[2]

def firstlayergenerator(upperlimit):
    c = 1
    while (c <= upperlimit):
        b = 1
        while b <= c and b * c <= upperlimit:
            a = 1
            while a <= b and a * b * c <= upperlimit:
                if a * b * c <= upperlimit:
                    yield([a,b,c])
                a += 1
            b += 1
        c += 1

k = 0
count = dict()

upperlimit = 10000000
answers = []
ready = 0

for i in firstlayergenerator(upperlimit):
#    for n in range(1,100):
#        if score(i,n) <= upperlimit:
    queue.put((score(i,1),i,1))
    k = (k + 1) % 5
    if i[0] == 1:
        print i[2],sorted(answers)
    while (queue.qsize() > 1):
        temp = queue.get()
#        while (temp[0] <= i[2]):
        while(queue.qsize() > 0):
#            print "    ", queue.qsize(),temp
            if count.has_key(temp[0]):
                count[temp[0]] += 1
                if ready < 1000 and count[temp[0]] >= ready:
                    ready = count[temp[0]]
                    print ready,temp
                if count[temp[0]] == 1000:
                    answers.append(temp[0])
#                    print i[2],sorted(answers)
                if count[temp[0]] == 1001:
                    answers.remove(temp[0])
#                    print i[2],sorted(answers)
            else:
                count[temp[0]] = 1
            if score(temp[1],temp[2]+1) <= upperlimit:
                queue.put((score(temp[1],temp[2]+1),temp[1],temp[2]+1))
            temp = queue.get()
        queue.put(temp)
