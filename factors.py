"""Factor an integer into primes."""

import unittest
from gmpy import is_prime

def factors(argument):
    """Factor an integer into a list of primes."""
    if is_prime(argument):
        return [argument]
    answer = []
    i = 2
    while argument > 1 and not is_prime(argument):
        while argument % i == 0:
            answer.append(i)
            argument /= i
        i += 1
    if argument > 1:
        answer.append(argument)
    return answer

class TestFactors(unittest.TestCase):
    """Ensure that factors algorithm works."""
    def runTest(self):
        """Test from Problem #3."""
        self.assertEqual(factors(13195), [5, 7, 13, 29],
            "factors.py is broken.")
