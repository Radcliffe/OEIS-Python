# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059215

from itertools import count
from gmpy2 import digits, is_prime
def a(n): return next(k for k in count(2) if is_prime(int(digits(k**n)[::-1])))
print([a(n) for n in range(1, 68)]) # _Michael S. Branicky_, Jul 16 2023

