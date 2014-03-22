from collections import defaultdict

matrix = defaultdict(set)

matrix[1] = set([(60, 1)])

print matrix

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for i in range(2, 19):
#    for j in range(1, i):
#        matrix[i] = matrix[i] | matrix[j]
#    matrix[i].union(matrix[i-1])
    for j in range(0, i):
#         for k in range(0, i - j + 1):
         k = i - j
         if j <= k:
             for l in matrix[j]:
                 for m in matrix[k]:
                     matrix[i] |= set([(l[0]*m[1] + m[0]*l[1], m[1]*l[1])])
                     if l > 0 and m > 0:
                         top = l[0] * m[0]
                         bottom = l[0]*m[1] + l[1]*m[0]
                         temp = gcd(top, bottom)
                         top /= temp
                         bottom /= temp
                         matrix[i] = matrix[i].union([(top, bottom)])
    print i, matrix
    print i, len(matrix[i])
print matrix
finalanswer = set([])
for i in matrix:
    finalanswer = finalanswer | matrix[i]
print len(finalanswer)