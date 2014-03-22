total = 0
for i in range(2,16):
    subtotal = 0
    print i
    j = 0
    k = 0
    while j <= 1.99:
        if j > 0:
            print "    ",j
        j = j + 2.0/(i+1)
        k += 1
        subtotal += j ** k
        print subtotal,"!"
    total += int(subtotal)
print total
