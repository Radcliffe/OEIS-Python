# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367356

from itertools import islice
from sympy.ntheory.factor_ import digits
def a(n, b=3): # generator of terms
    an, y, c = n, 1, 0
    while y < b:
        an, y, c = an + b*(an%b), 1, c+1
        while y < b:
            if str(digits(an+y, b)[1]) == str(y):
                an += y
                break
            y += 1
    return c
print([a(n) for n in range(1, 101)]) # _Michael S. Branicky_, Nov 18 2023

