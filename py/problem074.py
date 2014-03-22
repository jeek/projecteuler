answers = set()

fac = [1]
for i in xrange(1, 10):
    fac.append(i * fac[-1])

def chain(i):
    answer = 0
    for j in [int(k) for k in str(i)]:
        answer += fac[j]
    return answer

for i in xrange(1, 10000000):
#    print i
    answers.add(i)
    i = chain(i)
    while i not in answers:
        print i
        answers.add(i)
        i = chain(i)