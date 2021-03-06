""" 
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
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

def problem001(argument = 1000):
    """Floor is automatic when dealing with integers, and X * (I / X) *
    (I / X + 1) / 2 is how many multiples of X are below I."""
    argument -= 1
    return (3 * int(argument / 3) * int(argument / 3 + 1) / 2 \
          + 5 * int(argument / 5) * int(argument / 5 + 1) / 2 \
          - 15 * int(argument / 15) * int(argument / 15 + 1) / 2)

def problem001alternate(argument = 1000):
    """A simple brute-forcing of the searchspace."""
    return sum([x for x in range(argument) if x % 3 == 0 or x % 5 == 0])

class TestCaseProblem001(unittest.TestCase):
    """Test case from the problem description."""
    def runTest(self):
        """The actual test."""
        self.assertEqual(problem001(10), 23, "Problem #1 Test Case is wrong.")

class TestProblem001(unittest.TestCase):
    """Ensure that problem #1 is correct and timely."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.start = time()
        self.assertEqual(problem001(), 233168, "Answer to Problem #1 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            "Problem #1 took over 60 seconds.")


if __name__ == "__main__":
    start = time()
    answer = problem001()
    print(1, (time() - start), answer)
