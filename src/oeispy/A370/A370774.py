# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370774

from fractions import Fraction
def A370774(n): return sum(Fraction(n-i+1,i**2) for i in range(1,n+1)).denominator # _Chai Wah Wu_, May 01 2024

