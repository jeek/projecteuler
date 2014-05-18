"""A Pythagorean triplet is a set of three natural numbers, a  b  c, for
which,

a ** 2 + b ** 2 = c ** 2
For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
import unittest
from time import time

def problem009():
    """Try possibilities until the answer is found."""
    for a in range(1, 1001):
        for b in range(a + 1, 1001 - a):
            c = 1000 - a - b
            if c > b:
                if a ** 2 + b ** 2 == c ** 2:
                    return a * b * c

class TestProblem009(unittest.TestCase):
    """Test that #9 is correct and runs in a timely manner."""
    # pylint: disable=W0201
    def runTest(self):
        """The test itself."""
        self.start = time()
        self.answer = self.assertEqual(31875000, problem009(),
            """Answer to problem #9 is wrong.""")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60,
            """Problem #9 took too long.""")

if __name__ == "__main__":
    start = time()
    answer = problem009()
    print(9, answer, (time() - start))
