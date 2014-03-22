from gmpy import is_square
from gmpy import is_prime
def factors(x):
    while x % 2 == 0:
        yield 2
        x /= 2
    if is_prime(x):
        yield x
    if x != 1:
        if is_square(x):
            for i in factors(int(x ** .5)):
                if i != 1:
                    yield i
                    yield i
                    x /= i
                    x /= i
        if x >= 2:
                y = int(x ** .5 + 1)
                while not is_square(y ** 2 - x):
                    y += 1
                for i in factors(y - int((y ** 2 - x) ** .5)):
                    if i != 1:
                        yield i
                        for i in factors(y + int((y ** 2 - x) ** .5)):
                            if i != 1:
                                yield i
def factorb(x):
    for i in factors(x + 1):
        yield ("A", i)
    for i in factors(x ** 2 - x + 1):
        yield ("B", i)
    for i in factors(x ** 4 - x ** 3 + x ** 2 - x + 1):
        yield ("C", i)
    for i in factors(x ** 8 + x ** 7 - x ** 5 - x ** 4 - x ** 3 + x + 1):
        yield ("D", i)
for i in factorb((10 ** 8)):
    print i
    