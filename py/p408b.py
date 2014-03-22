import copy
import gmpy

array = [[1]]
array.append([])

size = 10000000

row = size
for i in range(size * 2):
    print row
    row -= 1
    x = row
    y = size
    if row <= 0:
        x -= row + 1
        y += row + 1
    if gmpy.is_square(x) and gmpy.is_square(y) and gmpy.is_square(x + y) and x > 0 and y > 0:
        array[-1].append(0)
    else:
        array[-1].append(array[-2][0])
    for j in range(len(array[-2]) - 1):
        x += 1
        y -= 1
        if gmpy.is_square(x) and gmpy.is_square(y) and gmpy.is_square(x + y) and x > 0 and y > 0:
            array[-1].append(0)
        else:
            array[-1].append((array[-2][j] + array[-2][j + 1]) % 1000000007)
    x += 1
    y -= 1
    if gmpy.is_square(x) and gmpy.is_square(y) and gmpy.is_square(x + y) and x > 0 and y > 0:
        array[-1].append(0)
    else:
        array[-1].append(array[-2][-1])
#    array[-2] = copy.deepcopy(array[-1])
    array.append([])
    if row < 0:
        array[-2].pop(0)
        array[-2].pop(-1)
    array[-1] = []
    array.pop(0)
array.pop()
print array[-1][0]