from multiprocessing import Pool

def g(x):
    return ((a - 1) ** n + (a + 1) ** n) % a ** 2

def f(a):
    pool = Pool(processes = 4)
    return max(pool.map(g, xrange(int(a * 1.5 + 1))))

if __name__ == '__main__':
    answer = 0
    pool = Pool(processes=4)              # start 4 worker processes
    print sum(pool.map(f, xrange(3, 1001)))
