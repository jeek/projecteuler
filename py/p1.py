print 1, sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
print 2, sum([j for j in [int((((1.0 + 5.0 ** .5) / 2) ** i - ((1 - 5 ** .5) / 2) ** i) / (((1.0 + 5.0 ** .5) / 2) - ((1 - 5 ** .5) / 2))) for i in range(1000)] if j % 2 == 0 and j < 4000000])
print 3, max([i for i in reduce( (lambda r,x: (r.difference_update(range(x*x,int(600851475143 ** .5),2*x)) or r) if (x in r) else r), range(3, int((int(600851475143 ** .5)+1)**0.5+1), 2), set([2] + range(3,int(600851475143 ** .5),2))) if 600851475143 % i == 0])
print 4, max([i * j for i in xrange(100, 1000) for j in range(100, 1000) if str(i * j) == str(i * j)[::-1]])
print 5, reduce(lambda a, b: a * b /  sorted(set(map(lambda x: (x*int(a/x)==a) * x, xrange(1,a+1))).intersection(set(map(lambda x: (x*int(b/x)==b) * x, xrange(1,b+1)))))[-1], range(1, 21))
print 6, sum(range(101)) ** 2 - sum([i ** 2 for i in range(101)])
print 7, (lambda table: [[table.__setitem__(mult,False) for mult in range(i**2,1000000,i)] for i in range(2,int(1000000**0.5)+1) if table[i]] and [p for p in table if p][1:])(list(range(1000000)))[10000]
