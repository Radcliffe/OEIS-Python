# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376165

from gmpy2 import digits
from itertools import count
def a(n):
    t = digits(n).count("1")
    return next(k*n for k in count(2) if digits(k*n).count("1") - t == 1)
print([a(n) for n in range(1, 100)]) # _Michael S. Branicky_, Oct 22 2024

