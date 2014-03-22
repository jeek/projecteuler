from multiprocessing import Pool

def f(a):
    print a
    return max([((a - 1) ** n + (a + 1) ** n) % a ** 2 for n in xrange(int(a * 1.5 + 1))])

if __name__ == '__main__':
    answer = 0
    pool = Pool(processes=5)              # start 4 worker processes
    print sum(pool.map(f, xrange(3, 1001)))
