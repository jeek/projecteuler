import unittest
from time import time
from primegen import primegen

def problem087(upperlimit = 50000000):
    primes = primegen()
    a = [primes.next() ** 2]
    while a[-1] < upperlimit:
        a.append(primes.next() ** 2)
    a.pop()
    primes = primegen()
    b = [primes.next() ** 3]
    while b[-1] < upperlimit:
        b.append(primes.next() ** 3)
    b.pop()
    primes = primegen()
    c = [primes.next() ** 4]
    while c[-1] < upperlimit:
        c.append(primes.next() ** 4)
    c.pop()
    return len(list(set([aa + bb + cc for aa in a for bb in b for cc in c if aa + bb + cc < upperlimit])))

class TestProblem087(unittest.TestCase):
    def runTest(self):
        self.start = time()
        self.assertEqual(problem087(), 1097343, "Answer to Problem #87 is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60, "Problem #87 took too long.")

class TestProblem087TestCase(unittest.TestCase):
    def runTest(self):
        self.start = time()
        self.assertEqual(problem087(50), 4, "Answer to Problem #87 Test Case is wrong.")
        self.stop = time()
        self.assertLess(self.stop - self.start, 60, "Problem #87 Test Case took too long.")

if __name__ == "__main__":
    print problem087()
