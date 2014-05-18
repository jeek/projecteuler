"""
Determines if the argument is part of an amicable pair by confirming that the
sum of the divisors does not equal itself, but that the sum of the divisors
of the sum of the divisors does.
"""

from divisors import divisors

def isamicable(x):
    if sum(divisors(x)) != x and sum(divisors(sum(divisors(x)))) == x:
        return True
    return False