def calc(K, X):
    for k in xrange(1, K + 1):
        for a in xrange(-X, X + 1):
            for b in xrange(a + 1, X + 1):
                for c in xrange(b + 1, X + 1):
                    print k, a, b, c
calc(10**6, 10**9)