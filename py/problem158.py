fac = lambda n:[1,0][n>0] or fac(n-1)*n
k = 0
maxanswer = 0
for i in range(1, 27):
    k = k * 2 + (i - 1)
    maxanswer = max(k * (fac(26) / (fac(i) * fac(26 - i))), maxanswer)
print maxanswer
