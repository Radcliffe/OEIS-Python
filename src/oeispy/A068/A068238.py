# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068238

from fractions import Fraction
from sympy import factorint
def A068238(n): return Fraction(sum((Fraction(e,p) for p,e in factorint(n).items())),n).denominator # _Chai Wah Wu_, Nov 03 2022

