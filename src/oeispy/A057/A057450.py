# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A057450

from sympy import prime
from itertools import accumulate
def f(an, _): return prime(an)
print(list(accumulate([4]*12, f))) # _Michael S. Branicky_, Apr 07 2021

