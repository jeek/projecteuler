from gmpy import is_prime
from itertools import permutations

print max([int(str.join("",list(j))) for j in permutations("1234567") if is_prime(int(str.join("",list(j))))])
    