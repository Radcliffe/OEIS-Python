# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A006232

from fractions import Fraction
from sympy.functions.combinatorial.numbers import stirling
def A006232(n): return sum(Fraction(stirling(n,k,kind=1,signed=True),k+1) for k in range(n+1)).numerator # _Chai Wah Wu_, Jul 09 2023

