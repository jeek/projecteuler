# Sum of inverse squares using distinct integers between 2 and 8 inclusive
# answer is 301

# needs to sum up to 1/2

import copy

print [1.0 / x ** 2 for x in range(2, 81)]
left = sum([1.0 / x ** 2 for x in range(2, 81)])
last = []
next = []
for i in [1.0 / x ** 2 for x in range(2, 81)]:
    length = len(next)
    for j in range(length):
        next.append(next[j] + i)
    next.append(i)
#    next = sorted(next)
#    print "Presort:", next
    left -= i
    next = [x for x in next if x <= .5]
    next = [x for x in next if x + left >= .5]
    print (1/i**.5),len(next)
print len(next)    