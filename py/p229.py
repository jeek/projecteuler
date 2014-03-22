upperlimit = 2 * 10 ** 9
upperlimit = 10 ** 7

i = 1
squares = list()
while i * i <= upperlimit:
   squares.append(i * i)
   i += 1

count = 0
i = 1
while i <= upperlimit:
    j = 0
    while j < len(squares) and squares[j] <= i / 2:
        if i - squares[j] in squares:
            j = len(squares)
            k = 0
            while k < len(squares) and squares[k] <= i:
                if (i - squares[k]) % 7 == 0 and (i - squares[k]) / 7 in squares:
                    k = len(squares)
                    l = 0
                    while l < len(squares) and squares[l] <= i:
                        if (i - squares[l]) % 3 == 0 and (i - squares[l]) / 3 in squares:
                            l = len(squares)
                            m = 0
                            while m < len(squares) and squares[m] <= i:
                                if (i - squares[m]) % 2 == 0 and (i - squares[m]) / 2 in squares:
                                    m = len(squares)
                                    print i
                                    count += 1
                                m += 1
                        l += 1
                k += 1
        j += 1
    i += 1

print len(squares)
