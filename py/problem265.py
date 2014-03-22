size = 5
array = []

def build(size,array):
    total = 0
    for i in range(len(array) - size):
        match = 0
        for j in range(size):
            if (array[-size+j] == array[i+j]):
                match += 1
        if match == size:
            return 0
    if (2 ** size == len(array)):
        arraycopy = array[:]
        for i in range(size - 1):
            arraycopy.append(0)
        for j in range(len(arraycopy)):
            for k in range((j+1),len(arraycopy)):
                match = 0
                for l in range(size):
                    try:
                        if (arraycopy[j+l] == arraycopy[k+l]):
                            match += 1
                    except:
                        pass
                if match == size:
                    return 0
        answer = 0
        for i in range(size-1):
          arraycopy.pop()
        for i in arraycopy:
            answer *= 2
            answer += i
#        print answer,arraycopy
        return answer
    else:
        array.append(0)
        total += build(size,array)
        array.pop()
        array.append(1)
        total += build(size,array)
        array.pop()
        return total

for i in range(size):
    array.append(0)
i = 0
sum = 0

print build(size,array)