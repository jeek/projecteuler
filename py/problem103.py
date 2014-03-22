a = 0
done = 0
count = 0
while (done == 0 or 7 * a + 21 < done):
  for b in range(a + 1, a * 2):
    if done == 0 or a + 6 * b + 15 < done:
      for c in range(b + 1, a + b):
        if done == 0 or a + b + 5 * c + 10 < done:
          for d in range(c + 1, a + b):
            if done == 0 or a + b + c + 4 * d + 6 < done:
              for e in range(d + 1, a + b):
                if done == 0 or a + b + c + d + 3 * e + 3 < done:
                  for f in range(e + 1, a + b):
                    if done == 0 or a + b + c + d + e + 2 * f + 1 < done:
                      for g in range(f + 1, a + b):
                        if done == 0 or a + b + c + d + e + f + g < done:
                          if (a + b + c + d > e + f + g):
                            array = dict()
                            i = 1
                            unique = 1
                            total = 0
                            while i <= 2 ** 7 and unique == 1:
                              total = 0
                              for j in range(7):
                                if i & 2 ** j > 0:
                                  total += (a,b,c,d,e,f,g)[j]
                              if array.has_key(total):
                                unique = 0
                              else:
                                array[total] = 1
                              i += 1
                            if unique == 1:
                              if done == 0 or a + b + c + d + e + f + g < done:
                                print a,b,c,d,e,f,g
                                done = a + b + c + d + e + f + g
                                    
  a = a + 1