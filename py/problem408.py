import gmpy
size = 16

array = dict()

for x in range(size, -1, -1):
    for y in range(size, -1, -1):
        if gmpy.is_square(x) and gmpy.is_square(y) and gmpy.is_square(x + y) and x > 0 and y > 0:
            array[y] = 0
        else:
            if x == size and y == size:
                array[y] = 1
            else:
                if x == size:
                    array[y] = array[y + 1]
                else:
                    if y == size:
                        pass
                    else:
                        array[y] = (array[y] + array[y + 1])
    print x, array[0]
        
print array[0]
