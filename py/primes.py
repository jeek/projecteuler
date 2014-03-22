primelist = [2, 3]

primeslist = dict()

for i in primelist:
    primeslist[i] = 1

def isprime(x):
    i = primelist[-1]
    while (primelist[-1] < x):
        i += 2
        flag = True
        j = 0
        while j < len(primelist):
            if i % primelist[j] == 0 or primelist[j] ** 2 > i:
                if i % primelist[j] == 0:
                    flag = False
                j = len(primelist)
            j += 1
        if flag == True:
            primelist.append(i)
            primeslist[i] = 1
    return primeslist.has_key(x)
print isprime(1000000)
print sorted(primeslist.keys())