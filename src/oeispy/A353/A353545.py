# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353545

from math import factorial
from fractions import Fraction
def A353545(n): return sum(Fraction(1, k*factorial(k)) for k in range(1,n+1)).numerator # _Chai Wah Wu_, May 27 2022

