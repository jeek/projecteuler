"""Generate a Fibonacci sequence."""
import unittest

def fib_generator(a, b):
    """Starting with a and b, yield successive sums."""
    yield a
    yield b
    while True:
        (a, b) = (b, a + b)
        yield b

class TestFibGenerator(unittest.TestCase):
    """Test the Fibonacci generator."""
    def runTest(self):
        """The test itself."""
        from itertools import islice
        self.assertEqual([i for i in islice(fib_generator(1, 2), 10)],
            [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
