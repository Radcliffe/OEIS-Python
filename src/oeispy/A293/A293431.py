# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A293431

from sympy import divisors
def A293431(n): return sum(1 for d in divisors(n,generator=True) if (m:=3*d+1).bit_length()>(m-3).bit_length()) # _Chai Wah Wu_, Apr 18 2025

