"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import unittest
try:
    unittest.TestCase.assertLess
except NameError:
    def assertLess(self, a, b, msg=None):
        if not a < b:
            self.fail('%s not less than %s' % (repr(a), repr(b)))
    unittest.TestCase.assertLess = assertLess
from time import time
from palindrome import is_palindrome

def problem004(digits = 3):
    """Brute force the search space."""
    answers = set()
    for i in range(10 ** (digits - 1), 10 ** digits):
        for j in range(i, 10 ** digits):
            answers.add(i * j)
    for i in sorted(list(answers), key = lambda score: -score):
        if is_palindrome(i):
            return i

class TestProblem004(unittest.TestCase):
    """Test the solution to problem #4."""
    def runTest(self):
        """The test itself."""
        # pylint: disable=W0201
        self.start = time()
        self.assertEqual(problem004(), 906609, "Answer to Problem #4 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60, "Problem #4 took too long.")

class TestCaseProblem004(unittest.TestCase):
    """Test using the provided example."""
    def runTest(self):
        """The test itself."""
        self.assertEqual(problem004(2), 9009, "#4 Test Case is wrong.")

if __name__ == "__main__":
    start = time()
    answer = problem004()
    print(4, (time() - start), answer)
