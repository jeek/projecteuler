"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?"""

from primes import primegen
from time import time
import unittest

def problem007(argument = 10001):
    """Generate a list of primes and then return the last element."""
    primes = []
    nextprime = primegen()
    while len(primes) < argument:
        primes.append(nextprime.next())
    return primes[-1]

class TestProblem007(unittest.TestCase):
    """Ensure that problem #7 is correct and runs in a timely manner."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.start = time()
        self.assertEqual(104743, problem007())
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            "Problem #7 took over 60 seconds.")

class TestCaseProblem007(unittest.TestCase):
    """Ensure that problem #7 test case is correct and runs in a timely
        manner."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.assertEqual(13, problem007(6))

if __name__ == "__main__":
    start = time()
    answer = problem007()
    print(7, (time() - start), answer)
