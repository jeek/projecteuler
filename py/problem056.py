import unittest
from time import time
from digitsum import digitsum

def problem056():
    return max([digitsum(a ** b) for a in range(100) for b in range(100)])

class TestProblem056(unittest.TestCase):
    def runTest(self):
        self.start = time()
        self.assertEqual(problem056(), 972, "The answer to Problem #56 is wrong.")
        self.stop = time()

if __name__ == "__main__":
    print problem056()
