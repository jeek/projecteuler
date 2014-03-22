from divisors import divisors

def isabundant(x):
    if sum(divisors(x)) != x and sum(divisors(sum(divisors(x)))) == x:
        return True
    return False