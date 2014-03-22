import unittest
from time import time
from isprime import isprime

def problem046():
    i = 1
    while True:
        i += 2
        if not isprime(i):
            good = True
            for k in [2 * j ** 2 for j in range(int(i ** .5 + 1)) if 2 * j ** 2 < i]:
                if isprime(i - k):
                    good = False
            if good:
                return i

class TestProblem046(unittest.TestCase):
    def runTest(self):
        self.start = time()
        self.assertEqual(problem046(), 5777, "Answer to Problem #46 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60, "Problem #46 took too long.")

if __name__ == "__main__":
    print problem046()
