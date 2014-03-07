"""Reverse an integer."""

def reverseint(x):
    """
    Form a new integer by lopping off the end of the current one, one
    digit at a time.
    """
    y = x
    z = 0
    while y > 0:
        z = z * 10 + y % 10
        y /= 10
    return z
