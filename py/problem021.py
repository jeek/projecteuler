"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import unittest
from isabundant import isabundant
from time import time

def problem021(argument = 10000):
    return sum(i for i in xrange(argument) if isabundant(i))

class TestProblem021(unittest.TestCase):
    """Ensure that problem #21 is correct and timely."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.start = time()
        self.assertEqual(problem021(), 31626, "Answer to Problem #21 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            "Problem #21 took over 60 seconds.")


if __name__ == "__main__":
    start = time()
    answer = problem021()
    print 21, (time() - start), answer
