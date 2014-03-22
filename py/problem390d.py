from multiprocessing import Pool

import gmpy
def count(limit): 
    n = limit
    while n >= 2: 
        yield n 
        n -= 2

def handle(c):
    b = c + 2
    dd = b ** 2 + c ** 2 + b ** 2 * c ** 2
    answer = []
    answer.append(0)
    total = 0
    while ((gmpy.sqrt(dd))/2 < 10 ** 10):
        if (gmpy.is_square(dd) and (gmpy.sqrt(dd)) % 2 == 0):
            total += (gmpy.sqrt(dd)) / 2
            print total,b,c
        b += 2
        dd = b ** 2 + c ** 2 + b ** 2 * c ** 2
    if total > 0:
        print c,"Done!",total
    return total

if __name__ == '__main__':
    pool = Pool(processes = 10)
    
    n = 10 ** 10
    total = 0
    
    c = 2
    b = 2
    print sum(pool.imap(handle, count(141422)))
