import unittest

def primefactors(x):
    answers = []
    i = 2
    while x > 1:
        while x % i == 0:
            answers.append(i)
            x /= i
        i += 1
    return answers

class TestPrimefactors(unittest.TestCase):
    def runTest(self):
        self.assertEqual(primefactors(13195), [5, 7, 13, 29], "primefactors is broken")
