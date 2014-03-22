""" 
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import unittest
from factorial import factorial
from sumofdigits import sumofdigits
from time import time

def problem020(argument = 100):
    """Floor is automatic when dealing with integers, and X * (I / X) *
    (I / X + 1) / 2 is how many multiples of X are below I."""
    return sumofdigits(factorial(argument))

class TestCaseProblem020(unittest.TestCase):
    """Test case from the problem description."""
    def runTest(self):
        """The actual test."""
        self.assertEqual(problem020(10), 27, "Problem #20 Test Case is wrong.")

class TestProblem020(unittest.TestCase):
    """Ensure that problem #1 is correct and timely."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.start = time()
        self.assertEqual(problem020(), 648, "Answer to Problem #20 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            "Problem #20 took over 60 seconds.")


if __name__ == "__main__":
    start = time()
    answer = problem020()
    print 20, (time() - start), answer
