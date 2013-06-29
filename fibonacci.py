import unittest

def fib_generator(a, b):
    yield a
    yield b
    while True:
        (a, b) = (b, a + b)
        yield b

class TestFibGenerator(unittest.TestCase):
    def runTest(self):
        from itertools import islice
        self.assertEqual([i for i in islice(fib_generator(1, 2), 10)], [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
