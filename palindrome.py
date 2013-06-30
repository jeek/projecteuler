from reverseint import reverseint

def is_palindrome(x):
    if x == reverseint(x):
        return True
    return False
