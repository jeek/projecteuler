t = 0
array = []
row = 0
triangle = []
while len(triangle) < 1000:
    i = 0
    triangle.append([])
    while i <= row:
        t = (615949 * t + 797807) % 2 ** 20
        (triangle[row]).append(t - 2 ** 19)
        i += 1
    row += 1
minimum = 0
for i in range(1000):
    print i,minimum
    for j in range(1 + len(triangle[i])):
        total = 0
        for k in range(i,1000):
            for l in range(i,k+1):
                total += triangle[k][l]
#                print k,l,total
            if total < minimum:
                minimum = total
                print i,j,k,minimum
