"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import unittest
from time import time
from factors import factors

try:
    reduce
except NameError:
    from functools import reduce
try:
    xrange
except NameError:
    xrange = range

def problem003(argument = 600851475143):
    """Return the maximum factor."""
    return max(factors(argument))

class TestProblem003(unittest.TestCase):
    """Unit test for problem #3 to confirm correct answer."""
    # pylint: disable=W0201

    def runTest(self):
        """The test itself."""
        self.start = time()
        self.assertEqual(problem003(), 6857, "Answer to Problem #3 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60, "Problem #3 took too long.")

class TestCaseProblem003(unittest.TestCase):
    """Test the example solution from the problem."""
    def runTest(self):
        """The test itself."""
        self.assertEqual(problem003(13195), 29, "#3 Test Case is wrong.")

if __name__ == "__main__":
    start = time()
    answer = problem003()
    print(3, (time() - start), answer)
