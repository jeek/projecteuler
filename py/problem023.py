import unittest
from time import time
from divisors import divisors

def problem023():
    abundantnumbers = [i for i in range(1, 28124) if sum(divisors(i)) > i]
    abundantsums = set()
    for i in abundantnumbers:
        for j in [j for j in abundantnumbers if j >= i]:
            abundantsums.add(i + j)
    return sum([i for i in range(28124) if i not in abundantsums])

class TestProblem023(unittest.TestCase):
    def runTest(self):
        self.start = time()
        self.assertEqual(problem023(), 4179871, "Answer to Problem #23 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60, "Problem #23 took too long.")

if __name__ == "__main__":
    print problem023()
