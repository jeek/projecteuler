fac = [1]

for i in xrange(1, 10):
   fac.append(fac[-1] * i)

def f(n):
    if n == 0:
        return 1
    answer = 0
    while n > 0:
        answer += fac[n % 10]
        n /= 10
    return answer

def sf(n):
    answer = 0
    n = f(n)
    while n > 0:
        answer += n % 10
        n /= 10
    return answer

def numlen(x):
    if x == 0:
        return 1
    answer = 0
    while x > 0:
        answer += 1
        x /= 10
    return answer

def numgenerator():
    i = 1
    while i:
        yield i
        i += 1
        if i % 10 == 0:
            temp = 0
            while i % 10 == 0:
                temp += 1
                i /= 10
            while temp:
                i = i * 10 + i % 10
                temp -= 1

numgen = numgenerator()

lefttodo = set(range(1, 151))
answer = 0
i = 0
while len(lefttodo):
    i = numgen.next()
    current = sf(i)
    if current in lefttodo:
        lefttodo.remove(current)
        temp = i
        lastanswer = answer
        while temp:
            answer += temp % 10
            temp /= 10
        print i, f(i), current, (answer - lastanswer), answer
