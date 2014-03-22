import shelve
from collections import defaultdict

upperlimit = 10 ** 7
#upperlimit = 1000

def arrays(n):
    a = 1
    while a ** 2 < n:
        b = 1
        while a ** 2 + 2 * b < n:
            c = 1
            while a ** 2 + 2 * b * c < n:
                d = 1
                while a ** 2 + 2 * b * c + d ** 2 < n:
                    yield (a * a + b * c, a * b + b * d, a * c + c * d, b * c + d * d)
                    d += 1
                c += 1
            b += 1
        a += 1

#answers = shelve.open("420.txt")
answers = defaultdict(int)

for i in arrays(upperlimit):
#    temp = str(mult(i, i))
#    print i, temp
    if i[0] + i[3] < upperlimit:
        print i
#        i = str(i)
#        if i not in answers:
#            answers[i] = 0
#        answers[i] += 1
#for i in answers:
##    i = eval(i)
##    if answers[i] > 1:
##    i = eval(i)
#    if answers[i] == 2 and i[0] + i[3] < upperlimit:
#        print i, answers[i]
#print len([1 for i in answers if answers[i] == 2])
