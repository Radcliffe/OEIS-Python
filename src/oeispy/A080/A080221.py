# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A080221

from sympy.ntheory.factor_ import digits
def A080221(n): return n-sum(1 for b in range(2,n) if n%sum(digits(n,b)[1:])) # _Chai Wah Wu_, Oct 19 2022

