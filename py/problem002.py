from fib import fib_generator
import unittest
from time import time

def problem002():
    total = 0
    for i in fib_generator(1, 2):
        if i > 4000000:
            return total
        if i % 2 == 0:
            total += i

class TestProblem002(unittest.TestCase):
    def runTest(self):
        self.start = time()
        self.assertEqual(4613732, problem002(), "Answer to #2 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60, "Problem #2 took over 60 seconds.")

if __name__ == "__main__":
    print problem002()
