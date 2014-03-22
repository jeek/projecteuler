fac = lambda n:[1,0][n>0] or fac(n-1)*n
print max([(2 ** k - k - 1) * (fac(26) / (fac(k) * fac(26 - k))) for k in range(27)])