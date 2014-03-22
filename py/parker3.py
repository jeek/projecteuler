"""
parkiepie.py

jeek attempts to cram his math/coding balls down parker's throat by showing him
a better way to accomplish some meaningless task
"""

def is_prime(number):
    """ Check if a given number is prime. """
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for prime_iterator in xrange(3, int(number ** .5 + 1), 2):
        if number % prime_iterator == 0:
            return False
    return True
    

def number_generator():
    """ Yield prime numbers that start and end with 3. """
    yield 3
    digits = 1
    while True:
        # 33, 303, 3003, etc
        for number in xrange(3 * 10 ** digits + 3, 4 * 10 ** digits, 10):
            if is_prime(number):
                yield number
        digits += 1
        
if __name__ == "__main__":
    COUNT = 0
    for i in number_generator():
        COUNT += 1
        if COUNT == 333:
            print i
            quit()
