from collections import defaultdict
#         0
#        012
#       01234
#      0123456
#     012345678
#    0123456789A
#   0123456789ABC
#  0123456789ABCDE

count = 0

row = [[]]

row[0].append([0])
row[0].append([1])
row[0].append([2])

for i in range(1,15):
    row.append([])
    last = i - 1
    for j in row[last]:
        for k in range(3):
            temp = j[:]
            if temp[-1] != k:
                temp.append(k)
#                print temp
                row[i].append(temp)
for i in range(13,0,-2):
    row.pop(i)

print len(row[-1])

count = []
for i in range(10):
    count.append([])
count[7] = [1] * 50000
for i in range(6,-1,-1):
    print i
    count[i] = [0] * 50000
    j = 0
    while j < len(row[i]):
#    for j in row[i]:
        print j,len(row[i])
        k = 0
        while k < len(row[i+1]):
        #for k in row[i+1]:
            good = 1
#            print "!!",len(row[i][j])
            for l in range(0,len(row[i][j]),2):
#                print j,k,l
                #print "!",row[i][j],row[i+1][k]
                if row[i][j][l] == row[i+1][k][l+1]:
                    good = 0
            if good == 1:
                count[i][j] += count[i+1][k]
            k += 1
        j += 1
print count[0][0:10]