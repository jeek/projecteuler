from memoize import Memoize

def d(k, i = 2):
    if k == 1:
        return [1]
    answer = [1]
    if k % i == 0:
         answer = answer + [i * j for j in d(k / i, i)]
    else:
         answer = answer + d(k, i + 1)
    return list(set(answer))
print d(1000)
quit()
#print divisors(100)
            

#def d(k): # sum of all divisors of k#
#    answer = 0
#    i = 1
#    while i * i < k:
#        if k % i == 0:
#            answer += i
#            answer += k / i
#        i+=1
#    if i * i == k:
#        answer += i
#    return answer

def S(N):
    answer = 0
    for i in range(1, N + 1):
        print i
        for j in range(1, N + 1):
            answer += sum(d(i * j))
#            answer %= 10 ** 9
    return answer

d = Memoize(d)

S = Memoize(S)

print d(9)
print S(1000)