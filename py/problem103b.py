max = 0

def generator(length, master = 1):
    global max
    if length == 1:
        x = [1]
        while (x):
            yield [x]
            x += 1
    if length == 2:
        x = 1
        while (x):
            y = 1
            while y < x:
                yield [y,x]
                y += 1
            x += 1
            if master == 1 and max > 0 and x > max:
                return
    for i in generator(length - 1, 0):
        for j in range(i[-1] + 1, i[0] + i[1]):
            i.append(j)
            k = 1
            unique = 1
            total = 0
            array = dict()
            while k <= 2 ** len(i) and unique == 1:
                total = 0
                for l in range(len(i)):
                    if k & 2 ** l > 0:
                        total += i[l]
                if array.has_key(total):
                    unique = 0
                else:
                    array[total] = 1
                k += 1
            if unique == 1:
                total = 0
                for k in i:
                    total += k
                if master == 1 and (max == 0 or total < max):
                    max = total
                if max > 0 and total > max:
                    break
                yield i
            i.pop()

for i in generator(7):
    print max, i
