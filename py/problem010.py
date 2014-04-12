"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
from primes import is_prime
from time import time
import unittest

def problem010(argument = 2000000):
    """Simple summation of matching numbers."""
    return sum([i for i in xrange(2, argument) if is_prime(i)])

class TestProblem010(unittest.TestCase):
    """Verify that problem #10 is correct and timely."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.start = time()
        self.assertEqual(problem010(), 142913828922, "Problem #10 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            """Problem #10 takes too long.""")

class TestCaseProblem010(unittest.TestCase):
    """Verify that problem #10 test case is correct."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.assertEqual(problem010(10), 17, "Problem #10 test case is wrong.")

if __name__ == "__main__":
    start = time()
    answer = problem010()
    print 10, answer, time() - start
