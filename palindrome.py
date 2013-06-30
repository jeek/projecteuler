"""
Check to see if a given number is a palindrome.
"""
from reverseint import reverseint

def is_palindrome(x):
    """If the number equals its reverse, it is a palindrome."""
    if x == reverseint(x):
        return True
    return False
