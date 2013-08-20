"""Use gmpy prime checker if possible."""
# pylint: disable=0611
try:
    from gmpy import is_prime
except ImportError:
    def is_prime(argument):
        """Rudimentary factor checking."""
        if argument == 2:
            return True
        if argument % 2 == 0:
            return False
        for i in xrange(3, int(argument ** .5 + 1), 2):
            if argument % i == 0:
                return False
        return True

def primegen():
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2
