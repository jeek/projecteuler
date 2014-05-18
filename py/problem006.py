"""The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""

from time import time
import unittest
try:
    unittest.TestCase.assertLess
except NameError:
    def assertLess(self, a, b, msg=None):
        if not a < b:
            self.fail('%s not less than %s' % (repr(a), repr(b)))
    unittest.TestCase.assertLess = assertLess

def problem006(argument = 100):
    """Exactly what it says on the package."""
    return abs(sum(range(argument + 1)) ** 2 -
        sum([i ** 2 for i in range(argument + 1)]))

class TestProblem006(unittest.TestCase):
    """Ensure that problem #6 is correct and timely."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.start = time()
        self.assertEqual(problem006(), 25164150,
            "Answer to Problem #6 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            "Problem #6 took over 60 seconds.")

class TestCaseProblem006(unittest.TestCase):
    """Ensure that problem #6 test case is correct."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.assertEqual(problem006(10), 2640,
            "Answer to Problem #6 Test Case is wrong.")

if __name__ == "__main__":
    start = time()
    answer = problem006()
    print(6, (time() - start), answer)
