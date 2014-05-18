"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import unittest
try:
    unittest.TestCase.assertLess
except:
    def assertLess(self, a, b, msg=None):
        if not a < b:
            self.fail('%s not less than %s' % (repr(a), repr(b)))
    unittest.TestCase.assertLess = assertLess
from time import time
from gcd import gcd
try:
    reduce
except:
    from functools import reduce

def problem005(argument = range(1, 21)):
    """Return the lcm of 1 through 20."""
    return reduce(lambda a, b: a * b / gcd(a, b), argument)

class TestProblem005(unittest.TestCase):
    """Test the solution to problem #5."""
    def runTest(self):
        """The test itself."""
        # pylint: disable=W0201
        self.start = time()
        self.assertEqual(problem005(), 232792560,
            "Answer to Problem #5 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            "Problem #5 took too long.")

class TestCaseProblem005(unittest.TestCase):
    """Test the example for problem #5."""
    def runTest(self):
        """The test itself."""
        self.assertEqual(problem005(range(1, 11)), 2520,
            "#5 Test Case is wrong.")

if __name__ == "__main__":
    start = time()
    answer = problem005()
    print(5, (time() - start), answer)
