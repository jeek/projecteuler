"""Use gmpy's gcd for now."""

# pylint: disable=W0611
try:
    from gmpy import gcd
except ImportError:
    def gcd(a, b):
        """Return the greatest common denominator."""
        while b != 0:
            (a, b) = (b, a % b)
        return b
